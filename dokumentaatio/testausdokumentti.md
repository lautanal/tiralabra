## Testausdokumentti

### Yksikkötestit

Yksikkötestit eivät ole niin tärkeitä tässä sovelluksessa, koska ohjelman toiminta varmistetaan parhaiten vertailemalla visuaalisesti eri menetelmien tuloksia testikartoilla.  Olen kuitenkin tehnyt melko kattavat yksikkötestit, jotka ovat hyödyksi jos ohjelmaan tehdään jatkossa muutoksia.  Käyttöliittymä ja Pygame-piirtorutiinit on jätetty testauksen ulkopuolelle.

Yksikkötestit suoritetaan komennolla: poetry run coverage run --branch -m pytest src

Testikattavuus voidaan raportoida komennolla: poetry run coverage report -m 


### Empiirinen testaus

Testaus on ollut pääosin kokeilevaa, manuaalista empiiristä testaamista.  Graafinen käyttöliittymä antaa tähän hyvän mahdollisuuden.

Graafinen käyttöliittymä helpottaa huomattavasti ohjelman toiminnan varmistamisessa ja räikeimpien ongelmien selvittämisessä. Esimerkiksi voidaan havaita, poikkeaako laskennan antama "paras" polku merkittävästi silmämääräisesti parhaalta tai lyhimmältä polulta. 

Ottamalla animointi käyttöön, voidaan tarkastella eri algoritmien etenemistä ja mitkä solmut ovat kulloinkin käsittelyssä ja missä järjestyksessä.  

Erilaisilla testikartoilla on varmistettu algoritmien toiminta ja oikeellisuus.  Kartalta on määritetty manuaalisesti lyhin reitti ja todettu, että algoritmit antavat saman tuloksen.


<img src="/dokumentaatio/png/testi05.png" width="750">


Suorituskykyä on vertailu eri kokoisilla random-kartoilla.  Paras reitti on haettu samalla kartalla kolmella eri menetelmällä.  On tarkastettu, että menetelmät antavat yhtäpitävät tulokset (polut voivat joskus olla hieman eroavat).  Suorituskykytestin tulokset löytyvät toteutusdokumentista.