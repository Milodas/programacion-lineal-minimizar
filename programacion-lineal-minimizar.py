#funcion programacion lineal entera--------------------------------------------------------------------             
def programacion_lineal_minimizar_dos_incognitas(primer_elemento_columna_uno, segundo_elemento_columna_uno, total_columna_uno, primer_elemento_columna_dos, segundo_elemento_columna_dos, total_columna_dos, total_primer_elemento, total_segundo_elemento):
    # F(x;y) = total_primer_elemento * p + total_segundo_elemento * s

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
    xx = primer_elemento_columna_uno - primer_elemento_columna_dos
    yy = segundo_elemento_columna_uno - segundo_elemento_columna_dos
    res = total_columna_uno - total_columna_dos

    xx = res / (xx + yy) 
    yy = (total_columna_uno - (primer_elemento_columna_uno * xx)) / segundo_elemento_columna_uno

    #primer extremo 
    #A = (0:y_limite)
    #B = (x;y)
    #C = (x_limite:0)
    # F(x;y) = total_primer_elemento * x + total_segundo_elemento * y

    a = total_segundo_elemento * y_limite
    b = (total_primer_elemento * xx) + (total_segundo_elemento * yy)
    c = total_primer_elemento * x_limite

    print ("primera opcion: 0 de primer elemento y", y_limite, " del segundo elemento, da como resultado ", a)
    print ("segunda opcion: ", xx, " del primer elemento y ", yy, " del segundo elemento, da como resultado ",  b)
    print ("tercera opcion: ", x_limite, " del primer elemento y 0 del segundo elemento, da como resultado ", c)



programacion_lineal_minimizar_dos_incognitas(120, 100, 1000, 2, 5, 30, 60, 80)