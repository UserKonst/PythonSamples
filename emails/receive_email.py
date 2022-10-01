import imaplib

imap = imaplib.IMAP4_SSL('imap.gmail.com')
login = 'kostyan.vk@gmail.com'
password = input('enter password: ')

imap.login(login, password)
imap.select('inbox')

typ, data = imap.search(None, 'FROM kostyan.vk@gmail.com')
result, email_data = imap.fetch(data[0], '(RFC822)')


raw_email = email_data[0][1]
print(raw_email.decode('utf-8'))
