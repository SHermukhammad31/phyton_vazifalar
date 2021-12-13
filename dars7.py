#MAVZU: List ro'yhatlar

#mevalar = ['olma', 'anjir', 'Behi']

#del mevalar [-1]

#print(mevalar [-1],'Ma`lumot turi:', type(mevalar))

"""

AMALIYOT:

Quydagi mashiqlarni bajaring:

1. Isimlar degan ro'yhat yarating va kamida 3
ta yaqin do'stingizning ismini kiriting 

2. Ro'yhatdagi harbir do'stingizga qisqa
xabar yozib konsolga chiqaring:

salom abror, bugun choyxona bormi?
Mahmud, choyxonaga boramizmi?

3.sonlar deb nomlangan ro'yhat yarating
va ichiga turli sonlar yuklang (musbat,
manfiy, butun , o'nlik).

4.t_shaxslar va z_shaxslar degan 
2 ta ro'yhat yarating va biriga o'zingiz eng 
ko'p hurmat qiladigan tarixiy shaxslarning,
ikkinchisiga esa zamonamizdagi trik 
bo'lgan shaxslarning ismini kiriting. 

5.Yuqoridagi ro'yxatlarning har biridan 
bittadan qiymat olib .pop(), quydagi ko'rinishda chiqaring:

    Men tarixiy shaxslardan Imom Buxoriy bilan,
    zamonaviy shaxslardan esa  Bil Getes bilan 
    suhbat qilishni istar edim!

6.friends nomli bo'sh ro'yhat tuzing va
unga append() yordamida 5-6 ta 
mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

6.Yuqoridagi ro'yhatdan mehmonga kela
olmaydign odamlarni .remove() 
metodi yordamida o'chirib tashlang

7.Ro'yhatning oxiriga, boshiga va o'rtasiga 
yangi isimlarni qo'shing

8.Yangi mehmonlar deb nomlangan 
bo'sh ro'yhat yarating. .pop() va 
.append() metodlari yordamida
mehmonga kelgan do'stlaringizning 
ismini friends ro'yxatidan sug'urib olib,
mehmonlar ro'yhatiga qo'shing!

"""

#1. Isimlar degan ro'yhat yarating va kamida 3ta yaqin do'stingizning ismini kiriting 

isimlar = ['Anvar', 'Aziz', 'Aziza']

#2. Ro'yhatdagi harbir do'stingizga qisqa xabar yozib konsolga chiqaring:

print(f'{isimlar[0]} salom bormisan!')
print(f'{isimlar[1]} salom jigar!')
print(f'{isimlar[-1]} salom qalaysan!')


"""
3.sonlar deb nomlangan ro'yhat yarating
va ichiga turli sonlar yuklang (musbat,
manfiy, butun , o'nlik).
"""

sonlar = [152, -68, 56.39, 56]


"""
4.t_shaxslar va z_shaxslar degan 
2 ta ro'yhat yarating va biriga o'zingiz eng 
ko'p hurmat qiladigan tarixiy shaxslarning,
ikkinchisiga esa zamonamizdagi trik 
bo'lgan shaxslarning ismini kiriting.
"""

t_shaxslar = ['Muhammad S.A.V.', 'Amir Temur', 'Jaloliddin Rumiy']

z_shaxslar = ['Temurbek Adhamov', 'Umidjon Ishmuhammaedov', 'Laziz Adhamov']


"""
5.Yuqoridagi ro'yxatlarning har biridan 
bittadan qiymat olib .pop(), quydagi ko'rinishda chiqaring:

    Men tarixiy shaxslardan Imom Buxoriy bilan,
    zamonaviy shaxslardan esa  Bil Getes bilan 
    suhbat qilishni istar edim!
"""

print(f'\nMen tarixiy shaxslardan {t_shaxslar[-1]} bilan, \nzamonaviy shaxslardan esa {z_shaxslar[-1]} bilan \nsuhbat qilishni istar edim!')


"""
6.friends nomli bo'sh ro'yhat tuzing va
unga append() yordamida 5-6 ta 
mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

"""

friends = []

friends.append('Dilshod')
friends.append('Faxriddin')
friends.append('Xudayberdi')
friends.append('Abdulaziz')
friends.insert(0, 'Suxrob')

print(friends)

"""
6.Yuqoridagi ro'yhatdan mehmonga kela
olmaydign odamlarni .remove() 
metodi yordamida o'chirib tashlang
"""

friends.remove('Dilshod')
friends.remove('Faxriddin')

print(friends)


"""
7.Ro'yhatning oxiriga, boshiga va o'rtasiga 
yangi isimlarni qo'shing
"""

friends.append('Xumoyin')
friends.insert(0,'SHirinqul')
friends.insert(-3, 'Og\'abek')

print(friends)


"""
8.Yangi mehmonlar deb nomlangan 
bo'sh ro'yhat yarating. .pop() va 
.append() metodlari yordamida
mehmonga kelgan do'stlaringizning 
ismini friends ro'yxatidan sug'urib olib,
mehmonlar ro'yhatiga qo'shing!
"""

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))





print('Do\'stlar: ', friends)
print('mehmonlar: ', mehmonlar)



