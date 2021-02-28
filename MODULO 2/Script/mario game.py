n= int(input("ingrese un numero como maximo hasta el 8: "))
if n>0:
    if n<9:
        for i in range (1,n+1) :
            print("")

            for j in range(1,i+1):
                print('#',end=" ")
    else:
        print("ingrese un numero entre 1 y 8")
else:
    print("ingrese un numero tiene que estar entre 1 y 8")
 