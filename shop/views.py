from django.shortcuts import render, redirect

# Create your views here.
from .models import Category, Review, Product
from .forms import ReviewForm, LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout


def index(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()[:4],
        'index_page_status': 'active',
    }
    return render(request, 'shop/index.html', context=context)


def shop(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'shop_page_status': 'active',
        'products_count': Product.objects.count(),
    }

    return render(request, "shop/shop.html", context=context)


def detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'products': Product.objects.filter(category=product.category),
        'form': ReviewForm(),
        'reviews': Review.objects.filter(product=product).order_by('-pk'),
    }

    return render(request, 'shop/detail.html', context=context)


def product_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(category=category),
        'shop_page_status': 'active',
        'products_count': Product.objects.count(),
    }

    return render(request, 'shop/shop.html', context=context)


def review_save(request, product_slug):
    if request.user.is_authenticated:
        product = Product.objects.get(slug=product_slug)
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            messages.success(request, "Your review has been saved!")
            return redirect('detail', product_slug=product_slug)
        else:
            messages.error(request, "Your review has not been saved!")
            return redirect('detail', product_slug=product_slug)
    else:
        messages.info(request, "Login first!!!")
        return redirect('login')


def user_logout(request):
    """This is for logout"""

    logout(request)
    return redirect('login')


def user_login(request):
    """This is for login"""

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successfully!")
            return redirect('index')

        if form.errors:
            messages.error(request, "Check that the fields are correct!")

    form = LoginForm()
    context = {
        'form': form,
        'title': 'Sign in'
    }
    return render(request, 'shop/login.html', context=context)


def user_register(request):
    """This is for sing up"""

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "You can log in by entering your username and password.")
            return redirect('login')

        if form.errors:
            messages.error(request, "Check that the fields are correct!")

    form = RegisterForm()
    context = {
        'form': form,
        'title': 'Sign up'
    }
    return render(request, 'shop/register.html', context=context)
