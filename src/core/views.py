from django.http import HttpResponse
from django.shortcuts import render

def home(request, *args, **kwargs) -> HttpResponse:
    """Home view"""

    ctx = {
        'messages': ["This is message 1",
                    "This is message 2",
                    "This is message 3",
                    "This is message 4"
        ] 
    }

    return render(request, 'core/index.html', context=ctx)

