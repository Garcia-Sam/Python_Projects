from datetime import date
nasci = int(input('Em qual ano você nasceu? '))
data = date.today().year - nasci
if data <= 9:
    print(f'Você tem {data} anos.'
          f' Sua categoria é MIRIM.')
elif data <= 14:
    print(f'Você tem {data} anos.'
          f' Sua categoria é INFANTIL.')
elif data <= 19:
    print(f'Você tem {data} anos.'
          f' Sua categoria é JUNIOR.')
elif data <= 25:
    print(f'Você tem {data} anos.'
          f' Sua categoria é SÊNIOR.')
else:
    print(f'Você tem {data} anos.'
          f' Sua categoria é MASTER.')
