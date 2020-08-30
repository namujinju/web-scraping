from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

browser = webdriver.Chrome()
# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# browser.back()
# browser.forward()
# browser.refresh()
# browser.back()

# 3. id, pw 입력

browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys(
    "naver_password", Keys.ENTER)

# 4. id 새로 입력
time.sleep(3)
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("new_id")

# 5. html 정보 출력
print(browser.page_source)

# 6. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료


# elem = browser.find_element_by_id("query")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# elem = browser.find_elements_by_tag_name("a")
# for e in elem:
#     e.get_attribute("href")

# browser.get("http://daum.net")
# elem = browser.find_element_by_name("q")

# elem = browser.find_element_by_xpath(
#     "//*[@id='daumSearch']/fieldset/div/div/button[2]")

# browser.quit()
