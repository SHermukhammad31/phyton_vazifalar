#mehmonlar = ['Ali', 'Baxodir', 'Bexruz']

#for bek in mehmonlar:
#	print('Salom', bek , 'Qalisiz?')

"""
sonlar = list(range(1,11))

for son in sonlar:
	print(f"{son} ning kvadrati: {son**2} ga teng")



dostlar = []
print('5ta eng yaqin do\'stingiz kim? ')
for n in range(5):
    dostlar.append(input(f'{1+n}chi dostingiz ismi?>>>'))
    print("----------------------------------  \n----------------------------------")

print("ro\'yhat: ", dostlar)
"""


"""
AMALIYOT


1.Kamida 5 elementdan iborat isimlar
degan ro'yhat tuzing, va ro'yhatdagi har bir 
ismga takrorlanuvchi xabar yozing 



2.Yuqoridagi tsikl tugagandan so'ng,
ekranga "Kod n marta takrorlanadi " degan 
xabarni chiqaring (n o'rniga kod
nech marta takrorlanganini yozing)



3.10 da 100 gacha bo'lgan toq sonlar ro'yhatini 
tuzing. Ro'yxatning xar bir 
elementining kubini yangi qatorda 
konsolga chiqaring.



4.Foydalanuvchidan 5 ta eng sevimli
kinolarini kiritishni so'rang va kinolar
degan ro'yxatga saqlab oling. Natijani konsolga
chiqaring.



4.Foydalanuvchidan bugun nechta odam 
bilan uchrashganini (suhbatlashganini)
so'rang va har bir suhbatlashgan 
odamining ismini birma bir so'rab 
ro'yxatga yozing. Ro'yxatini konsolga 
chiqaring. 
"""


"""
print('\n\n\nAMALIYOT')


print('1.Kamida 5 elementdan iborat isimlar')
print('degan ro\'yhat tuzing, va ro\'yhatdagi har bir ')
print('ismga takrorlanuvchi xabar yozing')


isimlar = ['Anvar', 'Temurbek', 'Olim', 'Aziz', 'Abdulaziz', 'Akmal']
z = 0

for n in isimlar:
    print(f'\n Assalomu alaykum {n} sizni bugungi bazmimizga lutfan chaqirib qolamiz!')
    print('---------------------')
    z = z + 1
print(f'Ko\'d {z} marta takrorlanadi !')




print('\n\n\n2.Yuqoridagi tsikl tugagandan so\'ng,')
print('ekranga "Kod n marta takrorlanadi " degan') 
print('xabarni chiqaring n o\'rniga kod')
print('nech marta takrorlanganini yozing')



print('3.10 da 100 gacha bo\'lgan toq sonlar ro\'yhatini') 
print('tuzing. Ro\'yxatning xar bir ')
print('elementining kubini yangi qatorda ')
print('konsolga chiqaring.')


toq_sonlar = list(range(9, 100, 2))
print(f'Toq sonlar: {toq_sonlar}')

for f in toq_sonlar:
    print(f'{f} sonining kubi {f**3} ga teng!')




print('4.Foydalanuvchidan 5 ta eng sevimli')
print('kinolarini kiritishni so\'rang va kinolar')
print('degan ro\'yxatga saqlab oling. Natijani konsolga')
print('chiqaring.')
kinolar = list()

for n in range(1, 6):
    kinolar.append(input(f'{n}-yoqtirgan kinoyingiz >>>'))

print(kinolar)
"""


print('4.Foydalanuvchidan bugun nechta odam ')
print('bilan uchrashganini (suhbatlashganini)')
print('so\'rang va har bir suhbatlashgan') 
print('odamining ismini birma bir so\'rab') 
print('ro\'yxatga yozing. Ro\'yxatini konsolga ')
print('chiqaring.')

speekers = list()

suhbat = int(input('\nBugun nechta odam bilan suhbatlashdingiz? >>>' )) 
for z in range(1, suhbat+1):
    speekers.append(input(f'{z}-suhbatlashgan odamingiz ismi >>>'))

print('speekers ro\'yhati: ', speekers)
