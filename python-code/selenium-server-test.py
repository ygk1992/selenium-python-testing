from selenium import webdriver
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
option=Options()
option.add_argument("ignore-infobars")
option.add_argument("--ignore-certificate-errors")
driver=webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME,options=option)
driver.get("http://www.baidu.com")
print(driver.title)

