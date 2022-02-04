import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode

qr = pyqrcode.create("https://www.instagram.com/mssurya_/")

qr.png("Instagram.jpg",scale=8)

d = decode(Image.open("Instagram.jpg"))
print(d)