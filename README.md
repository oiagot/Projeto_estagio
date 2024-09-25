# Projeto_estagio
Este projeto visa a criação de um sistema de cadastro de clientes, com validações de dados, geração de documentos PDF, e exclusão de clientes com controle documental. O projeto é desenvolvido em Python e MySQL, proporcionando uma aplicação eficiente e organizada para gestão de cadastros.

# Pré-requisitos
Antes de iniciar, você precisará ter os seguintes itens instalados:

Python 3.x
MySQL (Servidor de banco de dados)
MySQL Connector para Python (biblioteca para conectar o Python ao MySQL)
Biblioteca reportlab para geração de PDFs
Configuração do MySQL
Inicie o servidor MySQL e crie um banco de dados:
sql
Copiar código
CREATE DATABASE cadastro_clientes;
Atualize o arquivo de configuração do projeto com suas credenciais do MySQL (ex.: usuário, senha e host).

# Requisitos
1. Cadastro de Clientes
O sistema permite cadastrar clientes com os seguintes campos obrigatórios:

Nome: Nome completo do cliente.
CPF: Deve ser validado para garantir que o CPF é válido e único.
E-mail: Validado utilizando expressões regulares para garantir a conformidade com o formato correto.
Endereço: Informação completa do endereço do cliente.
Telefone: Número de telefone de contato.
# 2. Emissão de Documento PDF
Após o cadastro, um documento em PDF deve ser gerado automaticamente contendo as seguintes informações:
Nome do cliente.
CPF do cliente.
Data de emissão do documento.
O arquivo PDF será salvo localmente no sistema para futuros acessos e consultas.
3. Exclusão de Cliente
O sistema permite a exclusão de um cliente do banco de dados.
Após a exclusão, um novo documento em PDF será gerado com os seguintes dados:
Nome do cliente.
CPF do cliente.
Data da exclusão.
Motivo da exclusão informado.
# Tecnologias Utilizadas
Python: Usado para a lógica do sistema, validações, e interação com o banco de dados.
MySQL: Banco de dados relacional para armazenamento dos dados dos clientes.
PDF Library: Para a geração dos documentos PDF com as informações dos clientes.
GitHub: Controle de versão e repositório do código.
VSCode: Ambiente de desenvolvimento integrado (IDE).
draw.io: Utilizado para criar fluxogramas e diagramas do sistema.
ChatGPT: Auxílio na criação de soluções e elaboração do código.


