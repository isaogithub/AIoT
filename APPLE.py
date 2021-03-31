from selenium import webdriver
from PIL import Image # pillow 安裝 Anaconda 時已自動安裝
import time
from time import sleep
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# 取出 綱頁圖中的驗證圖片，存入 檔
# 請調整解析度

print("Please input your lastName")
lastName = input()
print("Please input your firstName")
firstName = input()
print("Please input your emailAddress")
emailAddress = input()
print("Please input your mobilePhone")
mobilePhone = input()
print("Please input your cardNumber")
cardNumber = input()
print("Please input your expiration 到期月日")
expiration = input()
print("Please input your 安全碼")
securityCode = input()
print("Please input your 地址")
street = input()
print("Please input your 郵政區碼")
postalCode = input()


url = "https://www.apple.com/tw/shop/buy-iphone/iphone-12"
driver = webdriver.Chrome("./2/chromedriver.exe")
driver.get(url)

time.sleep(30)

driver.find_element_by_id('Item1-dimensionScreensize-6_1inch').click()



driver.execute_script("window.scrollTo(0,200)")

time.sleep(1)
driver.find_element_by_css_selector(".white > .ir").click()

time.sleep(1)
driver.find_element_by_css_selector("#Item364gb_label > .form-selector-title").click()

driver.execute_script("window.scrollTo(0,850)")

WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.label')))
driver.find_element_by_css_selector(".label").click()
sleep(4)
driver.find_element_by_name("proceed").click()
sleep(3)

driver.find_element_by_id("shoppingCart.actions.navCheckout").click()

sleep(3)
driver.find_element_by_id("signIn.guestLogin.guestLogin").click()

sleep(3)
driver.find_element_by_css_selector(".as-svgicon-applestorepickup").click()

sleep(3)
driver.find_element_by_css_selector(".as-storelocator-searchitem:nth-child(1) .as-storelocator-available-quote").click()

sleep(3)
driver.find_element_by_css_selector(".rs-pickup-slot:nth-child(3) .form-selector-label").click()

driver.find_element_by_id("2021-03-31timeWindows").click()
dropdown = driver.find_element_by_id("2021-03-31timeWindows")
dropdown.find_element_by_xpath("//option[. = '下午 2:15 – 下午 2:30']").click()
driver.find_element_by_id("2021-03-31timeWindows").click()

driver.find_element_by_id("rs-checkout-continue-button-bottom").click()
sleep(3)
driver.find_element_by_css_selector(".large-6:nth-child(1) .rs-pickup-optionstitle").click()
sleep(1)
driver.find_element_by_name("lastName").click()

driver.find_element_by_name("lastName").send_keys(lastName)
driver.find_element_by_name("firstName").click()
driver.find_element_by_name("firstName").send_keys(firstName)

driver.find_element_by_name("emailAddress").click()
driver.find_element_by_name("emailAddress").send_keys(emailAddress)
driver.find_element_by_name("mobilePhone").click()
driver.find_element_by_name("mobilePhone").send_keys(mobilePhone)


###############
driver.find_element_by_id("rs-checkout-continue-button-bottom").click()
time.sleep(3)
driver.find_element_by_css_selector("#checkout\\.billing\\.billingOptions\\.options\\.0-selector .row").click()
time.sleep(3)

driver.find_element_by_name("cardNumber").click()
driver.find_element_by_name("cardNumber").send_keys(cardNumber)

driver.find_element_by_name("expiration").click()
driver.find_element_by_name("expiration").send_keys(expiration)

driver.find_element_by_name("securityCode").click()
driver.find_element_by_name("securityCode").send_keys(securityCode)




driver.find_element_by_name("lastName").click()
driver.find_element_by_name("lastName").send_keys(lastName)

driver.find_element_by_name("firstName").click()
driver.find_element_by_name("firstName").send_keys(firstName)



#dropdown.find_element_by_xpath("//option[. = '新北市']").click()
#//driver.find_element_by_id("city").click()

driver.find_elements_by_tag_name("")


driver.find_element_by_name("street").click()
driver.find_element_by_name("street").send_keys(street)

driver.find_element_by_name("postalCode").click()
driver.find_element_by_name("postalCode").send_keys(postalCode)

driver.find_element_by_css_selector(".form-selector-group:nth-child(5) .form-selector-label").click()
driver.find_element_by_css_selector(".form-selector-group:nth-child(5) .row .row").click()
driver.find_element_by_id("recon-0-229").click()
driver.find_element_by_id("recon-0-229").send_keys("1221")
driver.find_element_by_id("recon-0-230").click()
driver.find_element_by_id("recon-0-230").send_keys("1221")
driver.find_element_by_css_selector(".rs-fapiao").click()
driver.find_element_by_css_selector("#rs-checkout-continue-button-bottom > span").click()
driver.find_element_by_id("rs-checkout-continue-button-bottom").click()