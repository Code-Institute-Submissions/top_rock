from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """View to return teh bag an its contents """

    return render(request, 'bag/bag.html')
