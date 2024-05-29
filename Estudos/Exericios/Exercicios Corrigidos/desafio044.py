#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
forma1= "1 - à vista dinheiro/cheque"
forma2= "2 - à vista no cartão"
forma3= "3 - em até 2x no cartao"
forma4= "4 - 3x ou mais no cartão"

preco_produto = float(input("Digite o valor do produto: R$"))
forma_pagamento = int(input("Digite a forma de pagamento:\n"
                            "{}\n"
                            "{}\n"
                            "{}\n"
                            "{}\n:".format(forma1,forma2,forma3,forma4)))

if forma_pagamento ==1:
    preco_pago = preco_produto - (preco_produto * 0.10)
    forma_pagamento = forma1
elif forma_pagamento == 2:
    preco_pago = preco_produto - (preco_produto * 0.05)
    forma_pagamento = forma2
elif forma_pagamento == 3:
    preco_pago = preco_produto
    forma_pagamento = forma3
elif forma_pagamento == 4:
    preco_pago = preco_produto + (preco_produto * 0.20)
    forma_pagamento = forma4
else:
    print("Forma de pagamento inválida. Tente novamente!")
print("O preço pago pelo produto foi R$ {:.2f} pois selecionou {} como forma de pagamento.".format(preco_pago,forma_pagamento))
