"""
ism = 'ahad'

familya = 'qayum'

isim_familya = f'{ism.title()} {familya.capitalize()}'
isim_familya = isim_familya.upper( )
print(isim_familya)
"""


"""
AMALIYOT
Quyidagi mashqlarni bajaring:

Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"


1Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
 Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat)
 qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin
 yangi qatordan yozing


Yuqoridagi matnni f-string yordamida, yangi,
 manzil deb nomlangan o'zgaruvchiga yuklang manzilga biz yuqorida o'rgangan 
 title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.

"""


"""
#1

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"


print(kocha, " ko'chasi, ", mahalla, " mahallasi, ", tuman, " tumani,", viloyat, "viloyati" )

"""

"""
#2
kocha   =  str(input("ko'changizni kiriting: " ))
mahalla =  str(input("mahallangizni kriting: " ))
tuman   =  str(input("tumaningzni kriting: "   ))
viloyat =  str(input("viloyatingzni kriting: " ))


print("siz", kocha, " ko'chasi, ", mahalla, " mahallasi, ", tuman, " tumani,", viloyat, "viloyatida yashar ekansiz!" )

"""

"""
#3

kocha   =  str(input("ko'changizni kiriting: " ))
mahalla =  str(input("mahallangizni kriting: " ))
tuman   =  str(input("tumaningzni kriting: "   ))
viloyat =  str(input("viloyatingzni kriting: " ))


print("siz", kocha, " ko'chasi,\n", mahalla, " mahallasi,\n", tuman, " tumani,\n", viloyat, "viloyatida yashar ekansiz!" )

"""

#4

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"



yangiboy = f"Siz {kocha.title()} kochasi, {mahalla.capitalize()} mahallasi, {tuman.upper()} tumani, {viloyat.lower()} viloyatda yashar ekansiz"

print(yangiboy)