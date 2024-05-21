# Instalação e Configuração do Projeto StockFlow
Este README fornece instruções passo a passo para a instalação e configuração de um projeto Django de controle de estoque chamado StockFlow. 
Certifique-se de seguir todas as etapas para configurar corretamente o ambiente de desenvolvimento.

## Pré-requisitos
Certifique-se de que você possui o seguinte software instalado em sua máquina:

```
Python (versão 3.6 ou superior)
pip (gerenciador de pacotes do Python)
```

## Configuração do Ambiente Virtual
1. Crie um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos no terminal:

```
python -m venv .venv
```
## Linux / Mac
```
source .venv/bin/activate
```
## Windows
```
.\.venv\Scripts\activate
```

Isso criará um ambiente virtual na pasta .venv e ativará-o.

2. Atualize o pip para a versão mais recente:

```
python -m pip install --upgrade pip
```

## Instalação das Dependências
Instale o Django e as dependências do projeto usando o pip (demora alguns minutos):

```
pip install django django-browser-reload django-tailwind python-decouple pandas matplot plotly
```

## Configuração do Tailwind CSS
Instale o Tailwind CSS e configure-o no projeto:

```
python manage.py tailwind install
python manage.py tailwind start
```

## Migração do Banco de Dados
Execute as migrações do banco de dados para criar as tabelas necessárias:

```
python manage.py migrate
```

## Inicialização do Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento Django:

```
python manage.py runserver
```

Lembre-se de ainda ter outro terminal com o "python manage.py tailwind start" rodando.

O servidor estará disponível em http://127.0.0.1:8000/. 
Você pode acessar esta URL em seu navegador para ver a aplicação em execução.

---------------------------------------------------------------------------
## Comando caso dê erro no PowerShell do Windows

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
