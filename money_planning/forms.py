from django.forms import ModelForm
from .models import Users,Transactions

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'
