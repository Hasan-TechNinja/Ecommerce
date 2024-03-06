from django.shortcuts import render
from django.views import View
from . models import Customer, Product, Cart, OrderPlaced
from . forms import CustomerRegistrationForm

# Create your views here.
class ProductView(View):
 def get(self,request):
  gentspants = Product.objects.filter(category = 'GP')
  borkhas = Product.objects.filter(category = "BK")
  lehenga = Product.objects.filter(category = 'L')
  saree = Product.objects.filter(category = "S")
  baby_fashion = Product.objects.filter(category = "BF")

  return render(request, 'Shop/home.html', {'gentspants': gentspants, 'borkhas': borkhas, 'lehenga':lehenga, 'saree': saree, 'baby_fashion':baby_fashion })
 
class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk = pk)
  return render(request, 'Shop/productdetail.html', {'products': product})     

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')

def profile(request):
 return render(request, 'Shop/profile.html')

def address(request):
 return render(request, 'Shop/address.html')

def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request):
 return render(request, 'Shop/lehenga.html')

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
  return render(request, 'Shop/customerregistration.html',{'form': form})

def checkout(request):
 return render(request, 'Shop/checkout.html')
