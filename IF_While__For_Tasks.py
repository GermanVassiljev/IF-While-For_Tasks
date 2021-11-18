#Ask_P=" "
#Ask_N=" "
#while type(Ask_P)!=int:
#    try:
#        Ask_P=int(input("Сколько чисел вы хотите ввести? "))
#    except:
#        ValueError
#Maks=0
#if Ask_P >0:
#    while type(Ask_N)!=int:
#        try:
#            Ask_N=int(input("Какое число вводим? "))
#        except:
#            ValueError
#    Ask_P-=1
#    Maks=Ask_N
#    while Ask_P>0:
#        Ask_P-=1
#        while type(Ask_N)!=int:
#            try:
#                Ask_N=int(input("Какое число вводим? "))
#            except:
#                ValueError
#        if Maks<Ask_N:
#            Maks=Ask_N
#    print("Максимальное значение это: " + str(Maks))
#else:
#    print("Нету максимального значения")

#Km=10
#print("Первый день: ",Km)
#S=10
#for I in range(2,8,1):
#    Km=Km*1.1
#    S+=Km
#    print("В",I,"день он пробижал: ",round(Km,2))
#print("Суммарно он пробижал: ",round(S,2))

#Ask_L=""
#Ask_M=0
#M=100
#while True:
#    Ask_L=int(input("Сколько ткани купили? "))
#    if Ask_L<=M:
#        M-=Ask_L
#        print("У нас ткани ",M)
#        if M<=0:
#            print("У нас кончилась ткань.")
#            break
#    else:
#        Ask_M=str(input("У нас осталось "+str(M)+" ткани. Хотите её купить? да или нет. "))
#        if Ask_M.lower()=="да":
#            M=0
#            print("У нас кончилась ткань.")
#            break
#        else:
#            print("Ладно...")
a=""
b=""
h=""
I=0
while True:
    I=str(input("Хотите решить трапецию? y/n: "))
    if I.lower()=="y":
        while type(a)!=int:
            try:
                a=int(input("Верхнее основание в сантиметрах: "))
            except:
                ValueError
        while type(b)!=int:
            try:
                b=int(input("Нижнее основание в сантиметрах: "))
            except:
                ValueError
        while type(h)!=int:
            try:
                h=int(input("Высота в сантиметрах: "))
            except:
                ValueError
    else:
        break
        if a<=0 and b<=0 and h<=0:
            True
        else:
            print("Площадь трапеции в сантиметрах: ",(a+b)/2*h)