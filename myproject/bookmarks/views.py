from django.shortcuts import render

# Create your views here.

def index(request):
	context = {}
	return render(request, 'index.html', context)

def tag(request, tag_name):
	context = {
		'tag': tag_name
	}
	return render(request, 'tag.html', context)

