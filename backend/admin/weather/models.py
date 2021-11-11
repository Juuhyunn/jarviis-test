import time

import pandas as pd
from django.db import models

# Create your models here.
from admin.common.models import ValueObject
from bs4 import BeautifulSoup
from selenium import webdriver


class Weather(object):
    def __init__(self):
        pass

    def process(self):
        vo = ValueObject()
        # self.search_old(vo)
        # self.search_now(vo)


    def search_now(self, vo):
        vo.context = 'admin/weather/data/'
        vo.url = 'https://www.weather.go.kr/w/index.do#'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver.exe')
        driver.maximize_window()
        driver.get(vo.url)
        time.sleep(3)
        search = driver.find_element_by_class_name('input')
        search.clear()
        search.send_keys("동작구")
        time.sleep(3)
        driver.find_element_by_css_selector("#index-local-search > div.cmp-local-search-items.on.opened.places > ul > li:nth-child(1) > a").click()
        self.crawling_now(driver)

    def crawling_now(self, driver):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # weather = soup.find('span', {'class':'wic DB05 large'}).string
        weather = soup.find('span', {'class':'wic DB05'}).string
        location = soup.find_all('div', {'class':'serch-area accordionsecond-wrap'})
        driver.close()
        print(location)
        print(weather)

    def search_old(self, vo):
        vo.context = 'admin/weather/data/'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver.exe')
        loc = "108"  # 서울
        year = "2021"  # 년도
        weather = self.crawing_weather(vo, loc, year, driver)
        # cloud = self.crawing_cloud(vo, loc, year, driver)
        self.weather_to_dict(weather)


    def crawing_weather(self, vo, loc, year, driver):
        weather_keyword = "obs=90&x=19&y=11"  # 비, 눈, 소나기 등
        vo.url = f'http://web.kma.go.kr/weather/climate/past_table.jsp?stn={loc}&yy={year}&{weather_keyword}'
        driver.maximize_window()
        driver.get(vo.url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        weather = soup.find_all('table', {'class': 'table_develop'})
        driver.close()
        # print(weather)
        return weather

    def crawing_cloud(self, vo, loc, year, driver):
        cloud_keyword = "obs=59&x=25&y=9"  # 구름양
        vo.url = f'http://web.kma.go.kr/weather/climate/past_table.jsp?stn={loc}&yy={year}&{cloud_keyword}'
        driver.maximize_window()
        driver.get(vo.url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cloud = soup.find_all('table', {'class': 'table_develop'})
        driver.close()
        # print(cloud)
        return cloud

    def weather_to_dict(self, weather):
        month = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
        ls = str(weather).split('td')
        del ls[0]
        for i, j in enumerate(ls):
            ls[i] = j.replace('\n','')
            ls[i] = ls[i].replace('>','')
            ls[i] = ls[i].replace('<','')
            ls[i] = ls[i].replace('/','')
            ls[i] = ls[i].replace('\xa0','Unkown')
            ls[i] = ls[i].replace('trtr','')
            ls[i] = ls[i].replace('br',',')
            ls[i] = ls[i].replace(' scope="row"','')
        ls2 = []
        [ls2.append(i) for i in ls if i != '']
        del ls2[-1]
        ls3 = [ls2[i:i+13] for i in range(0, len(ls2), 13)]
        print(ls3)
        dict = {h+i[0]:i[j+1] for j, h in enumerate(month) for i in ls3}
        print(dict)












