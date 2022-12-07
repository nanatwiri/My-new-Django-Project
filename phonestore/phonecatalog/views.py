from django.shortcuts import render

# Create your views here.


def index(request):
    return Httpresponse("""hello class this is our ohone catalog landing page""")
