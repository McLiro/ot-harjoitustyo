# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus mahdollistaa laivanupotus pelin pelaamisen tietokonetta vastaan.

## Sovelluksen toiminnallisuus

- Käyttäjä voi aloittaa uuden pelin tietokonetta vastaan.
  - Käyttäjä valitsee laivojen sijoituksen peliruudukkoon.
    - Kun valinnat on tehty, tulee valita vaikeustaso.
  - Kaksi mahdollista vaikeustasoa.
    - Helppo valitsee ammuttavat ruudut satunnaisesti, eikä kiinnitä huomiota osumiin.
    - Keskitasoinen valitses vain parillisia tai parittomia ruutuja kunnes tulee osuma. Kun osuma tulee, alkaa tietokone selvittämään osutun laivan suuntaa ja pyrkii upottamaan sen. Kun laiva on upotettu, tietokone jatkaa tyhjien ruutujen ampumista.

- Pelin tila tallentuu automaattisesti jokaisen siirron jälkeen tietokantaan.
  - Vanhaa keskeneräistä peliä voi jatkaa latausnäkemästä, jossa vanhoja pelejä voi myös poistaa.
  - Kun pelin voittaa joko käyttäjä tai tietokone, pelin tallenne poistuu automaattisesti tietokannasta.

- Peli seuraa koko ajan pelin tilannetta ja antaa jokaisen kierroksen jälkeen palautteen tuliko osuma, upposiko laiva vai huti.
  - Huti menneet merkitään sinisellä ympyrällä.
  - Osumat punaisella ympyrällä.
  - Vastustajan upotut laivat tulevat näkyviin punaisena.

- Peli loppuu automaattisesti kun jokoo käyttäjän tai tietokoneen kaikki laivat on upotettu.