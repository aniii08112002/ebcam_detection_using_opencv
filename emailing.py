import smtplib, ssl
from email.message import EmailMessage
import imghdr

def send_email(image_path):

    password = "cmvckqrttrljgzxw"
    username = 'anirudhloveshismotheralot@gmail.com'
    reciever = 'anirudhsharmakr76@gmail.com'
    email_message=EmailMessage()
    email_message["Subject"]="New Coustmer SHOED UP!!"
    email_message.set_content("HEy ,we just saw new coustmer ")
    with open(image_path,"rb") as file:
        content=file.read()
    email_message.add_attachment(content,maintype='image',subtype=imghdr.what(None,content))

    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username,password)
    gmail.sendmail(username,reciever,email_message.as_string())
    gmail.quit()

if __name__=="__main__":
    send_email(image_path="images/19.png")
