import pyqrcode
img = "https://youtube.com/shorts/xHEgHjJvR94?si=WjFwRC5mqRUrEim9"
path = pyqrcode.create(img)
path.svg("qr-code-3.svg", scale=10)