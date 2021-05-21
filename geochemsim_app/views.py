from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def supcrtbl2(request):
    return render(request, 'geochemsim_app/supcrtbl2.html')
