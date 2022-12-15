# Tietoliikenteen sovellusprojekti
   # Syksy 2022 /  Ville Sandberg

# Arkkitehtuurikaavio

Tavoitteena oli koodata Arduinolle client, joka mittaa kiihtyvyysanturin dataa ja lähettää sen 433Mhz radiorajapinnan yli IoT-reitittimelle (Rasberry pi) tallennettavaksi tie-tokantaan. Tämän jälkeen Pythonil-la koodattiin ohjelma joka hakee datan tietokannasta HTTP Api:n kautta ja välittää sen K-Means algoritmille.

![arkkitehtkaavio](https://user-images.githubusercontent.com/99398876/207575739-eff09a86-39f3-411a-a2eb-e9300c74c337.PNG)


# Arduino mittaukset

Kuvassa arduino kytkentä käyttäen GY-61 kiihtyvyysanturia sekä lähetintä ja vastaanotinta mittausten siirtämikseksi tietokantaan
![arduinomittaukset](https://user-images.githubusercontent.com/99398876/207831490-312a3bac-0d3f-4d4f-b671-dd9417fa86c6.PNG)


# Kmeans

Punaisilla tähdillä arvatut pisteet kuudessa eri kiihtyvyysanturin asennossa ja oma data iteroituna vihreillä palloilla.

![image](https://user-images.githubusercontent.com/99398876/205662060-edba5896-98dd-46a0-a435-34141e5c69a0.png) 


# Confusion matrix

Mitattu sata kertaa jokaisessa kuudessa suunnassa ja niiden perusteellä tulostettu matriisi.

![image](https://user-images.githubusercontent.com/99398876/206994697-35a1516c-5424-4507-93c8-72416099b257.png)



# kmeans harjoitustehtävä

Valmiilla datalla neljällä pisteellä

![image](https://user-images.githubusercontent.com/99398876/204475630-815fb3b7-66dc-460f-a5cb-d410711c659b.png)







