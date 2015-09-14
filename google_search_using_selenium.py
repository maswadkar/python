__author__ = 'mbp'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


def getlink(search_string):
    result = []
    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.get('http://www.google.com/ncr')

    elem = browser.find_element_by_name('q')  # Find the search box
    elem.send_keys(search_string + " xls")
    elem.send_keys(Keys.RETURN)

    time.sleep(11)

    for i in range(4):
        # bing x_path = '//*[@id="b_results"]/li[' + str(i+1) +  ']/h2/a'
        x_path = '//*[@id="rso"]/div[2]/div[' + str(i+1) + ']/div/h3/a'
        try:
            elem = browser.find_element_by_xpath(x_path)
            result.append(elem.get_attribute('href'))
        except NoSuchElementException:
            print('SOMETHING IS wrong')
    time.sleep(1)
    browser.quit()
    return result


with open('xxx.txt', 'r') as fin:
        data = fin.read().splitlines(True)

with open('xxx.txt', 'w') as fout:
        fout.writelines(data[9:])

for s_string in range(0,9):
    x = getlink(data[s_string].strip())
    for i in range(4):
        try:
            fi = open('SearchLinks.txt',mode='a',newline='\n',encoding = 'utf8')
            fi.write(x[i] + '\n')
            fi.close()
        except IndexError:
            print('list index out of range')