from bs4 import BeautifulSoup
import requests


URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun="
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")


def extract_date():
    s_descript = soup.find("p", "s_descript").string
    date = " ".join(s_descript.split(" ")[-3:-1])
    return date


def extract_continents():
    continents = {}
    ths = soup.find("table", "num").find_all(
        "th", {"scope": "row"})[:-1]  # 표 최하단 합계 제외
    for th in ths:
        continent = th.text
        rowspans = th["rowspan"]
        continents[continent] = rowspans

    continents_arr = []

    for key, value in continents.items():
        for v in range(int(value)):
            continents_arr.append(key)

    return continents_arr


def extract_sum():
    row = soup.find("table", "num").find_all("tr")[-1].find("td").text
    patient, deceased = row.split("명(사망 ")
    deceased = deceased.strip(")")

    return {"": None, "합계": "합계", "patient": patient, "deceased": deceased}


def extract_data():
    datas = []
    rows = soup.find("table", "num").find("tbody").find_all("tr")
    rows = rows[:-1]  # 표 최하단 합계 제외

    continents = extract_continents()
    for row in rows:

        continent = continents.pop(0)
        country, cases = row.find_all("td")
        # <tr>의 <td> 값이 2개이고, 각각의 값은 country, cases이다.
        country = country.text
        patient = cases.text.split("명")[0]
        if "사망" in cases.text:  # 사망자 없는 경우
            deceased = cases.text.split(" ")[-1].strip().strip(")")
        else:
            deceased = "0"
        data = {"continent": continent, "country": country,
                "patient:": patient, "deceased": deceased}
        datas.append(data)

    datas.append(extract_sum())
    return datas
