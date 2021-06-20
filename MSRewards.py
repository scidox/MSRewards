#!/usr/bin/env python3

import random
import webbrowser
import time
import os
import selenium.webdriver as webdriver

#login in your bing account manually on edge and chrome

#insert address edge file location
edge="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None,webbrowser.BackgroundBrowser(edge))

user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1'
#if you want to change user agent open firefox> Ctrl+Alt+m and choose the new user_agent
profile= webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override',user_agent)
#insert in the folder geckodriver.exe, download from https://github.com/mozilla/geckodriver/releases
FireFoxDriverPath= os.path.join(os.getcwd(), 'Drivers',r"C:\Users\Giorgio\Desktop\py\geckodriver.exe")
url='https://www.bing.com'
browser=webdriver.Firefox(executable_path=FireFoxDriverPath,firefox_profile=profile)
browser.get(url)

#now login in your mobile bing account manually
time.sleep(50)

#if you want to search for a text file  enable the following 2 lines and comment line: file=open('a.txt')
#name= input ("What content of the text file do you want to search on web? ")
#file=open(name)

#create in your folder a file txt with the words you want to search for
file=open('a.txt')

cicli=54

for n in range(cicli):
        a=n+1
        if a<35:
                 
            if a<31:
                print('chrome')       
                print('iteration',+(a),'of',+(cicli))
                lettura=file.readline()
                value=random.randint(4,14)
                print(lettura)
                webbrowser.open('https://www.bing.com/search?q='+str(lettura))
                time.sleep(value)
                
            else:
                print('desktop_edge')
                print('iteration',+(a),'of',+(cicli))
                lettura=file.readline()
                value=random.randint(3,13)
                print(lettura)                        
                webbrowser.get('edge').open_new_tab('https://www.bing.com/search?q='+str(lettura))       
                time.sleep(value)
                
        else:   

            print('mobile')
            print('iteration',+(a),'of',+(cicli))
            lettura=file.readline()
            value=random.randint(5,15)
            print(lettura)
            browser.get('https://www.bing.com/search?q='+str(lettura))
            time.sleep(value)            
            
time.sleep(15)
#close all browser
browser.close()
os.system("taskkill /im chrome.exe /f")
os.system("taskkill /im msedge.exe /f")



