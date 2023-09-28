from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# personal import
from app_data_off.models import Product, Category, UserProduct
from app_data_off.management.commands.constante import list_categories


# Create your views here.

def base(request):
    return render(request, '../templates/base.html')


def termes(request):
    return render(request, 'termes.html')


def index(request):
    form=SearchForm(request.POST)
    context={
        'form': form
    }
    return render(request, 'index.html', context)


def search(request):
    # For method GET data is passed along with url.
    # dict request.GET and q is the key and variable is the value
    # Use GET if:
    # The interaction is more like a question (i.e., it is a safe operation such as a query, read operation, or lookup).
    if request.method == 'GET':
        search=request.GET.get('search')
        if search in list_categories:

            # gets the category in the database which name equals to search and result is
            # assigned to the fk_category variable
            fk_category=Category.objects.get(name=search)

            # get the first product of the category above
            p1=Product.objects.filter(category_id=fk_category.id).first()

            # get all products ordered by nutriscore of the category
            # type Queryset and then SQL generated when affected to variable
            products=fk_category.product_set.all().order_by("nutrition_grade")
            # request.GET contains GET variables and appear in the address bar,e.g http://127.0.0.1:8000/?page=2
            # The .get() is a python method used to return the value of items with a specific key from
            # a dictionary. If nothing is found None is returned.
            page_number=request.GET.get('page')
            # paginator settings
            # Paginator class to split the results of products variable into pages and each page has only 6 products
            paginator=Paginator(products, 6)
            try:
                # returns a Page object and If the page isn’t a number, it returns the first page.
                page_obj=paginator.page(page_number)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                page_obj=paginator.page(1)
            except EmptyPage:
                # If page is out of range
                # Delivery last page of results
                page_obj=paginator.page(paginator.num_pages)

        else:
            products=Product.objects.filter(name__icontains=search).order_by('nutrition_grade')
            p1=Product.objects.filter(name__icontains=search).first()

            paginator=Paginator(products, 6)
            page_number=request.GET.get('page', 1)
            try:
                page_obj=paginator.page(page_number)
            except PageNotAnInteger:
                page_obj=paginator.page(1)
            except EmptyPage:
                page_obj=paginator.page(paginator.num_pages)
        context={
            'products': page_obj,
            'p': p1,
            'paginate': True,
            'list_categories': list_categories,
        }

        return render(request, 'search.html', context)


def detail(request, product_id):
    form=SearchForm(request.POST)
    p=get_object_or_404(Product, id=product_id)
    context={
        'p': p,
        'form': form
    }
    return render(request, 'detail.html', context)


@login_required(login_url='/login/')
def save(request, product_id):
    """ save a product choosed as a substitute . """

    if request.method == 'POST':
        user_id=request.user.id
        user_product=UserProduct.objects.filter(product_id=product_id, user_id=user_id)
        if not user_product.exists():
            UserProduct.objects.create(product_id=product_id, user_id=user_id)
        else:
            return redirect("index")

    # By default, redirect () returns a temporary redirect. All of the above forms accept a permanent parameter which,
    # if set to True, produces a permanent redirect:
    # return redirect('/index', permanent=True)
    return redirect('/favorite', permanent=True)


@login_required(login_url='/login/')
def favorite(request):
    user_id=request.user.id
    fav_products=UserProduct.objects.filter(user_id=user_id)
    if fav_products.exists():
        products=[]
        for fav_product in fav_products:
            product=Product.objects.get(id=fav_product.product_id)
            if product not in products:
                products.append(product)
    else:
        return redirect('/index', permanent=True)

    context={
        'favori': products,
    }
    return render(request, 'favorite.html', context)


@login_required(login_url='/login/')
def remove_favorite(request, pk):
    user_id=request.user.id
    fav_products=UserProduct.objects.filter(user_id=user_id)

    if fav_products.exists():
        remove_fav=fav_products.get(product_id=pk)
        remove_fav.delete()
        return redirect('/favorite/')
    # else:
    return redirect('/index', permanent=True)

