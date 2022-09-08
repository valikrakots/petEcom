import urllib

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import ListView, DetailView
from rest_framework.generics import get_object_or_404

from .models import Product, Image, FavouriteItems
#import pyrebase


# firebaseConfig = {
#   'apiKey': "AIzaSyDBWojLiSvBqKN4pKPl6UPQnVPeTgBkJdc",
#   'authDomain': "ecom-486a3.firebaseapp.com",
#   'projectId': "ecom-486a3",
#   'storageBucket': "ecom-486a3.appspot.com",
#   'messagingSenderId': "294539198516",
#   'appId': "1:294539198516:web:32d9181d298bf097dfca61",
#   'measurementId': "G-QZ0Z8W39P2",
#   'databaseURL': ""
# }
#
# firebase = pyrebase.initialize_app(firebaseConfig)
# authe = firebase.auth()
# database = firebase.database()


class home(ListView):

    model = Product
    context_object_name = 'products'
    template_name = 'store/home.html'

class product_detail(DetailView):

    model = Product
    template_name = 'store/product_info.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        carted = False
        if self.request.user.username != '' and FavouriteItems.objects.all().filter(user=self.request.user,
                                                                               product=Product.objects.get(
                                                                                       id=id)).first():
            carted = True
        context = super().get_context_data(**kwargs)
        context['carted'] = carted
        return context



def signUp(request):
    return render(request,"store/registration.html")


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    rep_pass = request.POST.get('pass_repeat')
    try:
        if passs != rep_pass:
            raise Exception("Passwords should match")
        if len(passs) < 6:
            raise Exception("Password should be at least 6 characters long")
        # creating a user with the given email and password
        user = User.objects.create_user(email, email, passs)
        user.save()

    except Exception as e:
        print(e)
        msg = str(e)
        content = {
            'message': msg,
        }
        return render(request, "store/registration.html", content)
    return render(request, "store/login.html")




def signIn(request):
    return render(request, "store/login.html")



def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user = authenticate(username=email, password=pasw)
        if user is None:
            raise Exception("")
        request.user = user
    except:
        message = "Invalid Credentials!!"
        return render(request, "store/login.html", {"message": message})
    content = {
        'products': Product.objects.all(),
        'username': request.user.username,
    }
    return render(request, 'store/home.html', content)


@login_required
def favourite_add(request, id):
    product = get_object_or_404(Product, id=id)
    favourite = FavouriteItems.objects.all().filter(user=request.user, product=product).first()
    if favourite:
        favourite.delete()
    else:
        favourite = FavouriteItems.objects.create(user=request.user, product=product)
        favourite.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



class cart_details(ListView):
    model = Product
    template_name = 'store/cart.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = FavouriteItems.objects.all().filter(user=self.request.user)
        return products

    # content = {}
    # if request.user.username:
    #     products = FavouriteItems.objects.all().filter(user=request.user)
    #     content = {
    #         'products': products,
    #         'username': request.user.username
    #     }
    # return render(request, 'store/cart.html', content)