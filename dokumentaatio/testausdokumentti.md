## Testausdokumentti

### Yksikkötestit

Yksikkötestit eivät ole niin tärkeitä tässä sovelluksessa, koska ohjelman toiminta varmistetaan parhaiten vertailemalla visuaalisesti eri menetelmien tuloksia testikartoilla.  Olen kuitenkin tehnyt melko kattavat yksikkötestit, jotka ovat hyödyksi jos ohjelmaan tehdään jatkossa muutoksia.  Käyttöliittymä ja Pygame-piirtorutiinit on jätetty testauksen ulkopuolelle.

Yksikkötestit suoritetaan komennolla: poetry run coverage run --branch -m pytest src

Testikattavuus voidaan raportoida komennolla: poetry run coverage report -m 

Kattavuusraportti:

Name               Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------
src/algorithm.py      39      1     20      2    95%   39->exit, 64, 74->76
src/astar.py          34      1     14      1    96%   61
src/bheap.py          49      2     20      2    94%   34, 47
src/dijkstra.py       32      1     14      1    96%   59
src/idastar.py        59      2     28      1    97%   82-83
src/map.py           102      0     70      2    99%   113->115, 121->123
src/node.py           56      1      4      1    97%   120
--------------------------------------------------------------
TOTAL                371      8    170     10    97%


### Empiirinen testaus

Testaus on ollut pääosin kokeilevaa, manuaalista empiiristä testaamista.  Graafinen käyttöliittymä antaa tähän hyvän mahdollisuuden.

Graafinen käyttöliittymä helpottaa huomattavasti ohjelman toiminnan varmistamisessa ja räikeimpien ongelmien selvittämisessä. Esimerkiksi voidaan havaita, poikkeaako laskennan antama "paras" polku merkittävästi silmämääräisesti parhaalta tai lyhimmältä polulta. 

Ottamalla animointi käyttöön, voidaan tarkastella eri algoritmien etenemistä ja mitkä solmut ovat kulloinkin käsittelyssä ja missä järjestyksessä.  

Erilaisilla testikartoilla on varmistettu algoritmien toiminta ja oikeellisuus.  Kartalta on määritetty manuaalisesti lyhin reitti ja todettu, että algoritmit antavat saman tuloksen.


<img src="/dokumentaatio/png/testi05.png" width="750">


Suorituskykyä on vertailu eri kokoisilla random-kartoilla.  Paras reitti on haettu samalla kartalla kolmella eri menetelmällä.  On tarkastettu, että menetelmät antavat yhtäpitävät tulokset (polut voivat joskus olla hieman eroavat jos löytyy useampi yhtä hyvä reitti).  Suorituskykytestin tulokset löytyvät toteutusdokumentista.