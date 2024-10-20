from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Tour
from django.contrib.auth import login, logout, authenticate 
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from .forms import TourForm
from django.urls import reverse_lazy
# Create your views here.


def home_page(request):
    categories = Category.objects.all()
    tours = Tour.objects.all().order_by('-created_at')[:4] # Последние четыре вакансии

    context = {
        "categories": categories, 
        "tours": tours,
    }

    return render(request, './home.html', context=context)

def tours_page(request):
    tours = Tour.objects.all().order_by('-created_at')

    context = {
        "tours": tours,
    }

    return render(request, './tours.html', context=context)

def categories_page(request):
    categories = Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(request, './categories.html', context=context)


def tour_detail_page(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    tours = Tour.objects.all().order_by('-created_at')[:4]
    context = {'tour': tour, 'tours': tours}
    return render(request, './tour-detail.html', context)


def tours_by_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    tours = Tour.objects.filter(category=category)
    context = {
        'category': category,
        'tours': tours
    }

    return render(request, './tours-by-category.html', context)


def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "./sign-up.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "./login.html", context)


def logout_action(request):
    logout(request)
    return redirect('home_page')

class TourForms(CreateView):
    form_class = TourForm
    template_name = 'create_tour.html'
    success_url = reverse_lazy('home_page')


    # <a href="{% url 'tours_by_category_page' slug=c.slug %}"