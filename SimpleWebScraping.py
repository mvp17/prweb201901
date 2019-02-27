#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set file encoding = utf-8

from urllib.request import urlopen
import bs4


class WebScraping(object):

    def __init__(self):
        super(WebScraping, self).__init__()

    @staticmethod
    def get_html():
        url = urlopen("https://www.banggood.com/Flashdeals.html")
        data = url.read()
        url.close()
        return data

    @staticmethod
    def scraping_process(html):
        tree = bs4.BeautifulSoup(html, "lxml")
        products = tree.find_all("ul", "goodlist_1")
        elements = []
        for element in products:
            offer = element.find("span", "price")
            regular = element.find("span", "price_old")
            title = element.find("span", "title")
            elements.append((title.text, (offer.text, regular.text)))
        return elements

    def run(self):
        html = self.get_html()
        data = self.scraping_process(html)
        print(data)


if __name__ == "__main__":
    webScraping = WebScraping()
    webScraping.run()
