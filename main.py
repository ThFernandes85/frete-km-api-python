def calcular_frete(km, valor_km):
    total = km * valor_km
    return total


if __name__ == "__main__":
    km = float(input("Digite a distância em KM: "))
    valor = float(input("Digite o valor por KM: "))

    resultado = calcular_frete(km, valor)

    print(f"Valor total do frete: R$ {resultado:.2f}")

