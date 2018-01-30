import smtplib
content="nothing"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login("surajitdey394.sd@gmail.com",'mahlyfmahrulz')
mail.sendmail('surajitdey394.sd@gmail.com','surajitdey394.sd@gmail.com',content)
mail.close()
 
