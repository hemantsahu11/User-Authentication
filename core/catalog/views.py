from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required     # login_required decorator for login authentication
from django.contrib.auth.mixins import LoginRequiredMixin     # for class based views we have to pass this class / inherit LoginRequiredMixin class
from django.contrib.auth.forms import UserCreationForm        # model form for User class

# Create your views here.


def home(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()  # search for it what it is used for
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avail': num_instances_avail
    }
    return render(request, 'catalog/index.html', context=context)


class BookCreate(LoginRequiredMixin, CreateView):   # by using class based views by default template will be available for model Book
    template_name = "catalog/book_form.html"
    model = Book
    fields = '__all__'


class BookDetail(DetailView):
    template_name = "catalog/book_detail.html"
    model = Book


@login_required      # login required decorator same as available in flask this will wrap the function that only authenticated users can only use this
def my_view(request):
    return render(request, 'catalog/my_view.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class CheckOutByUserView(LoginRequiredMixin, ListView):
    # List of Book instances but we will filter based off current logged in user
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower = self.request.user).all()







