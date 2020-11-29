from rest_framework import serializers

from alpifoodapp.models import Restaurant, Meal, Customer, Order, OrderDetails, Driver

from phone_field import PhoneField
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class RestaurantSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self, restaurant):
        request = self.context.get('request')
        logo_url = restaurant.logo.url
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "category", "phone", "address", "logo")

# Convert each meal to JSON for REST API
class MealSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = serializers.CharField(source='get_category_display')

    def get_image(self, meal):
        request = self.context.get('request')
        image_url = meal.image.url
        return request.build_absolute_uri(image_url)

    def get_categories (self, meal):
        return Meal.get_category_display

    class Meta:
        model = Meal
        fields = ("id", "category", "name", "short_description", "image", "price", "available")


# ORDER SERIALIZER
class OrderCustomerSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source="user.get_full_name")

    class Meta:
        model = Customer
        fields = ("id", "name", "avatar", "phone", "address")

class OrderDriverSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source="user.get_full_name")

    class Meta:
        model = Customer
        fields = ("id", "name", "avatar", "phone", "address")

class OrderRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "phone", "address")

class OrderMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id", "name", "price")

class OrderDetailsSerializer(serializers.ModelSerializer):
    meal = OrderMealSerializer()

    class Meta:
        model = OrderDetails
        fields = ("id", "meal", "quantity", "sub_total")

class OrderSerializer(serializers.ModelSerializer):
    customer = OrderCustomerSerializer()
    driver = OrderDriverSerializer()
    restaurant = OrderRestaurantSerializer()
    order_details = OrderDetailsSerializer(many=True)
    status = serializers.ReadOnlyField(source="get_status_display")

    class Meta:
        model = Order
        fields = ("id", "customer", "restaurant", "driver", "order_details",
                  "total", "status", "address")