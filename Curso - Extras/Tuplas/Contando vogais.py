palavras = (
    'gato', 'cachorro', 'banana', 'computador', 'arroz', 'celular',
    'abacaxi', 'livro', 'praia', 'chocolate', 'carro', 'caneta',
    'sol', 'casa', 'amor', 'janela', 'lápis',
)
print(f"Lista de palavras {palavras}")
for i in range(len(palavras)):
    palavra = palavras[i]
    print(f"Vogais de {palavra}")
    for letra in palavra:
        if letra in ("a","e","i","o","u"):
            print(f"{letra} ",end="")
    print()