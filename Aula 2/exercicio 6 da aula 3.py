valor_da_compra = float(input("Valor gasto:R$ "))
if valor_da_compra <= 100:
    desconto = valor_da_compra * 0.05  #desconto de 5%
    valor_com_desconto = (valor_da_compra - desconto)
    print("Valor a ser pago com desconto:R$",valor_com_desconto)
elif valor_da_compra >= 101 and valor_da_compra <=199:
    desconto = valor_da_compra * 0.1   #desconto de 10%
    valor_com_desconto = (valor_da_compra - desconto)
    print("Valor a ser pago com desconto:R$",valor_com_desconto)
else:
    desconto = valor_da_compra * 0.2   #desconto de 20%
    valor_com_desconto = (valor_da_compra - desconto)
    print("Valor a ser a pago com desconto:R$",valor_com_desconto)
