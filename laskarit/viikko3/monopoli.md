```mermaid
classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    
    class Pelaaja {
        rahat
    }

    class Katu {
        nimi
    }

    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- Katu
    
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    
    Sattuma -- Kortti
    Yhteismaa -- Kortti
    Kortti -- Toiminto
    Ruutu "1" -- "1" Toiminto
    
    Katu "1" -- "0..4" Talo
    Katu "1" -- "0..1" Hotelli
    
    Pelaaja "1" -- "*" Katu
    Pelaaja "1" -- "*" Asema
    Pelaaja "1" -- "*" Laitos
```