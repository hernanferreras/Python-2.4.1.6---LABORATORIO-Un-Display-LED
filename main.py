def input_num():
    a = int(input("ingrese un numero no negativo para imprimir en el led: "))
    while a < 0:
        print("El numero debe ser mayor o igual a 0")
        a = input_num()
    return a

led = (('***','* *','* *','* *','***')    #numero_0
    ,('  *','  *','  *','  *','  *')    #numero_1
    ,('***','  *','***','*  ','***')    #numero_2    
    ,('***','  *','***','  *','***')    #numero_3
    ,('* *','* *','***','  *','  *')    #numero_4
    ,('***','*  ','***','  *','***')    #numero_5
    ,('***','*  ','***','* *','***')    #numero_6
    ,('***','  *','  *','  *','  *')    #numero_7
    ,('***','* *','***','* *','***')    #numero_8
    ,('***','* *','***','  *','***')    #numero_9
    )

num = str(input_num())

for z in range(5):
    for x in num:
        print(led[int(x)][z], end=' ')
    print()
