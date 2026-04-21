import unicodedata


def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto


livros_disponiveis = [
    "Bíblia",
    "A Cabeça do Santo",
    "Noites Brancas",
    "Verity",
    "Harry Potter",
    "Senhor dos Anéis"
]

while True:
    busca = normalizar(input("Qual livro deseja procurar?: "))
    encontrado = None
    for livro in livros_disponiveis:
        if busca in normalizar(livro):
            encontrado = livro
            break
    if encontrado:
        print(f"Livro encontrado: {encontrado}")
        resposta = input("Deseja alugá-lo? (sim/não): ").lower().strip()
        if resposta == "sim":
            nome = input("Digite seu nome: ")
            numero = input("Digite seu número ou matrícula: ")
            print(f"{encontrado} está pronto para retirada, até logo!")
        else:
            print("Até logo!")
        break
    else:
        resposta = input(
            "Livro indisponível, deseja pesquisar por outro? (sim/não): ").lower().strip()
        if resposta != "sim":
            print("Até logo!")
            break
