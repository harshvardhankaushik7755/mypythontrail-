import pyqrcode
img = "https://youtu.be/8F1Hm5F-2KE?si=h5NqFcDnfq5K3odN"
path = pyqrcode.create(img)
path.svg("qr-code-1.svg", scale=10)