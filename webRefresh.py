#Constantly refreshes page at a rate of choice
#Must download selenium first
from selenium import webdriver
import time
import urllib
import urllib2

x=input("Enter the URL you wish to refresh:")
r=input("Enter the number of seconds till next refresh:")
r=int(r)
driver = webdriver.Firefox()
driver.get(x)
while True:
    time.sleep(r)
    driver.refresh()
