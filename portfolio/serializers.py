from rest_framework import serializers
from .models import Customer, Investment, Stock
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk','name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'email', 'cell_phone')
        
        
class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ('pk','customer', 'cust_number', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date')
    
    
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('pk','customer', 'cust_number', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')




class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):  # http://zetcode.com/python/bcrypt/
        # if not self.context['request'].user.is_authenticated:
        # raise serializers.ValidationError('User is not authenticated!')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')