#8-dars

"""
Amaliyot:


1.Yangi cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
degan ro'yxat tuzing, ro'yxat elementlarining 
birinchi harfini katta qilib konsolga 
chiqaring. Gm uchun ikkala  harfni 
katta qiling.



2.Yuqooridagi mashiqni teng emas (!=)
operatori yordamida bajaring.



3.Foydalanuvchi login ismini  so'rang. Agar
login  admin bo'lsa, xushkelibsiz Admin. "Foydalanuvchilar
ro'yxatini ko'rasizmi?" xabarini
konsolga chiqaring. Aks holda, "Xush 
kelibsiz,
{foydalanuvchi_ismi}! matnini 
konsolga chiqaring."



4.Foydalanuvchidan 2 ta son kiritishini
so'rang. Agar ikki son bir-birig  teng bo'lsa 
"Sonlar teng " degan yozuvni komsolga chiqaring.



5.Foydalanuvchidan  istalgan son kiritishni
so'rang. Agar son manfiy son bo'lsa konsolga 
"Manfiy son" , agar musbat bo'lsa
"Musbat son" degan xabarni chiqaring.



6.Foydalanuvchidan son kiritishni so'rang,
agar son musbat bo'lsa uning ildizini hsoblab konsolga chiqaring. 
Agar son manfiy bo'lsa, "Musbat son kiriting"
degan xabarni chiqaring.
"""


"""

print('Amaliyot:')


print('1.Yangi cars=[\'toyota\', \'mazda\', \'hyundai\', \'gm\', \'kia\']')
print('degan ro\'yxat tuzing, ro\'yxat elementlarining ')
print('birinchi harfini katta qilib konsolga ')
print('chiqaring. Gm uchun ikkala  harfni ')
print('katta qiling.')


f=0
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

print('\n cars: ', cars)

for n in cars:
	if n != cars[3]:
		print(f'>>> {n.title()}')
		print('------------')
	else:
		print('>>>', n.upper())
		print('------------')

print('\n2.Yuqooridagi mashiqni teng emas (!=)')
print('operatori yordamida bajaring.\n')




print('3.Foydalanuvchi login ismini  so\'rang. Agar')
print('login  admin bo\'lsa, xushkelibsiz Admin. "Foydalanuvchilar')
print('ro\'yxatini ko\'rasizmi?" xabarini')
print('konsolga chiqaring. Aks holda, "Xush ')
print('kelibsiz,')
print('\{foydalanuvchi_ismi\}! matnini ')
print('konsolga chiqaring.')



print('\n ----------')
print('Assalomu alaykum mehmon xushkelibsiz: ')

foydalanuvchilar = ['Anvar', 'Aziz', 'Nigora', 'Oybek']

isim = str(input('Ismingiz_>>>'))
login =  str(input('Loginingiz_>>'))



if login.lower() != 'admin' :
	print(f'Xush kelibsiz {isim} !')
	print('------------')

else :
    print('Xush kelibsiz',  login, ' !')
    print('Foydalanuvchilar ro\'yhatini ko\'rasizmi?>>>')
	
print('------------')





print('4.Foydalanuvchidan 2 ta son kiritishini')
print('so\'rang. Agar ikki son bir-birig  teng bo\'lsa ')
print('"Sonlar teng " degan yozuvni komsolga chiqaring.')


print('----------------')
son1 = input('1-Istalgan son kriting>>>')
print('----------------')
son2 = input('2-Istalgan son kriting>>>')


if son1 == son2:
	print('--------------')
	print(f'{son1} va {son2} sonlari teng ekan!!!')
	print('Sonlar teng')

else:
	print(f'{son1} va {son2} sonlari teng emas ekan!!!')

"""



print('5.Foydalanuvchidan  istalgan son kiritishni')
print('so\'rang. Agar son manfiy son bo\'lsa konsolga ')
print('"Manfiy son" , agar musbat bo\'lsa')
print('"Musbat son" degan xabarni chiqaring.')


print('_________________')
while True:
    son3 = float(input('Istalgan son kiriting>>>'))


    if son3 <= 0:
	    
    	print(son3,' soni manfiy son!')
    	print('_________________')
    else:
    	
    	print(son3,' soni musbat son!')
    	print('_________________')

    if son3 == 9:
    	print('Xayir !')
    	break