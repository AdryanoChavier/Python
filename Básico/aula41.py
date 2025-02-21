"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = 'Luiz'.__iter__()
texto2 = iter('Luiz')
print(texto)
print(texto2)