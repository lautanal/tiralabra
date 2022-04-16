# Käyttöohje

## Ohjelman lataus

Lataa sovelluksen [release](https://github.com/lautanal/tiralabra/releases/tag/VIIKKO5).

## Ohjelman asentaminen

Ohjelma kopioidaan haluttuun hakemistoon.

Hakemistoon luodaan virtuaaliympäristö seuraavasti:

$ poetry install

## Ohjelman käynnistäminen

Ohjelma käynnistetään asennushakemistossa komennolla:

$ poetry run python3 src/bestroute.py

## Käyttöliittymä

Sovellusta käytetään Pygamella luodun käyttöliittymän avulla :

<img src="png/Ui.png" width="750">

Käyttäjä valitsee lähtö- ja maaliruudun hiiren vasemmalla näppäimellä.  Kun lähtö ja maali on valittu, hiiren vasemmalla näppäimellä voi asettaa esteet, joiden läpi reitti ei voi kulkea.
Lähdön ja maalin sekä esteet voi poistaa hiiren oikealla näppäimellä.

Haluttu menetelmä reitin hakemiseen valitaan näppäilemällä m.

Laskenta käynnistetään näppäilemällä s.

## Komennot

### Ohjelman näppäinkomennot:

c : clear, poistaa kartan ja generoi uuden

r : reset, pyyhkii lasketun reitin

m : metodi, Dijkstra / A* / IDA*

d : diagonal, polun tyyppi, vain x ja y-suunnat / väli-ilmansuunnat sallittu

s : start, laskee parhaan reitin

a : animointi, päälle / pois

t : test, ohjelma käy läpi kymmenen testikarttaa (koko 100 x 100) ja laskee keskimääräisen hakuajan
    eri menetelmille

\+ : lisää ruutujen lukumäärää 10:llä molemmissa suunnissa ja generoi uuden kartan

\- : vähentää ruutujen lukumäärää 10:llä molemmissa suunnissa ja generoi uuden kartan

1 : lataa kartta 1.map (hakemistosta maps)

2 : lataa kartta 2.map (hakemistosta maps)

w : write, talleta kartta tiedostoon f.map (hakemistoon maps)

f : file, lue karttatiedosto f.map (hakemistosta maps)

e : edit, editoi karttaa

q : quit, lopeta editointi

### Hiiren toiminnot:

Hiiren vasen näppäin valitsee reitin lähtöpisteen (jos sitä ei ole ennestään kartalla)

Hiiren vasen näppäin valitsee reitin maalipisteen (kun lähtöpiste on valittu ja maalipiste puuttuu)

Hiiren vasen näppän asettaa esteen (kun alku- ja maalipiste on asetettu)

Hiiren oikea näppäin pyyhkii ruudun (alkupisteen, maalipisteen tai esteen)

Editoinnissa hiiren vasen näppäin lisää ruudun painoarvoa, oikea vähentää





