import random

options = ('piedra', 'papel', 'tijera')

computerWins = 0
userWins = 0
rounds = 1

while True:
    print('*' * 15)
    print ('Round', rounds)

    print('User wins ' + str(userWins))
    print('Computer wins ' + str(computerWins))

    user_option = input ('Piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print(user_option + ' no se encuentra dentro de las opciones, porfavor digite una opcion valida')
        continue

    computer_option = random.choice(options)

    print ('User option => ' + user_option)
    print('Computer option => ' + computer_option)

    if user_option == computer_option:
        print ('Empate! :p')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print ('Piedra le gana a tijera')
            print ('User gana! :)')
            userWins += 1
        else:
            print('Papel le gana a piedra')
            print('Computer gana :p')
            computerWins +=1

    elif user_option == 'papel':
        if computer_option == 'piedra':
            print ('Papel le gana a piedra')
            print ('User gana! :)')
            userWins += 1
        else:
            print('Tijera le gana a papel')
            print('Computer gana :p')
            computerWins += 1

    elif user_option == 'tijera':
        if computer_option == 'papel':
            print ('Tijera le gana a papel')
            print ('User gana! :)')
            userWins += 1
        else:
            print('Piedra le gana a papel')
            print('Computer gana :p')
            computerWins += 1

    if computerWins == 2:
        print('El ganador es la computadora :p')
        break

    if userWins == 2:
        print('El ganador es el usuario :)')
        break

    rounds +=1