""" view for app shop """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from .models import Category, Product
from .forms import UserForm, UserProfileForm
# Create your views here.


def user_login(request):
    """ user login """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("account is disable")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'app/product/login.html', {})


@login_required
def user_logout(request):
    """ user logout """
    logout(request)
    return redirect('/')


def product_list(request, category_slug=None):
    """
    Function used to display a list of products.
    Second parameter category_slug=None use if products are filtered using
    a given category by our users.
     """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'app/product/list.html', context)


def product_detail(request, id, slug):
    """ detail of the product """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'app/product/detail.html', context)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() or profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    # for new model we have to import the new model My regsitration formn
    # post the request the new My Registartion form
    # Render the template depending on the context.
    print("Yahoo")
    context = {'user_form': user_form,
               'profile_form': profile_form, 'registered': registered}
    print("holahhh")
    return render(request, 'app/product/register.html', context)
