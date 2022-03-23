## Viikko 2

### Ohjelman alustava toteutus

Ohjelma perusrunko on saatu toteutettua Pythonilla.  Visualisointiin käytetään ainakin aluksi Matplotlib-standardikirjastoa.

Algoritmeista on kokeiltu Dijkstran algoritmi kahdella eri variantilla.  Toisessa sallitaan vain vaaka- tai pystysuorat siirtymät pikselien välillä.  Toisessa sallitaan myös diagonaalisiirtymät.

### Havaintoja matkan varrelta

Kun sallitaan diagonaalisiirtymät pikselien välillä, saadaan luonnollisesti lyhyempi reitti, mutta laskenta kestää helposti kaksi kertaa kauemmin.

Pythonin PriorityQueue luokka tuntuu toimivan nopeasti Dijkstran menetelmän iteroinnisssa.  Esim 100*100 ruudukon reitin laskenta kestää yleensä alle 0.1 sekuntia.

### Työtunnit

Tähän mennessä käytetty aikaa 23 tuntia.  

### Ensi viikko

Ensi viikolla laitetaan työn alle muut menetelmät eli A* ja JPS.
Myös käyttöliittymää aloitetaan rakentamaan.  Tällä hetkellä ohjelman saa syötteen kovakoodattuna.




