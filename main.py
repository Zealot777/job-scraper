# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:
db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    
    if not keyword:
        return render_template("home.html")

    # 1. 캐시 확인
    if keyword in db:
        print(f"Using cache for: {keyword}")
        jobs = db[keyword]
    else:
        # 2. 캐시에 없으면 필터링 진행
        print(f"Searching for: {keyword}")
        all_jobs = load_jobs()
        jobs = []
        
        for job in all_jobs:
            # 제목(title)이나 설명(description)에 키워드가 포함되어 있는지 확인 (대소문자 무시)
            if keyword.lower() in job["title"].lower() or \
               keyword.lower() in job["description"].lower():
                jobs.append(job)
        
        # 3. 결과를 캐시에 저장
        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)


# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT