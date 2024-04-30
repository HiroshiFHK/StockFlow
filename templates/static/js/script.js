function consultarAPI() {
    var inputValor = document.getElementById('inputDescription').value;

    // Substitua a URL pela sua API
    var apiUrl = 'https://brasilapi.com.br/api/ncm/v1';

    // Faz a requisição à API
    fetch(apiUrl + '?search=' + inputValor, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => popularSelect(data))
    .catch(error => console.error('Erro:', error));
}

function popularSelect(data) {
    var select = document.getElementById('ncmDropdown');
    select.innerHTML = ''; // Limpa opções anteriores

    // Adiciona as opções ao select
    for (var i = 0; i < data.length; i++) {
        var option = document.createElement('option');
        option.value = data[i].codigo;
        option.innerHTML = data[i].descricao.replace(/^--\s/, '').replace(/^-/, '');
        select.appendChild(option);
    }
}
