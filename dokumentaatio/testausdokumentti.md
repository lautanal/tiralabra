## Testausdokumentti

### Yksikkötestit

Yksikkötestit eivät ole niin tärkeitä tässä sovelluksessa, koska ohjelman toiminta varmistetaan parhaiten vertailemalla visuaalisesti eri menetelmien tuloksia testikartoilla.  Olen kuitenkin tehnyt muutaman yksikkötestin, jotka ovat hyödyksi jos ohjelmaan tehdään jatkossa muutoksia.

### Empiirinen testaus

Testaus on ollut pääosin kokeilevaa, manuaalista empiiristä testaamista.  Graafinen käyttöliittymä antaa tähän hyvän mahdollisuuden.

Graafinen käyttöliittymä auttaa huomattavasti ohjelman toiminnan varmistamisessa ja räikeimpien ongelmien selvittämisessä. Esimerkiksi voidaan havaita, poikkeaako laskennan antama "paras" polku merkittävästi silmämääräisesti parhaalta tai lyhimmältä polulta. 

Ottamalla animointi käyttöön, voidaan tarkastella eri algoritmien etenemistä ja mitkä solmut ovat kulloinkin käsittelyssä ja missä järjestyksessä.  

Erilaisilla testikartoilla on varmistettu algoritmien toiminta ja oikeellisuus.  Kartalta on määritetty manuaalisesti lyhin reitti ja todettu, että algoritmi antaa saman tuloksen.

<img src="/dokumentaatio/png/testi05.png" width="750">

Suorituskykyä on vertailu eri kokoisilla random-kartoilla.  Paras reitti on haettu samalla kartalla kolmella eri menetelmällä.  On tarkastettu, että menetelmät antavat saman tuloksen (polku voi joskus olla hieman eri).  Suorituskykytestin tulokset löytyvät toteutusdokumentista.