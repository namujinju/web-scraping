import csv


def save_to_file(datas, date):
    file = open(f"COVID-19-{date}.csv", mode="w", newline="")
    writer = csv.writer(file)
    writer.writerow(["지역", "국가", "환자 발생 수", "사망"])
    for data in datas:
        writer.writerow(data.values())
        
    return
