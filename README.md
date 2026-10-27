# Desafio Nível 1 - PDV com Descontos (Python)

## O que o código faz

Este programa simula um PDV (Ponto de Venda) que aplica descontos progressivos. Ele registra as compras do dia, uma a uma, calcula o valor final de cada compra aplicando as regras de desconto (idade, valor da compra e, no bônus, quantidade de itens e cupom de fidelidade) e, quando o usuário digita `0`, mostra um resumo do dia com a quantidade de compras, o total bruto, o total de descontos concedidos e o total final. O resumo também é gravado no arquivo `resumo.txt`.

## Como ele faz

1. O código pede o **valor da compra**. Se for `0`, o loop termina; se for negativo, mostra um aviso e pede novamente.
2. Pede a **idade do cliente**. Se for negativa, mostra um aviso e pede novamente.
3. Verifica se a idade é maior ou igual a 65 e, se for, aplica **20%** de desconto.
4. Verifica se o valor **já descontado pela idade** passa de R$ 100,00 e, se passar, aplica mais **10%** sobre esse valor.
5. **Bônus - quantidade:** pede a quantidade de itens e, se for maior que 3, aplica mais **5%**. Quantidade menor ou igual a zero mostra um aviso e pede novamente.
6. **Bônus - cupom:** pede um cupom (pode ficar em branco) e, se for `FIDELIDADE10`, aplica mais **10%**.
7. Calcula o desconto total (valor bruto menos valor final) e guarda o valor bruto, o valor final e o desconto em três listas, usando `.append()`.
8. Mostra o valor final da compra com duas casas decimais (exemplo: `R$ 144.00`) e volta ao passo 1 para a próxima compra.
9. Quando o usuário digita `0`, soma as listas e mostra o **resumo do dia** na tela.
10. **Bônus - histórico:** abre o arquivo `resumo.txt` com `open(..., "w")` e, com um `for` sobre as listas, grava uma linha por compra, seguida dos totais.

Os descontos são aplicados em sequência: cada um incide sobre o valor que já passou pelos descontos anteriores, e não sobre o valor original.

## Como rodar

```
python pdv.py
```

Ao final da execução, o arquivo `resumo.txt` é criado (ou sobrescrito) na mesma pasta.

## Tabela de exemplos

Casos de teste do enunciado. Para conferi-los, informe o valor e a idade de cada linha, digite `1` na quantidade de itens e deixe o cupom em branco.

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|------------|-------|----------------|----------------|----------------------|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

### Casos extras (bônus)

| # | Valor | Idade | Qtd. itens | Cupom | Cálculo | Valor final |
|---|-------|-------|------------|-------|---------|-------------|
| B1 | 50.00 | 30 | 4 | - | -5% (mais de 3 itens) | R$ 47.50 |
| B2 | 50.00 | 30 | 1 | FIDELIDADE10 | -10% (cupom) | R$ 45.00 |
| B3 | 50.00 | 30 | 3 | - | 3 itens não passa de 3: sem desconto | R$ 50.00 |
| B4 | 200.00 | 70 | 5 | FIDELIDADE10 | -20% = 160; -10% = 144; -5% = 136.80; -10% = 123.12 | R$ 123.12 |
