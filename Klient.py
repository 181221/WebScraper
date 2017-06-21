import schedule
import time
from pushbullet import Pushbullet
from Pris import Pris
from WebScrape import Webscrape

def main():
    prisen = Pris()
    prisen.currentPris = Webscrape.webScrape()
    prisen.forjePris = prisen.currentPris
    pb = Pushbullet("skriv inn api key her")

    while Webscrape.kjorProg:
        if prisen.forjePris != prisen.currentPris:
            Webscrape.kjorProg = False
            print(Webscrape.kjorProg)
            print("Pris er oppdatert:")
        else:
            prisen.forjePris = prisen.currentPris
            prisen.currentPris = Webscrape.webScrape()
            print(prisen.currentPris)
            schedule.run_pending()
            time.sleep(14400) #sleep 4 timer kjør igjen.
    if Webscrape.kjorProg is False:
        push = pb.push_note("Prisendring", "Prisen er nå {} ".format(str(prisen.currentPris)))

main()
