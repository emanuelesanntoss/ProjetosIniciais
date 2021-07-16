import pyqrcode
import png
from pyqrcode import QRCode

#link desejado para o QRCode
QRString = 'https://www.instagram.com/pycodebr/'

#montar QRCode
url =pyqrcode.create(QRString)

#salvar o QRCode gerado no local desejado
url.png(r'CODE.png', scale=8)