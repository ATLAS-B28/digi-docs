import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from photos.forms import CustomUserCreationForm
from django.http import HttpResponse
from .models import Document, DocCategory
# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('document_list')

    return render(request, 'documents/login_register.html', {'page': page})


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
                return redirect('document_list')

    context = {'form': form, 'page': page}
    return render(request, 'documents/login_register.html', context)


@login_required(login_url='login')
def displayall(request):
    documents = Document.objects.all()
    doccategories = DocCategory.objects.all()

    return render(request, 'documents/displayall.html', {'documents': documents, 'doccategories': doccategories})

@login_required(login_url='login')
def document_list(request):
    user = request.user
    doccategory = request.GET.get('doccategory')
    if doccategory == None:
        documents = Document.objects.filter(doccategory__user=user)
    else:
        documents = Document.objects.filter(doccategory__name=doccategory, doccategory__user=user)

    doccategories = DocCategory.objects.filter(user=user)
    context = {'documents': documents, 'doccategories': doccategories}
    return render(request, 'documents/document_list.html',context)

@login_required(login_url='login')
def document_view(request, pk):
    document = Document.objects.get(id=pk)
    return render(request, 'documents/document_view.html', {'document': document})

@login_required(login_url='login')
def add_doc(request):
    user = request.user
    categories = user.category_set.all()
    if request.method == 'POST':
        data = request.POST
        docuements = request.FILES.getlist('files')
        if data['doccategory'] != 'none':
            category = DocCategory.objects.get(id=data['doccategory'])
        elif data['doccategory_new'] != '':
            category, created = DocCategory.objects.get_or_create(
                user=user,
                name=data['doccategory_new'])
        else:
            category = None

        for doc in docuements:
            document = Document.objects.create(
                doccategory=category,
                description=data['description'],
                file= doc
            )
        
        return redirect('document_list')
    
    context = {'doccategories': categories}
    return render(request, 'documents/add_doc.html', context)

@login_required(login_url='login')
def downloadDocument(request, pk):
    document = Document.objects.get(id=pk)
    file_path = document.file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        
@login_required(login_url='login')
def deleteDocument(request, pk):
    document = Document.objects.get(id=pk)
    document.delete()
    file_path = document.file.path
    if os.path.exists(file_path):
        os.remove(file_path)
        
    return redirect('document_list')

@login_required(login_url='login')
def about(request): 
    return render(request, 'documents/about.html')