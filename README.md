

## 🔍 Skill Difference — Know the Gap Between You and Your Dream Job

### 🚀 Overview

**Skill Difference** is a simple web application built using **Flask** that helps users discover the **top 5 skills required** for any job role they enter. It’s designed to highlight the **skill gap** between the user’s current knowledge and their target career, helping them plan their learning journey more effectively.

The project **dynamically scrapes real-time job listings from [TimesJobs](https://www.timesjobs.com)** based on the user's input and extracts the most relevant skill keywords from the job postings.

---

### 💡 Features

* 🔎 User inputs a job role (e.g., “Data Scientist”)
* 🌐 Web scraping of [timesjobs.com](https://www.timesjobs.com) for real job listings
* 🏷️ Extracts and ranks the most frequently mentioned required skills
* 📊 Returns the **top 5 in-demand skills** for that role
* 🚫 Displays a friendly message if the job role isn’t found
* 🎨 Stylish and responsive frontend using HTML & CSS
* ⚙️ Built with Flask for clean server-side rendering

---

### 🛠️ Technologies Used

* Python 3
* Flask
* Jinja2
* HTML5 & CSS3
* **Requests** & **BeautifulSoup** (for web scraping)

---

### 📁 Project Structure

```
project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── README.md
└── requirements.txt
```

---

### 🌐 How It Works

1. User enters a job title (e.g., "Data Scientist").
2. The app sends a request to TimesJobs and fetches job postings for that role.
3. It extracts the **tags** and **key skills** listed in each posting.
4. It tallies the most frequently occurring skills.
5. The top 5 skills are displayed back to the user.

---

### 📦 How to Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/skill-difference.git
   cd skill-difference
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:

   ```bash
   python app.py
   ```

5. **Open your browser**:

   ```
   http://127.0.0.1:5000
   ```


