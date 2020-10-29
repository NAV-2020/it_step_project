from django.http import HttpResponse


def home(request, *args, **kwargs) -> HttpResponse:
    """Home view"""
    # TODO: Resume from here
    return HttpResponse("<i><h1>Home page</h1></i>")

def about(request, *args, **kwargs) -> HttpResponse:
    """About view"""
    return HttpResponse("About page")
