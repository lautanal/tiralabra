## Aihe

Sovellus on pikselikarttaa hyväksi käyttävä navigaattori, joka löytää lyhimmän tai nopeimman reitin kahden pisteen välillä.  Kartan pikselien väri merkitsee joko kuljettavaa reittiä tai estettä.  Pikselien väri voi merkitä nopeampaa tai hitaampaa reittiä.

## Ohjelmointikieli

Ohjelmointikielenä käytetään Pythonia (versio 3.9)

## Algoritmit ja tietorakenteet

Polunetsinnän nopeutta testataan kahdella eri algoritmilla, jotka ovat Dijkstran perinteinen ja Jump Point Search.

## Ohjelman syötteet ja tulosteet

Ohjelma lataa pohjaksi halutun png-tiedoston.  Png-kuvan eri värit merkitsevät joko kuljettavaa reittiä tai estettä.  Jos aikaa riittää, eri väreille voidaan asettaa eri etenemisnopeudet.

Käyttäjä valitsee halutun reitin alku- ja loppupisteet sekä käytetyn algoritmin ja muut tarvittavat parametrit.

Ohjelma näyttää polunetsinnän etenemisen visuaalisesti

## Aika- ja tilavaativuudet

Aikavaatimus: O((|V|+|E|)\log |V|)
Tilavaatimus: O(|E|)

## Lähteet

[Dijkstra Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[JPS Wikipedia](https://en.wikipedia.org/wiki/Jump_point_search)

## Opinto-ohjelma

Tietojenkäsittelyn kandidaatti

## Dokumentaation kieli

Suomi
