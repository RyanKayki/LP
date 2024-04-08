from flask import Flask, jsonify
from flask_cors import CORS

lista_charadas = [
  {"pergunta": "<p>características do Pré-Modernismo:</p><br><ul><li>a) Riqueza em detalhes e pelo exagero.</li><li>b) Linguagem coloquial.</li><li>c) Exaltação da natureza.</li><li>d) Mudança de perspectiva temporal.</li><li>e) Nacionalismo e Indianismo.</li></ul>", "resposta":"b) Linguagem coloquial", "explicacao":"No Pré-Modernismo, a linguagem utilizada é simples e coloquial, bem como os trabalhos literários caracterizam-se pela presença de personagens como sertanejos, caipiras e mulatos, entre outros."},
  {"pergunta": "<p>Indique a alternativa que contenha apenas autores pré-modernistas:</p><br><ul><li>a) Euclides da Cunha, Graça Aranha, Monteiro Lobato.</li><li>b) Arianos Suassuna, Graciliano Ramos, Monteiro Lobato.</li><li>c) Lima Barreto, José de Anchieta, Euclides da Cunha.</li><li>d) José de Anchieta, Santa Rita Durão, Tomás Antônio Gonzaga.</li><li>e) Manuel Bandeira, Graciliano Ramos, Clarice Lispector.</li></ul>", "resposta":"a) Euclides da Cunha, Graça Aranha, Monteiro Lobato.", "explicacao":"Quanto aos outros autores: Ariano Suassuna é pós-modernista, Graciliano Ramos, Manuel Bandeira e Clarice Lispector são modernistas, Lima Barreto é Pré-modernista, José de Anchieta é quinhentista, Santa Rita Durão e Tomás Antônio Gonzaga são arcadistas."},
  {"pergunta": "<p>\"Malazarte\", \"A Estética da Vida\" e \"Correspondência de Machado de Assis e Joaquim Nabuco\" foram escritas por qual escritor pré-modernista?</p><br><ul><li>a) Machado de Assis</li><li>b) Graça Aranha</li><li>c) Paulo Leminski</li><li>d) Euclides da Cunha</li><li>e) Lima Barreto</li></ul>", "resposta": "b) Graça Aranha", "explicacao": "Graça Aranha, cuja obra mais emblemática é Canaã (1902), também é autor de Malazarte (1914), A Estética da Vida (1921) e Correspondência de Machado de Assis e Joaquim Nabuco (1923)."},
  {"pergunta": "<p>Quais desses acontecimentos marcam o contexto histórico do Pré-Modernismo?</p><br><ul><li>a) Chegada da família real portuguesa.</li><li>b) Transferência da capital do Brasil para Salvador.</li><li>c) Inconfidência mineira.</li><li>d) Revolta da Chibata.</li><li>e) Era Vargas.</li></ul>", "resposta":"d) Revolta da Chibata.", "explicacao":"No Pré-Modernismo (1910-1922), o Brasil vivia um momento de agitação política. Dentre as revoltas que ocorreram nesse período, podemos citar a Revolta da Chibata, a qual foi organizada pela Marinha brasileira e teve início no dia 22 de novembro de 1910"},
  {"pergunta": "<p>(UFR) Crítico feroz do Modernismo, grande incentivador da disseminação da cultura, defensor dos valores e riquezas nacionais; conhecido, particularmente, pela sua grande obra infantil, em que se destacam os personagens do Sítio do Picapau Amarelo.</p><br><ul><li>a) Lima Barreto</li><li>b) José Lins do Rego</li><li>c) Monteiro Lobato</li><li>d) Mário de Andrade</li><li>e) Cassiano Ricardo</li></ul>", "resposta":"c) Monteiro Lobato.", "explicacao":"Monteiro Lobato é um dos maiores autores infantis. É por isso que, em sua homenagem, o dia do seu nascimento é o Dia Nacional do Livro Infantil."},
  {"pergunta": "<p>(PUC-RS) Na figura de ________, Monteiro Lobato criou o símbolo do brasileiro abandonado ao seu atraso e miséria pelos poderes públicos.</p><br><ul><li>a) O Cabeleira</li><li>b) Jeca Tatu</li><li>c) João Miramar</li><li>d) Blau Nunes</li><li>e) Augusto Matraga</li></ul>", "resposta":"b) Jeca Tatu", "explicacao":"O personagem do livro Urupês, de Monteiro Lobato, é uma crítica ao Brasil. Jeca Tatu é um caipira que vive desanimado."}
]

app = Flask(__name__)
CORS(app)

current_index = 0

@app.route('/')
def index():
    return 'API CHARADA ESTÁ ONLINE!'

@app.route('/charadas', methods=['GET'])
def charadas():
    global current_index
    charada = lista_charadas[current_index]
    current_index = (current_index + 1) % len(lista_charadas)  # Avança para a próxima charada, retornando ao início quando atinge o final da lista
    return jsonify(charada)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
