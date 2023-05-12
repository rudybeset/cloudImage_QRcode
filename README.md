# cloudImage_QRcode
python commandline tool om een plaatje te uploaden naar imagekit, om daarna een QRcode te krijgen van de directe publieke downloadlink.

Dit is een kleine tool voor een project van de Vughtse programmeerclub 
Nodig: Python 3.10.x
Extra modules: qrcode en imagekit io

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


