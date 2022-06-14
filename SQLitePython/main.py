import sqlite3
import datetime

# criando a conexão
con = sqlite3.connect('cadastro.db')

# criando o cursor
c = con.cursor()

# definindo todas as funções necessárias para a aplicação


# criar tabela caso não exista
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS clientes(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nome VARCHAR(60) NOT NULL,
atualizado VARCHAR,
nascimento VARCHAR,
sexo VARCHAR(1) NOT NULL
)''')


# inserir dados de cliente no cadastro
def cliente_insert():
    print('\nREALIZANDO NOVO CADASTRO\n')
    # nome
    while True:
        nome = input('Nome do cliente: ').strip()
        if len(nome) > 5:
            break
        else:
            print('''O nome digitado é muito pequeno.
Digite o nome correto.''')

    # data de nascimento
    nascimento = input('Data de nascimento (aaaa-mm-dd): ').strip()

    # data do cadastro
    atualizado = datetime.datetime.now()

    # sexo
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo in 'fFmM':
            break
        else:
            print('Você deve digitar para sexo apenas M ou F.')

    c.execute(f"""INSERT INTO clientes (nome, atualizado, nascimento, sexo) 
VALUES ('{nome}', '{atualizado}', '{nascimento}', '{sexo}')""")

    if sexo in 'mM':
        print(f'O cliente {nome} foi inserido com sucesso!')
    else:
        print(f'A cliente {nome} foi inserido com sucesso!')

    con.commit()


# ler tabela
def cliente_select():
    print('\nEXIBINDO TODA A TABELA\n')
    c.execute('SELECT * FROM clientes')
    for i in c.fetchall():
        print(i)


# ler dados agrupados por sexo
def cliente_selectsexo():
    while True:
        filtro = input('Quer exibir os resultados de qual sexo? [M/F] ').strip().upper()
        if filtro in 'fFmM':
            break
        else:
            print('Você deve digitar para o filtro de sexo apenas M ou F.')

    if filtro in 'mM':
        s = 'MASCULINO'
    else:
        s = 'FEMININO'
    print(f'\nSELECIONANDO E EXIBINDO TODOS OS CLIENTE DO SEXO {s}\n')
    c.execute(f"SELECT * FROM clientes WHERE sexo = '{filtro}'")
    for i in c.fetchall():
        print(i)


# atualizar dado de cliente
def clientes_update():
    # puxando cliente a ter cadastro atualizado pelo id
    print('\nATUALIZANDO CADASTRO DE CLIENTE\n')
    while True:
        idc = input('id do cliente: ')
        if idc.isnumeric():
            break
        else:
            print('O id do cliente deve ser um número.')

    # escolhendo o dado a ser modificado
    print('''\nQual o dado a ser mudado?
1 - Nome
2 - Nascimento
3 - Sexo''')
    while True:
        resp = input('').strip()
        if resp in '123':
            break
        else:
            print('Você deve digitar 1, 2 ou 3, segundo o índice.')
    if int(resp) == 1:
        dado = 'nome'
    elif int(resp) == 2:
        dado = 'nascimento'
    else:
        dado = 'sexo'

    # inputando novo valor para o dado
    while True:
        if dado == 'nome':
            while True:
                novo_valor = input(f'Digite o novo valor para o {dado} do cliente: ').strip()
                if len(novo_valor) > 5:
                    break
                else:
                    print('''O nome digitado é muito pequeno.
Digite o nome correto.''')

        elif dado == 'nascimento':
            novo_valor = input(f'Digite o novo valor para o {dado} do cliente: ').strip()

        elif dado == 'sexo':
            while True:
                novo_valor = input(f'Digite o novo valor para o {dado} do cliente: ').strip().upper()
                if novo_valor in 'fFmM':
                    break
                else:
                    print('Você deve digitar para sexo apenas M ou F.')

        break

    dt = datetime.datetime.now()

    c.execute(f"""UPDATE clientes 
SET {dado} = '{novo_valor}'
WHERE id = '{idc}'
""")
    c.execute(f"""UPDATE clientes
SET atualizado = '{dt}'
WHERE id = '{idc}'""")

    print(f'O dado {dado} do cliente foi atualizado com sucesso!')
    con.commit()


# removendo cliente
def clientes_remove():
    print('\nEXCLUINDO CADASTRO DE CLIENTE\n')
    while True:
        idc = input('id do cliente: ')
        if idc.isnumeric():
            break
        else:
            print('O id do cliente deve ser um número.')
    c.execute(f"DELETE FROM clientes WHERE id = '{idc}'")


# programa principal de cadastro e consulta a tabela clientes no banco de dados

# criando a tabela
create_table()

print('''Seja bem vindo ao programa de consulta e cadastro de clientes da CB Company.''')
while True:
    # escolha da ação
    print('''
MENU:
1 - Cadastrar Cliente
2 - Atualizar Dado de um Cliente
3 - Visualizar Toda a Tabela de Clientes
4 - Visualizar Clientes por Sexo
5 - Excluir Cadastro de um Cliente
''')
    while True:
        # escolhendo uma das opções
        ans = input('Qual a opção desejada? ').strip()
        if ans in '12345':
            break

    ans = int(ans)

    if ans == 1:
        cliente_insert()

    elif ans == 2:
        clientes_update()

    elif ans == 3:
        cliente_select()

    elif ans == 4:
        cliente_selectsexo()

    elif ans == 5:
        clientes_remove()

    else:
        print('\nVocê deve digitar 1, 2, 3, 4 ou 5, de acordo com o índice.')

    while True:
        power = input('\nDeseja realizar mais alguma ação [S/N]? ').strip().upper()
        if power[0] in 'sSnN':
            break
        else:
            print('Você deve digitar S ou N.')

    if power[0] in 'Nn':
        print('\nVolte sempre que quiser consultar os dados dos nossos clientes!')
        print('Encerrando programa...')
        break
