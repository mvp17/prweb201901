#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set file encoding = utf-8

from urllib.request import urlopen
import bs4


class WebScraping(object):

    def __init__(self):
        super(WebScraping, self).__init__()

    @staticmethod
    def getHtml():
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
    def printData(tuples):
        print("\n")
        for i in range(len(tuples)):
            print("Title: ", tuples[i][0], " ", "Current Price: ", tuples[i][1], " ", "Old Price: ", tuples[i][2])

    @staticmethod
    def getTuples(titles, prices):
        tuples = []
        for i in range(len(titles)):
            tuples.append((titles[i], prices[i][0], prices[i][1]))
        return tuples

    def scrapingProcess(self, html):
        tree = bs4.BeautifulSoup(html, "lxml")
        titles = self.getTitles(tree)
        prices = self.getPrices(tree)
        tuples = self.getTuples(titles, prices)
        self.printData(tuples)

    def run(self):
        html = self.getHtml()
        self.scrapingProcess(html)


if __name__ == "__main__":
    webScraping = WebScraping()
    webScraping.run()
