#!/usr/bin/env python
#vim fileencoding = utf-8

from urllib.request import urlopen
import bs4

class ClientWeb(object):
    """Client web per la web de la EPS"""
    def __init__(self):
        super(ClientWeb, self).__init__()

    def descarregar_html():
        f = urlopen("http://www.eps.udl.cat/ca/")
        html = f.read()
        f.close()
        return html

    def buscar_activitats(self, html):
        arbre = bs4.BeautifulSoup(html, features = "lxml")
        activitats = arbre.find_all("div","featured-links-item")
        return activitats


    def run(self):
        #descarregar-me html
        html = self.descarregar_html()
        #buscar activitats
        activitats = self.buscar_activitats(html)
        #imprimir resultat
        print(activitats)

if __name__=="__main__":
    c = ClientWeb()
    c.run()
