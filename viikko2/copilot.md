### Kuinka hyödyllisiksi koit koodin täydennyksen ehdotukset?

Mielestäni ehdotus `top_goal_scorers` metodille oli järkevä ja toimiva, hyväksyin sen sellaisenaan. Koodi ei tyyliltään mielestäni eronnut aiemmasta `top_scorers_by_nationality` metodista.

### Pitikö Copilotin selitys Pylint-varoituksesta paikkansa?

Selitys piti paikkaansa ja oli mielestäni informatiivisempi kuin Pylintin dokumentaatio. Aiheutin line-too-long varoituksen mikä saattoi kyllä olla turhan helppo pähkinä purtavaksi.

### Tekikö agentti toimivan ratkaisun, ja testit?

Agentti teki toimivan ratkaisun ja testit pienen paimentamisen jälkeen. Selitin erikseen, että haluan käyttää uv:ta ja virtuaaliympäristöä. Pyysin agenttia ensin tekemään vain testit, jonka jälkeen minun piti erikseen spesifioida pytest-kirjasto. Agentti teki ensin jonkun mielestäni vähän epäsiistin path-ratkaisun testitiedostoon, kun mainitsin tästä agentti ehdotti testauspolun lisäämistä `pyproject.toml`-tiedostoon joka vaikutti paremmalta ratkaisulta. Puhuin ensin vain jokkueiden valinnasta, jolloin agentti lisäsi joukkuvalintaan merkkijonoyhdistelmiä, kuten COL/NSH pelaajille, jotka olivat pelanneet useassa joukkueessa saman kauden aikana. Selitin, että haluan jokaisen joukkueen esiintyvän valinnassa kerran ja merkkijonoyhdistelmien kuten COL/NSH kuulumaan hakuun sekä joukkueelle COL että NSH, agentti teki tähän selityksen jälkeen toimivan ratkaisun. Painotin agentille etteivät testit saa tehdä verkkokutsuja, jolloin agentti lisäsi tälle vielä erillisen testin stubin lisäksi mikä mielestäni vaikutti perusteelliselta.

### Eroaako testeissä joku siitä miten testejä tehtiin edellisellä viikolla?

Sen sijaan, että käytettäisiin Coveragea ja määritettäisiin source `.coveragerc`:ssa määritetään `pyproject.toml`-tiedostossa `[tool.pytest.ini_options]` alla `pythonpath = ["src"]`, jotta pytest löytää testit. pytest kirjastoa sinänsä käytetään samalla tavalla.

### Löysikö Pylint agentin koodista virheitä?

Pylint antoi ensimmäisestä agentin ehdottamasta ratkaisusta varoituksen `src\index.py:37:0: R0915: Too many statements (12/10) (too-many-statements)`. Pyysin agenttia korjaamaan virheen, se korjasi sen mielestäni järkevästi ja pyysi aina jatkossa lupaa ajaa pylint testit jokaiselle uudelle muutokselle. Tämän jälkeen pylint virheitä ei enää esiintynyt.

### Mitä muuta opit?

Agentti tekee mielestäni hyödyllisiä asioita, mutta sen tuotokset ovat helposti jollain tavalla puutteellisia. Mitä tarkemmin agenttia opastaa, sitä parempaa työtä se tekee. Siinä mielessä puutteet agentin toiminnassa ovat puutteita käyttäjän toiminnassa, huomasin, että annoin alkuun liian huonosti rajattuja prompteja ja mitä yksityiskohtaisemmin selitin sitä millä tavalla halusin agentin tekevän jotain, sitä parempi lopputulos oli. Kun olin selittänyt jonkin toimintatavan agentti myös muisti sen ja käytti sitä jatkossa. Koska en ollut aiemmin käyttänyt agenttia meni tällaisen yksinkertaisen tehtävän toteutuksessa enemmän aikaa kuin itse koodatessa, kun tutkin agentin tuotoksia ja kyselin ja selitin sille asioita, mutta on helppo uskoa että agentin kanssa saa aikaan enemmän ja nopeammin kunhan sen käyttöön ja sen ohjaamiseen tottuu.