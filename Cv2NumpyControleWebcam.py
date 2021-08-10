#necessário instalar numpy e opencv-python

#importar a biblioteca
import cv2 as cv
#chamada para conectar com a webcam (somente cria a conexão com a webcam)
webcam = cv.VideoCapture(0)
#verificar se a conexão deu certo (se a webcam está conectada (funcionando))
#pegar a informação que vem da webcan
#o retorno em formato de lista  (RGB) - forma um frame da tela 
if webcam.isOpened():
    #print('Conectou com a webcam')
    #print(webcam.read())
    validacao, frame = webcam.read()

#Ler a webcam como um video (frame por frame)
    while validacao: #colocar while validação que verifica antes se está conectado, caso não    coloque a validacao vai entrar em loop infinito sem a webcam está conectada.
        validacao, frame = webcam.read()
#mostrar imagem
        cv.imshow('Video da webcam', frame)
#indicar para esperar um momento - 5 milisegundo
#e armazena teclas do teclado dentro da variável key
        key = cv.waitKey(5)
        if key == 27: # ESC
            break
#tirar uma foto (ultimo frame) - fora do while
    cv.imwrite('FotoNada.png', frame)
#fechar a conexão com a webcam
webcam.release()
#fechar a janela da webcam
cv.destroyAllWindows()