import numpy as np

def uno():  
    inputUn = input('Donne moi chiffre 1\n')
    inputDeux = input('Donne moi chiffre 2\n')
    try :
        if int(inputDeux) > 0 and int(inputUn) > 0 :
            print('positif')
        else : 
            print ('negatif')
    except:
        print ('tu es débile')

def dos():
    inputUn = input('Donne moi chiffre\n')
    i=0
    test=0
    try :
        while(int(inputUn) >= i):
            test = test + i
            i+=1
        print(test)
    except:
        print ('tu es débile')

def tres():
    test = 0
    array = [1,2,3,4,5,6,7]
    for i in range(0, len(array)):
        test = array[i] + test
    print(test)

def quatro():
    test = 0
    arrayUno = [1,2,3]
    arrayDos = [1,2,3]
    for i in range(0, len(arrayUno)):
        test = arrayUno[i] * arrayDos[i] + test
    print(test)

def cinco():
    array = [1,2,3,4,5,6,7]
    maximus = max(array)
    print(maximus)

def seis():
    try :
        a = int(input("Nombre de nombre dans le tableau "))
        n = list(map(int, input("Nombre : ").strip().split()))
        test = sum(n) / len(n)
        for i in range(0, len(n)):
            if (n[i] > test):
                    print(n[i])
    except:
        print ('tu es débile')

def siete():
    vectorUno=np.array([1,2,3,4,5])
    vectorDos=np.array([1,2,3,4,5])
    vectorSomme = (vectorUno * vectorDos)
    print(vectorSomme)

def ocho():
    array = [1,2,3,4,5,6,7]
    array.sort()
    print(array)