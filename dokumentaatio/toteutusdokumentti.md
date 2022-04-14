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

## Aikavaativuudet ja käytetyt tietorakenteet

## Tilavaativuudet

## Suorituskykyvertailu eri pituisilla avaimilla

Verkon laajuus | Algoritmi | Keskiarvo (10 suorituskertaa)|
-----|----------|-------------|
