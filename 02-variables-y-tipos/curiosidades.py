mi_texto = " 'Master' " #Comillas simples dentro de comillas dobles
mi_texto2 = " en \"Python\"" #Comillas dobles dentro de comillas dobles

texto_unido = mi_texto + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\n" + mi_texto2
print(texto_unido)
# \n salto de linea
texto_unido = mi_texto + "\t" + mi_texto2
print(texto_unido)
# \t tabulador
texto_unido = mi_texto + "\r" + mi_texto2
print(texto_unido)
# \r salto de carro
texto_unido = mi_texto + "\b" + mi_texto2
print(texto_unido)
# \b retroceso
texto_unido = mi_texto + "\\" + mi_texto2
print(texto_unido)
# \\ barra invertida
texto_unido = mi_texto + "\'" + mi_texto2
print(texto_unido)
# \' comilla simple


