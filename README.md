# prweb201901

Getting the titles and the prices of all products, it's scraped from the full lxml. Sometimes, there was an AttributeError (Nonetype), that problem appeared in scraping the prices. To solve it, it's checked if the price-old scrap was None, because it was which generated the conflict. The gathered data has stored in tuple form of the style (Title, Current Price, Old Price) to print easily the data.
