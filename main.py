import imghdr
import qrcode
img = qrcode.make("https://www.exemple.com/")
img.save("exemple.png")
