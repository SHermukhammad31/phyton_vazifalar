#8-dars

#Tartiblash:
sonlar = [16, 8, 0 , 3, 1, 12, 6, 20]
sonlar2 = sorted(sonlar)

#print('sonlar: ', sonlar, type(sonlar))

#print('sonlar2: ', sonlar2, type(sonlar2))

#print('sonlar: ', sonlar, type(sonlar))

"""
AMALIYOT:

1.o'zingizga ma`lum davlatlarning ro'yhatini 
 tuzing va ro'yhatni konsolga chiqaring 

2.ro'yhatning uzunligini konsolga chiqaring

3.sorted() funksiyasi orqali 
 ro'yxatni tartiblangan holda konsolga chiqaring  

4.sorted() funksiyasi orqali 
 ro'yhatni teskari tartibda  konsolga chiqaring  

5.Asil ro'yhatni qaytadan konsolga chiqaring

6.reverse() metodi yordamida ro'yhatni 
 ortidan boshlab chiqaring

7.sort() metodi yordamida ro'yhatni avval
 alifbo bo'yicha, keyin esa alifboga 
 teskari tartibda konsolga chiqaring.

8.120 dan 1200 gacha bo'lgan juft sonlar
 ro'yhatini tuzing

9.ro'yhatdagi sonlar yig'indisini hsoblang va
 konsolga chiqaring.

10.ro'yhatdagi eng katta va eng kichi son
 o'rtasidagi ayirmani hsoblang va
 konsolga chiqaring

11.Ro'yhatdagi elementlar sonini hsoblang

12.Ro'yhatning boshidan, o'rtasidan va oxiridan
 20ta qiymatni konsolga chiqaring

13.taomlar degan ro'yhat yarating va 
 ichiga istalgan 5ta taomni kriting.

14.nonushta degan yangi ro'yxatga
 taomlardan nusxa oling.

15.Yangi ro'yhatda faqat nonushtaga 
 yeyiladiag taomlarni qoldiring, va 
 qo'shimcha yangi 2ta taom kriting.

16.ikkala ro'yhatni ham (taomlar va
nonushta) konsolga chiqaring.

17.Yuqoridagi nonishta  ro'yhatini o'zgarmas
ro'yhatga  aylantiring va nonushta[0] = "qaymoq
va non" deb qiymat berib
ko'ring.


#Tuple
"""

