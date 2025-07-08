from operator import truediv


class Product:

    id_counter = 1
    def __init__(self, description, price, quantity):
        self.id = Product.id_counter
        Product.id_counter += 1
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.id}. {self.description} - ${self.price:.2f} ({self.quantity} disponibles)"


class Store:
    def __init__(self):
        self.products = []
        self.total_sales = 0

    def add_product(self, description, price, quantity):
        new_product = Product(description, price, quantity)
        self.products.append(new_product)

    def show_product(self):
        for product in self.products:
            print(product)

    def add_inventory_product(self, product_id, new_quantity):
        for product in self.products:
            if product.id == product_id:
                    product.quantity += new_quantity
                    return True
        print("Producto no encontrado.")
        return False

    def delete_inventory_product(self, product_id, remove_quantity):
        for product in self.products:
            if product.id == product_id:
                if product.quantity > remove_quantity:
                    product.quantity -= remove_quantity
                    return True
                else:
                    print("Cantidad de inventario insuficiente")
                    return False
        print("Producto no encontrado.")
        return False


    def sell_product(self, product_id, quantity):
        for product in self.products:
            if product.id == product_id:
                if product.quantity >= quantity:
                    total = product.price * quantity
                    print(f"Producto: {product.description}")
                    print(f"Precio unitario: ${product.price:.2f}")
                    print(f"Cantidad: {quantity}")

                    self.delete_inventory_product(product_id, quantity)
                    self.total_sales += total
                    return True
                else:
                    print("Inventario insuficiente para completar la venta.")
                    return False
        print("Producto no encontrado.")
        return False



