#سوال دو
prices = {"Laptop": 120000000, "Mouse": 2000000, "Keyboard": 3000000}





def process_order(customer, *products, **options):



    discount = options.get("discount", 0)

    tax = options.get("tax", 0)

    shipping = options.get("shipping", 0)



    total = 0



    for i in products:

        total += prices[i]



    total = total - (total * discount / 100)



    total = total + (total * tax / 100)



    total += shipping



    return {

        "customer": customer,

        "products": products,

        "discount": discount,

        "tax": tax,

        "shipping": shipping,

        "final_price": total}





result = process_order(

    "Ali",

    "Laptop",

    "Mouse",

    "Keyboard",

    discount=10,

    tax=9,

    shipping=200000)



print(result)
