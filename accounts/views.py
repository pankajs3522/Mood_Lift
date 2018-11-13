from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'accounts/homepage.html', {})



def main_page_view(request):
    return render(request, 'accounts/main_page.html', {})
