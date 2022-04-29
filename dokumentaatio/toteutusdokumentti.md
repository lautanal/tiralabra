# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma on toteutettu Python-kielellä (versio 3.8.8) olio-ohjelmointia käyttäen.  

Koodin yleisrakenne on seuraava:

<img src="/dokumentaatio/png/uml-kaavio-ver2.png" width="750">

- Pääohjelma bestroute.py käynnistää Ui-luokan määrittelemän käyttöliittymän
- Ui-luokka luo Pygame-kirjaston avulla graafisen käyttöliittymän
- Ui-luokka luo Map-luokan olion, joka mallintaa ruutukarttaa
- Map luokka luo Node-luokan oliot, jotka mallintavat kartan ruutuja
- Ui luokka luo Algorithm-luokan olion, joka käynnistää polun etsinnän
- Algorithm-instanssi kutsuu käyttäjän valinnan mukaan tarvittavaa algoritmia (Dijkstra, A* tai IDA*)
- Dijkstra-algoritmi käyttää minimikeon tietorakenteena Bheap-luokkaa
- Piirtorutiinit on keskitetty Draw-luokkaan
- Tiedostojen luku ja kirjoitus tehdään Files-luokan avulla
- Suorituskykytestit tehdään Perftest-luokan avulla

## Käytetyt algoritmit ja tietorakenteet

Parhaan reitin hakemisessa on käytetty kolmea vaihtoehtoista algoritmia:

### Dijkstra
Dijkstran menetelmä käyttää minimikekoa käsiteltävien solmujen tallennukseen.  Ohjelma ottaa keosta käsittelyyn aina solmun, jonka etäisyysarvo lähtösolmusta on pienin.  Tässä ohjelmassa minimikeko on toteutettu omalla Bheap-luokalla.

### A*
A* -menetelmä on hyvin samankaltainen Dijkstran menetelmän kanssa.  Lisäksi käytössä on  heuristiikka, joka ennustaa etäisyyden maaliin.  A* -menetelmän minimikeko on toteutettu Pythonin standardikirjaston heapq-moduulin avulla.

### IDA*
IDA* -menetelmä yhdistää A*-menetelmään syvyyshaun.  Syvyyshaku etenee käsiteltävästä solmusta syvemmälle verkkoon kunnes saavutetaan ennalta määritelty hakukynnys. Seuraavalla hakukierroksella jatketaan solmusta, jolla on pienin hakukynnyksen ylittävä arvo.  IDA* -menetelmän minimikeko on toteutettu Pythonin standardikirjaston heapq-moduulin avulla.

### Jump Point Search
IDA* -menetelmä yhdistää A*-menetelmään syvyyshaun.  Syvyyshaku etenee käsiteltävästä solmusta syvemmälle verkkoon kunnes saavutetaan ennalta määritelty hakukynnys. Seuraavalla hakukierroksella jatketaan solmusta, jolla on pienin hakukynnyksen ylittävä arvo.  IDA* -menetelmän minimikeko on toteutettu Pythonin standardikirjaston heapq-moduulin avulla.


## Suorituskykyvertailu ja aikavaativuudet

Suorituskykytestit on tehty eri kokoisilla random-kartoilla.  Paras reitti on haettu kullakin kartalla kolmella eri menetelmällä.

Verkon koko | Solmut | Kaaret | V + E log V | Algoritmi | Hakuajan keskiarvo (10 karttaa)|
--------|--------|--------|--------|-------------|-------------|
| 100 x 100 | 10000 | 19800 | 273097 | Dijkstra | 0.0896 |
| | | | | A\* | 0.0367 |
| | | | | IDA\* | 0.5331 |
| 200 x 200 | 40000 | 79600 | 1256902 | Dijkstra | 0.3970 |
| | | | | A\*     | 0.1560 |
| | | | | IDA\*   | 3.9088 |
| 300 x 300 | 90000 | 179400 | 2042500 | Dijkstra | 0.9518 |
| | | | | A\*     | 0.3692 |
| | | | | IDA\*   | 13.3590 |
| 400 x 400 | 160000 | 319200 | 5678238 | Dijkstra | 1.7554 |
| | | | | A\*      | 0.6370 |
| | | | | IDA\*    | 29.5708 |
| 500 x 500 | 250000 | 499000 | 9197853 | Dijkstra | 2.8174  |
| | | | | A\*     | 1.0455  |
| | | | | IDA\*   | 56.3359 |

Mitatut Dijkstran ja A\* -menetelmän aikavaativuudet vastaavat hyvin teorian mukaista O(V + E logV) aikavaativuutta.

<img src="/dokumentaatio/png/aikavaativuus.png" width="750">

A\* -menetelmä on kautta linjan nopein vaikka tämän kaltaisessa verkossa heuristiikka ei toimi parhaalla mahdollisella tavalla.  Dijkstran menetelmä toimii myös melko hyvin, mutta IDA\* ei näytä olevan hyvä ratkaisija tämän tapaisessa verkossa.

## Puutteet ja parannukset

Pygame-kirjaston animaatio polun etsinnän etenemisestä on vielä toivottoman hidas.  En ole ehtinyt perehtyä, mistä tämä johtuu.  Todennäköisesti sitä pystyy nopeuttamaan huomattavasti.

JPS-menetelmää ei voi suoraan käyttää painotetussa ruutuverkossa.  Sitä voisi kuitenkin käyttää kun verkon kaikki solmut ovat saman painoisia.  JPS-menetelmän implementaatio on vielä työn alla.