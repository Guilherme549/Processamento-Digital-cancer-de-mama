# Análise de mamografia para inferir presença ou ausência de câncer de mama

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem processada em escala de cinza
imagem_mamografia = cv2.imread('imagem_mama_contornada.jpg', cv2.IMREAD_GRAYSCALE)

# Definir um limiar para identificar as regiões de interesse (áreas suspeitas)
_, imagem_binaria = cv2.threshold(imagem_mamografia, 150, 255, cv2.THRESH_BINARY)

# Contar os pixels brancos (potenciais áreas suspeitas) e pretos
pixels_area_suspeita = np.count_nonzero(imagem_binaria == 255)
pixels_fundo = np.count_nonzero(imagem_binaria == 0)

# Calcular a proporção de pixels brancos (regiões suspeitas)
percentual_area_suspeita = (pixels_area_suspeita / (pixels_area_suspeita + pixels_fundo)) * 100

# Definir um limite para a decisão, baseado na análise de áreas brancas
limiar_diagnostico = 25  # Percentual arbitrário que pode ser ajustado para maior precisão

# Inferir se há presença de câncer de mama com base no percentual de áreas suspeitas
if percentual_area_suspeita >= limiar_diagnostico:
    resultado_diagnostico = 'Indícios de câncer de mama detectados.'
else:
    resultado_diagnostico = 'Nenhuma evidência significativa de câncer de mama detectada.'

# Exibir os resultados
print(resultado_diagnostico)
print(f'Porcentagem de áreas suspeitas: {percentual_area_suspeita:.2f}%')

# Exibir a imagem binária (áreas suspeitas destacadas)
plt.imshow(imagem_binaria, cmap='gray')
plt.title('Áreas Suspeitas Destacadas')
plt.axis('off')
plt.show()
