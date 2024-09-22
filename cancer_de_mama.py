# Processamento de imagem de câncer de mama com detecção de contornos

from PIL import Image, ImageDraw, ImageEnhance
from skimage import measure
import numpy as np
import matplotlib.pyplot as plt

# Abrir a imagem de mamografia
imagem_mamografia = Image.open('mama.jpg')

# Transformar a imagem para escala de cinza
imagem_em_cinza = imagem_mamografia.convert('L')

# Converter a imagem em um array numpy para processamento
imagem_array = np.array(imagem_em_cinza)

# Usar a função find_contours para detectar contornos na imagem
contornos_detectados = measure.find_contours(imagem_array, level=0.8)

# Desenhar os contornos encontrados sobre a imagem original
desenho = ImageDraw.Draw(imagem_mamografia)
for contorno in contornos_detectados:
    pontos = list(zip(contorno[:-1], contorno[1:]))  # Criar pares de pontos
    for ponto_atual, proximo_ponto in pontos:
        desenho.line(
            [ponto_atual[1], ponto_atual[0], proximo_ponto[1], proximo_ponto[0]],
            fill='blue',  # Alterado para azul
            width=2,
        )

# Aumentar o contraste da imagem processada
ajuste_contraste = ImageEnhance.Contrast(imagem_mamografia)
imagem_com_contraste = ajuste_contraste.enhance(16.0)  # Nível de contraste ajustado

# Salvar a imagem processada com contornos
imagem_com_contraste.save('imagem_mama_contornada.jpg')

# Exibir a imagem final com contornos e contraste elevado
plt.imshow(imagem_com_contraste, cmap='gray')
plt.title('Mamografia com Contornos Detectados e Contraste Ajustado')
plt.axis('off')
plt.show()
