medium_zp = 100000
your_zp = int(input('Write you zp: '))
zzp = round(your_zp/medium_zp*100)
zp = round(your_zp/medium_zp*100)

if medium_zp > your_zp:
    print(f'Ха-ха у тебя маленька зарплата.\n Это {zzp}% от нормы по Москве')
else:
    print(f'Вау ты обгоняешь всех на {zp}%')

# Это был обычный цикл
# Вложенный выглядит так

if medium_zp < your_zp:
    if medium_zp < (your_zp*10):
        print("У вас очень много денег.")
    else:
        print("У вас достаточно денег.")
else:
    print("У вас маловато денег.")

'''То есть расшифровывает он как если а>б и если а > б *10,
то *****, иначе *****, если не иначе то так ****'''