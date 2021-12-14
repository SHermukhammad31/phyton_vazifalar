

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
"""



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


