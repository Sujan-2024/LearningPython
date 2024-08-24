import qrcode
img = qrcode.make("Sujan Kurumbang")
type(img) # qrcode.image.pil.pilimg
img.save("Sujan.png")