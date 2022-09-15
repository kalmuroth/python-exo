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
        print ('faux')

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
        print ('faux')

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
        print ('faux')

def siete():
    vectorUno=np.array([1,2,3,4,5])
    vectorDos=np.array([1,2,3,4,5])
    vectorSomme = (vectorUno * vectorDos)
    print(vectorSomme)

def ocho():
    array = [1,2,3,4,5,6,7]
    array.sort()
    print(array)

def niete():
    inputUn = input('Donne moi chiffre\n')
    i=1
    test=1
    try :
        while(int(inputUn) >= i):
            test = test * i
            i+=1
        print(test)
    except:
        print ('faux')

def diez():
    matriceUn= [ [2, 2, 2], [2, 2, 2] ]
    matriceDeux = [ [2, 2, 2], [2, 2, 2] ]
    n=len(matriceUn)
    m=len(matriceUn[0]) 
    fusion = [[0]*m for i in range(n)] 
    for i in range(n):
        for j in range(m):
            fusion[i][j]= matriceUn[i][j] + matriceDeux[i][j]

    print("Fusion des deux matrices : ", fusion)

def eleven():
    base = 10
    f0 = 0
    f1 = 1
    print("La suite fibonacci est :")
    print(f0, ",", f1, end=" , ")
    
    for i in range(2, base):
        suivant = f0 + f1
        print(suivant, end=" , ")
        f0 = f1
        f1 = suivant

def twelve(): 
    k = int(input('Donne moi chiffre\n'))
    i = 0
    x = 1
    while (k >= i):
        i = 1/x + i
        x+=1
