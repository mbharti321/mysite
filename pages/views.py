from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html", {})
	# return HttpResponse("<h1> Hello World</h1>")

def contact_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Contact page</h1>")
	return render(request, "contact.html",{})

def about_view(request, *args, **kwargs):
	# return HttpResponse("<h1>About page</h1>")
	return render(request, "about.html",{})

def social_view(request, *args, **kwargs):
	# return HttpResponse("<h1>social page</h1>")
	return render(request, "social.html",{})