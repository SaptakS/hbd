from django.shortcuts import render, redirect


def main_view(request):
    """
    This is the home.
    """
    template = 'index.html'

    return render(request, template, {
        'message': 'Hello World'
    })

def index(request):
    """redirect to main view
    """
    return redirect('main_view')