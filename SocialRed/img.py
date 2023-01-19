import requests
from PIL import Image

r = requests.get("https://th.bing.com/th/id/OIP.ItbYHZ-_TICIj4lCJQow1AHaHa?pid=ImgDet&rs=1")

with open("./SocialRed/imagen.jpg", "wb") as f:
    f.write(r.content)

img = Image.open( "./SocialRed/imagen.jpg")

#img.display()