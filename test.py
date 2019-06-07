#documentation : https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_dynamic_websites.htm

from selenium import webdriver

PROXY="127.0.0.1:3128"
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
path = r'/usr/local/sbin/chromedriver'
driver = webdriver.Chrome(executable_path=path,options=options)
driver.get("http://www.aip-immobilier.fr/recherche,basic.htm?ci=290019&idqfix=1&idtt=2&idtypebien=2&saisie=Brest&tri=d_dt_crea&")

driver.close()