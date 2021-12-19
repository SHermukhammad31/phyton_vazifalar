"""
AMALIYOT
Quyida bir nechta kodlar berilgan, kodlar avvalgi darsdagi uy vazifalaridan iborat. Kodlardagi xatolarni toping va to'g'rilang. Har bir dasturda bir nechta xatolar mavjud bo'lishi mumkin. Xatolarni topish uchun dasturlarni bir necha marta, turli qiymatlar bilan bajarib ko'ring.

#1
son = float(input("Juft son kiriting: ")
if son%2==0:
    print("Bu son juft emas.')
else:
    print("Rahmat!"))


#2
yosh = (input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18
    narh = 10000
else:
    narh = 20000
    print(f"Chipta {narh} so'm")



#3
x = float(input("Birinchi sonni kiriting: ")
y = float(input("Ikkinchi sonni kiriting: ")
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}")
else
    print(f"{x}>{y}")



#4
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun'

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")  



mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


#5
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: '))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahslot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
   



users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:' )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")
"""


#Javoblar
"""
#1son = float(input('Juft son kiriting: '))
if son%2!=0:
    print('Bu son juft emas.')
else:
    print('Rahmat!')




#2yosh = int(input('Yoshingiz nechida?'))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f'Chipta {narh} so\'m')





#3x = float(input('Birinchi sonni kiriting:'))
y = float(input('Ikkinchi sonni kiriting: '))
if x==y:
    print(f'{x} = {y}')
elif x<=y:
    print(f'{x} < {y}')
else:
    print(f'{x} > {y}')





#4

mahsulotlar = ['un', 'yog\'', 'sovun', 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = list()
yoqlar = list()
borlar = list()

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
    


for mahsulot in savat :
        if mahsulot in mahsulotlar:
            borlar.append(f'Do\'konimizda {mahsulot} bor')
        else:
            yoqlar.append(f'Do\'konimizda {mahsulot} yo\'q')

if len(yoqlar) == 5:
    print('Savatingiz bo\'sh') 

else:
    for n in yoqlar:
        print('------------------------')
        print(n)
        print('------------------------')
    for z in borlar:
        print('------------------------')
        print(z)
        print('------------------------')


#5
mahsulotlar = ['un', 'yog\'', 'sovun', 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)



if len(mavjud_emas) != 0:
    print('Do\'konimizda quyidagi mahsulotlar yo\'q:')
    for n in mavjud_emas:
        print('------------------')
        print(n)
        print('------------------')

else:
    print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
"""

 
 
#6
users = ['alisher1983', 'aziza', 'yasina', 'umar']

login = input('Yangi login tanlang:' )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print('Xush kelibsiz!')     