# WebScraper
Python programm for å tracke prisendring på en internettside. 

## Getting Started
Programmet krever en link til internettsiden du skal tracke og xpath elementet. 
Legg også til pushbullet API key om du vil ha notifikasjon hvis en pris endres.

## Instruksjoner
I webscraper filen finner legger du inn nettaddressen og xpath elementet du finner xpath ved å bruke google chrome sin inspiser tool.
finn elemenet ok trykk copy xpath. 
Husk å legg til "/text()" på slutten av xpathen.

![Alt text](https://github.com/h181221/WebScraper/blob/master/xpath.JPG?raw=true "Optional Title")

slik vil xpathen se ut.
'//*[@id="node-21225459"]/div[2]/div[2]/div[1]/span/text()'

## info
programmet kjører hver fjerde time dette kan endres på i sleep funksjonen i klienten. 

