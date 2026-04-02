import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import urllib.parse

app = Flask(__name__)

def search_incruit():
    keyword = urllib.parse.quote("파이썬")
    url = f"https://search.incruit.com/list/search.asp?col=all&src={keyword}&startno=0"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    lis = soup.find_all("li", class_="c_col")
    jobs = []

    for li in lis:
        company_tag = li.find("a", class_="cpname")
        title_area = li.find("div", class_="cell_mid")

        if not company_tag or not title_area:
            continue

        title_tag = title_area.find("a")
        if not title_tag:
            continue

        cl_md_list = li.find_all("div", class_="cl_md")
        location = "지역 정보 없음"

        if len(cl_md_list) > 0:
            span_list = cl_md_list[0].find_all("span")
            if len(span_list) > 0:
                location = span_list[0].get_text(strip=True)

        company = company_tag.get_text(strip=True)
        title = title_tag.get_text(strip=True)
        href = title_tag.get("href")

        job_data = {
            "title": title,
            "company": company,
            "location": location,
            "href": href
        }

        jobs.append(job_data)

    return jobs


@app.route("/")
def home():
    jobs = search_incruit()
    return render_template("index.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True)