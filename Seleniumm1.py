from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("Test case started")  
driver = webdriver.Chrome('chromedriver.exe')  
 
driver.maximize_window()  
driver.get("https://www.google.com/")  
driver.find_element_by_name("q").send_keys("githubarjunvankani")  
time.sleep(3)  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)


driver.close()  
print("Test case successfully completed")