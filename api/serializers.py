from rest_framework import serializers
from store.models import Product, Image, PageImage
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image',)


class PageImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageImage
        #fields = ('id', 'image_url')
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'