
email = 'walex@hotmail.com'
email_gmail = email.endswith('@hotmail.com')
email_hotmail = email.endswith('@gmail.com')

if email_gmail or email_hotmail in email:
    print('Método 4°: E-mail é válido')
else:
    print('Método 4°: E-mail é inválido')