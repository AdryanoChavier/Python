a = 'A'
b = 'B'
c = 1.1
string = 'a = {} b = {} c = {:.2f}'
formato = string.format(a, b, c)
print(formato)

string2 = 'a = {1} b = {0} c = {2:.2f}'
formato2 = string2.format(a, b, c)
print(formato2)

string2 = 'a = {parametro1} b = {parametro2} c = {parametro3:.2f}'
formato2 = string2.format(parametro1 = a, parametro2 = b, parametro3 = c)
print(formato2)
