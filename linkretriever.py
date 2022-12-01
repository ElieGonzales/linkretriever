from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pag
from time import sleep

print('this program will get you all the links in a website')
website = input('enter a website (include https://): ')
openlinks = False
platform = input("please input a platform (Chrome/Firefox/Edge): ")
dotext = input('do you want the shown text as well? [Y/N]: ')

if website[:7] != "https://":
    website = "https://" + website

if platform.lower() == "chrome" or platform.lower() == "google chrome":
    driver = webdriver.Chrome()
elif platform.lower() == "edge" or platform.lower() == "microsoft edge":
    driver = webdriver.Edge()
elif platform.lower() == "firefox":
    driver = webdriver.Firefox()
else:
    print("please use one of the following platforms: chrome, edge, firefox")

try:  
    driver.get(website)
    links = driver.find_elements(By.XPATH,"//*[@href]")
    links = list(dict.fromkeys(links))
    finstr = ''
    finlinks = []
    for link in links:
        print(link.get_attribute('href'), "as" ,link.text)
        if openlinks:
            pag.hotkey('ctrl','t')
            pag.typewrite(link.get_attribute('href'))
            pag.hotkey('return')
            sleep(0.5)
        if dotext.lower() == 'y' or dotext.lower() == 'yes':
            textlink = link.text + " = " + link.get_attribute('href')
            finlinks.append(textlink)
        else:    
            finlinks.append(link.get_attribute('href'))

    with open('links.txt','w') as file:
        for i in finlinks:
            finstr = finstr + i + '\n'
        file.write(finstr)
except Exception as error:
    print("An error occured: "+ error)
finally:
    driver.close()
    input("press enter to close")