#'AQSH', 'Rossiya', 'Germanya', 'Xitoy', 'Turkiya', 'Italiya', 'albanya'
davlatlar = ['Belgya', 'albanya', 'belgya', 'City', 'city','Albanya', 'Uzb']
"""
print('1.o\'zingizga ma`lum davlatlarning ro\'yhatini') 
print('tuzing va ro\'yhatni konsolga chiqaring. ')
print(' ')

print('davlatlar o\'zgaruvchisi qiymati: ', davlatlar)
print(' ') 


print('2.ro\'yhatning uzunligini konsolga chiqaring')
print(' ')
print(f'Ro\'yhat ichida {len(davlatlar)} element bor !')
print(' ')


print('3.sorted() funksiyasi orqali') 
print(' ro\'yxatni tartiblangan holda konsolga chiqaring ')
print(' ')
print('davlatlar o\'zgaruvchisi tartiblangan holda: ', sorted(davlatlar))
print(' ')


print('4.sorted() funksiyasi orqali') 
print(' ro\'yhatni teskari tartibda  konsolga chiqaring')
print(' ')
d_uzunligi = int(len(davlatlar))
print(f'davlatlar ro\'yhati alifboga teskari tartibda: {sorted(davlatlar, reverse = True)} shunaqa bo\'ladi')



print('5.Asil ro\'yhatni qaytadan konsolga chiqaring')
print(' ')
print(f'Asil davlatlar ro\'yhati: {davlatlar} shunaqa ko\'rinishda!')


print('6.reverse() metodi yordamida ro\'yxatni ')
print(' ortidan boshlab chiqaring')
print(' ')
print('Asil: ', davlatlar)
davlatlar.reverse()
print('Reversa metodi yordamida: ', davlatlar)



print('7.sort() metodi yordamida ro\'yhatni avval')
print(' alifbo bo\'yicha, keyin esa alifboga ')
print(' teskari tartibda konsolga chiqaring. ')
davlatlar.sort()
print('Alifbo tartibi bo\'yicha: ', davlatlar)
davlatlar.sort(reverse = True)
print('Alifbo tartibga teskari: ',davlatlar)



print('8.120 dan 1200 gacha bo\'lgan juft sonlar')
print(' ro\'yhatini tuzing')

j_sonlar = list(range(120, 1_201, 2))
#print(j_sonlar)




print('9.ro\'yhatdagi sonlar yig\'indisini hsoblang va')
print(' konsolga chiqaring.')
javob = int()

for s in j_sonlar:
    javob = javob + s

print(javob)
print('')



print('10.ro\'yhatdagi eng katta va eng kichi son')
print(' o\'rtasidagi ayirmani hsoblang va')
print(' konsolga chiqaring')
ayirma = max(j_sonlar) - min(j_sonlar)

print('Javob: ', ayirma)
print('')




print('11.Ro\'yhatdagi elementlar sonini hsoblang')
print(f'Elementlar soni: {len(j_sonlar)} ta !')





print('12.Ro\'yhatning boshidan, o\'rtasidan va oxiridan')
print(' 20ta qiymatni konsolga chiqaring')
print(' ')


r_boshi = j_sonlar[0]

ortasi_i = int(len(j_sonlar) / 2)
r_ortasi = ortasi_i - 3

r_oxri = [-1]


#print(ortasi_i)
#print(r_ortasi)
#print(min(j_sonlar))



print('Boshidan 7ta element: ')
for k in range(1, 8):
    print('index: ', k, 'element: ', j_sonlar[k])


boshla = r_ortasi
toxta = r_ortasi + 7
print(' ')
print('O\'rtasidan 6 ta element: ')
for son in range(boshla, toxta):
    print('index: ', son, 'element: ', j_sonlar[son])


print(' ')
print('Ro\'yxat oxiridan 7ta element: ')
for son2 in range(-7, 0):
    print('index: ', son2, 'element: ', j_sonlar[son2])

"""


print('\n13.taomlar degan ro\'yhat yarating va') 
print(' ichiga istalgan 5ta taomni kriting.')

taomlar = ['osh', 'manti', 'sho\'rva', 'somsa', 'kabob']
print('\n taomlar ro\'yhati: ', taomlar)


print('\n \n14.nonushta degan yangi ro\'yxatga')
print(' taomlardan nusxa oling.')

nonushta = taomlar[:]
print('\n nonushta ro\'yhati elementlari: ', nonushta)





print('\n\n15.Yangi ro\'yhatda faqat nonushtaga ')
print(' yeyiladiag taomlarni qoldiring, va ')
print(' qo\'shimcha yangi 2ta taom kriting.')

nonushta.remove('osh')
nonushta.remove('kabob')
print('\nnonushta: ', nonushta)
nonushta.append('choy')
nonushta.insert(2,'quymoq')
print('nonushta ga 2ta taom qo\'shildi: ', nonushta)




print('\n\n16.ikkala ro\'yhatni ham (taomlar va')
print('nonushta) konsolga chiqaring.')
print('\nnonushta ro\'yhati: ', nonushta)
print('\ntaomlar ro\'yhati : ', taomlar)




print('\n\n17.Yuqoridagi nonishta  ro\'yhatini o\'zgarmas')
print('ro\'yhatga  aylantiring va nonushta[0] = "qaymoq')
print('va non" deb qiymat berib ko\'ring.')

nonushta = tuple(nonushta)
nonushta.append('qaymoq va non')
print('nonushta: ', type(nonushta),nonushta)
