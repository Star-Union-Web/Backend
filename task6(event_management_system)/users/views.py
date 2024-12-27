from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

# Create your views here.

def user_reg(request):
    user_reg_form = UserCreationForm()
    if request.method == 'POST':
        user_reg_form = UserCreationForm(request.POST)
        if user_reg_form.is_valid():
            print(request.POST)
            print(request.POST.get('user-role'))
            user_reg_form.save()
            x = User.objects.all().filter(username=request.POST.get('username'))[0]
            if request.POST.get('user-role') == 'on':
                organizer_group = Group.objects.get(name='organizer')
                x.groups.add(organizer_group)
            else:
                reqular_group = Group.objects.get(name='regular')
                x.groups.add(reqular_group)

           
            return redirect('login')
        else:
            #user_reg_form = UserCreationForm()
            #return render(request, 'register.html', {'form': user_reg_form})
            pass

    return render(request, 'register.html', {'form': user_reg_form})


