import random

def Polissacarideo():
    sequencia = ""
    for _ in range(7):
        base = random.choice(["G", "C"])
        sequencia += base
    return sequencia

def main():
    estrutura_de_codom = 0
    for _ in range(100):
        rna_M = Polissacarideo()
        if "CGG" in rna_M or "CGC" in rna_M:
            estrutura_de_codom += 1

    media = estrutura_de_codom / 100
    print("Média das sequências:", media)
    print("A)", round(1 - (1/3)**7, 5))
    print("B)", round(1 - (1/8)**7, 5))
    print("C)", round(1 - (3/4)**7, 5))
    print("D)", round((1/4)**7, 5))

if __name__ == "__main__":
    main()
