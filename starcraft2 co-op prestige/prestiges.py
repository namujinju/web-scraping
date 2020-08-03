from bs4 import BeautifulSoup
import requests


def extract_prestiges(commander):
    URL = f"https://starcraft.fandom.com/wiki/{commander}_(Co-op_Missions)"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    h3 = soup.find("span", {"id": "Prestiges"}).parent

    dl = h3.next_sibling.next_sibling  # 다음 형제 태그 가져오기
    prestiges_list = []

    for i in range(3):
        prestiges_dict = {}

        prestiges_name = dl.find("dt").get_text().strip()
        dd = dl.find_all("dd")
        prestiges_adv = dd[0].get_text().strip()
        prestiges_dis = dd[1].get_text().strip()

        prestiges_dict["commander"] = commander
        prestiges_dict["name"] = prestiges_name
        prestiges_dict["adv"] = prestiges_adv
        prestiges_dict["dis"] = prestiges_dis

        prestiges_list.append(prestiges_dict)

        dl = dl.next_sibling.next_sibling

    return prestiges_list
