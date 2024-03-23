from django.shortcuts import render
from django.views import View
from . models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.http import request


# Create your views here.
class ProductView(View):
    def get(self, request):
        gentspants = Product.objects.filter(category='GP')
        borkhas = Product.objects.filter(category="BK")
        lehenga = Product.objects.filter(category='L')
        saree = Product.objects.filter(category="S")
        baby_fashion = Product.objects.filter(category="BF")
        return render(request, 'Shop/home.html',
                      {'gentspants': gentspants, 'borkhas': borkhas, 'lehenga': lehenga, 'saree': saree,
                       'baby_fashion': baby_fashion})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'Shop/productdetail.html', {'products': product})


def add_to_cart(request):
    return render(request, 'Shop/addtocart.html')


def buy_now(request):
    return render(request, 'Shop/buynow.html')


# def profile(request):
#     
class ProfileView(View):
 def get(self, request):
  form = CustomerProfileForm()
  return render(request, 'Shop/profile.html', {'form':form, 'active':'btn-primary'})

 def post(self, request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
      usr = request.user
      name = form.cleaned_data['name']
      division = form.cleaned_data['division']
      district = form.cleaned_data['district']
      thana = form.cleaned_data['thana']
      villorroad = form.cleaned_data['villorroad']
      zipcode = form.cleaned_data['zipcode']
      reg = Customer(user=usr,name=name, division=division,district=district, thana=thana, villorroad=villorroad, zipcode=zipcode)
      reg.save()
      messages.success(request, 'Congratulations! Profile Updated Successfully')
  return render(request, 'Shop/profile.html', {'form':form, 'active':'btn-primary'})

def address(request):
    return render(request, 'Shop/address.html')


def orders(request):
    return render(request, 'Shop/orders.html')


def change_password(request):
    return render(request, 'Shop/changepassword.html')


def lehenga(request, data=None):
    global lehengas
    if data == None:
        lehengas = Product.objects.filter(category="L")
    elif data == 'lubnan' or data == 'infinity':
        lehengas = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'above':
        lehengas = Product.objects.filter(category = 'L').filter(discounted_price__gt=1000)
    elif data == 'below':
        lehengas = Product.objects.filter(category = 'L').filter(discounted_price__lt=1000)
    return render(request, 'Shop/lehenga.html', {'lehengas': lehengas})


def saree(request, data=None):
    if data is None:
        saree = Product.objects.filter(category="S")
    elif data == 'lubnan' or data == 'infinity':
        saree = Product.objects.filter(category="S").filter(brand=data)
    elif data == 'above':
        saree = Product.objects.filter(category = 'S').filter(discounted_price__gt=1000)
    elif data == 'below':
        saree = Product.objects.filter(category = 'S').filter(discounted_price__lt=1000)
    return render(request, 'Shop/saree.html', {'saree': saree})


def login(request):
    return render(request, 'Shop/login.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'Shop/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulation! succesfully Registration done')
        return render(request, 'Shop/customerregistration.html', {'form': form})


def checkout(request):
    return render(request, 'Shop/checkout.html')
