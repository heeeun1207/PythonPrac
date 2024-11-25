from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# '가는 날' 버튼이 로드될 때까지 기다리고 클릭
try:
    # '가는 날' 버튼이 로드될 때까지 최대 10초 기다림
    going_day_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "가는 날")]'))
    )
    going_day_button.click()

    # time.sleep(3)  # 클릭 후 잠시 대기

    # # 월을 클릭하기 위해 '2024.12.' 텍스트를 포함하는 div 요소를 기다리기
    # # 월 클릭을 위한 div 텍스트가 포함된 요소가 보일 때까지 기다림
    # month_button = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "2024.12.")]'))
    # )

    # # 요소가 화면에 보이도록 스크롤 (필요한 경우)
    # browser.execute_script("arguments[0].scrollIntoView();", month_button)
    
    # # 월 클릭
    # month_button.click()

    time.sleep(2)  # 월 클릭 후 잠시 대기

    # 날짜를 선택 (예: 27일 선택)
    going_day_27_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(.//b, "27")]'))
    )
    going_day_27_button.click()

    time.sleep(3)  # 클릭 후 잠시 대기

except Exception as e:
    print(f"Error occurred: {e}")

# 결과 확인을 위해 30초 대기
time.sleep(30)
