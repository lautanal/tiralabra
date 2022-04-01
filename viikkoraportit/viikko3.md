## Viikko 3

<img src="/dokumentaatio/png/viikko3.png" width="750">

### Ohjelman rungon toteutus

Ohjelman runko on toteutettu Pythonilla. Edellisen viikon ohjelma on kokenut täysmuutoksen. Ruutukartan mallinnus ja algoritmit ovat toteutettu luokkien avulla edellisen viikon taulukkopohjaisen toteutuksen sijasta. Visualisointi on nyt toteutettu Pygame-kirjastolla Matplotlib-kirjaston sijasta. Myös käyttöliittymä on toteutettu Pygame-kirjaston avulla hiiri- ja näppäinkomennoin.  

Ohjelma generoi automaattisesti ruutukartan, jossa jokaisella ruudulla on painoarvo, joka vastaa aika tai kustannuslisää ruudun läpi kulkiessa.  Kartta visualisoidaan Pygame-kirjaston avulla.  Käyttäjä valitsee hiirellä reitin alku- ja loppupisteet ja lisää halutessaan esteet, joiden läpi reitti ei voi kulkea.

Ohjelma löytää parhaan reitin (pienin kustannus) ruutukartan kahden pisteen välillä sekä Dijkstran, että  A* -menetelmillä (Ensi viikolla työn alle tulevat myös JPS- tai IDA*-menetelmät).  Parhaan reitin voi määrittää kahdella eri tavalla.  Joko siirrytään ruutujen välillä pelkästään vaaka- ja pystysuoraaan tai vaihtoehtoisesti myös diagonaalisiirtyvät ovat mahdollisia.

### Havaintoja matkan varrelta

Visualisointi Pygame-kirjaston avulla on huomattavasti nopeampi ja näyttävämpi kuin aikaisempi Matplotlib-toteutus.  

Pygamen avulla onistuu myös realiaikainen animointi.  Animointi on melko hidasta.

A* -menetelmän paremmuus verrattuna Dijkstran menetelmään riippuu paljon reitin alku- ja loppupisteiden sijainnista.

### Release

Viikon 3 release löytyy [täältä](https://github.com/lautanal/tiralabra/releases/tag/Viikko3)

### Työtunnit

Tähän mennessä käytetty aikaa 47 tuntia.  

### Seuraava viikko

Ensi viikolla laitetaan työn alle muut reititysmenetelmät eli JPS ja IDA* sekä.

Ohjelma testaus on ollut tähän mennessä lähes pelkästään kokeilevaa manuaalista testaamista.  Ensi viikolla lisätäään automaattiset yksikkötestaukset.



