[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?&repo=1239726001&hide_repo_select=true)

# Kehityskontti Python-kurssin tehtäville

Tämä repositorio sisältää [kehityskontin](https://code.visualstudio.com/docs/remote/containers), joka sisältää tarvittavat työkalut ja riippuvuudet Pythonin sekä TMC-tehtäväjärjestelmän käyttämiseksi. [Kehityskontti](https://code.visualstudio.com/docs/devcontainers/containers) on [Docker-kontti](https://www.docker.com/resources/what-container/), johon on asennettu tarvittavat työkalut ja riippuvuudet, jolloin voit työskennellä yhtenäisessä ympäristössä riippumatta siitä, mitä ohjelmia omalle koneellesi on asennettuna.

Kontti sisältää seuraavat VS Code -laajennukset, jotka on asennettu automaattisesti, kun avaat projektin kontissa:

* [TestMyCode (tehtävälaajennos)](https://marketplace.visualstudio.com/items?itemName=moocfi.test-my-code)
* [Python-kielen tuki (syntaksi, suorittaminen, debuggeri)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Pylint (koodin tarkistus)](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)
* [autopep8 (koodin muotoilu)](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8)


## Kontin ajaminen pilvipalvelussa

Voit käyttää tätä valmista kehitysympäristöä pilvipalveluissa, erityisesti [GitHub Codespacesissa](https://github.com/features/codespaces). GitHub Codespaces mahdollistaa kehitysympäristön luomisen pilveen, johon pääsee selaimen tai [paikallisesti asennetun VS Coden](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code) kautta.

Pilviratkaisun käyttämiseksi tarvitset GitHub-tilin, VS Code -koodieditorin sekä [GitHub Codespaces -laajennuksen](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces).

Voit avata projektin GitHub Codespacesissa seuraamalla [tätä ohjetta](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace). Tämä kehityskontti toimii hyvin pienillä resursseilla, joten suosittelemme valitsemaan kevyimmän tarjolla olevan laitteistovaihtoehdon codespacea luotaessa.

> [!NOTE]
> Pilvessä toimivat kehitysympäristöt ovat kaupallisia palveluita ja saattavat vaatia maksullisen tilauksen. Tarkista valitsemasi palvelun hinnoittelutiedot. Kirjoitushetkellä GitHub Codespaces tarjoaa ilmaisen tason rajoitetulla kuukausittaisella käyttötuntimäärällä ja lisätunteja voi ostaa tarvittaessa (katso [docs.github.com](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)).


### Etäkonttien pysäyttäminen ja poistaminen

Kehityskonteilla on aika- ja tallennusrajoitukset, jotka voivat ylittyä. Kun et enää tarvitse konttia, voit pysäyttä sen vähentääksesi kustannuksia ja säästääksesi resursseja. Kun et enää tarvitse konttia lainkaan, se on hyvä poistaa.

Lisätietoja konttien [pysäyttämisestä](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace) ja [poistamisesta](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace) löydät käyttämäsi palvelun dokumentaatiosta.


## Kontin käyttäminen paikallisesti

Kehityskontin käyttämiseksi paikallisesti tarvitset [Dockerin](https://www.docker.com/get-started) asennettuna koneellesi sekä [Visual Studio Code Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) -laajennuksen. Kun Docker on asennettu, voit avata projektin VS Codessa, ja se kehottaa sinua avaamaan kansion uudelleen kontissa. Vaihtoehtoisesti avaa komentovalikon (Ctrl+Shift+P) ja suorita komento "Reopen in Container" avataksesi kehityskontin.


### Paikallisten konttien pysäyttäminen ja poistaminen

Kontin pysäyttämiseen sekä poistamiseen voit käyttää Dockerin komentorivikomentoja tai Docker Desktop -sovellusta. Voit myös käyttää VS Coden Dev Containers -laajennusta tarpeettomien konttien siivoamiseen: avaa komentovalikko (Ctrl + Shift + P) ja suorita komento "Dev Containers: Clean Up Dev Containers" valitaksesi poistettavat kontit.


## Tietoa materiaalista

Tämän repositorion on luonut Teemu Havulinna, ja se on lisensoitu [Creative Commons BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) -lisenssillä.

Kielimalleja ja tekoälytyökaluja, kuten GitHub Copilot ja ChatGPT, on käytetty tämän repositorion luomisessa.
