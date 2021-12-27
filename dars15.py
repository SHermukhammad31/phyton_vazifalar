



"""
AMALIYOT


#1
Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z 
qo'shing. 

#2
Lug'atdagi har bir kalit va qiymatni
for tsikli yordamida, alifbo ketma-ketligida chiroyli 
qilib konsolga chiqaring. 

#3
Davlatlar va ularning poytaxtlari 
lug'atini tuzing. 

#4
Avval lug'atdagi davlatlarni, keyin poytaxtlarni 
alohida alohida, alifbo ketma-ketligida konsolga chiqaring.

#5
Foydalanuvchidan istalgan davlatni kiritishni so'rang va 
shu davlatning poytaxtini konsolga chiqaring. Agar
foydalanuvchi lug'atda yo'q davlatni kiritsa, 
"Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

#6
Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).

#7
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
taomlarni menu bilan solishtiring, agar taom menuda
bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" 
degan xabarni chiqaring
"""

print('AMALIYOT')



"""
#1
print('Python izohli lug\'atini yarating va lug\'atga kamida 10 ta so\'z') 
print('qo\'shing.\n')


python_words ={
	'print()' : 'ma`lumotlarni konso\'lga chiqaruvchi funksya.',
	'int()' : 'ma`lumotlarni int (butun son) ma`lumot turiga o\'tkazuvchi funksya.',
	'str()' : 'ma`lumotlarni str (yozuvli) ma`lumot turiga o\'tkazuvchi funksya.',
	'input()' : 'ma`lumot qabul qiluvchi funksya',
	'str' : 'yozuv ma`lumot turi.',
	'int' : 'butun son ma`lumot turi. ',
	'bool' : 'Mantiqiy ma`lumot turi.',
	'list' : 'ro\'yhat ma`lumot turi',
	'.title()' : 'Birinchi harfni yuqori registo\'rga o\'tkazuvchi str metodi.',
	'.lower()' : 'Barcha hariflarni quyi registo\'rga o\'tkazuvchi str metodi.'

}




#2
print('Lug\'atdagi har bir kalit va qiymatni')
print('for tsikli yordamida, alifbo ketma-ketligida chiroyli ')
print('qilib konsolga chiqaring. \n')


for kalit, qiymat in python_words.items():
	print('----------------------')
	print('----------------------\n')
	print(f"Kalit: {kalit}")
	print('----------------------\n')
	print(f"Qiymat: {qiymat}")
print('------------------')



print('#3')
print('Davlatlar va ularning poytaxtlari ')
print('lug\'atini tuzing.\n')
 
davlatlar = {
	'o\'zbekiston' : 'toshkent',
	'qozog\'iston' : 'olmaota',
	'aqsh' : 'vashingto\'ng',
	'rossiya' : 'maskva',
	'turkiya' : 'istambul',
	'germanya' : 'berlin',
	'fransya' : 'parij',
	'britanya' : 'london',
	'yapo\'niya' : 'tokio'
}
print(davlatlar)



print('#4')
print('Avval lug\'atdagi davlatlarni, keyin poytaxtlarni') 
print('alohida alohida, alifbo ketma-ketligida konsolga chiqaring.\n')

nomer = 0
print('DAVLATLAR:')
for n in sorted(davlatlar.keys()):
	nomer +=1
	print('--------------------')
	print(f"{nomer}.Kalit: {n.title()}")
	print('--------------------')

print('--------------------')
print('POYTAXTLAR:')
nomer = 0
for n in sorted(davlatlar.values()):
	nomer +=1
	print('--------------------')
	print(f"{nomer}.Qymat: {n.title()}")
	print('--------------------')

davlatlar = {
	'o\'zbekiston' : 'toshkent',
	'qozog\'iston' : 'olmaota',
	'aqsh' : 'vashingto\'ng',
	'rossiya' : 'maskva',
	'turkiya' : 'istambul',
	'germanya' : 'berlin',
	'fransya' : 'parij',
	'britanya' : 'london',
	'yapo\'niya' : 'tokio'
}


print('#5')
print('Foydalanuvchidan istalgan davlatni kiritishni so\'rang va') 
print('shu davlatning poytaxtini konsolga chiqaring. Agar')
print('foydalanuvchi lug\'atda yo\'q davlatni kiritsa, ')
print('"Bizda bunday ma`lumot yo\'q" degan xabarni chiqaring.\n')


for n in range(1, 5):
	print('--------------------------------')
	print(n,':')
	davlat = input('Istalgan davlat nomini kiriting_>>>')
	davlat = davlat.lower()

	if davlat in davlatlar:
		print(f"{davlat.title()}ning poytaxti {davlatlar[davlat].title()}")
	else:
		print(f"Afsus biz ma`lumotlar bazasidan '{davlat}'ni topa olmadik:(")
	print('--------------------------------')

"""

print('\n#6')
print('Restoran menusi lug\'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).\n')

menu = {
	'osh' : 20_000,
	'kabob' : 10_000,
	'somsa' : 8_000,
	'sho\'rva' : 15000,
	'manti' : 25_000,
	'choy' : 1000,
	'qahva' : 5000,
	'mastava' : 16000,
	'non' : 5000,
	'chuchvara' : 20000
}

for value, keys in menu.items():
	print('--------------------')
	print(f"Kalit: {value}, Qiymat: {keys}")
	print('--------------------')




print('#7')
print('Foydalanuvchidan 3 ta ovqat buyurtma berishni so\'rang. Foydalanuvchi kiritgan') 
print('taomlarni menu bilan solishtiring, agar taom menuda')
print('bo\'lsa narhini ko\'rsating, aks holda "bizda bunday taom yo\'q" ')
print('degan xabarni chiqaring.\n')

z = 0
narx = 0
for n in range(1, 4):
	z+=1
	buyurtma = input(f"{z}-ta`omni kiriting:")
	buyurtma = buyurtma.lower()

	if buyurtma in menu:
		print(f"Restoranimzda {buyurtma} bor! Narxi: {menu[buyurtma]} so\'m.")
		narx += menu[buyurtma]
	else:
		print(f"Afsus :( restoranimizda {buyurtma} yo\'q!")


