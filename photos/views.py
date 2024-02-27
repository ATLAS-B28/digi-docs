#import os
#from django.shortcuts import render, redirect
#from .models import Category, Photo
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
#from .forms import CustomUserCreationForm
#from django.http import HttpResponse
import os
from django.shortcuts import render ,redirect
from .models import Category, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.http import HttpResponse
# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('gallery')

    context = {'form': form, 'page': page}
    return render(request, 'photos/login_register.html', context)




@login_required(login_url='login')
def gallery(request):
    user = request.user
    photocategory = request.GET.get('photocategory')
    if photocategory == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(category__name=photocategory, doccategory__user=user)

    photocategories = Category.objects.filter(user=user)
    context = {'photos': photos, 'photocategories': photocategories}
    return render(request, 'photos/gallery.html',context)


@login_required(login_url='login')
def displayall(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    return render(request, 'photos/displayall.html', {'photos': photos, 'categories': categories})

@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

@login_required(login_url='login')
def deletePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    file_path = photo.image.path
    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect('gallery')

@login_required(login_url='login')
def downloadPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    file_path = photo.image.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

@login_required(login_url='login')
def about(request):
    return render(request, 'photos/about.html')