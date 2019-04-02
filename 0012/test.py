from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import time

#driver=webdriver.Firefox()
options = FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(firefox_options=options)

driver.get('https://www.qiushibaike.com/')
time.sleep(2) # 浏览器加载需要时间

hots=driver.find_elements_by_xpath("//div[@class='recommend-article']/ul/li")
for content in hots:
    if 'qiushi_tag_' in content.get_attribute('id'):
        #<li>含有广告，使用qiushi_tag_过滤
        t=content.find_element_by_xpath("./div/a")
        print(t.text)
