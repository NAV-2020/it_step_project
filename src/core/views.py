from django.http import HttpResponse

# Create your views here.

def home(request, *args, **kwargs) -> HttpResponse:
    """Home view"""

    return HttpResponse("Home page")
