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

num = input("ingrese un numero no negativo para imprimir en el led: ")

for z in range(5):
    for x in num:
        print(led[int(x)][z], end=" ")
    print()
