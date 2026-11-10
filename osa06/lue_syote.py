IKA_MINIMI = 0
IKA_MAKSIMI = 150


def lue_kokonaisluku(minimi: int, maksimi: int):
    while True:
        try:
            luku = int(input("Syötä kokonaisluku: "))

            if luku < minimi or luku > maksimi:
                raise AssertionError()

            return luku

        except ValueError:
            print("Virheellinen kokonaisluku")

        except AssertionError:
            print(f"Luku ei ole sallitulta väliltä {IKA_MINIMI} - {IKA_MAKSIMI}")


def main():
    luku = lue_kokonaisluku(IKA_MINIMI, IKA_MAKSIMI)
    print("Kiitos!")
    print(luku, "potenssiin kolme on", luku**3)

main()
