import smtplib

fromAddress = "ecjaydeepsoni@gmail.com"
toAddress = "ecjaydeepsoni@gmail.com"
subject = "Interesting-3"
body = "This mail sent using Python script"
email = "Subject: {}\n\n{}".format(subject, body)

mailServer = "smtp.gmail.com:587"
connection = smtplib.SMTP(mailServer)
connection.starttls()
connection.login("ecjaydeepsoni@gmail.com", "smrdzwkzupwijuph")

connection.sendmail(fromAddress, toAddress, email)
connection.quit()
