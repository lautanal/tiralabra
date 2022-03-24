<img src="/dokumentaatio/png/reittikartta.png" width="750">

## Aihe

Kehitettävä sovellus on ruutukarttaa hyväksi käyttävä navigaattori, joka löytää parhaan reitin kahden pisteen välillä.  Kartan jokaisella ruuduilla on tietty arvo (esim. välillä 1-10), joka kertoo  kustannuksen tai ajan inkrementin reitin kulkiessa ruudun kautta.  Ruudun arvo korreloi tummuusasteen kanssa.  Mitä tummempi ruutu, sitä suurempi kustannus tai hitaampi reitti

## Ohjelmointikieli

Ohjelmointikielenä käytetään Pythonia (versio 3.8.8)

## Algoritmit ja tietorakenteet

Polunetsinnän nopeutta testataan ainakin kahdella eri algoritmilla, joita ovat Dijkstran perinteinen, A* ja Jump Point Search.

## Ohjelman syötteet ja tulosteet

Ohjelma lataa pohjaksi karttatiedoston tai generoi itse ruutu- tai pikselikartan.

Käyttäjä valitsee halutun reitin alku- ja loppupisteet sekä käytetyn algoritmin ja muut tarvittavat parametrit.

Ohjelma näyttää polun visuaalisesti.

## Aika- ja tilavaativuudet

Aikavaatimus: O((n + m log n)

Tilavaatimus: O(n)

## Lähteet

[Dijkstra Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[JPS Wikipedia](https://en.wikipedia.org/wiki/Jump_point_search)

## Opinto-ohjelma

Tietojenkäsittelyn kandidaatti

## Dokumentaation kieli

Suomi
