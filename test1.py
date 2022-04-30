import math
# 1-ci sual
print(math.factorial(5))
# -------------------

def func(x): #6-ci sual
    preNumber = 0
    lastNumber = 1
    tempNumber = 0
    FiboArray = []
    FiboArray.append(0)
    while lastNumber < x:
        FiboArray.append(lastNumber)
        tempNumber =lastNumber+ preNumber
        preNumber = lastNumber
        lastNumber = tempNumber
    return FiboArray
print(func(610))
# ----------------------
# 4-CU SUAL
from os import sep


a="123456789"

t=a[::-1]
print(*t,sep=(" saniye\n"),end=(' saniye\nVaxt Bitti !'))
# ----------------------
    
# 3 CU SUAL
while True:
    phone_number = input("Nomrenizi daxil edin: ").strip()
    umumi =phone_number.startswith("+994")
    length = len(phone_number[1:])
    if phone_number[1:].isnumeric():
        if umumi:
            if length == 13 :
                 print("Qeydiyyatdan kecdiniz")
                 break
            else:
                print("nomreni duzgun qeyd edin")
        else:
            print("+994 ile baslayin")
    else:
        print("reqem daxil edin")

