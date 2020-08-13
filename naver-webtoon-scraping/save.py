import csv


def save_to_file(datas):
    file = open("naver-webtoon-all.csv", mode="w", newline="")
    writer = csv.writer(file)
    writer.writerow(["요일", "제목", "작가"])
    for data in datas:
        writer.writerow(data.values())
    return
