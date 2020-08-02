import csv


def save_to_file(jobs):
    # 웹 서버로 전달할 때
    file = open("jobs.csv", mode="w", newline="")

    # 엑셀 파일로 볼 때
    # file = open("jobs.csv", mode="w", encoding="UTF8", newline="")

    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Link"])
    for job in jobs:
        writer.writerow(job.values())
    return
