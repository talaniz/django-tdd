from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth import get_user # Added to new_list view
from django.contrib.auth.decorators import login_required # To restrict home_page, new_list and view_list
from django.shortcuts import redirect, render
from django.core.urlresolvers import resolve, reverse # Added for dynamic success_url

from authtools.forms import UserCreationForm # Pass to registration view
from authtools.views import LoginView, LogoutView # Subclassing to customize views from authtools

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import Item, List

@login_required(login_url='/login') # Test that these don't allow access w/o auth
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

@login_required(login_url='/login')
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)      
    return render(request, 'list.html', {'list': list_, 'form': form})

@login_required(login_url='/login')
def new_list(request):
    user = get_user(request)
    if request.method=='POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            list_ = List.objects.create(user=user)
            form.save(for_list=list_)
            return redirect(list_)
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = ItemForm()
        return render(request, 'home.html', {'form': form})

# Default is to redirect to /accounts/profile
class ListLoginView(LoginView):

    def get_queryset(self): # Test that the function redirects correctly
        try:
            queryset = List.objects.get(user_id=self.request.user.id) # Test the queryset
        except ObjectDoesNotExist:
            queryset = None
        return queryset

    def get_success_url(self, *args, **kwargs): # Test that this fucnction works and redirects correctly
        queryset = self.get_queryset()
        if queryset != None:
            success_url = reverse('view_list', args=[queryset.id])
        else:
            success_url = reverse('new_list')
        return success_url
    
class ListLogoutView(LogoutView):

    template_name = 'logout.html' # Test that the logout redirects correctly

def register(request):
    form = UserCreationForm() # Test that an instance of UserCreationForm is used
    if request.method == "POST": # Test post request is handled properly
        form = UserCreationForm(data=request.POST)
        if form.is_valid(): # Test form validation errors
            form.save() # Test that the user is created
            return redirect('login') # Test the login redirect
        else:
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {'form': form})
