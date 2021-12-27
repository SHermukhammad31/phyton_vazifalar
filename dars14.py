#14
#Lug'at (DICTIONARY)

"""
AMALIYOT

#1
otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga
shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, 
shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga 
chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

#2
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta 
ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga 
chiqaring: Alining sevimli taomi osh

#3
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar 
o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, 
float, string, if, else va hokazo) va har birining 
qisqacha tarjimasini yozing. Foydalanuvchidan biror so'z 
kiritishni so'rang va so'zning tarjimasini yuqoridagi 
lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, 
"Bunda so'z mavjud emas" degan xabarni chiqaring.

#4
Yuqoridagi vazifani if-else yordamida qiling va 
natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
"""

#1
"""
print('otam (onam, akam, ukam, va hokazo) degan lug\'at yarating va lug\'atga')
print('shu inson haqida kamida 3 ta m\'alumot kiriting (ismi, tu\'gilgan yili, ')
print('shahri, manzili va hokazo). Lug\'atdagi ma\'lumotni matn shaklida konsolga') 
print('chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug\'ilgan')


otam = {\
    'ism' : 'xolboy',
    't_yil' : 1956,
    'viloyat' : 'samarqand',
    'tuman' : 'Qo\'shrabot'

    }


onam = {\
    'ism' : 'gulnora',
    't_yil' : 1956,
    'viloyat' : 'samarqand',
    'tuman' : 'Qo\'shrabot'

    }


akam = {\
    'ism' : 'ro\'ziboy',
    't_yil' : 1994,
    'viloyat' : 'samarqand',
    'tuman' : 'Qo\'shrabot'

    }


"""

"""

print('-----------------------------------------------------------------------------------------------------')
print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda  {otam['viloyat'].title()} viloyatida tug\'ilgan!")
print('-----------------------------------------------------------------------------------------------------')
print(f"Onamning ismi {onam['ism'].title()}, {onam['t_yil']}-yilda  {onam['viloyat'].title()} viloyatda tug\'ilgan!")
print('-----------------------------------------------------------------------------------------------------')
print(f"Akamning ismi {akam['ism'].title()}, {akam['t_yil']}-yilda  {akam['viloyat']} viloyatda tug\'ilgan!")
print('-----------------------------------------------------------------------------------------------------')




#2
print('Oila a`zolaringizning sevimli taomlari lug\'atini tuzing. Lug\'atda kamida 5 ta')
print('ism-taom jufltigi bo\'lsin. Kamida uch kishining sevimli taomini konsolga') 
print('chiqaring: Alining sevimli taomi osh')


sevimli_taomlar = {\
    'ali' : 'Osh',
    'vali' : 'Xonim',
    'anvar' : 'Somsa',
    'akmal' : 'SHo\'rva',
    'elbek' : 'LAG\'MON'
    }
print(f"Alining sevimli taomi {sevimli_taomlar['ali'].capitalize()}!")
print(f"Valining sevimli taomi {sevimli_taomlar['vali'].capitalize()}!")
print(f"Anvarning sevimli taomi {sevimli_taomlar['anvar'].capitalize()}!")
print(f"Akmalning sevimli taomi {sevimli_taomlar['akmal'].capitalize()}!")
print(f"Elbekning sevimli taomi {sevimli_taomlar['elbek'].capitalize()}!")


print('#3')
print('Python izohli lu\'gati tuzing: Lug\'atga shu kunga qadar') 
print('o\'rgangan 10 ta so\'z (atamani) kiriting (masalan integer, ')
print('float, string, if, else va hokazo) va har birining ')
print('qisqacha tarjimasini yozing. Foydalanuvchidan biror so\'z') 
print('kiritishni so\'rang va so\'zning tarjimasini yuqoridagi ')
print('lug\'atdan chiqarib bering. Agar so\'z lu\'gatda mavjud bo\'lmasa, ')
print('"Bunda so\'z mavjud emas" degan xabarni chiqaring.')
print('--------------------------------------------------\n')


python_words = {\
    'integer' : 'butun son ma`lumot turi!' ,
    'float' : 'qoldiq son ma`lumot turi!',
    'type()' : 'Ma`lumot turini aniqlovchi funksya!',
    'print()' : 'Ma`lumotni konsolga chiqaruvchi funksya!',
    '.upper()' : 'Barcha hariflarni yuqori registorga o\'tkazuvchi metod',
    '.lower()' : 'Barcha hariflarni quyi registorga o\'tkazuvchi metod',
    '.title()' : 'Birinchi harifni yuqori registorga o\'tkazuvchi metod',
    '.capitalize()' : 'Birinchi harifni yuqori registorga o\'tkazuvchi metod',
    '/n' : 'Yaangi qatorga ajratuvchi buyruq',
    'input()' : 'Ma`lumot qabil qiluvchi funksya!'



    }


print(python_words)
print('----------------------------------------------------')


print('Pythonga oyid atama kiriting.')
for n in range(5):
    print(n)
    print('-----------------')
    z = input('INPUT__>>>')
    z.lower()
    z.lstrip()
    z.rstrip()
    print('-----------------')
            
    print(python_words.get(z, f"Kechrasiz biz ma`lumotlar bazsidan '{z}ni' topolmadik!"))
    print('-----------------')
"""


print('#4')
print('Yuqoridagi vazifani if-else yordamida qiling va ')
print('natijani ham foydalanuvchiga tushunarli ko\'rinishda chiqaring.')


python_words = {
    'integer' : 'butun son ma`lumot turi!' ,
    'float' : 'qoldiq son ma`lumot turi!',
    'type()' : 'Ma`lumot turini aniqlovchi funksya!',
    'print()' : 'Ma`lumotni konsolga chiqaruvchi funksya!',
    '.upper()' : 'Barcha hariflarni yuqori registorga o\'tkazuvchi metod',
    '.lower()' : 'Barcha hariflarni quyi registorga o\'tkazuvchi metod',
    '.title()' : 'Birinchi harifni yuqori registorga o\'tkazuvchi metod',
    '.capitalize()' : 'Birinchi harifni yuqori registorga o\'tkazuvchi metod',
    '/n' : 'Yaangi qatorga ajratuvchi buyruq',
    'input()' : 'Ma`lumot qabil qiluvchi funksya!'



    }


print(python_words)
print('----------------------------------------------------')


print('Pythonga oyid atama kiriting.')
for n in range(5):
    print(n)
    print('-----------------')
    z = input('INPUT__>>>')
    z.lower()
    z.lstrip()
    z.rstrip()
    print('-----------------')

    if z in python_words:
        print(python_words[z])

    else:
        print(f"Kechrasiz biz ma`lumotlar bazsidan '{z}ni' topolmadik!")


    print('-----------------')


