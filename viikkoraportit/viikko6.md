## Viikko 6

<img src="/dokumentaatio/png/viikko6b.png" width="750">

### Jump Point Search

Koska aikatauluni salli, ohjelmoin myös Jump Point Search (JPS) -etsintärutiinin.  JPS-menetelmä eroaa sikäli muista toteutetuista menetelmistä, että ruutuverkon solmut eivät voi olla painotettuja.  JPS soveltuu polun etsintään myös vain kun vinot siirtymät ruutujen välillä on sallittu.

JPS-menetelmällä voidaan saavuttaa tietynlaisissa verkoissa merkittävä etu verrattuna vaikkapa Dijkstran ja A* -menetelmiin.  Kun verkossa on suurehkoja avoimia alueita, JPS pystyy hyppimään yli tarpeettomat ruudut ja nopeuttamaan etsintää.

## Suorituskykyvertailu random-kartoilla

Suorituskykytestit on tehty eri kokoisilla random-kartoilla.  Kartan ruudut ovat ilman painokertoimia ja polku voi kulkea viistoon ruutujen välillä.  Paras reitti on haettu kullakin kartalla neljällä eri menetelmällä (Dijkstra, A*, IDA* ja JPS).

Verkon koko | Solmut | Kaaret | V + E log V | Algoritmi | Hakuajan keskiarvo (10 karttaa)|
--------|--------|--------|--------|-------------|-------------|
| 100 x 100 | 10000 | 19800 | 273097 | Dijkstra | 0.1218 |
| | | | | A\* | 0.0508 |
| | | | | IDA\* | 0.5023 |
| | | | | JPS | 0.0357 |
| 200 x 200 | 40000 | 79600 | 1256902 | Dijkstra | 0.5343 |
| | | | | A\*     | 0.2319 |
| | | | | IDA\*   | 5.5076 |
| | | | | JPS | 0.2637 |
| 300 x 300 | 90000 | 179400 | 2042500 | Dijkstra | 1.2569 |
| | | | | A\*     | 0.5283 |
| | | | | IDA\*   | 18.9459 |
| | | | | JPS | 0.7785 |
| 400 x 400 | 160000 | 319200 | 5678238 | Dijkstra | 2.3001 |
| | | | | A\*      | 0.9362 |
| | | | | IDA\*    | 51.8285 |
| | | | | JPS | 1.6054 |
| 500 x 500 | 250000 | 499000 | 9197853 | Dijkstra | 3.6767  |
| | | | | A\*     | 1.4412  |
| | | | | IDA\*   | 109.4129 |
| | | | | JPS | 2.6955 |

### Havaintoja matkan varrelta

JPS-menetelmällä saavutetaan tietynlaisissa verkoissa merkittävä nopeusetu.  A* -menetelmä näyttää kuitenkin olevan paras yleismenetelmä kaikenlaisille verkoille.

### Työtunnit

Tähän mennessä käytetty aikaa 113 tuntia.  

### Seuraava viikko

Ensi viikolla parantelen vielä mahdollisesti ohjelman käyttöliittymää.  JPS-menetelmän toteusta voi myös viilata paremmaksi.




