import time
def corpo_1():
    
    queda =  False
    salto =  False 
    passo = -1
    passo_peso = 1 
    massa_c1 = 1
    pos_c1x, pos_c1y = [200], [200]

    peso_c1 = [(massa_c1 * gravidade) + 1]
    força_oposta_c1 = [(+massa_c1 * gravidade)+ 1]
    força_resultante_c1 = [(peso_c1[0] - força_oposta_c1[0])]
    
    if salto:

        for peso_c1[0] in range(peso_c1[0], 0, passo):
            
            time.sleep(0.5 )
            força_oposta_c1[0] += passo_peso
            peso_c1[0] -= passo_peso
            força_resultante_c1[0] += força_oposta_c1[0] - peso_c1[0]
            print(peso_c1)
            
            for pos_c1y[0] in pos_c1y:
                
                pos_c1y[0] -= passo_peso
                print(pos_c1y)
    
    if peso_c1[0] == 0:
        passo = +1
        passo_peso = - 1 
        salto = False
        queda = True

    if peso_c1[0] == 10:
        salto = False

    if queda:

        for peso_c1[0] in range(peso_c1[0], 10, passo):
            
            time.sleep(0.1)
            força_oposta_c1[0] += passo_peso
            peso_c1[0] -= passo_peso
            força_resultante_c1[0] += força_oposta_c1[0] - peso_c1[0]
            print(peso_c1)
            
            for pos_c1y[0] in pos_c1y:
                
                pos_c1y[0] -= passo_peso
                print(pos_c1y)

gravidade = 10

corpo_1()

