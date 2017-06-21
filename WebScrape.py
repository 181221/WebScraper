from lxml import html
import requests

class Webscrape:
    kjorProg = True

    @staticmethod
    def webScrape():
        nettSide = requests.get('https://www.akademika.no/computer-organization-and-architecture-global-edition/william-stallings/9781292096858')
        tree = html.fromstring(nettSide.content)
        return tree.xpath('//*[@id="node-21225459"]/div[2]/div[2]/div[1]/span/text()')


