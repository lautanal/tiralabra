## Viikko 5

<img src="/dokumentaatio/png/viikko5.png" width="750">

### Yksikkötestit

<img src="/dokumentaatio/png/testikattavuus.png" width="750">

Yksikkötestien kattavuus on melko hyvä.  Käyttöliittymän ja Pygame-piirtorutiinit olen jättänyt kokonaan testien ulkopuolelle.  Yksikkötestejä enemmän olen keskittynyt empiiriseen vertailevaan testaamiseen.

### Suorituskykytestit

Suorituskykyä on vertailu eri kokoisilla random-kartoilla.  Paras reitti on haettu samalla kartalla eri menetelmillä.  Tuloksia on vertailtu ja tarkastettu, että menetelmät antavat yhtäpitävät tulokset.

Alla oleva taulukko kertoo eri menetelmien nopeuden eri suuruisilla random-ruutukartoilla.  Raportoitu tulos on kymmenen kartan hakuajan keskiarvo.

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

### Havaintoja matkan varrelta

A* -menetelmä on kautta linjan paras vaikka sen heuristiikka olekaan parhaimmillaan tällaisella painotetulla ruutukartalla.  IDA* -menetelmä ei ilmeisesti sovellu parhaalla mahdollisella tavalla tämänlaiseen hakuongelmaan.

Dijkstra ja A* -menetelmien mitatut nopeudet toteuttavat hyvin O(V + E logV) aikavaativuuden.

<img src="/dokumentaatio/png/aikavaativuus.png" width="750">

### Työtunnit

Tähän mennessä käytetty aikaa 98 tuntia.  

### Seuraava viikko

Ensi viikolla parantelen vielä ohjelman käyttöliittymää ja ajan salliessa ohjelmoin JPS-menetelmän algoritmin.



