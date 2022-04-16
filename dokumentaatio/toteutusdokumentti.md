# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma on toteutettu Python-kielellä (versio 3.8.8) olio-ohjelmointia käyttäen.  

Koodin yleisrakenne on seuraava:

<img src="/dokumentaatio/png/uml-kaavio.png" width="750">

- Pääohjelma bestroute.py käynnistää Ui-luokan määrittelemän käyttöliittymän
- Ui-luokka luo Pygame-kirjaston avulla graafisen käyttöliittymän
- Ui-luokka luo Map-luokan olion, joka mallintaa ruutukarttaa
- Map luokka luo Node-luokan oliot, jotka mallintavat kartan ruutuja
- Ui luokka luo Algorithm-luokan olion, joka käynnistää polun etsinnän
- Algorithm-instanssi kutsuu käyttäjän valinnan mukaan tarvittavaa algoritmia (Dijkstra, A* tai IDA*)
- Dijkstra-algoritmi käyttää minimikeon tietorakenteena Bheap-luokkaa
- Piirtorutiinit on keskitetty Draw-luokkaan

## Aikavaativuudet ja käytetyt tietorakenteet

## Tilavaativuudet

## Suorituskykyvertailu eri suuruisilla ruutukartoilla

Verkon koko | Solmut | Kaaret | Algoritmi | Keskiarvo (10 suorituskertaa)|
--------|--------|--------|-------------|-------------|
100 x 100 | 10000 | 19800 | Dijkstra | 0.1508 |
          |       |       |  A\*     | 0.0990 |
          |       |       |  IDA\*   | 0.5368 |
200 x 200 | 40000 | 79600 | Dijkstra | 0.6351 |
          |       |       |  A\*     | 0.4020 |
          |       |       |  IDA\*   | 3.9984 |
300 x 300 | 90000 | 179400 | Dijkstra | 1.4897 |
          |       |        |  A\*     | 0.9183 |
          |       |        |  IDA\*   | 12.6262 |
400 x 400 | 160000 | 319200 | Dijkstra | 2.7773 |
          |        |       |  A\*      | 1.6956 |
          |        |       |  IDA\*    | 29.5669 |
500 x 500 | 250000 | 499000 | Dijkstra | 4.4715  |
          |        |        |  A\*     | 2.7333  |
          |        |        |  IDA\*   | 58.3025 |
          
Mitattu Dijkstran menetelmän aikavaativuus vastaa hyvin teorian mukaista O(V + E logV) aikavaativuutta.  A\* -menetelmän aikavaativuus on hieman parempi kuin Dijkstran menetelmän.  IDA\* -menetelmän aikavaativuus on tämän testin mukaan lähinnä O(E + V)

