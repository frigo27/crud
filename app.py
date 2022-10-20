import mysql.connector

conexao = mysql.connector.connect(
    host='localhost'
    user='root',
    password='123456',
    database='bdyoutube'
)
cursor = conexao.cursor()

#crud

# resultado = cursor.fetchall() # ler o banco de dados

# resultado 


cursor.close()
conexao.close()

#create

nome_produto= "todynho"
valor = 3
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

cursor.execute(comando)
conexao.commit() # edita o bancos de dados

#read
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

# update

nome_produto= "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'

cursor.execute(comando)
conexao.commit() # edita o bancos de dados

# delete

nome_produto= "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'

cursor.execute(comando)
conexao.commit() # edita o bancos de dados
