import os

#Clientes
listaClientes = []

class Cliente:
    def __init__(self, nome, sobrenome, senha, email, telefone, endereco, dataNasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.senha = senha
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.dataNasc = dataNasc

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getSobrenome(self):
        return self.sobrenome

    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def getSenha(self):
        return self.senha
    
    def setSenha(self, senha):
        self.senha = senha

    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email

    def getTelefone(self):
        return self.telefone
    
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getEndereco(self):
        return self.endereco
    
    def setEndereco(self, endereco):
        self.endereco = endereco

    def getDataNasc(self):
        return self.dataNasc
    
    def setDataNasc(self, dataNasc):
        self.dataNasc = dataNasc
    
def cadCliente():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    senha = input("Senha: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereco: ")
    dataNasc = input("Data de nascimento: ")
    cli = Cliente(nome, sobrenome, senha, email, telefone, endereco, dataNasc)
    listaClientes.append(cli)

def listarClientes():
    i = 0
    print("========"*5)
    if len(listaClientes) == 0:
            print("Sem registros...")
    while i < len(listaClientes):
        print(f"[{i+1}]. {listaClientes[i].nome} {listaClientes[i].sobrenome}")
        i+=1
    print("========"*5)

def altCadCliente():
    print("========"*5)
    listarClientes()
    esc = int(input("Digite o número correspondente ao cliente que deseja gerenciar o cadastro: "))
    print("========"*5)
    os.system('cls')
    print("========"*5)
    listaClientes[esc-1]
    print("Dados do Cliente:") #transformar em func
    print(f"Nome: {listaClientes[esc-1].nome} {listaClientes[esc-1].sobrenome}")
    print(f"Email: {listaClientes[esc-1].email}")
    print(f"Tel.:{listaClientes[esc-1].tel}")
    print(f"Endereço: {listaClientes[esc-1].endereco}")
    print(f"Data de nascimento: {listaClientes[esc-1].dataNasc}") #ate aqui
    print("[1]. Alterar nome\n"
        +"[2]. Alterar propriedades de login\n"
        +"[3]. Alterar número de telefone\n"
        +"[4]. Alterar endereço")
    esc1 = int(input("Digite o número de sua escolha: "))
    match esc1:
        case 1:
            esc2 = int(input("[1]. Para alterar nome\n"
                            +"[2]. Para alterar sobrenome\n"
                            +"Digite o número da operação de deseja realizar: "))
            while esc2!=1 or esc2!=2:
                esc2 = int(input("[1]. Para alterar nome\n"
                            +"[2]. Para alterar sobrenome\n"
                            +"Digite o número da operação de deseja realizar: "))
            match esc2:
                case 1:
                    novo = input("Digite o novo nome: ")
                    listaClientes[esc-1].setNome(novo)
                case 2:
                    novo = input("Digite o novo sobrenome: ")
                    listaClientes[esc-1].setSobrenome(novo)
        case 2:
            esc2 = int(input("[1]. Para alterar email\n"
                            +"[2]. Para alterar senha\n"
                            +"Digite o número da operação de deseja realizar: "))
            while esc2!=1 or esc2!=2:
                esc2 = int(input("[1]. Para alterar email\n"
                            +"[2]. Para alterar senha\n"
                            +"Digite o número da operação de deseja realizar: "))
            match esc2:
                case 1:
                    novo = input("Digite o novo email: ")
                    listaClientes[esc-1].setEmail(novo)
                case 2:
                    novo = input("Digite a nova senha: ")
                    listaClientes[esc-1].setSenha(novo)
    print("========"*5)

cadCliente()
cadCliente()
listarClientes()
altCadCliente()
#Clientes
# Requisitos básicos p/ produtos
# - Cadastrar novos produtos, incluindo nome, descrição, preço, quantidade em estoque, categoria, etc.
# - Editar informações de produtos existentes.
# - Remover produtos do sistema.
# - Realizar buscas por produtos, filtrando por nome, categoria, preço, etc.


# Produtos
listaProdutosSis = []

class Produto:
    def __init__(self, nome, id, desc, preco, qntEstoque, cat):
        self.nome = nome
        self.id = id
        self.desc = desc
        self.preco = preco
        self.qntEstoque = qntEstoque
        self.cat = cat

def cadProduto():
    print("Insira os dados do novo produto.")
    nome = input("Nome: ")
    id = input("ID: ")
    desc = input("Descrição: ")
    preco = float(input("Preço: ")) #usar "." para centavos
    qnt = int(input("Quantidade no estoque: "))
    cat = input("Categoria: ")
    prod = Produto(nome, id, desc, preco, qnt, cat)
    listaProdutosSis.append(prod)

def listarProdutos():
    i = 0
    print("========"*5)
    if len(listaProdutosSis) == 0:
            print("Sem registros...")
    while i < len(listaProdutosSis):
        print(f"[{i+1}]. {listaProdutosSis[i].nome}")
        i+=1
    print("========"*5)

def remProdutoSis():
    esc = input('digite o número do produto que deseja remover')
    listaProdutosSis.pop(esc-1)

def acoesProdutos():
    while True:
        print("========"*5+
            "\n[1]. Listar produtos no estoque\n"+
            "[2]. Adicionar produto ao estoque\n"+
            "[3]. Remover produto do estoque\n"+
            "[0]. Sair\n"+
            "========"*5)
        esc = int(input("Escolha o número da operação desejada\n"))
        while esc<0 or esc>3:
            esc = int(input("Escolha o número da operação desejada\n"))
        match esc:
            case 1:
                listarProdutos()
            case 2:
                cadProduto()
            case 3:
                remProdutoSis()
        if esc == 0:
            break

#Produtos
