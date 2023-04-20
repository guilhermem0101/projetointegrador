import mysql.connector
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Cria uma conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="unictec"
)

# Cria um cursor para executar comandos SQL
cursor = mydb.cursor()

# Cria um objeto Faker para gerar dados fictícios

fake = Faker(['pt_BR'])

# Inserção na tabela curso
for i in range( 15):
    cod_curso = str(i)
    nome_curso = fake.job()
    qntd_semestres = fake.random_int(min=1, max=10)
    bach_tecn_prof = fake.random_element(elements=('Bacharelado', 'Tecnológico', 'Profissionalizante'))
    insert_query = ("INSERT INTO curso "
                    "(cod_curso, nome_curso, qntd_semestres, bach_tecn_prof) "
                    "VALUES (%s, %s, %s, %s)")
    data = (cod_curso, nome_curso, qntd_semestres, bach_tecn_prof)
    cursor.execute(insert_query, data)

# Inserção na tabela endereco
for i in range(100):
    cep = fake.postcode()
    n_residencia = fake.building_number()
    logradouro = fake.street_name()
    insert_query = ("INSERT INTO endereco "
                    "(cep, n_residencia, logradouro) "
                    "VALUES (%s, %s, %s)")
    data = (cep, n_residencia, logradouro)
    cursor.execute(insert_query, data)

# Inserção na tabela aluno
# for i in range(100):
#     ra = fake.random_int(min=1000000, max=9999999)
#     cod_curso = fake.random_int(min=1, max=5)
#     cpf = fake.cpf()
#     situacao = fake.random_element(elements=('Ativo', 'Inativo', 'Trancado'))
#     nome_aluno = fake.name()
#     email = fake.email()
#     data_matricula = fake.date_between(start_date='-4y', end_date='today')
#     cep = fake.postcode()
#     insert_query = ("INSERT INTO aluno "
#                     "(ra, cod_curso, cpf, situacao, nome_aluno, email, data_matricula, cep) "
#                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
#     data = (ra, cod_curso, cpf, situacao, nome_aluno, email, data_matricula, cep)
#     cursor.execute(insert_query, data)

# Inserção na tabela disciplina



mydb.commit()
mydb.close()
