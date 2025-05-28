import calcArea

def pedir_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Por favor, digite um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Valor inválido! Tente novamente.")

def calcular_area_circulo():
    raio = pedir_float("Digite o raio do círculo: ")
    area = calcArea.calcular_area_circulo(raio)
    print(f"A área do círculo é: {area:.2f}")

def calcular_area_triangulo():
    base = pedir_float("Digite a base do triângulo: ")
    altura = pedir_float("Digite a altura do triângulo: ")
    area = calcArea.calcular_area_triangulo(base, altura)
    print(f"A área do triângulo é: {area:.2f}")

def calcular_area_retangulo():
    largura = pedir_float("Digite a largura do retângulo: ")
    altura = pedir_float("Digite a altura do retângulo: ")
    area = calcArea.calcular_area_retangulo(largura, altura)
    print(f"A área do retângulo é: {area:.2f}")

def main():
    opcoes = {
        1: calcular_area_circulo,
        2: calcular_area_triangulo,
        3: calcular_area_retangulo
    }

    print("Cálculo das áreas de figuras geométricas:")
    print("1. Círculo")
    print("2. Triângulo")
    print("3. Retângulo")

    try:
        opcao = int(input("Qual figura deseja calcular a área? "))
        if opcao in opcoes:
            opcoes[opcao]()
        else:
            print("ERRO! Essa não é uma opção válida!")
    except ValueError:
        print("ERRO! Digite um número válido!")

if __name__ == "__main__":
    main()
