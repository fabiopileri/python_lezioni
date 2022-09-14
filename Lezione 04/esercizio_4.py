try:
    ore_lavorate = int(input('Ore lavorate: '))
except:
    print('valore non valido')
    exit()
tariffa_oraria = 10
limite_ore = 40
if int(ore_lavorate) <= limite_ore:
    paga_totale = int(ore_lavorate) * tariffa_oraria
else:
    paga_totale = (limite_ore * tariffa_oraria) + ((int(ore_lavorate) - limite_ore) * tariffa_oraria * 1.5)
print('Paga totale: ' + str(paga_totale))
