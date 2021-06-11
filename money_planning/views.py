from django.shortcuts import render
from .models import Users,Transactions
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import UsersForm, TransactionsForm

def index(request):
    list_of_users = Users.objects.all()
    template = 'index.html'
    context={

    'list_of_users' : list_of_users
    }
    return render(request, template, context)

# show all users
def users(request):
    list_of_users = Users.objects.all()
    template = 'Users.html'
    context={
    'list_of_users' : list_of_users
    }
    return render(request, template, context)

# show user
def user_view(request, pk):
    get_user = Users.objects.get(id=pk)
    template = 'user_view.html'
    context={
    'list_of_users' : get_user
    }
    return render(request, template, context)

#create new user
def create_user(request):
    template = 'create_user.html'
    context={
          'form':UsersForm()
    }
    if request.method == "POST":
        user = UsersForm(request.POST)
        if user.is_valid():
            user.save()
        else:
            return HttpResponse("Invalid data")
    else:
        return render(request, template, context)

    return render(request, template, context)


# edit information about user
def edit_user(request, pk):
    try:
        person = Users.objects.get(id=pk)
        template = 'edit_user.html'
        context={
              'form':UsersForm(instance=person)
        }
        if request.method == "POST":
            user = UsersForm(request.POST, instance=person)
            if user.is_valid():
                user.save()
                return render(request, template, context)
            else:
                return HttpResponse("Invalid data")
        else:
            return render(request, template, context)
    except Users.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")

# delete user in database
def delete_user(request, pk):
    try:
        user =  Users.objects.get(id=pk)
        user.delete()
        return HttpResponseRedirect("/users")
    except Users.DoesNotExist:
        return HttpResponseNotFound("<h2> User not found</h2>")

# show all transactions
def transactions(request):
    list_of_transact= Transactions.objects.all()
    template = 'Transactions.html'
    context={
    'list_of_transact' : list_of_transact
    }
    return render(request, template, context)

# show transaction
def transact_view(request, pk):
    get_transact = Transactions.objects.get(id=pk)
    template = 'transact_view.html'
    context={
    'list_of_users' : get_transact
    }
    return render(request, template, context)

# create new transaction
def create_transact(request):
    template = 'create_transact.html'
    context={
          'form':TransactionsForm()
    }
    if request.method == "POST":
        transact = TransactionsForm(request.POST)
        if transact.is_valid():
            transact.save()
        else:
            return HttpResponse("Invalid data")
    else:
        return render(request, template, context)

    return render(request, template, context)

# edit information about transaction
def edit_transact(request, pk):
    try:
        trans = Transactions.objects.get(id=pk)
        template = 'edit_transact.html'
        context={
              'form':TransactionsForm(instance=trans)
        }
        if request.method == "POST":
            transact = TransactionsForm(request.POST, instance=trans)
            if transact.is_valid():
                transact.save()
                return render(request, template, context)
            else:
                return HttpResponse("Invalid data")
        else:
            return render(request, template, context)
    except Users.DoesNotExist:
        return HttpResponseNotFound("<h2>Transactions not found</h2>")

# delete transaction in database
def delete_transact(request, pk):
    try:
        transact = Transactions.objects.get(id=pk)
        transact.delete()
        return HttpResponseRedirect("/transactions")
    except Transactions.DoesNotExist:
        return HttpResponseNotFound("<h2>Transaction not found</h2>")
