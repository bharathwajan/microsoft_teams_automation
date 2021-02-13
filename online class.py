from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import datetime
from datetime import date
import time
import calendar
from selenium.webdriver.chrome.options import Options



chromedriver="C:\chromedriver"  #place the file path of your chrome driver 
chrome_options = webdriver.ChromeOptions()
driver=webdriver.Chrome(chromedriver,options=chrome_options)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
driver=webdriver.Chrome(chromedriver,options=chrome_options)
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

# Pass the argument 1 to allow and 2 to block


driver.get('https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/group-chat-software')

time.sleep(15)

driver.find_element_by_xpath('//a[@class="c-button f-secondary ow-slide-in ow-slide-in-2 xs-ow-mr-0 ow-mt-10 ow-txt-trans-upper ow-bvr-signin"]').click()

driver.switch_to.window(driver.window_handles[1])#switching to tab 1 
time.sleep(5)

driver.switch_to_active_element().send_keys('enter your username here')
time.sleep(2)
driver.find_element_by_xpath('//input[@class="button ext-button primary ext-primary"]').click()
print('username entered')
time.sleep(5)

driver.switch_to_active_element().send_keys('enter your password here')
time.sleep(2)
driver.find_element_by_xpath('//input[@id="idSIButton9"]').click()
print('password entered')
time.sleep(10)

time.sleep(5)
driver.find_element_by_xpath('//input[@class="button ext-button primary ext-primary"]').click()#yes button always remember
print('yes button is clicked')
time.sleep(10)

driver.find_element_by_xpath('/html/body/promote-desktop/div/div/div/div[1]/div[2]/div/a').click()
time.sleep(10)
print('using web app')

driver.find_element_by_xpath('//div[@class="team-card"]').click()#clicking team card
print('team is selected')
time.sleep(5)



def pom():
    print('Its POM hour')
    time.sleep(10)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/left-rail/div/div/school-app-left-rail/single-team-channel-list/div/div/div/div[3]/ul/li[8]/a/div[1]/span").click()
    time.sleep(15)                          
    driver.find_element_by_xpath("//button[@class='ts-sym ts-btn ts-btn-primary inset-border icons-call-jump-in ts-calling-join-button app-title-bar-button app-icons-fill-hover call-jump-in']").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]").click()
    driver.find_element_by_xpath("//button[@class='join-btn ts-btn inset-border ts-btn-primary']").click()
def cc():
    print('Its cc hour')
    time.sleep(10)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/left-rail/div/div/school-app-left-rail/single-team-channel-list/div/div/div/div[3]/ul/li[4]/a/div[1]/span").click()
    time.sleep(15)                     
    driver.find_element_by_xpath("//button[@class='ts-sym ts-btn ts-btn-primary inset-border icons-call-jump-in ts-calling-join-button app-title-bar-button app-icons-fill-hover call-jump-in']").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]").click()
    driver.find_element_by_xpath("//button[@class='join-btn ts-btn inset-border ts-btn-primary']").click()
def spm():
    print('Its spm hour')
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='channel-19:bee78f364be04d49824795d89c70c627@thread.tacv2']/a/div[1]/span").click()
    time.sleep(15)
    driver.find_element_by_xpath("//button[@class='ts-sym ts-btn ts-btn-primary inset-border icons-call-jump-in ts-calling-join-button app-title-bar-button app-icons-fill-hover call-jump-in']").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]").click()
    driver.find_element_by_xpath("//button[@class='join-btn ts-btn inset-border ts-btn-primary']").click()
def ire():
    print('Its ire hour')
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='channel-19:7bf76d7da80143bfbec4101bbc488760@thread.tacv2']/a/div[1]/span").click()
    time.sleep(15)
    driver.find_element_by_xpath("//button[@class='ts-sym ts-btn ts-btn-primary inset-border icons-call-jump-in ts-calling-join-button app-title-bar-button app-icons-fill-hover call-jump-in']").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]").click()
    driver.find_element_by_xpath("//button[@class='join-btn ts-btn inset-border ts-btn-primary']").click()
def cns():
    print('Its cns hour')
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='channel-19:f78d136d2d36407aa88f30a449b0d918@thread.tacv2']/a/div[1]/span").click()
    time.sleep(15)
    driver.find_element_by_xpath("//button[@class='ts-sym ts-btn ts-btn-primary inset-border icons-call-jump-in ts-calling-join-button app-title-bar-button app-icons-fill-hover call-jump-in']").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]").click()
    driver.find_element_by_xpath("//button[@class='join-btn ts-btn inset-border ts-btn-primary']").click()
    
def csharp():
    print('Its csharp hour')
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='channel-19:b61c5ca30edc4138a4930fa458df7f8b@thread.tacv2']/a/div[1]/span").click()
    time.sleep(15)
    driver.find_element_by_xpath("//button[@class='ts-sym ts-btn ts-btn-primary inset-border icons-call-jump-in ts-calling-join-button app-title-bar-button app-icons-fill-hover call-jump-in']").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]").click()
    driver.find_element_by_xpath("//button[@class='join-btn ts-btn inset-border ts-btn-primary']").click()
    
c=datetime.datetime.now()
d=c.strftime("%H%M")
e=int(d)#time as integer
print("the current time is :")
print(e)

today=date.today()
day=today.day
year=today.year
month=today.month
a=calendar.weekday(year,month,day)#weekday function says the day number say: thurusday is 3
b=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(b[a])

if a==0:
    if 910<e<1110:
        cc()
    elif 1111<e<1250:
        pom()
        
        
elif a==1:
     if 910<e<1110:
        pom()
     elif 1111<e<1250: 
        cns()
    
elif a==2:
     if 910<e<1110:
        pom()
     elif 1111<e<1250:
        cns()
   
elif a==3:
     if 910<e<1110:
        spm()
     elif 1111<e<1250:
        csharp()
    
elif a==4:
     if 910<e<1110:
        ire()
     elif 1111<e<1250:
        csharp()
    
elif a==5:
     if 910<e<1110:
        cc()
     elif 1111<e<1250:
        ire()
elif a==6:
    print('happy holiday')

print('sucess')
    

