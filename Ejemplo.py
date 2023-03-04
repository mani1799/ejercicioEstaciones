month = input ('Ingrese el mes ')
day   = input ('ingrese el dia ')

month = month.lower()
day   = int(day)

if ((day <= 31) and (day >= 1)):
    if((month == 'marzo') and (day >= 21)):
        print('Primavera')
    elif((month == 'abril') or (month == 'mayo')):
        print('Primavera')
    elif((month == 'junio') and (day <= 20)): 
        print('Primavera')
    elif((month == 'junio') and (day >= 21)):
        print('verano')
    elif((month == 'julio') or (month == 'agosto')):
        print('verano')
    elif((month == 'septiembre') and (day <= 20)):
        print('verano')
    elif((month == 'septiembre') and (day >= 21)):
        print('otono')
    elif((month == 'octubre') or (month == 'noviembre')):
        print('otono')
    elif((month == 'diciembre') and (day <= 20)): 
        print('otono')
    elif((month == 'diciembre') and (day >= 21)):
        print('invierno')
    elif((month == 'enero') or (month == 'febrero')):
        print('invierno')
    elif((month == 'marzo') and (day <= 20)): 
        print('invierno')
    else:
        print('Mes erroneo')
else:
    print('dia erroneo')
    