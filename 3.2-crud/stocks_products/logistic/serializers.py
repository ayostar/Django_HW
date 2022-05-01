from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def update_stock_products(self, stock, positions):
        for position in positions:
            product = position.pop('product')
            defaults = position
            StockProduct.objects.update_or_create(
                stock = stock,
                product = product,
                defaults = defaults
            )

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        self.update_stock_products(stock, positions)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        self.update_stock_products(stock, positions)

        return stock
