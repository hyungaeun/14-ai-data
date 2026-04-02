import csv

def save_to_file(jobs):
    with open("jobs.csv", "w", encoding="cp949") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["NO", "제목", "회사", "지역", "Link"])

        for i, job in jobs:
            csv_writer.writerow([i, job["title"], job["company"]])