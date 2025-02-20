"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação aprorpriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Que horas são? exemplo: XX:XX ')
pegar_hora = entrada[0:2]
hora_int = int(pegar_hora)
if hora_int  >= 00 and hora_int <= 23:
    if hora_int  >= 00 and hora_int  <= 11:
        print(f'Bom dia. São exatamente {entrada}') 
    elif hora_int  >= 12 and hora_int  <= 17:
        print(f'Boa tarde. São exatamente {entrada}')
    else:
        print(f'Boa noite. São exatamente {entrada}')
else:
    print('Você digitou a hora errada!')