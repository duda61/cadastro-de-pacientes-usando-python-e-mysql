conn = sqlite3.connect('meublogger.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    );
''')

def addUser():
    nome = input('Digite seu nome:\n')
    email = input('Digite seu email:\n')
    senha = input('Digite sua senha:\n')

    query = '''
    INSERT INTO usuarios (nome, email, senha)
    VALUES (?, ?, ?)
'''
    cursor.execute(query, (nome, email, senha))





while True:
    menu = input('1 - Adicionar usuário \n2 - Ver todos os usuários \n3 - Sair \n')
    if menu == '1':
        addUser()
    elif menu == '2':
        query = 'SELECT nome, email FROM usuarios'
        data = cursor.execute(query).fetchall()
        if len(data) == 0:
            print('Nenhum usuário cadastrado')
        else:
            for row in data:
                print(f'{row[0]} - {row[1]}')
    elif menu == '3':
        print('Até logo!')
        conn.close()
        break
    else:
        print('Opção inválida!')
