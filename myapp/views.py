import json
from myapp.OtherDatabase import GetData
from .models import Product
from django.shortcuts import render
from .serializers import ProductSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def djangodb(request):

    product = Product.objects.all()
    product_data = ProductSerializer(product, many = True)
    serialized_data = json.dumps(product_data.data)

    DataSetDict = {}
    for i,val in enumerate(product):
        DataSetDict[i] = val.name

    DataSetDict = json.dumps(DataSetDict)

    return render(request, 'myapp/index.html', {'data': serialized_data, 'data_set_names' : DataSetDict})

def otherdb(request):
    
    serialized_data, DataSetDict = GetData.GetDataFrame()
    serialized_data, DataSetDict = json.dumps(serialized_data), json.dumps(DataSetDict)

    return render(request, 'myapp/index.html', {'data': serialized_data, 'data_set_names' : DataSetDict})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'