def cero(lista): #numero 0
    print(lista[3])
    for x in range(3):
        print(lista[2])
    print(lista[3])
    
def uno(lista):  #numero 1
    for x in range(5):
        print(lista[1])
    
def dos(lista):  #numero 2
    print(lista[3])
    print(lista[1])
    print(lista[3])
    print(lista[0])
    print(lista[3])
    
def tres(lista):  #numero 3
    for x in range(2):
        print(lista[3])
        print(lista[1])
    print(lista[3])
   
def cuatro(lista):  #numero 4
    for x in range(2):
        print(lista[2])
    print(lista[3])
    for x in range(2):
        print(lista[1])

def cinco(lista):  #numero 5
    print(lista[3])
    print(lista[0])
    print(lista[3])
    print(lista[1])
    print(lista[3])

def seis(lista):  #numero 6
    print(lista[3])
    print(lista[0])
    print(lista[3])
    print(lista[2])
    print(lista[3])

def siete(lista):  #numero 7
    print(lista[3])
    for x in range(4):
        print(lista[1])

def ocho(lista):  #numero 8
    for x in range(2):
        print(lista[3])
        print(lista[2])
    print(lista[3])

def nueve(lista):  #numero 9
    print(lista[3])
    print(lista[2])
    print(lista[3])
    print(lista[1])
    print(lista[3])

dicc = {
    "0":"cero",
    "1":"uno",
    "2":"dos",
    "3":"tres",
    "4":"cuatro",
    "5":"cinco",
    "6":"seis",
    "7":"siete",
    "8":"ocho",
    "9":"nueve",
}

led = ["*  ", "  *", "* *", "***"]     
num_strng = input("Ingrese un numero para presentarlo en el led: ")
#num_strng= str(num)

for x in num_strng:
    valor = dicc[x]
    if valor == "cero":
        cero(led)
    elif valor == "uno":
        uno(led)
    elif valor == "dos":
        dos(led)
    elif valor == "tres":
        tres(led)
    elif valor == "cuatro":
        cuatro(led)
    elif valor == "cinco":
        cinco(led)
    elif valor == "seis":
        seis(led)
    elif valor == "siete":
        siete(led)
    elif valor == "ocho":
        ocho(led)
    else:
        nueve(led)
