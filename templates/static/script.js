function fetchNCM() {
    // Pegar o valor inserido pelo usuÃ¡rio
    let descricao = document.getElementById("descricaoInput").value;

    // Definir o endpoint da API
    let apiEndpoint = `https://brasilapi.com.br/api/ncm/v1?search=${descricao}`;

    // Usar a Fetch API para obter os dados da API
    fetch(apiEndpoint)
        .then(response => response.json())
        .then(data => {
            // Limpar resultados anteriores
            let dropdown = document.getElementById("ncmDropdown");
            dropdown.innerHTML = '';

            // Adicionar os novos resultados ao dropdown
            data.forEach(item => {
                let option = document.createElement("option");
                option.value = item.codigo;
                option.textContent = `${item.codigo} - ${item.descricao}`;
                dropdown.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Erro ao buscar dados:", error);
        });
}