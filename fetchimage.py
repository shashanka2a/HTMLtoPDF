import requests
from io import BytesIO
from PIL import Image

url = 'https://preview.redd.it/ij7qycfg11i51.png?width=1280&format=png&auto=webp&s=92e7e0e4497d39d56d0753fcbaeba3d7d736488c'
r = requests.get(url)
print("Status code:"+r.status_code)

image = Image.open(BytesIO(r.content))
print(image.size,image.format,image.mode)

path = './image'+image.format
try:
  image.save(path,image.format)
except:
  print("Couldnt save image")
