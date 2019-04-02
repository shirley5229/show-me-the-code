from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://book.douban.com")

#将获得cookie 的信息打印
cookie= driver.get_cookies()
print(cookie)
time.sleep(2)
c1={u'domain': u'book.douban.com',
u'value': u'48246448:m2K9sm17ri4',
u'name': u'dbcl2',
u'secure': False,
u'httpOnly': False,
u'path': '/'}



driver.add_cookie(c1)
time.sleep(2)
#刷新后，页面为登录状态
driver.refresh()
