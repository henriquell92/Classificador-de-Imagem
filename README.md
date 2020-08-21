# Classificador-de-Imagem
Rede Neural Convolucional - Classificador de Cão e Gato.

Criação de uma rede neural convolucional para classificação de imagem, procurando obter como resultado a classificação de duas classes: Cão e Gato.

# Desenvolvimento:
* Foi Utilizado no modelo de classificação de imagem Tensorflow e Keras.
* Foi utilizado uma base de treinamento e uma base de teste para preparação das imagens.
* O modelo CNN utiliza uma sequencia de camadas para treinamento.
* O modelo de CNN foi salvo para utilização em uma API.
* Foi realizado apenas uma previsão para o teste do modelo.

# Requisitos:
* As bibliotecas utilizadas no processo são informados no requerimento.

# Criacação da API.
* A Api foi desenvolvida com Flask, sendo VSCode a IDE escolhida.
* É feito uma solicitação [POST] predição usando:

{
"imagem": "imagebase64"
}


# Referências

https://medium.com/@estevestoni/agrupando-conceitos-e-classificando-imagens-com-deep-learning-5b2674f99539

https://medium.com/data-hackers/disponibilizando-o-seu-modelo-de-machine-learning-em-produ%C3%A7%C3%A3o-com-python-flask-e-docker-aa4c43c35b50

# Autor

* Henrique Luiz Lohmann
