from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")


inputboxes =  driver.find_elements(By.CLASS_NAME,'text_field')

print(len(inputboxes))
print("Hello world")

driver.find_elements(By.ID,'RESULT_TextField-1').send_keys("Mithu")