nome_utente = input('Come ti chiami? ')
eta_utente = int(input('Quanti anni hai? '))
if eta_utente >= 18:
    print('Benvenuto ' + nome_utente + ', sei maggiorenne ')
else:
    print('Benvenuto ' + nome_utente + ', sei minorenne ')
