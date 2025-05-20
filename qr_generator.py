import qrcode
import image

qr = qrcode.QRCode(
    version = 15,  # 15 is the maximum version of qr code higher the number bigger the code image and complicated picture
    box_size = 10, # size of box where each qr code will be displayed
    border = 5 #It is the white part of the image --border in all 4 side with white color
)

data = "https://github.com/Aish1718"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white") # fill color is the color of the code and back color is the background color
img.save("github_qr.png") # save the image in the current directory