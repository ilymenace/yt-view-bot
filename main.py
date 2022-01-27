deom selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_Path="the location of google drivers on your device")
driver2 = webdriver.Chrome(executable_Path="the location of google drivers on your device")
driver3 = webdriver.Chrome(executable_Path="the location of google drivers on your device")

driver1.get("link of video")
driver2.get("link of video")
driver3.get("link of video")

while true:
  sleep(60) #you can change the time deppending on the lenght of video
  driver1.refresh()
  driver2.refresh()
  driver3.refresh()
