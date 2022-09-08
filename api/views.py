
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProductSerializer, ImageSerializer, PageImageSerializer, UserSerializer
from store.models import Product, Image, PageImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AllProducts(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductImages(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        product_id = self.kwargs['id']
        queryset = Image.objects.filter(product_id=product_id)
        return queryset

class PageImages(generics.ListAPIView):
    serializer_class = PageImageSerializer
    queryset = PageImage.objects.all()


@api_view(['POST'])
def RegisterUser(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        try:
            user = User.objects.create_user(
                serialized.initial_data.get('email'),
                serialized.initial_data.get('username'),
                serialized.initial_data.get('password')
            )
            user.save()
        except Exception as e:
            return Response(str(e), status=status.HTTP_403_FORBIDDEN)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def LoginUser(request):
    serialized = request.data
    serialized = dict(serialized.lists())
    try:
        user = authenticate(username=serialized.get('email')[0], password=serialized.get('password')[0])
        if user is None:
            raise Exception("No such user")
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    return Response(str(user), status=status.HTTP_200_OK)



