def bojorquezSerrano(fp,numcats=5,maximo=1.0,minimo=0.0):
    

    
    numeroDeCortes = numcats - 1
    laSuma = 0
    
    for i in range(numcats) :
        laSuma += ((fp) ** i)
    
    cachito = (maximo-minimo) / laSuma
    
    cut = []
    cut.append(minimo)
    for i in range(numcats) :
       
        anterior = cut[i]
            
        corte = anterior + fp ** i * cachito
        cut.append(corte)
    
    #cut.append(maximo)

    return cut

print bojorquezSerrano(2.0,maximo=2.0, minimo=1.0,numcats=5)
print bojorquezSerrano(1.0,maximo=2.0, minimo=1.0,numcats=5)

print bojorquezSerrano(2.0,maximo=1.0, minimo=0.0,numcats=5)
print bojorquezSerrano(1.0,maximo=1.0, minimo=0.0,numcats=5)
