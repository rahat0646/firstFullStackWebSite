from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.template.loader import get_template, render_to_string
from django.contrib import messages
from .models import *
import json
from django.views import View
from django.db.models import Avg, Max, Q

from .forms import *


def Home(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    banner = Banner.objects.all()
    abous = AboutUs.objects.all()
    product = Product.objects.filter(status=True)
    brand = Brand.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
        added_to_cart_product_ids = cart.values_list('product__id', flat=True)
        added_to_wishlist_product_ids = wishlist.values_list('product__id', flat=True)
    return render(request,"index.html",locals())


def ProductView(request,pk,name):
    product = Product.objects.get(pk=pk)
    productImage = ProductImages.objects.all()
    related_products = Product.objects.filter(status=True) and Product.objects.filter(Q(category_id=product.category.id) | Q(category__menu__id=product.category.menu.id) ).exclude(id=pk)[:10] or Product.objects.filter(brand=product.brand.id).exclude(id=pk)[:10]
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        rel_cart = Cart.objects.filter(user=request.user)
        added_to_cart_product_ids = rel_cart.values_list('product__id', flat=True)
        rel_wishlist = Wishlist.objects.filter(user=request.user)
        added_to_wishlist_product_ids = rel_wishlist.values_list('product__id', flat=True)
    for proimg in productImage:
        if product.id == proimg.product.id:
            proImage = ProductImages.objects.filter(product_id=product.id)
    # productColor = ProductColor.objects.all()
    # for proCol in productColor:
        # if product.id == proCol.product.id:
            # proColor = ProductColor.objects.filter(product_id=product.id)
    reviews = Review.objects.filter(product_id=pk).order_by('-created_at')
    review_count = reviews.count()
    total_rating_points = sum(int(rev.rate) for rev in reviews)
    try:
        rating_star = (total_rating_points / (review_count * 5)) * 5
    except ZeroDivisionError:
        rating_star = 0
    menu = Menu.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        cartpro = Cart.objects.filter(Q(product=product) & Q(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        wish = Wishlist.objects.filter(user=request.user)
    return render(request,"product.html",locals())

def Review_rate(request):
    if request.method == "GET":
        product_id = request.GET.get('product_id')
        product = Product.objects.get(pk=product_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        user = request.user
        Review(user=user,product=product,comment=comment,rate=rate).save()
        # return redirect('product',pk=product_id)
        return redirect('product',pk=product_id,name=product)
    
class CategoryView(View):
    def get(self,request,categoryName,id):
        product = Product.objects.filter(Q(category_id=id) & Q(status=True)).order_by('-date')
        menu = Menu.objects.all()
        category = Category.objects.all()
        brand = Brand.objects.filter(product__category__id=id).distinct()
        menus = Menu.objects.get(category=id)
        reviews = Review.objects.filter(product__in=product).order_by('-created_at')
        review_count = reviews.count()
        abous = AboutUs.objects.all()
        total_rating_points = sum(int(rev.rate) for rev in reviews)
        try:
            rating_star = (total_rating_points / (review_count * 5)) * 5
        except ZeroDivisionError:
            rating_star = 0
        title = Product.objects.filter(category_id=id).values('productName').annotate(total=Count('productName'))
        if request.user.is_authenticated:
            user = request.user
            cart = Cart.objects.filter(user=user)
            wishlist = Wishlist.objects.filter(user=user)
            added_to_cart_product_ids = cart.values_list('product__id', flat=True)
            added_to_wishlist_product_ids = wishlist.values_list('product__id', flat=True)
        return render(request,"category.html",locals())
    
class MenuView(View):
    def get(self,request,menuName,id):
        product = Product.objects.filter(Q(category__menu__id=id)& Q(status=True)).order_by('-date')
        menu = Menu.objects.all()
        menus = Menu.objects.get(id=id)
        category = Category.objects.all()
        brand = Brand.objects.filter(product__category__menu__id=id).distinct()
        title = Product.objects.filter(category__menu__id=id).values('productName').annotate(total=Count('productName'))
        abous = AboutUs.objects.all()
        if request.user.is_authenticated:
            user = request.user
            cart = Cart.objects.filter(user=user)
            wishlist = Wishlist.objects.filter(user=user)
            added_to_cart_product_ids = cart.values_list('product__id', flat=True)
            added_to_wishlist_product_ids = wishlist.values_list('product__id', flat=True)
        return render(request,"category.html",locals())
    

def register(request):
    if request.method=='POST':
        register=Register(request.POST)
        if register.is_valid():
            register.save()
            phone = register.cleaned_data.get('phone')
            username = register.cleaned_data.get('username')
            messages.success(request,'Ustunlikli agza boldunuz giris edin!')
            return redirect('login')
    else:
        register=Register()
    menu = Menu.objects.all()
    category = Category.objects.all()
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'signup.html',locals())

def giris(request):
    if request.method == 'POST':
        log = Login(request.POST) 
        if log.is_valid():
            number = log.cleaned_data.get('number')
            password = log.cleaned_data.get('password')
            user = authenticate(username=number,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,'Telefon belginiz ýa-da açar söziňiz nadogry')
        else:
            messages.error(request,'Telefon belginiz ýa-da açar söziňiz nadogry')
    loginS=Login()
    menu = Menu.objects.all()
    category = Category.objects.all()
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'login.html',locals())

class BrandViewAll(View):
    def get(self,request,brandName,id):
        product = Product.objects.filter(Q(brand_id=id) & Q(status=True)).order_by('-date')
        menu = Menu.objects.all()
        category = Category.objects.all()
        title = Product.objects.filter(brand_id=id).values('productName').annotate(total=Count('productName'))
        abous = AboutUs.objects.all()
        if request.user.is_authenticated:
            user = request.user
            cart = Cart.objects.filter(user=user)
            wishlist = Wishlist.objects.filter(user=user)
            added_to_cart_product_ids = cart.values_list('product__id', flat=True)
            added_to_wishlist_product_ids = wishlist.values_list('product__id', flat=True)
        return render(request,"brand_list.html",locals())    

def BrandView(request,id,brandName):
    product = Product.objects.filter(Q(brand__id=id) & Q(status=True)).order_by('-date')
    products = Product.objects.filter(Q(brand__id=id) & Q(status=True)).order_by('-date')[:25]
    brand = Brand.objects.get(id=id)
    menu = Menu.objects.all()
    category = Category.objects.all()
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
        added_to_cart_product_ids = cart.values_list('product__id', flat=True)
        added_to_wishlist_product_ids = wishlist.values_list('product__id', flat=True)
    return render(request,"brands.html",locals())

class Adressa(View):
    def get(self,request):
        form = AdressForm()
        menu = Menu.objects.all()
        category = Category.objects.all()
        city = City.objects.all()
        cart = Cart.objects.filter(user=request.user)
        if cart:
            return render(request,'adress.html',locals())
        else:
            return redirect('/')
    def post(self,request):
        menu = Menu.objects.all()
        category = Category.objects.all()
        form = AdressForm(request.POST)
        asdress = Adress.objects.filter(user=request.user)
        city_id = request.POST.get('city')
        city_etrap_id = request.POST.get('city_etrap')
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            adress = form.cleaned_data['adress']
            cities = City.objects.get(id=city_id)
            city_etrap = Etrap.objects.get(id=city_etrap_id)
            reg = Adress(user=user,name=name,last_name=last_name,city=cities,city_etrap=city_etrap,adress=adress).save()
            return redirect('checkout')
        else:
            messages.error(request,'Nädogry maglumat')
        cart = Cart.objects.filter(user=request.user)
        if cart:
            return render(request,'adress.html',locals())
        else:
            return redirect('/')
    
def get_cities(request):
    city_id = request.GET.get('city_id')
    city_etrap = Etrap.objects.filter(city_id=city_id)
    city_etrap_data = [{'id': etrap.id, 'name': etrap.name} for etrap in city_etrap]
    return JsonResponse({'cities': city_etrap_data})

def CheckOut(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    add = Adress.objects.filter(user=user).order_by('time')
    for adrs in add:
        adrs = adrs.city_etrap.toleg
        print(adrs)
    if request.method == "POST":
        adres = Adress.objects.filter(user=user).order_by('-time')
        for a in adres:
            adr = "Alyjy: " + str(a.user) + "\nSaher: " + str(a.city) + "\netraby/sahercesi: " + str(a.city_etrap) + "\nSalgysy: " + str(a.adress)
        payment_choice = request.POST.get('payment_choices')
        jemi = 0
        for p in cart:
            value = p.quantity * p.product.price
            jemi += value
        totalamount = jemi + adrs
        for i in cart:
            order = Order(
                user=user,
                product=i.product.productName,
                productBrand=i.product.brand.name,
                productCode=i.product.productCode,
                productDesc=i.product.description,
                productImage=i.product.image.url,
                price=i.product.price,
                quantity=i.quantity,
                adress=adr,
                total=totalamount,
                payment_choices=payment_choice
            )
            order.save()
        cart.delete()
        return redirect('/')
    jemi = 0
    for p in cart:
        value = p.quantity * p.product.price
        jemi += value
    totalamount = jemi + adrs
    form = StatusPayment()
    if add and cart:
        return render(request, 'checkout.html', locals())
    else:
        return redirect('adress')

def order_page(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        user = request.user
        order = Order.objects.filter(user=user)
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
        return render(request,"order.html",locals())
    else:
        return redirect("login")
    
def help_page(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    help = Help.objects.all()
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
    return render(request,"help.html",locals())

def aboutus_page(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
    return render(request,"aboutus.html",locals())

def cargofee_page(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    abous = AboutUs.objects.all()
    city_etrap = Etrap.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
    return render(request,"cargofee.html",locals())

def exchange_page(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    ExCondition = ExchangeCondition.objects.all()
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
    return render(request,"exchange.html",locals())

def contacts(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    abous = AboutUs.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
    if request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        message = request.POST.get('contact_message')
        if name != '' and last_name != '' and message != '':
            Contact(name=name,lastName=last_name,message=message).save()
            messages.success(request,'Üstünlikli! Habar uradyldy!')
        else:
            messages.error(request,'Maglumatlary dolduryň')
    return render(request,"contacts.html",locals())

def search_results(request):
    if request:
        product = request.POST.get('product')
        spro = Product.objects.filter(productName__icontains=product) | Product.objects.filter(brand__name__icontains=product) | Product.objects.filter(description__icontains=product)
        sbrand = Brand.objects.filter(name__icontains=product)
        if len(product) > 0 and len(spro) > 0:
            data = []
            for pros in spro:
                item = {
                    'id':pros.id,
                    'name':pros.productName,
                    'brand':pros.brand.name,
                    'image':str(pros.image.url)
                }
                data.append(item)
            res = data
        else:
            res = 'Gozleginiz ucin netije yok ...'
        return JsonResponse({'data': res})
    return JsonResponse({})

def search_results_brand(request,id):
    if request:
        product = request.POST.get('product')
        brand = request.POST.get('brand')
        spro = Product.objects.filter(Q(productName__icontains=product) & Q(brand__name__icontains=brand))
        sbrand = Brand.objects.filter(name__icontains=brand)
        if len(product) > 0 and len(spro) > 0:
            data = []
            for pros in spro:
                item = {
                    'id':pros.id,
                    'name':pros.productName,
                    'brand':pros.brand.name,
                    'image':str(pros.image.url)
                }
                data.append(item)
            res = data
        else:
            res = 'Gozleginiz ucin netije yok ...'
        return JsonResponse({'data': res})
    return JsonResponse({})


def filter_product(request,categoryId,categoryName):
    brands = request.GET.getlist('brand[]')
    allProduct = Product.objects.all().order_by('-id').distinct() and Product.objects.filter(Q(category_id=categoryId) & Q(status=True)).order_by('-date')
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
        added_to_cart_product_ids = cart.values_list('product__id', flat=True)
        added_to_wishlist_product_ids = wishlist.values_list('product__id', flat=True)
    # sort_option = request.GET.get('selectedSort', '')
    # if sort_option == 'arzandan_gymmada':
    #     allProduct = allProduct.order_by('price')
    # elif sort_option == 'gymmatdan_arzana':
    #     allProduct = allProduct.order_by('-price')
    # else:
    #     allProduct = allProduct.all()
    minPrice = int(request.GET.get('minPrice', 0))
    maxPrice = int(request.GET.get('maxPrice', float('inf')))
    if maxPrice == 0:
        allProduct = allProduct.order_by('-date')
    if  maxPrice > 0:
        allProduct = allProduct.filter(price__gte=minPrice, price__lte=maxPrice)
    if len(brands) > 0:
        allProduct = allProduct.filter(brand__id__in=brands).distinct()
    if request.user.is_authenticated:
        t=render_to_string('filteredProductsMenu.html',{'data':allProduct,'added_to_cart_product_ids':added_to_cart_product_ids,'added_to_wishlist_product_ids':added_to_wishlist_product_ids,'wishlist':wishlist,'cart':cart})
    else:
        t=render_to_string('filteredProductsMenu.html',{'data':allProduct})
    return JsonResponse({'data':t})

def filter_product_menu(request,id,menuName):
    brands = request.GET.getlist('brand[]')
    allProduct = Product.objects.all().order_by('-id').distinct() and Product.objects.filter(Q(category__menu__id=id) & Q(status=True)).order_by('-date')
    menu = Menu.objects.get(id=id)
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
        added_to_cart_product_ids = cart.values_list('product__id', flat=True)
        added_to_wishlist_product_ids = wishlist.values_list('product__id', flat=True)
    sort_option = request.GET.get('sort','')
    if sort_option == 'arzandan_gymmada':
        allProduct = allProduct.order_by('price')
    elif sort_option == 'gymmatdan_arzana':
        allProduct = allProduct.order_by('-price')
    else:
        allProduct = allProduct.filter(Q(category__menu__id=id) & Q(status=True)).order_by('-date')
    minPrice = int(request.GET.get('minPrice', 0))
    maxPrice = int(request.GET.get('maxPrice', float('inf')))
    if maxPrice == 0:
        allProduct = allProduct.order_by('-date')
    if  maxPrice > 0:
        allProduct = allProduct.filter(price__gte=minPrice, price__lte=maxPrice)
    if len(brands) > 0:
        allProduct = allProduct.filter(brand__id__in=brands).distinct()
    if request.user.is_authenticated:
        t=render_to_string('filteredProductsMenu.html',{'data':allProduct,'added_to_cart_product_ids':added_to_cart_product_ids,'added_to_wishlist_product_ids':added_to_wishlist_product_ids,'wishlist':wishlist,'cart':cart})
    else:
        t=render_to_string('filteredProductsMenu.html',{'data':allProduct})
    return JsonResponse({'data':t})

def filter_product_brand(request,id,brandName):
    brands = request.GET.getlist('brand[]')
    allProduct = Product.objects.all().order_by('-id').distinct() and Product.objects.filter(Q(brand__id=id) & Q(status=True)).order_by('-date')
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
        added_to_cart_product_ids = cart.values_list('product__id', flat=True)
        added_to_wishlist_product_ids = wishlist.values_list('product__id', flat=True)
    sort_option = request.GET.get('sort','')
    if sort_option in 'arzandan_gymmada':
        allProduct = allProduct.order_by('price')
    elif sort_option in 'gymmatdan_arzana':
        allProduct = allProduct.order_by('-price')
    else:
        allProduct = allProduct.all()
    minPrice = int(request.GET.get('minPrice', 0))
    maxPrice = int(request.GET.get('maxPrice', float('inf')))
    if maxPrice == 0:
        allProduct = allProduct.order_by('-date')
    if  maxPrice > 0:
        allProduct = allProduct.filter(price__gte=minPrice, price__lte=maxPrice)
    if request.user.is_authenticated:
        t=render_to_string('filteredProductsMenu.html',{'data':allProduct,'added_to_cart_product_ids':added_to_cart_product_ids,'added_to_wishlist_product_ids':added_to_wishlist_product_ids,'wishlist':wishlist,'cart':cart})
    else:
        t=render_to_string('filteredProductsMenu.html',{'data':allProduct})
    return JsonResponse({'data':t})

def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        user = request.user
        Cart(user=user,product=product).save()
        messages.success(request,product.brand.name+" "+product.productName+' sebediňize goşuldy!')
        return redirect('/cart')
    else:
        return redirect('/login')

def show_cart(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    banner = Banner.objects.all()
    product = Product.objects.filter(status=True)
    brand = Brand.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount += value
        totalamount = amount
        return render(request,'cart.html',locals())
    else:
        return redirect('/login')

def wishlist(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    banner = Banner.objects.all()
    product = Product.objects.filter(status=True)
    brand = Brand.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
        return render(request,'wishlist.html',locals())
    else:
        return redirect('/login')

def plus_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount += value
        totalamount = amount
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        if c.quantity > 0:
            c.save()
        else:
            c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount += value
        totalamount = amount
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.price
            amount += value
        totalamount = amount
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        messages.success(request,c.product.productName+" sebediňizden aýryldy!")
        return JsonResponse(data)


def plus_wishlist(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            prod_id = request.GET['prod_id']
            product = Product.objects.get(id=prod_id)
            user = request.user
            Wishlist(user=user,product=product).save()
            data = {
                'message':'{{product.productName}} halananlaryňyza goşuldy!',
            }
            messages.success(request,product.productName+' halananlaryňyza goşuldy!')
            return JsonResponse(data)
    else:
        return redirect('login')
    
def minus_wishlist(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            prod_id = request.GET['prod_id']
            product = Product.objects.get(id=prod_id)
            user = request.user
            Wishlist.objects.filter(user=user,product=product).delete()
            data = {
                'message':'{{product.productName}} halananlaryňyzdan aýryldy!',
            }
            messages.success(request,product.productName+' halananlaryňyzdan aýryldy!')
            return JsonResponse(data)
    else:
        return redirect('login')