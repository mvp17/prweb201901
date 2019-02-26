#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set file encoding = utf-8

from urllib.request import urlopen
# import bs4
# import xmltodict
import json


class ClientWeb(object):
    """Web client for openwearthermap"""

    def __init__(self):
        super(ClientWeb, self).__init__()

    @staticmethod
    def do_request():
        # https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid=81e8695c285ce7e2fba13e0c7d7d811d
        f = urlopen("https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid"
                    "=81e8695c285ce7e2fba13e0c7d7d811d&mode=json&lang=ca")
        data = f.read()
        f.close()
        return data

    def run(self):
        # download html
        data = self.do_request()
        # process data
        data = self.process_weather(data)
        # print data
        print(data)

    @staticmethod
    def process_weather(html):
        # dic = xmltodict.parse(html)
        dic1 = json.loads(html)
        temp = dic1['list'][0]['main']['temp']
        weather = dic1['list'][0]['weather'][0]['description']
        return str(temp)+" and "+str(weather)


"""
            def process_weather(self, html):
                print(html)
                arbre = bs4.BeautifulSoup(html, features="lxml")  # TODO: fix features
                temperature = arbre.find("temperature")
                weather = arbre.find("weather")
                print(temperature["value"] + "and" + weather["value"])
                return " "
"""


if __name__ == "__main__":
    c = ClientWeb()
    c.run()