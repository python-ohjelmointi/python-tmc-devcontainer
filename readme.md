[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?&repo=1239726001&hide_repo_select=true)

# Kehityskontti Python-kurssin tehtäville

Tämä repositorio sisältää [kehityskontin](https://code.visualstudio.com/docs/remote/containers), joka sisältää tarvittavat työkalut ja riippuvuudet Pythonin sekä TMC-tehtäväjärjestelmän käyttämiseksi. [Kehityskontti](https://code.visualstudio.com/docs/devcontainers/containers) on [Docker-kontti](https://www.docker.com/resources/what-container/), johon on asennettu tarvittavat työkalut ja riippuvuudet, jolloin voit työskennellä yhtenäisessä ympäristössä riippumatta siitä, mitä ohjelmia omalle koneellesi on asennettuna.


## Kontin määritykset

Jos haluat välttää mahdollisia asennusongelmia ja käyttää valmista kehitysympäristöä, voit käyttää tässä projektissa määritettyä [kehityskontin määritystiedostoa](./.devcontainer/devcontainer.json).

Tässä tapauksessa kehityskontti on [määritetty](./.devcontainer/devcontainer.json) sisältämään Python-ohjelmointikielen sekä tyypilliset laajennokset, joiden avulla voit kehittää Python-sovelluksia. Mukana on myös TMC-laajennos, joka on tarpeen TMC-tehtävien suorittamiseksi ja palauttamiseksi.


## Kontin käyttäminen paikallisesti

Kehityskontin käyttämiseksi paikallisesti tarvitset [Dockerin](https://www.docker.com/get-started) asennettuna koneellesi sekä [Visual Studio Code Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) -laajennuksen. Kun Docker on asennettu, voit avata projektin VS Codessa, ja se kehottaa sinua avaamaan kansion uudelleen kontissa. Vaihtoehtoisesti avaa komentovalikon (Ctrl+Shift+P) ja suorita komento "Reopen in Container" avataksesi kehityskontin.


### Paikallisten konttien pysäyttäminen ja poistaminen

Kontin pysäyttämiseen sekä poistamiseen voit käyttää Dockerin komentorivikomentoja tai Docker Desktop -sovellusta. Voit myös käyttää VS Coden Dev Containers -laajennusta tarpeettomien konttien siivoamiseen: avaa komentovalikko (Ctrl + Shift + P) ja suorita komento "Dev Containers: Clean Up Dev Containers" valitaksesi poistettavat kontit.


## Kontin ajaminen pilvipalvelussa

Jos Dockerin asentaminen paikallisesti ei ole ensisijainen vaihtoehtosi, voit käyttää samaa kehityskonttia pilvessä, esimerkiksi [GitHub Codespacesissa](https://github.com/features/codespaces). GitHub Codespaces mahdollistaa kehitysympäristön luomisen pilveen, johon pääsee selaimen tai [paikallisesti asennetun VS Coden](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code) kautta. Kehittäjäkokemus Codespacesissa on hyvin samankaltainen kuin paikallisen kehityskontin tai paikallisen asennuksen käyttäminen.

Voit avata projektin GitHub Codespacesissa seuraamalla [tätä ohjetta](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace). GitHub Codespaces voi olla kätevä vaihtoehto, jos haluat välttää Dockerin asentamisen tai jos haluat työskennellä eri koneilla ilman ympäristön pystyttämistä joka kerta. Tämä kehityskontti toimii hyvin pienillä resursseilla, joten suosittelemme valitsemaan kevyimmän tarjolla olevan laitteistovaihtoehdon.

Pilvessä toimivat kehitysympäristöt ovat kaupallisia palveluita ja saattavat vaatia maksullisen tilauksen. Tarkista valitsemasi palvelun hinnoittelutiedot. Kirjoitushetkellä GitHub Codespaces tarjoaa ilmaisen tason rajoitetulla kuukausittaisella käyttötuntimäärällä ja lisätunteja voi ostaa tarvittaessa (katso [docs.github.com](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)).


### Etäkonttien pysäyttäminen ja poistaminen

Kehityskonteilla on aika- ja tallennusrajoitukset, jotka voivat ylittyä. Kun et enää tarvitse konttia, voit pysäyttä sen vähentääksesi kustannuksia ja säästääksesi resursseja. Kun et enää tarvitse konttia lainkaan, se on hyvä poistaa.

Lisätietoja konttien [pysäyttämisestä](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace) ja [poistamisesta](https://docs.github.com/en/codespaces/developing-in-a-codespace/deleting-a-codespace) löydät käyttämäsi palvelun dokumentaatiosta.


## Tietoa materiaalista

Tämän repositorion on luonut Teemu Havulinna, ja se on lisensoitu [Creative Commons BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) -lisenssillä.

Kielimalleja ja tekoälytyökaluja, kuten GitHub Copilot ja ChatGPT, on käytetty tämän repositorion luomisessa.
