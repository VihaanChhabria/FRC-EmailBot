import smtplib

senderEmail = open("/home/vihaan/keys/FRC-EmailBotAppPass.txt").readlines()[0].strip("\n")
senderPass = open("/home/vihaan/keys/FRC-EmailBotAppPass.txt").readlines()[1].strip("\n")

def sendEmail(message, recipentEmail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, senderPass)

    server.sendmail(senderEmail, recipentEmail, message)

    server.quit()