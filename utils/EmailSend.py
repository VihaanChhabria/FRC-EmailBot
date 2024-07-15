import smtplib

with open("/home/vihaan/keys/FRC-EmailBotAppPass.txt").readlines() as __SENDER_INFO:
    __SENDER_EMAIL = __SENDER_INFO[0].strip("\n")
    __SENDER_PASS = __SENDER_INFO[1].strip("\n")

def sendEmail(message, recipentEmail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(__SENDER_EMAIL, __SENDER_PASS)

    server.sendmail(__SENDER_EMAIL, recipentEmail, message)

    server.quit()