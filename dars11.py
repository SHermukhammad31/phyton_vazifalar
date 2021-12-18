

"""
AMALIYOT
Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

1.Foydalanuvchidan juft son kiritishni so'rang.

2.Agar foydalanuvchi juft son kiritsa "Rahmat!",
 agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

3.Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini 
quyidagicha chiqaring:

4.Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

5.Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring 
va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

6.mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.

7.Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga 
kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar 
ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
"Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" 
degan xabarlarni chiqaring.

8.Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 
5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni 
yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas 
degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha 
mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar 
do'konimizda yo'q: ....." degan xabarni chiqaring.

9.foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni 
foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda 
bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda 
"Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

10.Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan 
sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini 
konsolga chiqaring.

"""

"""

print('AMALIYOT')

print('\n1.Foydalanuvchidan juft son kiritishni so\'rang.')

son = float(input('Iltimos juft son kiriting>>>'))

print('\n2.Agar foydalanuvchi juft son kiritsa "Rahmat!",')
print(' agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.')
print('\n')


if son % 2 == 0:
    print('--------')
    print('Raxmat!')
    print('--------')

else:
    print('Bu son juft emas!')



print('\n3.Foydalanuvchi yoshini so\'rang, va muzeyga kirish uchun chipta narhini ')
print('quyidagicha chiqaring:')

print('\n4.Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo\'lsa bepul')
print('Agar foydalanuvchi 18 dan kichik bo\'lsa 10000 so\'m')
print('Agar foydalanuvchi 18 dan katta bo\'lsa 20000 so\'m\n')


yosh = int(input('Yoshingizni nechada?>>>')) #son kiriting

print('-------------------')
print('Sizga kirish narxi: ')

if 4 >= yosh :
    print('Bepul')

elif yosh >= 60:
    print('Bepul')

elif yosh <= 18:
    print('10 000 so\'m')

else :
    print('20 000 so\'m')




print('\n5.Foydalanuvchidan ikita son kiritishni so\'rang, sonlarni solishtiring ')
print('va ularning teng yoki katta/kichikligi haqida xabarni chiqaring')

son1 = float(input('1-sonni kiriting:>>>'))
son2 = float(input('2-sonni kiriting:>>>'))



if son1 == son2:
    print(f'{son1} va {son2} o\'zaro teng!')


elif son1 <= son2:
    print(f'{son1} soni kichik {son2} sonidan!')


elif son1 >= son2:
    print(f' {son1} Soni katta {son2} sonidan!')




print('6.mahsulotlar degan ro\'yxat yarating va kamida 10 ta turli mahsulotni kiriting.')

mahsulotlar = ['Olma', 'coca cola', 'kolbasa', 'sasiska', 'pepsi', 'mandarin', 'banan','go`sht', 'sabzi', 'anjir']


print('7.Yangi, savat degan bo\'sh ro\'yxat yarating va foydalanuvchidan savatga ')
print('kamida 5 ta mahsulot kiritishni so\'rang. Savatdagi elementlarni, mahsulotlar') 
print('ro\'yxati bilan solishtiring va qaysi biri ro\'yxatda bo\'lsa ')
print('"Mahsulot do\'konimizda bor" aks holda, "Mahsulot do\'konimizda yo\'q" ')
print('degan xabarlarni chiqaring.')
savat = list()




for n in range(1, 6):
    mahsulot = input(f'{n}-harid qilmoqchi bo\'lgan mahsulotingizni kiriting_>>>')

    if mahsulot in mahsulotlar:
        print('--------------------------')
        print('Mahsulot Do\'konimizda bor')
        print('--------------------------')
    else:
        print('----------------------------')
        print('Mahsulot do\'konimizda yo\'q')
        print('----------------------------')





print('8.Yuqoridagi dasturni quyidagicha o\'zgartiring: foydalanuvchidan ')
print('5 ta mahsulot kiritishni so\'rang. Foydalanuvchi so\'ragan ')
print('va do\'konda bor mahsulotlarni ')
print('yang, bor_mahsulotlar degan ro\'yxatga, do\'konda yo\'q mahsulotlarni ')
print('esa mavjud_emas degan ro\'yxatga qo\'shing. Agar mavjud_emas ')
print('ro\'yxati bo\'sh bo\'lsa, "Siz so\'ragan barcha mahsulotlar do\'konimizda bor"') 
print('degan xabarni, aks holda esa "Quyidagi mahsulotlar ')
print('do\'konimizda yo\'q: ....." degan xabarni chiqaring.')


mahsulotlar = ['Olma', 'coca cola', 'kolbasa', 'sasiska', 'pepsi', 'mandarin', 'banan','go`sht', 'sabzi', 'anjir']
savat = list()
bor_mahsulotlar = list()
mavjud_emas = list()
boshla = True


for n in range(1, 6):
    mahsulot = input(f'{n}-harid qilmoqchi bo\'lgan mahsulotingizni kiriting_>>>')

    if mahsulot in mahsulotlar:
        print('--------------------------')
        print(f'{mahsulot} Do\'konimizda bor')
        print('--------------------------')
        bor_mahsulotlar.append(mahsulot)
    else:
        boshla = False
        print('----------------------------')
        print(f'{mahsulot} do\'konimizda yo\'q')
        print('----------------------------')
        mavjud_emas.append(mahsulot)


    
if boshla :
    print('---------------------------------------------------')
    print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor!')
    print('---------------------------------------------------')

else:
    print('------------------------------------------')
    print(f'Siz so\'ragan quydagi: {mavjud_emas} ')
    print('mahsulotlar afsuski do\'konimzda yo\'q!')
    print('------------------------------------------')


print('9.foydalanuvchilar degan ro\'yxat tuzing, va kamida 5 ta login qo\'shing.') 
print('Foydalanuvchidan yangi login tanlashni so\'rang va foydalanuvchi kiritgan ')
print('loginni foydalanuvchilar degan ro\'yxatning tarkibi bilan solishtiring. ')
print('Agar ro\'yxatda bunday login mavjud bo\'lsa, "Login band, yangi login tanlang!" ')
print('aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.')


foydalanuvchilar = ['temirov', 'shermukhammad', 'shake', 'xon007', 'agent007', 'jeyms_bond']
boshla = 1
toxta = 3




for n in range(boshla, toxta):
    print('Sign in:')
    yangi_boy = input('o\'zingiz uchun yangi login kiriting_>>>')

    if yangi_boy in foydalanuvchilar:
        print('-----------------------------------')
        print(n)
        print(f'Kechirasiz ushbu {yangi_boy} band!')
        print('Yangi login tanlang')
        print('-----------------------------------')
        toxta =+ 2
    else:
        print('-----------------------------')
        print(f'Xush kelibsiz, foydalanuvchi!')
        print('-----------------------------')
"""



print('10.Foydalanuvchidan biror butun son kiritishni so\'rang.')
print('Foydalanuvchi kiritgan sonni 2 da 10 gacha bo\'lgan sonlardan qay') 
print('biriga qoldiqsiz bo\'linishini konsolga chiqaring.')


son = int(input('Butun son kiriting_>>>'))
natija = list()



for n in range(2, 11):
    if son % n == 0:
        natija.append(n)
        bosh = True
        



print(f'{son} soni {natija} qoldiqsiz bo\'linadi! ')
    


        


        






 



