import calendar
ano = 2021
mes = 8
dia = 23

dia_semana = calendar.weekday(ano, mes, dia)

if dia_semana == 0:
    print('Segunda-feira')
elif dia_semana == 1:
    print('Terça-feira')
elif dia_semana == 2:
    print('Quarta-feira')
elif dia_semana == 3:
    print('Quinta-feira')
elif dia_semana == 4:
    print('Sexta-feira')
elif dia_semana == 5:
    print('Sabado')
else:
    print('Domingo')