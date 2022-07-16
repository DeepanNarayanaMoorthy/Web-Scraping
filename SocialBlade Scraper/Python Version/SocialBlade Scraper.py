from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pprint
import time


def getdataa(path, username):
    chromeOptions = Options();
    chromeOptions.add_argument("--start-maximized");
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--window-size=1920,1080')
    chromeOptions.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Safari/537.36')
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument('--start-fullscreen')
    chromeOptions.add_argument('--single-process')
    chromeOptions.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=pathh, options=chromeOptions)#, desired_capabilities=caps)
    time.sleep(2)
    driver.get("https://socialblade.com/login");
    driver.find_element_by_name("dashboard_email").send_keys("yyxx0610@gmail.com")
    driver.find_element_by_name("dashboard_password").send_keys("deepan2000")
    driver.find_element_by_css_selector("#login-submit > input").click()
    time.sleep(2)
    driver.get("https://socialblade.com/instagram/user/"+username)
    time.sleep(2)
    chartcount=driver.execute_script("return Highcharts.chartCount")
    dictt={}
    for i in range(chartcount):
        namee=driver.execute_script("return Highcharts.charts["+str(i)+"].title.textStr")
        dataa=driver.execute_script("return Highcharts.charts["+str(i)+"].options.series[0].data")
        dictt[namee]=dataa
    time.sleep(2)
    htmlinfolen=driver.execute_script('return document.getElementsByClassName("YouTubeUserTopInfo").length')
    htmlinfos=[]
    for i in range(htmlinfolen):
        txtt=driver.execute_script('return document.getElementsByClassName("YouTubeUserTopInfo")['+str(i)+'].innerText')
        htmlinfos.append(txtt)
    time.sleep(2)
    FOLLOWERS_RANK=driver.execute_script('return document.querySelector("#socialblade-user-content > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > p").innerText')
    FOLLOWING_RANK=driver.execute_script('return document.querySelector("#socialblade-user-content > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p").innerText')
    ENGAGEMENT_RANK=driver.execute_script('return document.querySelector("#socialblade-user-content > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > p").innerText')
    MEDIA_RANK=driver.execute_script('return document.querySelector("#socialblade-user-content > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > p").innerText')
    time.sleep(2)
    somelist=[FOLLOWERS_RANK, FOLLOWING_RANK, ENGAGEMENT_RANK, MEDIA_RANK]
    somelist=[int(''.join(filter(str.isdigit, i))) for i in somelist]
    somelist={"FOLLOWERS_RANK":somelist[0], "FOLLOWING_RANK":somelist[1], "ENGAGEMENT_RANK":somelist[2], "MEDIA_RANK":somelist[3]}
    time.sleep(2)
    finalcontentt=[htmlinfos, somelist, dictt]
    return finalcontentt

# pathh=r'C:\Users\deepa\Pictures\chromedriver_win32\chromedriver.exe')
pathh=r"C:\Program Files\Google\Chrome\Application\chrome.exe"

pprint.pprint(getdataa(pathh, "ihansika"))

