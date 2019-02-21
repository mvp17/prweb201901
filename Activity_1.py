#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set file encoding = utf-8

from urllib.request import urlopen
import bs4


class Client_web(object):
    """Client web per la web de la Packt"""

    def __init__(self):
        super(Client_web, self).__init__()

    def descarregar_html(self):
        f = urlopen("https://www.packtpub.com/packt/offers/free-learning/")
        html = f.read()
        f.close()
        return html

    def getTitle(self, html):
        tree = bs4.BeautifulSoup(html, features="lxml")  # TODO fix features
        book = tree.find_all("div", "product__right")
        book_list = []
        for book in book:
            title = book.find("h2", "product_title")
            book_list.append(title)
        return book_list

    def run(self):
        html = self.descarregar_html()
        book = self.getTitle(html)
        print(book)


if __name__ == "__main__":
    c = Client_web()
    c.run()