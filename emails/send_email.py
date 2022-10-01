import smtplib

login = 'kostyan.vk@gmail.com'

# another port 465
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

password = input('enter password: ')
smtp.login(login, password)

from_address = login
to_address = login
subject = 'test'
message = 'test message'

smtp.sendmail(from_address, to_address, message)
smtp.quit()
