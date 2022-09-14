password_sicura = 'Qwerty123.'
nome_utente = input('Digita username: ')
eta_utente = input('Digita la tua età: ')
pwd_utente = input('Digita la password: ')
if eta_utente >= 18:
    if pwd_utente == password_sicura:
        print('Benvenuto ' + nome_utente + ', password corretta ')
    else:
        print('Password non corretta')
else:
    print('Accesso consentito ai soli maggiorenni')