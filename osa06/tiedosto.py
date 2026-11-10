from pathlib import Path

def lue_rivi(md_rivi: str) -> tuple:
    """
    >>> lue_rivi("| C | 0.0020 | 0.002 |")
    ('C', 0.002, 0.002)
    """
    a, b, c = md_rivi[2: -2].split(" | ")

    return (a, float(b), float(c))


try:
    polku = Path("benchmark.md")
    teksti = polku.read_text(encoding="utf-8")

    erotin = teksti.find("\n\n")

    taulukko = teksti[0 : erotin]

    rivit = taulukko.splitlines()

    kielet = rivit[2:]

    tilastot = {}

    for rivi in kielet:
        try:
            kieli, luku1, luku2 = lue_rivi(rivi)
            tilastot[kieli] = (luku1, luku2)
        except ValueError:
            print(f"Tiedostossa oli virhe, virheellinen rivi: \"{rivi}\"")

    for avain in tilastot:
        mediaani, minimi = tilastot[avain]
        print(f"{avain}, mediaani {mediaani} s, minimi {minimi} s")

except FileNotFoundError:
    print("Tiedostoa ei löytynyt")

except PermissionError:
    print("Ei lukuoikeutta")
