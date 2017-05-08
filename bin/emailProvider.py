import smtplib

sender='<username>@gmail.com'
receiver='<username>@<emailServiceProvider>.<extension>'

username='<username>@gmail.com'
passwd='<passwd>'

msg='Test email provider'

def sendmail():
	smtpServer=smtplib.SMTP('smtp.gmail.com', 587)
	smtpServer.ehlo()
	smtpServer.starttls()
	smtpServer.ehlo()
	smtpServer.login(username, passwd)
	smtpServer.sendmail(sender, receiver, msg)
	print 'Mail sent successfully'
	smtpServer.close()

sendmail()