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

def addProduto(produto):
    listaProdutosSis.append(produto)

def listarProdutos():
    i = 0
    while i < len(listaProdutosSis):
        print(f"[{i+1}]. {listaProdutosSis[i]}")
        i+=1

def remProdutoSis():
    esc = input('digite o número do produto que deseja remover')
    listaProdutosSis.pop(esc-1)

def acoesProdutos():
    print("[1].Listar produtos no estoque\n"+
        "[2]. Adicionar produto ao estoque\n"+
        "[3]. Remover produto do estoque\n"+
        "[0]. Sair")
    esc = int(input("Escolha o número da operação desejada\n"))
    while esc<0 or esc>3:
        esc = int(input("Escolha o número da operação desejada\n"))

acoesProdutos()