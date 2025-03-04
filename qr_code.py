import qrcode
website_link = input('enter ur link: ')
qr = qrcode.QRCode(version = 5, box_size = 10, border = 5)
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = 'blue', back_color = 'pink')
img.save('youtube_qr123.png')