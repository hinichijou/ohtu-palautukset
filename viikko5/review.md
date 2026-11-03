### Mitä huomioita Copilot teki koodistasi
Copilot teki kolme huomiota:

* Vakavuusaste medium: Use package-relative import for Player. This absolute import only works when src itself is placed on sys.path; importing the module through its repository package path (for example from viikko5.tennis.src.tennis_game import TennisGame) now fails with ModuleNotFoundError: No module named 'player'. Use a package-relative import (or a deliberate compatibility fallback if the direct from tennis_game test style must remain supported). Copilot haluaisi korvata absoluuttisen importin `from player import Player` package relative importilla. Varoitus on varmaankin hyvä olla olemassa, mutta mielestäni import noudattaa kurssilla käytettyä tyyliä, joten merkitsin sen won't fixiksi.

* Vakavuusaste low: Rename misleading has_advantage variable. has_advantage stores the Player object with the higher score, not a boolean indicating whether someone has an advantage. This name is misleading at the point where it is used to format both advantage and win messages; rename it to something like leading_player or player_with_higher_score. Makuasioista ja siitä mikä on selkeää ja mikä ei on aina hyvä kiistellä. Mielestäni varoituksessa oli kyllä pointtinsa, kun hehkutin PR:ssä, että muuttujat ovat nyt selkeästi nimettyjä. Tarkemmin ajateltuna player_with_advantage olisi aika itseään selittävä ja ei kuulostaisi booleanilta. Hyväksyin muutoksen.

* Vakavuusaste low: Remove duplicated word in comment. The comment contains a duplicated word (Either either), which makes the explanation unclear. Please remove the duplicate so it reads Either player has the advantage or has won the game. Copilot ei anna armoa myöskään englannin kielen taidon osalta. Hyväksyin muutoksen.

### Olivatko ehdotetut muutokset hyviä

Mielestäni ehdotukset olivat hyviä. Importin tyylin potentiaaliset ongelmat on aina hyvä pitää mielessä vaikka en ehdotusta toteuttanutkaan, ehdotuksen voi aina ohittaa, kuten itsekin tein. Pidin nopeasti itse koodaillessa muuttujan nimeä selkeänä, mutta objektiivisesti katsottuna ehdotus oli selkeämpi. Kommenteissa ja kielen käytössäkin on hyvä pitää jotain tasoa yllä niin en pitänyt kommenttiin liittyvää korjausta mitenkään huonona asiana.

### Kuinka hyödylliseksi koit Copilotin tekemän katselmoinnin

Mitään mielestäni kriittiseksi laskettavaa ei löytynyt, mutta en myöskään keksi miksi katselmointi ei olisi ollut hyödyllinen. Pidin katselmointia hyödyllisenä. Koodia katsellessa on aina hyvä olla "useampi pari silmiä" ja on hyödyllistä saada objektiivinen mielipide.

### Huomasiko Copilot jotain, minkä olisit itse jättänyt huomaamatta? Entä jäikö siltä jotain oleellista huomaamatta?

En usko, että olisin itse alkanut viilaamaan pilkkua toisen ihmisen tekemien kommenttien kanssa. En olisi myöskään huomioinut muuttujan nimeä kunhan se on jokseenkin selkeä kontekstissa (tietysti itsehän sen nimesin). En olisi myöskään huomioinut importia kunhan importit noudattavat projektin tyyliä. Ts. olisin tuskin huomioinut mitään copilotin huomioimista asioista. En osaa sanoa jäikö jotain oleellista huomioimatta koska pyrin tekemään refaktoroinnin miten itsestäni tuntui järkevältä enkä jättänyt koodiin copilottia varten jotain ansoja sen löydettäväksi.

### Miltä Copilotin kommentit tuntuivat verrattuna siihen, että saman palautteen olisi antanut tiimikaveri? Mitä palautteen antamisessa kannattaa ottaa huomioon, kun katselmoijana on ihminen?

Copilotin kommentit oli helppo ottaa vastaan neutraaleina kommentteina, jotka perustuvat suureen määrään koulutusdataa. Kun vastapuolena on ihminen, saattaa kommentti tuntua enemmän mielipiteeltä kuin joltain mitä kannattaa toteuttaa. Palautteessa kannattaa mielestäni pyrkiä olemaan mahdollisimman objektiivinen ja neutraali. Palautteen antoon, kuten melkeinpä kaikkeen muuhunkin ihmiskommunikaatioon pätee, että kannattaa olla ystävällinen ja kunnioittava. Mielestäni homma ei saa mennä kiistelyksi makuasioista tai tuntua käskemiseltä. Sävyn pitää olla keskusteleva "tässä on tehty näin, mutta mietin, että jos tekisikin näin, koska..." ja käydä lyhyt keskustelu aiheesta kommenteissa jos aiheesta on keskusteltavaa. Selkeät virheet voi toki mielestäni osoittaa suoraan ja ne lienevät selkeitä ja helppoa hyväksyä molemmille osapuolille, kun paikan näyttää koodista ja selittää ongelman lyhyesti.