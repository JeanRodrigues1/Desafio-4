import mysql.connector

def connect_db():
    db = mysql.connector.connect(
        host ="localhost",
        user="root",
        password="mulinhas",
        database="universidade",
        auth_plugin='mysql_native_password'
    )
    return db

def create_database():
    db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mulinhas",
            auth_plugin='mysql_native_password'
        )

    cursor = db.cursor()
    sql = "CREATE DATABASE universidade; USE universidade"
    cursor.execute(sql)
    db.commit()

def create_table_contact():
    db = connect_db()
    cursor = db.cursor()
    sql = "CREATE TABLE contato (email varchar(20), assunto varchar(255), descricao varchar(255))"
    cursor.execute(sql)
    db.commit()

def inserir_dados(email, assunto, descricao):
    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO contato (email, assunto, descricao) VALUES (%s, %s, %s);"
    values = [email, assunto, descricao]
    cursor.execute(sql, values)
    db.commit()