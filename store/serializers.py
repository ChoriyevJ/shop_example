from rest_framework import serializers

from store.models import Product, Category
from store.cart import Cart


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "title", "price", "category"


class ProductDetailSerializer(serializers.ModelSerializer):
    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

    quantity = serializers.ChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        write_only=True
    )

    override = serializers.BooleanField(required=False,
                                        initial=False,
                                        read_only=True
                                        )

    title = serializers.CharField(read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
    category = serializers.StringRelatedField(source="category.title", read_only=True)

    class Meta:
        model = Product
        fields = "title", "price", "category", "quantity", "override"

    def update(self, instance, validated_data):

        print('\n\n')
        print(instance)
        print(self.context['request'])
        print(validated_data)
        print('\n\n')
        request = self.context['request']
        quantity = validated_data['quantity']
        cart = Cart(request)
        cart.add(instance, quantity)
        return super().update(instance, validated_data)
