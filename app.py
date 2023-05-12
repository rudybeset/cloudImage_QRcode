
#use: app.py <arg> 
#<arg> = naam van het bestand
#pip install imagekitio  <-- niet vergeten
#pip install qrcode  <-- niet vergeten

import base64
import os
import sys

import qrcode
import qrcode.image.svg

from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions

imagekit = ImageKit(
    private_key='private_XXXXXXXXXXXXXXXX',
    public_key='public_XXXXXXXXXXXXXXXX',
    url_endpoint='https://ik.imagekit.io/XXXXXXXXXXXXXXXX'
)

#argument filename foto
n= len(sys.argv)
if (n> 1):
    filename = sys.argv[1]
else:
    filename = 'dc.jpg'

with open(filename, 'rb') as f:
   
    image_data = f.read()

    encoded_image = base64.b64encode(image_data)
    encoded_image


options = UploadFileRequestOptions(
    use_unique_file_name=False,
    #tags=['abc', 'def'],
    folder='/testing/',
    is_private_file=False,
    custom_coordinates='10,10,20,20',
    overwrite_file=True,
    overwrite_ai_tags=False,
    overwrite_tags=False,
    
)

upload = imagekit.upload(
        encoded_image,
	    file_name="Vughts_Museum.jpg",
	    options=UploadFileRequestOptions(
		tags = ["Het Vughts Museum", "Vught"]
	    ) 
)

#print(upload.response_metadata.raw)


finalURL= upload.url

print(finalURL)

img = qrcode.make(finalURL)
type(img)  
img.save(upload.name+".png")