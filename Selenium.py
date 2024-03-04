'''Selenium'''
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
from time import sleep
from selenium.webdriver.chrome.options import Options
import keyboard
from termcolor import cprint
k=1                                  
def urll(website,urls,strng,c):
    global k
    chrome_options = Options()

    chrome_options.add_argument('--headless')

    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_argument('--disable-dev-shm-usage')
    driver=webdriver.Chrome(executable_path=r"/home/alphx/chrome-driver/chromedriver",chrome_options=chrome_options)
    
    for Url,name  in zip(urls,strng): #use itertools.izip()
        if(name!=None):
            cprint(k,"green",end="")
            print(".",end="")
            cprint(name,"cyan",end="")
            print(".....")
        else:
            name = Url
            cprint(k,"green",end="")
            print(".",end="")
            cprint(name,"cyan",end="")
            print(".....")
    
        try:
            if("http" in Url or "https" in Url or ".com" in Url):
                driver.get(Url)
            elif("/" in Url):
                driver.get(website + Url)
            else:
                driver.get(website + "/" + Url)
            driver.maximize_window()
            sleep(2)
            if("." not in name):
                driver.save_screenshot(os.getcwd() + "/Screen-Shots/" + name + str(k) +"_ss.png")
            else:
                driver.save_screenshot(os.getcwd()+"/Screen-Shots/" + (name.split("."))[1] + "_" + str(k) +"_ss.png")
            print("Next...")
        except:
            pass
            
        k+=1
        if(k%10==0):
            ans=input("take more ss?(y/n):")
            if( ans =="Y" or ans =="y"):
                continue
            else:
                break
    driver.close()
 