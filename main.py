from flask import Flask, jsonify
from flask_cors import CORS
import random

lista_charadas = [
  {"pergunta": "Quem é considerado o precursor do Pré-Modernismo na literatura brasileira?", "resposta":"Euclides da Cunha"},
  {"pergunta": "Qual obra de Euclides da Cunha é considerada um marco do Pré-Modernismo?", "resposta":"Os Sertões"},
  {"pergunta": "Quais são os temas principais abordados no Pré-Modernismo?", "resposta": "Conflitos sociais, realismo e crítica à modernização."},
  {"pergunta": "Quem foi o autor do livro 'Os Sertões'?", "resposta":"Euclides da Cunha"},
  {"pergunta": "Qual foi o conflito retratado em 'Os Sertões'?", "resposta":"A Guerra de Canudos"},
  {"pergunta": "Qual é o principal evento histórico retratado em 'Os Sertões'?", "resposta":"A Guerra de Canudos"},
  {"pergunta": "Além de 'Os Sertões', qual outra obra importante de Euclides da Cunha é relacionada ao Pré-Modernismo?", "resposta":"À Margem da História"},
  {"pergunta": "Quais são os elementos estilísticos marcantes do Pré-Modernismo?", "resposta":"Uso de linguagem coloquial, narrativa fragmentada e crítica social."},
  {"pergunta": "Que autor produziu obras de teatro influentes durante o Pré-Modernismo?", "resposta":"Martins Pena"},
  {"pergunta": "Qual foi o contexto histórico que influenciou o surgimento do Pré-Modernismo no Brasil?", "resposta":"A crise do regime imperial, a abolição da escravatura e a transição para a República."}
]
  


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'API CHARADA ESTÁ ONLINE!'

@app.route('/charadas', methods=['GET'])
def charadas():
  charada = random.choice(lista_charadas)
  return jsonify(charada)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)