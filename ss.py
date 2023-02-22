#import all necesaries libraries
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#set up path andf binary location
import time
options = Options()
#setup your own mozilla firefox location
options.binary_location=rf'C:\Program Files\Mozilla Firefox\firefox.exe'
#setup yout own geckodriver location
path=rf'C:\Users\Usuario\Desktop\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path,options=options)
#load linkedin (you must set your own login page)
driver.get("https://www.linkedin.com/")
#accepting cookies (you must setup your own xpath)
i=driver.find_element('xpath','/html/body/nav/div/a[2]')
i.click()
#reading cheatsheet
f=open('commands.txt','r')
for i in f:
    #e=username (you must setup your own xpath)
    e=driver.find_element('xpath','//*[@id="username"]')
    e.clear()
    e.send_keys(i)
    #p=password (you must setup your own xpath)
    p=driver.find_element('xpath','//*[@id="password"]')
    p.clear()
    p.send_keys(i)
    #try login (you must setup your own xpath)
    b=driver.find_element("xpath","/html/body/div/main/div[3]/div[1]/form/div[3]/button")
    b.click()