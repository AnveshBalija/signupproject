from django.shortcuts import render
from testapp.forms import SignupForm

# Create your views here.
def signup_view(request):
    sent=False
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            print('Basic validation success')
            print('Name = ',form.cleaned_data['name'])
            print('Password = ',form.cleaned_data['password'])
            print('Email = ',form.cleaned_data['email'])
            sent=True
    return render(request, 'testapp/input.html', {'form':form,'sent':sent})
