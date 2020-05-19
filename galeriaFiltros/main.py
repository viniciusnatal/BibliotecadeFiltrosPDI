# Biblioteca desenvolvida por Vinícius Natal Gonçalves - 19/05/2020
# Analista e Desenvolvedor de sistemas - IFTM Campus Ituiutaba
import cv2
import numpy as np

img = cv2.imread("kurama.pgm", 1 )
kernel = np.ones((3,3))#Proporção escolhida para aplicação de filtros (3x3)

while True:
    print("\n~ Selecione o tipo de filtro à ser aplicado ~"
          "\n...: 1- Mostrar imagem Original :..."
          "\n...: 2- Correção Gamma :..."
          "\n...: 3- Filtro Negativo :..."
          "\n...: 4- Filtro Sobel  :..."
          "\n...: 5- Filtro Lapracian :..."
          "\n...: 6- Filtro Sharpen :..."
          "\n...: 7- Filtro Borrar Imagem :..."
          "\n...: 8- Filtro Glaussiano :..."
          "\n...: 9- Transformação Logarítmica :..."
          "\n...: 10- Filtro Escala Cinza :..."
          "\n...: 11- Filtro Erosão :..."
          "\n...: 12- Filtro Dilatação :..."
          "\n...: 13- Filtro Abertura :..."
          "\n...: 14- Filtro Fechamento :...\n")

    opcao= (int(input("Digite o Filtro Escolhido: ")))
    if(opcao == 1 ):
        cv2.imshow("Imagem Original",img)
        cv2.waitKey()

    elif (opcao == 2):
        gamma = (float(input("Digite a intensidade de Gamma à ser aplicada(Ex> 0.1): ")))
        def _ajustarGamma_(img, gamma):
            invGamma = 1.0/gamma
            table = np.array([((i / 255.0) ** invGamma) * 255
                for i in np.arange(0, 256)]).astype("uint8")
            return cv2.LUT(img, table)
        cv2.imshow("Correção Gamma",_ajustarGamma_(img,gamma))
        cv2.waitKey(0)

    elif (opcao == 3):
        img = cv2.bitwise_not(img)
        cv2.imshow("Filtro Negativo", img)
        cv2.waitKey(0)

    elif (opcao == 4):
        sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobelY = cv2.Sobel( img, cv2.CV_64F, 0, 1, ksize=5 )
        cv2.imshow('Filtro Sobel Horizontal', sobelX)
        cv2.imshow('Filtro Sobel Vertical', sobelY)
        cv2.waitKey()

    elif (opcao == 5):
        lapracian = cv2.Laplacian(img, cv2.CV_64F)
        cv2.imshow("Filtro Lapraciano", lapracian)
        cv2.waitKey()

    elif (opcao == 6):
        kernelSharpen = np.array([[- 1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        nitidez = cv2.filter2D(img, -1, kernelSharpen)
        cv2.imshow("Filtro Sharpen", nitidez)
        cv2.waitKey()

    elif (opcao == 7):
        blurred = cv2.filter2D( img, -1, kernel )
        cv2.imshow( "Filtro Borrar Imagem", blurred )
        cv2.waitKey()
        cv2.destroyAllWindows()

    elif (opcao == 8):
        gaussian = cv2.GaussianBlur( img, (7,7), 2 )
        cv2.imshow( "Filtro Gaussian", gaussian )
        cv2.waitKey()
        cv2.destroyAllWindows()

    elif (opcao == 9):
        img2 = np.uint8(np.log1p(img))
        thresh = 1
        img3 = cv2.threshold(img2, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow("Transformação Logaritmica", img3)
        cv2.waitKey()

    elif (opcao == 10):
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY,1 )
        cv2.imshow("Filtro Cinza", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif (opcao == 11):
        erosion = cv2.erode( img, kernel, iterations=1 )
        cv2.imshow( "Erosao", erosion )
        cv2.waitKey( 0 )
        cv2.destroyAllWindows()

    elif (opcao == 12):
        dilatacao = cv2.dilate(img, (x, y), iterations=1)
        cv2.imshow("Dilatação", dilatacao)
        cv2.waitKey()
        cv2.destroyAllWindows()

    elif (opcao == 13):
        open = cv2.morphologyEx( img, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Filtro Abertura", open)
        cv2.waitKey()
        cv2.destroyAllWindows()

    elif (opcao == 14):
        close = cv2.morphologyEx( img, cv2.MORPH_CLOSE, kernel )
        cv2.imshow("Filtro Fechamento", close)
        cv2.waitKey()
        cv2.destroyAllWindows()
    break
