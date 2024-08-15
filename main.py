class Cliente:
    def __init__(self, nome, sobrenome, senha, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.senha = senha
        self.email = email

listaProdutosSis = []

class Produto:
    def __init__(self, nome, id, desc, preco, qntEstoque, cat):
        self.nome = nome
        self.id = id
        self.desc = desc
        self.preco = preco
        self.qntEstoque = qntEstoque
        self.cat = cat

def addProduto():
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
    print("==="*5)
    while i < len(listaProdutosSis):
        print(f"[{i+1}]. {listaProdutosSis[i]}")
        i+=1
    print("==="*5)

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
                addProduto()
            case 3:
                remProdutoSis()
        if esc == 0:
            break

acoesProdutos()