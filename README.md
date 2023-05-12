# cloudImage_QRcode
python commandline tool om een plaatje te uploaden naar imagekit, Daarna krijg je een QRcode van de directe publieke downloadlink.

Dit is een kleine tool voor een project van de Vughtse programmeerclub 

Nodig
-------
Python 3.10.x

Extra modules: qrcode en imagekit io

Een account op https://imagekit.io/

Maak daar een account aan en vul in app.py de volgende velden met je persoonlijke keys:


    private_key='private_XXXXXXXXXXXXXXXX',
    public_key='public_XXXXXXXXXXXXXXXX',
    url_endpoint='https://ik.imagekit.io/XXXXXXXXXXXXXXXX'

Te vinden in: https://imagekit.io/dashboard/developer/api-keys

    
Installatie
-----------
#pip install imagekitio  <-- niet vergeten
#pip install qrcode  <-- niet vergeten

Gebruik
-------
app.py <arg> 
#<arg> = naam van het bestand

 Voorbeeld: >app.py mijn_plaatje.jpg
  
Resultaat is een png in de map waar je de code uitvoert met de QRcode van de directe link naar de online afbeelding.


