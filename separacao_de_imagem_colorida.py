# Separação de cores em uma imagem (Canais RGB)

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem do cachorro
imagem_original = cv2.imread('Leao_imagem.jpg')

# Dividindo a imagem em seus componentes de cor (canais RGB)
canal_b, canal_g, canal_r = cv2.split(imagem_original)

# Gerando imagens apenas com o canal correspondente em destaque
fundo_preto = np.zeros_like(canal_b)  # Fundo preto para combinar com os outros canais
imagem_canal_azul = cv2.merge([canal_b, fundo_preto, fundo_preto])
imagem_canal_verde = cv2.merge([fundo_preto, canal_g, fundo_preto])
imagem_canal_vermelho = cv2.merge([fundo_preto, fundo_preto, canal_r])

# Exibição dos canais separados
figura, eixos = plt.subplots(1, 3, figsize=(18, 6))
eixos[0].imshow(cv2.cvtColor(imagem_canal_vermelho, cv2.COLOR_BGR2RGB))
eixos[0].set_title('Vermelho')
eixos[1].imshow(cv2.cvtColor(imagem_canal_verde, cv2.COLOR_BGR2RGB))
eixos[1].set_title('Verde')
eixos[2].imshow(cv2.cvtColor(imagem_canal_azul, cv2.COLOR_BGR2RGB))
eixos[2].set_title('Azul')

# Remover os eixos
for eixo in eixos:
    eixo.axis('off')

plt.tight_layout()
plt.show()

# Salvando as imagens dos canais em arquivos separados
cv2.imwrite('imagem_canal_vermelho.jpg', imagem_canal_vermelho)
cv2.imwrite('imagem_canal_verde.jpg', imagem_canal_verde)
cv2.imwrite('imagem_canal_azul.jpg', imagem_canal_azul)
