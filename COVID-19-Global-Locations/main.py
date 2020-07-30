from covid import extract_date, extract_data
from save import save_to_file


date = extract_date()
datas = extract_data()
save_to_file(datas, date)
