## Viikko 2

### Ohjelman rungon toteutus

<img src="/dokumentaatio/png/reittikartta03.png" width="750">

Ohjelman runko on toteutettu Pythonilla. Edellisen viikon ohjelma on kokenut täysmuutoksen. Ruutukartan mallinnus ja algoritmit ovat toteutettu luokkien avulla edellisen viikon taulukkopohjaisen toteutuksen sijasta. Visualisointi on nyt toteutettu Pygame-kirjastolla Matplotlib-kirjaston sijasta. Myös käyttöliittymä on toteutettu Pygame-kirjaston avulla hiiri- ja näppäinkomennoin.  

Ohjelma generoi automaattisesti ruutukartan, jossa jokaisella ruudulla on painoarvo, joka vastaa aika tai kustannuslisää ruudun läpi kulkiessa.  Kartta visualisoidaan Pygame-kirjaston avulla.  Käyttäjä valitsee hiirellä reitin alku- ja loppupisteet ja lisää halutessaan esteet, joiden läpi reitti ei voi kulkea.

Ohjelma löytää parhaan reitin (pienin kustannus) ruutukartan kahden pisteen välillä sekä Dijkstran, että  A* -menetelmillä.  Ensi viikolla työn alle tulee myös JPS- tai IDA*-menetelmät.  Parhaan reitin voi määrittää kahdella eri tavalla.  Joko siirrytään vain vaaka- tai pystysuoraaan ruutujen välillä tai toisessa vaihtoehdossa myös diagonaalisiirtyvät ovat mahdollisia.

### Havaintoja matkan varrelta

Visualisointi Pygame-kirjaston avulla on huomattavasti nopeampi ja näyttävämpi kuin aikaisempi Matplotlib-toteutus.  Pygamen avulla onistuu myös realiaikainen animointi.

A* -menetelmän paremmuus verrattuna Dijkstran menetelmään riippuu paljon reitin alku- ja loppupisteiden sijainnista.

### Työtunnit

Tähän mennessä käytetty aikaa 42 tuntia.  

### Seuraava viikko

Ensi viikolla laitetaan työn alle muut reititysmenetelmät eli JPS ja IDA* sekä.

Ohjelma testaus on ollut tähän mennessä lähes pelkästään kokeilevaa manuaalista testaamista.  Ensi viikolla lisätäään automaattiset yksikkötestaukset.



