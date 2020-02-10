#funcion programacion lineal entera--------------------------------------------------------------------             
def programacion_lineal_minimizar_dos_incognitas(primer_elemento_columna_uno, segundo_elemento_columna_uno, total_columna_uno, primer_elemento_columna_dos, segundo_elemento_columna_dos, total_columna_dos, total_primer_elemento, total_segundo_elemento):
    
    # programacion_lineal_minimizar_dos_incognitas(120, 100, 1000, 2, 5, 30, 60, 80)

    # F(x;y) = total_primer_elemento * x + total_segundo_elemento * y

    # RESTRICCIONES
    # primer_elemento_columna_uno * x + segundo_elemento_columna_uno * y >= total_columna_uno
    # primer_elemento_columna_dos * x + segundo_elemento_columna_dos * y >= total_columna_dos
    # x >= 0  |  no 
    # y >= 0  |     negatividad

    #minimizar

    y_primera_funcion = total_columna_uno / segundo_elemento_columna_uno
    x_primera_funcion = total_columna_uno / primer_elemento_columna_uno
  
    y_segunda_funcion = total_columna_dos / segundo_elemento_columna_dos
    x_segunda_funcion = total_columna_dos / primer_elemento_columna_dos

    if y_primera_funcion >= y_segunda_funcion:
        y_limite = y_primera_funcion
    else:
        y_limite = y_segunda_funcion
        
    if x_primera_funcion >= x_segunda_funcion:
        x_limite = x_primera_funcion
    else:
        x_limite = x_segunda_funcion
       
    # primer_elemento_columna_uno * x + segundo_elemento_columna_uno * y >= total_columna_uno   
    # primer_elemento_columna_dos * x + segundo_elemento_columna_dos * y >= total_columna_dos
   
    if primer_elemento_columna_uno < primer_elemento_columna_dos:
       primer_elemento_columna_uno = primer_elemento_columna_uno + primer_elemento_columna_dos
       primer_elemento_columna_dos = primer_elemento_columna_uno - primer_elemento_columna_dos
       primer_elemento_columna_uno = primer_elemento_columna_uno - primer_elemento_columna_dos

       total_primer_elemento = total_primer_elemento + total_segundo_elemento
       total_segundo_elemento = total_primer_elemento - total_segundo_elemento
       total_primer_elemento = total_primer_elemento - total_segundo_elemento
      
    if segundo_elemento_columna_uno < segundo_elemento_columna_dos:
        segundo_elemento_columna_uno = segundo_elemento_columna_uno + segundo_elemento_columna_dos
        segundo_elemento_columna_dos = segundo_elemento_columna_uno - segundo_elemento_columna_dos
        segundo_elemento_columna_uno = segundo_elemento_columna_uno - segundo_elemento_columna_dos

    if total_columna_uno < total_columna_dos:
        total_columna_uno = total_columna_uno + total_columna_dos
        total_columna_dos = total_columna_uno - total_columna_dos
        total_columna_uno = total_columna_uno - total_columna_dos

    # print(primer_elemento_columna_uno , "-----", primer_elemento_columna_dos)
    # print(".....")

    # print("y_primera_funcion=", y_primera_funcion)
    # print("x_primera_funcion=", x_primera_funcion)
    # print("-")
    # print("y_segunda_funcion= ",y_segunda_funcion)
    # print("x_segunda_funcion= ",x_segunda_funcion)
    # print("-")
    # print("y_limite=", y_limite)
    # print("x_limite= ", x_limite)
    # print("-")

    # primer_elemento_columna_uno * x + segundo_elemento_columna_uno * y >= total_columna_uno
    # primer_elemento_columna_dos * x + segundo_elemento_columna_dos * y >= total_columna_dos

    xx = primer_elemento_columna_uno - primer_elemento_columna_dos
    yy = segundo_elemento_columna_uno - segundo_elemento_columna_dos
    res = total_columna_uno - total_columna_dos

    # #x 5 y 4

    # if xx < 0 or yy < 0 or res < 0:
    #     xx = xx * -1
    #     yy = yy * -1
    #     res = res * -1

    # print(xx," = ",primer_elemento_columna_uno , "-", primer_elemento_columna_dos)
    # print(yy," = ",segundo_elemento_columna_uno , "-", segundo_elemento_columna_dos)
    # print(res," = ",total_columna_uno , "-", total_columna_dos)
    
    xx = res / (xx + yy) 

    #print("..",xx,"x=",yy,"y = ",res)
       
    yy = (total_columna_uno - (primer_elemento_columna_uno * xx)) / segundo_elemento_columna_uno

    # print("x es: ",xx)
    # print("y es: ", yy)

    # print("---",xx)
    # print("---",yy)
    # print("---------",total_columna_uno, "-", "(",primer_elemento_columna_uno,"*",xx,")) /", segundo_elemento_columna_uno)

    # print("Vertice A =0:",y_limite)
    # print("Vertice B=",xx,":",yy)
    # print("Vertice C=",x_limite,":0")
    # print("--")
  
    #primer extremo 
    #A = (0:y_limite)
    #B = (x;y)
    #C = (x_limite:0)
    # F(x;y) = total_primer_elemento * x + total_segundo_elemento * y

    a = total_segundo_elemento * y_limite
    b = (total_primer_elemento * xx) + (total_segundo_elemento * yy)
    c = total_primer_elemento * x_limite

    # print(a, " =", total_segundo_elemento, " * ", y_limite)
    # print(b, " = (", total_primer_elemento, " * ", xx, ") + (", total_segundo_elemento, " * ", yy ," )")
    # print(c, " = ", total_primer_elemento, " * ", x_limite)
    # print("---------")

    print ("primera opcion:  0 de primer elemento y", y_limite, " del segundo elemento, da como resultado ", a)
    print ("segunda opcion: ",xx, " del primer elemento y ", yy, " del segundo elemento, da como resultado ",  b)
    print ("tercera opcion: ",x_limite, " del primer elemento y 0 del segundo elemento, da como resultado ", c)



programacion_lineal_minimizar_dos_incognitas(6, 5, 50, 2, 5, 30, 60, 80)
print("--------------------------------------------------------------------------")
programacion_lineal_minimizar_dos_incognitas(2, 5, 30, 6, 5, 50, 80, 60)






   