// Função para adicionar um novo filme
function adicionarNovoFilme() {
    // Redireciona o usuário para a página de adicionar filme
    window.location.href = "adicionar_filme.html";
}

// Função para carregar os cards de filmes
function carregarFilmes() {
    // Oculta o botão
    document.querySelector('#btnCarregarFilmes').style.display = 'none';

    // URL da sua API
    const apiUrl = 'http://localhost:8000/api/v1/movies';

    // Faz a requisição GET usando fetch
    fetch(apiUrl)
    .then(response => {
        // Verifica se a resposta da requisição foi bem-sucedida
        if (!response.ok) {
            throw new Error('Erro ao carregar os dados. Status: ' + response.status);
        }
        // Converte a resposta para JSON
        return response.json();
    })
    .then(data => {
        // Aqui você pode manipular os dados recebidos e criar os cards de filmes
        // Por exemplo, você pode iterar sobre os dados e criar um card para cada filme
        data.forEach(movie => {
            // Crie um elemento HTML para o card do filme e adicione ao seu DOM
            const card = document.createElement('div');
            card.classList.add('card');
            card.innerHTML = `
                <h2>${movie.name}</h2>
                <p>Data de Lançamento: ${movie.release_date}</p>
                <p>Classificação Indicativa: ${movie.rating}</p>
                <p>Descrição: ${movie.description}</p> 
            `;

            card.addEventListener('click', function() {
                // Redireciona para a página_filme.html com o ID do filme na URL
                window.location.href = `pagina_filme.html?id=${movie.id}`;
            });


            // Adicione o card ao seu DOM
            document.querySelector('#containerCards').appendChild(card);
        });

        // Adiciona o botão de adição de novo filme
        const addMovieButton = document.createElement('button');
        addMovieButton.textContent = "Adicionar Novo Filme";
        addMovieButton.classList.add('card', 'botao'); // Adiciona as classes do card e do botão
        addMovieButton.addEventListener('click', adicionarNovoFilme);
        document.querySelector('#containerCards').appendChild(addMovieButton); // Adiciona o botão ao container de cards
    })
    .catch(error => {
        // Caso ocorra algum erro na requisição
        console.error('Erro:', error);
    });
}

// Seleciona o botão
const botao = document.querySelector('#btnCarregarFilmes');

// Adiciona um event listener para o evento de clique no botão
botao.addEventListener('click', carregarFilmes);
