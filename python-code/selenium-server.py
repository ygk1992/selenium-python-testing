from selenium import webdriver;
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities;
 
# 获取远程浏览器driver，使用自己指定的selenium-server
def getChromeRemoteDriver(remoteUrl):
    return webdriver.Remote(command_executor=remoteUrl,desired_capabilities=DesiredCapabilities.CHROME)
	
getChromeRemoteDriver("http://127.0.0.1:4444/wd/hub");
