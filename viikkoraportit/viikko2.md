## Viikko 2

### Ohjelman alustava toteutus

<img src="/dokumentaatio/png/viikko2.png" width="750">

Ohjelman alustava runko on saatu toteutettua Pythonilla.  Tässä viritelmässä on keskitytty lähinnä algoritmin toimivuuteen ja käyttöliittymä sekä visualisointi ovat vielä alkuasteella.

Ohjelma löytää parhaan reitin ruutukartan kahden pisteen välillä Dijkstran menetelmällä.  Ohjelma laskee reitin kahdella eri tavalla.  Ensiksi sallitaan vain vaaka- tai pystysuorat siirtymät pisteiden välillä.  Toisessa vaihtoehdossa myös diagonaalisiirtyvät sallitaan.

Visualisointi on toteutettu aluksi Matplotlib-standardikirjastolla.  Varsinaista käyttöliittymää ei ole vielä rakennettu.

### Havaintoja matkan varrelta

Pythonin PriorityQueue-luokka tuntuu toimivan nopeasti Dijkstran menetelmän iteroinnisssa.  Esim 100*100 ruudukon reitin laskenta kestää alle 0.1 sekuntia.

Kun sallitaan diagonaalisiirtymät pikselien välillä, saadaan luonnollisesti lyhyempi reitti, mutta laskenta kestää helposti kaksi kertaa kauemmin.

Visualisointi Matplotlib-kirjastolla on hitaahko ja ei kovin näyttävä.

### Työtunnit

Tähän mennessä käytetty aikaa 26 tuntia.  

### Seuraava viikko

Ensi viikolla laitetaan työn alle muut menetelmät eli A* ja JPS.

Myös käyttöliittymää aloitetaan rakentamaan paremmaksi Pygame-kirjaston avulla.




