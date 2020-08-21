import io
import flask
import keras
import base64
import numpy as np
from PIL import Image
from flask import request
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator

app = flask.Flask(__name__)

app.config["DEBUG"] = True 

class Processamento_imagem():
    
    """
    A Função da classe é receber a imagem em base 64 e converter para a os padrões do modelo Convolucional.
    """
    
    def adequacao_imagem(self, image, target_size):
        
        if image.mode != "RGB":
            image = image.convert("RGB")
        image = image.resize(target_size)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        
        return image 

@app.route("/predicao", methods=["POST"])
def predict():
        
    """
    Processo de recebimento da imagem em base64, decodificar a imagem e retornar a predição treinada pelo modelo.
    """

    payload = request.get_json(force=True)
    encoded = payload['imagem']
    decoded = base64.b64decode(encoded)
    imagem = Image.open(io.BytesIO(decoded))
    imagem_processada = Processamento_imagem().adequacao_imagem(imagem, target_size=(64, 64))
    modelo = load_model(r"D:\ProjetoPython\TesteRoit\model.h5")
    resultado = modelo.predict(imagem_processada).tolist()

    if resultado[0][0] == 1:
        prediction = 'Gato'
    else:
        prediction = 'Cachorro'
        
    return prediction

if __name__ == '__main__':
    
    app.run()