password_sicura = 'Qwerty123.'
nome_utente = input('Digita username: ')
pwd_utente = input('Digita la password: ')
if pwd_utente == password_sicura:
    print('Benvenuto ' + nome_utente + ', password corretta ')
else:
    print('Password non corretta')
