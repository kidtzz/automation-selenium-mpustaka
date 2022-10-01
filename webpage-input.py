from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time

wb = load_workbook(filename="/home/kidtz/Documents/learning/selenium/bookP.xlsx")

sheetRange= wb['Sheet1']

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('http://localhost:3000/Book/addBook')
driver.maximize_window()
driver.implicitly_wait(10)

i = 2 
while i <= len(sheetRange['A']):
    name = sheetRange['A'+str(i)].value
    pengarang = sheetRange['B'+str(i)].value
    penerbit = sheetRange['C'+str(i)].value
    tahunTerbit = sheetRange['D'+str(i)].value
    description = sheetRange['E'+str(i)].value

    try:
         na = driver.find_elements(By.ID,":r1:")
         na[0].send_keys(name)
         pe = driver.find_elements(By.ID,":r3:")
         pe[0].send_keys(pengarang)
         pen = driver.find_elements(By.ID,":r5:")
         pen[0].send_keys(penerbit)
         tt = driver.find_elements(By.ID,":r7:")
         tt[0].send_keys(tahunTerbit)
         des = driver.find_elements(By.ID,":r9:")
         des[0].send_keys(description)
         clic = driver.find_elements(By.ID,'addBook')
         clic[0].click()
    except time:
        print("Enek Sing Error iki mau lek");
        pass

    time.sleep(2)
    i = i + 1

print("selesai ni bg")