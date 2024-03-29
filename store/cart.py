

class Cart:

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = dict()

        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity,
                                     'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += 1

        self.get_total_price(product_id)
        self.save()

    def get_total_price(self, item):
        quantity = self.cart[item]['quantity']
        price = self.cart[item]['price']
        total = quantity * float(price)
        self.cart[item]['total_price'] = str(total)

    def save(self):
        self.session.modified = True
        # del self.session['cart']



