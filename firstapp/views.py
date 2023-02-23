from django.shortcuts import render,HttpResponse,redirect
from .models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        bid = request.POST.get("book_id")
        name = request.POST.get("book_name")
        qty = request.POST.get("book_qty")
        price = request.POST.get("book_price")
        author = request.POST.get("book_author")
        is_pub = request.POST.get("book_is_pub")
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False    
        #print(name,qty,price,author,is_pub)
        if not bid:
             Book.objects.create(name=name, qty=qty, price=price, author=author,is_published=is_pub)
        else:
            book_obj = Book.objects.get(id=bid)  
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author 
            book_obj.is_published = is_pub
            book_obj.save()    
        return redirect("home_page")
        #return HttpResponse("Success")
    elif request.method == 'GET':
        #print(request.GET)
        return render(request,"home.html",context={"person_name":"Sanika"})
@login_required        
def show_active_books(request):
    return render(request,"show_books.html",{"books":Book.objects.filter(is_active=True),"active":True})
@login_required
def update_book(request,id):
    book_obj = Book.objects.get(id=id)
    return render(request,"home.html",{"single_book":book_obj})
@login_required
def delete_book(request,pk):
    Book.objects.get(id=pk).delete() 
    return redirect("all_active_books")   
@login_required
def soft_delete_book(request,pk):
     book_obj = Book.objects.get(id=pk)
     book_obj.is_active = False
     book_obj.save()
     return redirect("all_active_books")

@login_required
def show_inactive_books(request):
    return render(request,"show_books.html",{"books":Book.objects.filter(is_active=False),"inactive":True})  


@login_required
def restore_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = True
    book_obj.save()
    return redirect("all_active_books")    

from .forms import BookForm, AddressForm
from django.contrib.auth.forms import UserCreationForm

def book_form(request):
    
    return render(request,"book_form.html",{"form" : UserCreationForm()})


def sibtc(request):
    return render(request,"sibtc.html",{"form" : AddressForm()})    



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    book_list = Book.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator( book_list, 3)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books  = paginator.page(1)
    except EmptyPage:
        books  = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'books': books })

from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

    


class BookCreate(CreateView):
    model = Book
    fields = "__all__"
    success_url = "/cbv-create-book/"


from django.views.generic.list import ListView 
  
class BookRetrieve(ListView):  
    model = Book  
    queryset = Book.objects.filter(is_active=1)

class BookDetail(DetailView) :
    model = Book


class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"
    success_url = "/cbv-create-book/"


class BookDelete(DeleteView):  
    model = Book 
    # here we can specify the URL   
    # to redirect after successful deletion  
    success_url = "/cbv-create-book/"
import csv
def create_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-disposition'] = 'attachment;filename="test_csv"' 
    writer = csv.writer(response)
    writer.writerow(['name','qty','price','author','is_published','is_active'])
       
    books = Book.objects.all().values_list('name','qty','price','author','is_published','is_active')
    for book in books:
        writer.writerow(book) 
    return response   


def upload_csv(request):
    file = request.FILES["csv_file"]
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)   
    lst = []
    for element in reader:
        is_pub = element.get("is_published")
        if is_pub == "TRUE":
            is_pub = True
        else:
            is_pub = False    
        lst.append(Book(name=element.get("name"),qty=element.get("qty"),price=element.get("price"),author=element.get("author"),is_published=is_pub))  
    Book.objects.bulk_create(lst)
    print(lst)
    return HttpResponse("success")