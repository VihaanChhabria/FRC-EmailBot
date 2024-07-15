import smtplib

message = "Message_you_need_to_send"
senderEmail = "chhabria.vihaan2@gmail.com"
senderPass = 'poiy ygmh btfq zuyn'
recipentPass = "chhabria.vihaan@gmail.com"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, senderPass)

server.sendmail(senderEmail, recipentPass, message)

server.quit()