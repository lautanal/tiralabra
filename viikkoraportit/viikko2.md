## Viikko 2

### Ohjelman alustava toteutus

Ohjelma perusrunko on saatu toteutettua Pythonilla.

Ohjelma löytää parhaan reitin kahden pisteen välillä Dijkstran menetelmnällä.  Ohjelma laskee reitin kahdella eritavalla.  Ensiksi sallitaan vain vaaka- tai pystysuorat siirtymät pisteiden välillä.  Toisessa vaihtoehdossa myös diagonaalisiirtyvät sallitaan.

Visualisoinissa on käytetty vielä aluksi Matplotlib-standardikirjastoa, jolla ei voi tehdä kovin interaktiivista käyttöliittymää.

Algoritmeista on kokeiltu Dijkstran algoritmi kahdella eri variantilla.  Toisessa sallitaan vain vaaka- tai pystysuorat siirtymät pikselien välillä.  Toisessa sallitaan myös diagonaalisiirtymät.

### Havaintoja matkan varrelta

Pythonin PriorityQueue luokka tuntuu toimivan nopeasti Dijkstran menetelmän iteroinnisssa.  Esim 100*100 ruudukon reitin laskenta kestää alle 0.1 sekuntia.

Kun sallitaan diagonaalisiirtymät pikselien välillä, saadaan luonnollisesti lyhyempi reitti, mutta laskenta kestää helposti kaksi kertaa kauemmin.

Visualisointi Matplotlib-kirjastolla on hitaahko ja ei näyttävä.

### Työtunnit

Tähän mennessä käytetty aikaa 23 tuntia.  

### Seuraava viikko

Ensi viikolla laitetaan työn alle muut menetelmät eli A* ja JPS.
Myös käyttöliittymää aloitetaan rakentamaan paremmaksi Pygame-kirjaston avulla.




