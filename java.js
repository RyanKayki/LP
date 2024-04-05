async function gerarCharada() {
    const apiUrl = 'link-api';
    const btnquestao = document.getElementById('btn-questao');

    btnquestao.innerHTML = 'Outra Questão';

    loading()

    try {
        const consulta = await fetch(apiUrl)

        if (!consulta.ok) {
            console.log("A API não está funcionando")
            return
        }

        const dados = await consulta.json()
        console.log(dados)

        setTimeout(() => { 
            pergunta(dados)
        }, 1000)
        

    } catch (error) {
        console.error('Erro ao obter dados da API:', error)
    }
}

async function mostrarresposta() {
    const apiUrl = 'link-api';
    const btnresposta = document.getElementById('btn-resposta');

    loading(); // Mostra o loading antes de mostrar a resposta

    try {
        const consulta = await fetch(apiUrl);

        if (!consulta.ok) {
            console.log("A API não está funcionando");
            return;
        }

        const dados = await consulta.json();
        console.log(dados);

        resposta(dados);

    } catch (error) {
        console.error('Erro ao obter dados da API:', error);
    }
}

async function pergunta(dados) {
    const resp = document.getElementById('resp');

    resp.innerHTML = '';

    if (dados && dados.length > 0) {
        const charada = dados[0];
        const charadasCard = `
            <h3 class="card-title" style="font-size:50px; padding:10px;">${ charada.pergunta }</h3>
            <h3 class="card-title" style="font-size:50px; padding:10px; display: none;" id="respostaCharada">${charada.resposta}</h3>
            <button id="mostrarConteudo" class="btn" style="background-color: #2b4a4ebb; color: #fff; padding: 5px;">Mostrar Resposta</button>
        `
        resp.innerHTML += charadasCard;

        document.getElementById('mostrarConteudo').addEventListener('click', function() {
            var respostaCharada = document.getElementById('respostaCharada')
            if (respostaCharada.style.display === 'none') {
                respostaCharada.style.display = 'block'
            } else {
                respostaCharada.style.display = 'none'
            }
        })
    } else {
        console.error('Os dados da API estão vazios ou em formato incorreto.');
    }
}


function loading() {
    const resp = document.getElementById('resp')

    resp.innerHTML = `
        <div class="col-12">
            <p>Carregando...</p>
        </div>
    `
}
