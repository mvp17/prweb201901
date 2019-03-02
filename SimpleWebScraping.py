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
    def getTitles(tree):
        treeTitles = tree.find_all("span", "title")
        titles = []

        for title in treeTitles:
            titles.append(title.find("a").text)

        return titles

    @staticmethod
    def getPrices(tree):
        treePrices = tree.find_all("div", "priceitem")
        prices = []

        for price in treePrices:
            prices.append((price.find("span", "price").text, price.find("span", "price_old").text))

        return prices

    @staticmethod
    def printData(titles, prices):
        for i in range(len(titles)):
            print("Title: ", titles[i], " ", "Current Price: ", prices[i][0], " ", "Old Price: ", prices[i][1])
            print("\n")

    def scraping_process(self, html):
        tree = bs4.BeautifulSoup(html, "lxml")
        self.printData(self.getTitles(tree), self.getPrices(tree))

    def run(self):
        html = self.get_html()
        self.scraping_process(html)


if __name__ == "__main__":
    webScraping = WebScraping()
    webScraping.run()
