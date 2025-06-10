from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_skills', methods=['POST'])
def get_skills():
    job_role = request.form['job_role'].strip().lower()
    skills = webscraping(job_role)
    return render_template('skills.html', job_role=job_role.title(), skills=skills)

def webscraping(input):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt


    # links_address = ['https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=', 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Analyst&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=0DQT0data%20analyst0DQT0&pDate=I&sequence=2&startPage=1', 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Analyst&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=0DQT0data%20analyst0DQT0&pDate=I&sequence=3&startPage=1' , 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Analyst&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=0DQT0data%20analyst0DQT0&pDate=I&sequence=4&startPage=1' , 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Analyst&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=0DQT0data%20analyst0DQT0&pDate=I&sequence=5&startPage=1']
    # link_address = 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Analyst&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=100&postWeek=60&txtKeywords=0DQT0data%20analyst0DQT0&pDate=I&sequence=2&startPage='
    links_address = []
    # Custom input code
    input_search = input
    input_search = input_search.replace(" ", "%20").lower()
    # print(input_search)
    link_address_1 = 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords='
    link_address_2 = '&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=100&postWeek=60&txtKeywords=0DQT0'
    link_address_3 = '0DQT0&pDate=I&sequence='
    link_address_4 = '&startPage=1'

    link_address = link_address_1 + input_search + link_address_2 + input_search + link_address_3


    # Getting the number of pages for jobs
    html_text =  requests.get(link_address + str(1) + link_address_4).text
    soup = BeautifulSoup(html_text, 'html' )
    no_of_jobs = soup.find("span", {"id": "totolResultCountsId"})
    # print(no_of_jobs.get_text())
    no_of_pages = int(no_of_jobs.get_text())//100
    if(no_of_pages>10):
        no_of_pages = 10
    # print(no_of_pages)
    #  Scraping data using bs4
    for i in range(1, no_of_pages+2):
        
        links_address.append(link_address +str(i)+link_address_4)

    skills_list = []
    skills_required_div_list = []

    n = len(link_address)
    max_no_of_pages = 1
    if n >max_no_of_pages:
        n = max_no_of_pages # change variable to include more pages
    else:
        n = len(links_address)


    for link in links_address[:n]:
        html_text =  requests.get(link).text
        soup = BeautifulSoup(html_text, 'html')
        skills_required_div = soup.find_all('div' , class_ = 'more-skills-sections')
        skills_required_div_list.append(skills_required_div)
    # print(skills_required_div_list)
    for skills in skills_required_div:
            skills_span = skills = skills.find_all('span')
            for skill in skills_span:
                skills_list.append(skill.get_text().strip().lower())

                

    # print(links_address)

    df = pd.DataFrame(skills_list)
    # df.head()

    all_skills=[]
    for each in skills_list:
        for every in each.split(","):
            all_skills.append(every.strip())
    # df.head()

    skill_dict={}
    for each in all_skills:
        try:
            skill_dict[each]+=1
        except:
            skill_dict[each]=1
    # skill_dict


    new_df=pd.DataFrame(skill_dict,index=["count"]).T
    # new_df


    new_df=new_df.sort_values(by="count",ascending=False)
    new_df["count"].tolist()
    # new_df

    # if new_df.count:
    #     new_df.head(10).plot.bar()
    # else:
    #     print("Search not found")

    n1 = len(new_df)

    if 5<n1:
        top_5_skills = new_df[:5]
        top_5_skills = list(top_5_skills.index)
        
    else:
        top_5_skills = new_df[:n1]
        top_5_skills = list(top_5_skills.index)
    
    if n1:
        return top_5_skills
    else:
        return "Search not found"
    


if __name__ == '__main__':
    app.run(debug=True)
