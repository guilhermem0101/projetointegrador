import pymysql
import tkinter as tk

# Função para inserção de dados na tabela curso
def insert_curso(cod_curso, nome_curso, qntd_semestres, bach_tecn_prof):
    try:
        connection = pymysql.connect(
                                    host="localhost",
                                    user="root",
                                    password="root",
                                    database="unictec")
        cursor = connection.cursor()

        sql = "INSERT INTO curso (cod_curso, nome_curso, qntd_semestres, bach_tecn_prof) VALUES (%s, %s, %s, %s)"
        values = (cod_curso, nome_curso, qntd_semestres, bach_tecn_prof)
        cursor.execute(sql, values)

        connection.commit()
        print("Dados inseridos na tabela curso com sucesso!")
    except Exception as e:
        print("Erro ao inserir dados na tabela curso:", e)
    finally:
        connection.close()

# Função para inserção de dados na tabela endereco
def insert_endereco(cep, n_residencia, logradouro):
    try:
        connection = pymysql.connect(host="localhost",
                                    user="root",
                                    password="root",
                                    database="unictec")
        cursor = connection.cursor()

        sql = "INSERT INTO endereco (cep, n_residencia, logradouro) VALUES (%s, %s, %s)"
        values = (cep, n_residencia, logradouro)
        cursor.execute(sql, values)

        connection.commit()
        print("Dados inseridos na tabela endereco com sucesso!")
    except Exception as e:
        print("Erro ao inserir dados na tabela endereco:", e)
    finally:
        connection.close()

# Função para inserção de dados na tabela aluno
def insert_aluno(ra, cod_curso, cpf, situacao, nome_aluno, email, data_matricula, cep):
    try:
        connection = pymysql.connect(host="localhost",
                                    user="root",
                                    password="root",
                                    database="unictec")
        cursor = connection.cursor()

        sql = "INSERT INTO aluno (ra, cod_curso, cpf, situacao, nome_aluno, email, data_matricula, cep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (ra, cod_curso, cpf, situacao, nome_aluno, email, data_matricula, cep)
        cursor.execute(sql, values)

        connection.commit()
        print("Dados inseridos na tabela aluno com sucesso!")
    except Exception as e:
        print("Erro ao inserir dados na tabela aluno:", e)
    finally:
        connection.close()

# Função para inserção de dados na tabela disciplina
def insert_disciplina(cod_disciplina, cod_curso, nome_disciplina, carga_horaria):
    try:
        connection = pymysql.connect(host='localhost',
                                     user='username',
                                     password='password',
                                     db='unictec')
        cursor = connection.cursor()

        sql = "INSERT INTO disciplina (cod_disciplina, cod_curso, nome_disciplina, carga_horaria) VALUES (%s, %s, %s, %s)"
        values = (cod_disciplina, cod_curso, nome_disciplina, carga_horaria)
        cursor.execute(sql, values)

        connection.commit()
        print("Dados inseridos na tabela disciplina com sucesso!")

    except Exception as e:
        print("Erro ao inserir dados na tabela disciplina:", e)
    finally:
        connection.close()