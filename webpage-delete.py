from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get('http://localhost:3000/Book')
driver.maximize_window()
driver.implicitly_wait(10)

josdel = driver.find_elements(By.ID,'deleteBook')
josdel[0].click()

# idBok = driver.find_elements(By.CLASS_NAME,"MuiDataGrid-row")

i = 2
while i <= len(idBok):
    try:
        confDelete = driver.find_elements(By.XPATH,"/html/body/div[2]/div[3]/div/div[2]/button[2]")
        confDelete[0].click()
    except time:
        print('enek le error')
        pass

    time.sleep(3)
    i = i +1
print("uwes rampung cok")
