# Producten en prijzen
product_one = "Laptop"
price_one = 800
quantity_one = 2
 
product_two = "Mouse"
price_two = 25
quantity_two = 5
 
product_three = "Keyboard"
price_three = 50
quantity_three = 3
 
# Bereken de totale omzet
total_revenue = (
    price_one * quantity_one
    + price_two * quantity_two
    + price_three * quantity_three
)
 
# Toon de resultaten
print(product_one, price_one, quantity_one)
print(product_two, price_two, quantity_two)
print(product_three, price_three, quantity_three)
print("Totale omzet:", total_revenue, "euro")


