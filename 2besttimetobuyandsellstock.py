prices = [7, 1, 5, 3, 6, 4]

#Definir funcion y agregar el array prices
def max_profit(prices):
    #Si no hay ninguna lista retorna 0
    if not prices:
        return 0
    #Hacemos variables del maximo profit actual que es 0 y el precio minimo de compra 
    #que es actualmente la posicion 0 de la lista
    max_profit = 0
    min_price = prices[0]

    #Hacemos un for loop para recorrer la lista de precios con variables de dia precio
    for day, price in enumerate(prices):
        #Si el precio es menor al precio minimo actual, actualizamos el precio minimo
        if price < min_price:
            min_price = price
        #Si no, calculamos el profit actual y lo comparamos con el maximo profit actual, si es mayor lo actualizamos
        else:
            max_profit = max(max_profit, price - min_price)
            
    return max_profit

print(max_profit(prices))
