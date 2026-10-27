valores_brutos = []
valores_finais = []
descontos_concedidos = []

while True:
    valor = float(input("Digite o valor da compra (ou 0 para sair): "))

    if valor == 0:
        break

    if valor < 0:
        print("Aviso: O valor da compra não pode ser negativo. Tente novamente.")
        continue

    idade = int(input("Digite a idade do cliente: "))

    if idade < 0:
        print("Aviso: A idade não pode ser negativa. Tente novamente.")
        continue

    quantidade = int(input("Digite a quantidade de itens: "))

    if quantidade <= 0:
        print("Aviso: A quantidade de itens deve ser maior que zero. Tente novamente.")
        continue

    cupom = input("Digite o cupom de desconto (ou deixe em branco): ").strip().upper()

    valor_final = valor

    # Desconto de idoso: 20% para clientes com 65 anos ou mais
    if idade >= 65:
        valor_final = valor_final - (valor_final * 0.20)

    # Desconto por valor: 10% se o valor já descontado passar de 100
    if valor_final > 100:
        valor_final = valor_final - (valor_final * 0.10)

    # Desconto por quantidade: 5% extra para mais de 3 itens
    if quantidade > 3:
        valor_final = valor_final - (valor_final * 0.05)

    # Cupom de fidelidade: 10% extra
    if cupom == "FIDELIDADE10":
        valor_final = valor_final - (valor_final * 0.10)

    desconto_total = valor - valor_final

    valores_brutos.append(valor)
    valores_finais.append(valor_final)
    descontos_concedidos.append(desconto_total)

    print(f"Valor final da compra: R$ {valor_final:.2f}\n")

print("-" * 35)
print("RESUMO DO DIA")
print(f"Quantidade de compras registradas: {len(valores_brutos)}")
print(f"Total bruto: R$ {sum(valores_brutos):.2f}")
print(f"Total de descontos concedidos: R$ {sum(descontos_concedidos):.2f}")
print(f"Total final: R$ {sum(valores_finais):.2f}")

# Salvar histórico em resumo.txt
with open("resumo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("RESUMO DO DIA\n")
    arquivo.write("-" * 35 + "\n")

    for i in range(len(valores_brutos)):
        arquivo.write(
            f"Compra {i + 1}: "
            f"bruto R$ {valores_brutos[i]:.2f} | "
            f"desconto R$ {descontos_concedidos[i]:.2f} | "
            f"final R$ {valores_finais[i]:.2f}\n"
        )

    arquivo.write("-" * 35 + "\n")
    arquivo.write(f"Quantidade de compras registradas: {len(valores_brutos)}\n")
    arquivo.write(f"Total bruto: R$ {sum(valores_brutos):.2f}\n")
    arquivo.write(f"Total de descontos concedidos: R$ {sum(descontos_concedidos):.2f}\n")
    arquivo.write(f"Total final: R$ {sum(valores_finais):.2f}\n")

print("Resumo salvo em resumo.txt")