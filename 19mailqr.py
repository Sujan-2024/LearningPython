import qrcode
email = "kurumbangsujan2@gmail.com"
subject = "Hello world"
body = "My first email"
mail = f"mailto:{email},?subject = {subject}&body={body}"
img = qrcode.make(mail)
type(img)
img.save("Mail.png")