def shopping_cart():
   
    num_items = int(input("Enter the number of items you purchase: "))
    
    items = []
    
    for a in range(num_items):
        print(f"Item {a + 1}:")
        name = input("Enter the name of the item you purchased: ")
        price = float(input("Enter the price of the item you purchased : "))
        items.append({"name": name, "price": price})
    
    
    print("Shopping Cart Summary:")
    for i, item in enumerate(items,start=1):
        print(f"Item {i}: {item['name']} - ${item['price']:.1f}")
    total_price = sum(item['price'] for item in items)
    print(f"Total bill:${total_price:.1f}")

    has_loyalty_card = input("do you a loyalty card ? (yes/no):")
    
    seasonal_offer = input("is there any seasonal offer ? (yes/no):")
    loyalty_discount = 0.10 if has_loyalty_card else 0
    seasonal_discount =0.05 if seasonal_offer else 0
    total_discount = loyalty_discount+seasonal_discount
    discount_amount = total_price * total_discount
    final_price = total_price - discount_amount

    print(f"subtotal: ${total_discount:.1f}")
    print(f"discount applied:$ {discount_amount:.1f}")
    print(f"after applying all discount on the original bill")
    print(f"final price: ${final_price:.1f}")
  

shopping_cart()

