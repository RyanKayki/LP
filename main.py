from flask import Flask, jsonify
from flask_cors import CORS
import random

lista_charadas = [
  {"pergunta": "O que é, o que é? Tem um buraco no fundo e ninguém pode ver.", "resposta":"O espaço"},
  {"pergunta": "O que sempre desce mas nunca sobe?", "resposta":"A chuva"},
  {"pergunta": "O que é, o que é? É feito de água, mas se for colocado dentro da água morrerá.", "resposta": "O gelo"},
  {"pergunta": "O que é, o que é? Quanto mais se tira, maior ele fica?", "resposta":"Um buraco"},
  {"pergunta": "O que é, o que é? Pode ser atirado do alto de um prédio e ficar super bem. Mas quando é colocado na água morre pouco tempo depois.", "resposta":"O papel"},
  {"pergunta": "O que é, o que é? Você tira a minha pele. Eu não choro. Você, sim.", "resposta":"A cebola"},
  {"pergunta": "O que é, o que é? Ocorre uma vez a cada minuto, duas vezes a cada momento, mas jamais a cada quinhentos anos.","resposta":"A letra 'm'"},
  {"pergunta": "O que é, o que é? Quanto mais seca, mais molhada ela fica?", "resposta":"A toalha"},
  {"pergunta": "O que é, o que é? É mais útil quando é quebrado.", "resposta":"O ovo"},
  {"pergunta": "O que é, o que é? Tem dente mas não morde?", "resposta":"O pente"},
  {"pergunta": "O que é, o que é? Elas não têm carne, penas, escamas ou ossos. Mas têm dedos próprios.", "resposta":"As luvas"},
  {"pergunta": "O que é, o que é? Não tem pés, mãos ou asas, mas pode subir aos céus.", "resposta":"A fumaça"}
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