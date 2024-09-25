import mysql.connector
from validate_docbr import CPF
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Função para conectar ao banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_clientes"
    )

# Função para validar CPF
def validar_cpf(cpf):
    cpf_obj = CPF()
    return cpf_obj.validate(cpf)

# Função para validar e-mail
def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao, email)

# Função para gerar PDF
def gerar_pdf(nome, cpf, tipo='cadastro'):
    pdf_filename = f"{tipo}_{cpf}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(100, 750, f"Nome: {nome}")
    c.drawString(100, 730, f"CPF: {cpf}")
    c.drawString(100, 710, f"Data de Emissão: {datetime.now().strftime('%d/%m/%Y')}")
    if tipo == 'exclusao':
        c.drawString(100, 690, "Motivo: Exclusão do cadastro")
    c.save()
    print(f"PDF gerado: {pdf_filename}")

# Função para cadastrar cliente
def cadastrar_cliente(nome, cpf, email, endereco, telefone):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    if validar_cpf(cpf) and validar_email(email):
        try:
            sql = "INSERT INTO cadastro (nome, cpf, email, endereco, telefone) VALUES (%s, %s, %s, %s, %s)"
            valores = (nome, cpf, email, endereco, telefone)
            cursor.execute(sql, valores)
            conexao.commit()
            print(f"Cliente {nome} cadastrado com sucesso!")
            gerar_pdf(nome, cpf, tipo='cadastro')  # Gerar PDF após cadastro
        except mysql.connector.IntegrityError:
            print("Erro: CPF já cadastrado.")
    else:
        print("Erro: CPF ou e-mail inválido.")

    cursor.close()
    conexao.close()

# Função para listar todos os clientes
def listar_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM cadastro")
    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    cursor.close()
    conexao.close()

# Função para excluir cliente pelo CPF
def excluir_cliente(cpf):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM cadastro WHERE cpf = %s", (cpf,))
    cliente = cursor.fetchone()

    if cliente:
        cursor.execute("DELETE FROM cadastro WHERE cpf = %s", (cpf,))
        conexao.commit()
        print(f"Cliente {cliente[0]} excluído com sucesso!")
        gerar_pdf(cliente[0], cpf, tipo='exclusao')  # Gerar PDF após exclusão
    else:
        print("Cliente não encontrado.")

    cursor.close()
    conexao.close()

# Testes das funções

# Cadastrar cliente
# cadastrar_cliente("Iago Natan", "12345678909", "iago@email.com", "Rua X, São Paulo", "99999-9999")

# Listar clientes
# listar_clientes()

# Excluir cliente
# excluir_cliente("12345678909")
