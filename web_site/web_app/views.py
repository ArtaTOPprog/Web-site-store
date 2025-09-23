from django.shortcuts import render, HttpResponseRedirect, redirect
from web_app.models import Category, Product, CartItem, Order, Basket
from web_app.forms import UserRegistrationForm, UserLoginForm, UserProfileFrom
from django.http import HttpRequest
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main.html')

def product_list(request, category_id=None):
    categories = Category.objects.all()
    context: dict[str,any] = {'categories':categories}
    if category_id:
        context.update({'products':Product.objects.filter(category_id=category_id)})
    else:
        context.update({'products':Product.objects.all()})
    return render(request, 'product.html', context)


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request: HttpRequest):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username,password = password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user_section'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context) 


@login_required
def im_user(request: HttpRequest):
    if request.method == 'POST':
        form = UserProfileFrom(data=request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('user_section'))
    else:
        form = UserProfileFrom(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'User.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


@login_required
def basket(request):
    basket = Basket.objects.filter(user=request.user)
    total_count = sum(i.count for i in basket)
    total_summ = sum(i.Summ() for i in basket)
    context = {
        'baskets': basket,
        'total_count': total_count,
        'total_summ': total_summ,
    }
    return render(request, 'basket.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product, count=1)
        basket.save()
        return HttpResponseRedirect(reverse('basket'))
    else:
        basket = baskets.first()
        basket.count += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))