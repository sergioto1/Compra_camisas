'''
Hacer un algoritmo que calcule el total a pagar por la compra de camisas. 
Si se compran tres camisas o más se aplica un descuento del 20% sobre el 
total de la compra y si son menos de tres camisas un descuento del 10%
'''

def total_a_pagar(camisas: int, precio: float) -> float:
    if (camisas >= 3):
        valor_compra = camisas * precio
        total_conDescuento = valor_compra - (valor_compra * 0.2) 
        prueba = valor_compra * 0.8
        print(total_conDescuento)
        print(prueba)
    else:
        valor_compra = camisas * precio
        total_conDescuento = valor_compra - (valor_compra * 0.1) 
        prueba = valor_compra * 0.9
        print(total_conDescuento)
        print(prueba)
        
# prueba               
print(total_a_pagar(2,35000))
