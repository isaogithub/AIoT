from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os

loginUrl = ("https://aiot.kaitechstudio.com/Login/")
username = "ttu410607214"
driver = webdriver.Chrome("./2/chromedriver.exe")

driver.get(loginUrl)

driver.find_element_by_name("userID").send_keys(username)
driver.find_element_by_name("userID").send_keys(Keys.ENTER)

time.sleep(1)

counter = ''
while True:
    counter = driver.find_element_by_id("succesCounter").text
    if counter != '':
        break
print("counter is:",counter)
while True:

    Q1 = driver.find_element_by_id("Q1").get_attribute("value")
    Q2 = driver.find_element_by_id("Q2").get_attribute("value")
   

    Q1 = Q1.replace("|","ttu410607214")
    Q1 = Q1.replace(" ","")

    Q2 = Q2.split(" ")

    if Q2[1] == "+":
        Q2 = int(Q2[0])+int(Q2[2])
    elif Q2[1] == "-":
        Q2 = int(Q2[0])-int(Q2[2])

    elif Q2[1] == "*":
        Q2 = int(Q2[0])*int(Q2[2])

    elif Q2[1] == "%":
        Q2 = int(Q2[0])%int(Q2[2])

    print(Q1)
    print(Q2)

    Q1_answer = Q1
    Q2_answer = Q2
    driver.find_element_by_id("Q1a").send_keys(Q1_answer)
    driver.find_element_by_id("Q2a").send_keys(Q2_answer)

    driver.find_element_by_id("btnSubmit").click()
    time.sleep(0.3)
    counter = driver.find_element_by_id("succesCounter").text
    if counter == '200':
        driver.refresh()
        break
