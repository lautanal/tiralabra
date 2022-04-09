## Viikko 3

<img src="/dokumentaatio/png/viikko4.png" width="750">

### Käyttöliittymän parantaminen

Iso osa ajasta on kulunut käyttöliittymän parantamiseen.  Käyttöliittymää tarvitaan algoritmien varmentamiseen ja testaukseen.  Ohjelman käyttöliittymä perustuu näppäimistön ja hiiren komentoihin.

### Algoritmit

Ohjelma löytää parhaan reitin (pienin kustannus) ruutukartan kahden pisteen välillä sekä Dijkstran, A*, ja IDA* -menetelmillä.  Kaksi ensin mainittua tuntuvan soveltuvan parhaiten ruutukartan parhaan polun etsimiseen.

Parhaan reitin voi määrittää kahdella eri tavalla.  Reitti kulkee ruutujen välillä joko pelkästään vaaka- ja pystysuoraan tai valinnaisesti myös viistosuunnat (väli-ilmansuunnat) ovat mahdollisia.  Siirryttäessä vinosti ruudusta toiseen, pitempi matka ruutujen välillä otetaan huomioon.

### Manuaalinen testaus

<img src="/dokumentaatio/png/testikartta04.png" width="750">

Algoritmien oikeellisuutta on testattu testikartoilla ja tarkastamalla ohjelman antamia tuloksia manuaalisesti laskemalla.  

### Havaintoja matkan varrelta

Visualisointi Pygame-kirjaston avulla toimii hyvin, mutta realiaikainen animointi on melko hidas.

A* -menetelmän paremmuus verrattuna Dijkstran menetelmään riippuu paljon reitin alku- ja loppupisteiden sijainnista.  Molemmat laskevat 400x400 pisteen kartan lyhimmän polun alle sekunnissa (Mac Mini M1).  IDA* -menetelmä ei tunnu olevan kovin hyvä ruutukartan navigoinnissa, jossa vaihtoehtoisia reittejä on hyvin paljon.

### Release

Viikon 4 release löytyy [täältä](https://github.com/lautanal/tiralabra/releases/tag/Viikko4)

### Työtunnit

Tähän mennessä käytetty aikaa 65 tuntia.  

### Seuraava viikko

Ensi viikolla keskityn tekemään automaattisia yksikkötestauksia.



