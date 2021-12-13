

"""
Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:

`"Nexia", "Tico", 'Damas' ko'rganlar qilar havas`

Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:
1. 5 ning 4-darajasini toping
2. 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
3. Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
4. Diametri 12 ga teng bo'lgan doiraning yuzini toping  ( $\pi=3.14$ deb oling)
5. Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping ([Pifagor teoremasidan](https://fayllar.org/pifagor-teoremasi-va-uning-turli-hil-isbotlari-mavzusida-tajer.html) foydalaning)

>#### !! Javoblarni savol va yechim ko'rinishida chiqaring: `5 ning 4-darajasi 625` !!

"""


print('"Nexia", "Tico", \'Damas\' ko\'rganlar qilar havas')

print('5 ning 4-darajasi: ', 5**4,'ga teng!')

print('22 ni 4 ga bo\'lganda qancha qoldiq qoladi?')
print('Javob: ', 22%4)

print('Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping')
print('Javob: ', 'perimetri: : ', 125*4, ' , ', 'yuzi esa ', 125*125, 'ga teng!')

print('\n Diametri 12 ga teng bo\'lgan doiraning yuzini toping  ( $\pi=3.14$ deb oling)')
PI = 3.14
d = 12
r = d / 2
s = 2 * PI * r ** 2
print('Javob: ', 'Yuzi ', s, 'ga teng!' )


import math
print('Katetlari 6 va 7 bo\'lgan to\'g\'ri burchakli uchburchakning gipotenuzasini toping ')



a=6
b=7

c=(a**2)+(b**2)

c2=math.sqrt(c)
c2=c2//1

print('Javob: ', c2, 'ga teng!')