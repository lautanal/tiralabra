## Viikko 4

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

Visualisointi Pygame-kirjaston avulla toimii hyvin, mutta realiaikainen animointi on melko hidas.  Pygame-kirjaston nopeutta pitänee optimoida.

A* -menetelmän paremmuus verrattuna Dijkstran menetelmään riippuu paljon reitin alku- ja loppupisteiden sijainnista.  Molemmat laskevat 400x400 pisteen kartan lyhimmän polun alle sekunnissa (Mac Mini M1).  

IDA* -menetelmä tuntuu olevan aika hidas ruutukartan navigoinnissa verrattuna Dijkstran ja A*-menetelmiin.  IDA*-menetelmä ei ehkä ole parhaimmillaan tällaisessa ruutukartassa, vaihtoehtoisten reittien suuren määrän takia.  Toisaalta minun algoritmitoteutuksessani saattaa olla jotain mätää.  Pitää tutkia asiaa.

### Release

Viikon 4 release löytyy [täältä](https://github.com/lautanal/tiralabra/releases/tag/VIIKKO4)

### Työtunnit

Tähän mennessä käytetty aikaa 65 tuntia.  

### Seuraava viikko

Ensi viikolla keskityn parantamaan IDA*-menetelmän toimintaa, tekemään automaattisia yksikkötestauksia ja kirjoittamaan toteutusraporttia.



