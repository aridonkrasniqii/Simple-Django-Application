import qrcode

# qr = qrcode.make('hello world')
# qr.save('myqr.png')

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)
data = 'https://linkedin.com/in/aridon-krasniqi/'

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

img.save('Aridon Krasniqi\'s Linkedin profile.png')






