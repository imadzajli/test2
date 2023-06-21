from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def check_email(e):
    list_e=[]
    list_e.extend(e)
    d={'@':0,'.':0,' ':0}
    for i in list_e:
        if i=='@':
            d['@']+=1
        if i=='.':
            d['.']+=1
        if i==' ':
            d[' ']+=1
    if d['@']==1 and d['.']==1 and d[' ']==0:
        return True
    else:
        return False
def create_acc(request):
    fi=request.GET['firstname']
    la=request.GET['lastname']
    us=request.GET['username']
    em=request.GET['email']
    pas=request.GET['password']
    rpas=request.GET['rpassword']
    


