#elif usando várias condições
#variavel
volume = 190
if volume == 0:
    print ('Deligado!')
elif volume < 10:
    print ('Está muito baixo')
elif 20 <= volume < 40:
    print ('Está bom para música ambiente')
elif 40 <= volume < 60:
    print ('Perfeito, posso ouvir todos os detalhes')
elif 60 <= volume < 80:
    print('Está ótimo para festas')
elif 80 <= volume < 100:
    print ('Está muito alto!')
elif 100 <= volume < 120:
    print ('Desligue! Quem avisa amigo é')
elif 120 <= volume < 150:
    print ('Seus timpanos podem estourar!')
elif 150 <= volume < 200:
    print ('Vida louca!')
else:
    print('Policia chegando! Boa sorte')

