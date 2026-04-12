from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# -------------------------
# LOAD PROJECT DATA
# -------------------------
def load_projects():
    file_path = os.path.join(app.root_path, "data", "projects.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# -------------------------
# STATIC DATA (SKILLS)
# -------------------------
skills = [
    "Advanced SQL (T-SQL) for complex querying and optimization",
    "Database management using SQL and MongoDB",
    "Big data and NoSQL handling with MongoDB",
    "Exploratory Data Analysis (EDA)",
    "Data storytelling and insight generation",
    "Predictive modeling using Python (Scikit-learn)",
    "Data manipulation using Pandas, NumPy and Excel",
    "Business Intelligence dashboard development",
    "Web scraping using BeautifulSoup and Requests",
    "Data automation and scripting",
    "Data governance and quality assurance",
    "Building clean and scalable reporting systems"
]

# -------------------------
# MAIN ROUTE (ONE PAGE APP)
# -------------------------
@app.route("/")
def home():
    return render_template(
        "index.html",
        skills=skills,
        projects=load_projects()
    )

# -------------------------
# OPTIONAL ROUTES (KEEP IF YOU WANT DIRECT LINKS)
# -------------------------
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills_page():
    return render_template("skills.html", skills=skills)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=load_projects())

@app.route("/tools")
def tools():
    return render_template("tools.html")

# -------------------------
# API (GOOD FOR PORTFOLIO)
# -------------------------
@app.route("/api/projects")
def api_projects():
    return jsonify(load_projects())

# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)