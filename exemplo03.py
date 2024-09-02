def e_par(numero):
    if numero % 2 ==0:
        return True
    else:
        return False
    
numero  = 20
if e_par (numero):
        print(f"{numero} é um numero par.")
else:
        print(f"{numero} não é um numero par")

#essa função valida se o numero e par ou não se o resultado somado por 2 
#for igual a 0