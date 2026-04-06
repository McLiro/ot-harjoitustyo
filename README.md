### Ohjelmistotekniikka, harjoitustyö

# Laivanupotus peli

Sovelluksessa käyttäjä voi pelata laivanupotus peliä tietokonetta vastaan. Ennen pelin alkua pelaaja asettaa ruudukolle laivat haluamaansa järjestykseen, jonka jälkeen pelin voi aloittaa. Pelissä pelaajat eivät näe vastustajan laivojen sijaintia, vaan arvaavat vuorotellen laivojen olevan tietyssä kohtaa, jonka jälkeen peli merkitsee tuliko osuma. Kun jokaiseen laivan kohtaan on osuttu, uppoaa laiva, jonka peli myös merkitsee. Pelin voittaa se, upottaa vastustajan laivat ensin.

## Dokumentaatio

[Vaatimusmäärittely](battleships/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](battleships/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](battleships/dokumentaatio/changelog.md)

## Asennus

Kloonaa repositorio ja mene 'battleships' hakemistoon.

Asenna riippuvuudet komennolla:

```
poetry install
```

Käynnistä sovellus komennolla:
```
poetry run invoke start
```

## Komentorivi komennot

### Testaus
Testit voi suorittaa komennolla:
```
poetry run invoke test
```

Testikattavuusraportin voi luoda komennolla:
```
poetry run invoke coverage-report
```

### Pylint
Pylin tarkistuksen voi tehdä komennolla:
```
poetry run invoke lint
```