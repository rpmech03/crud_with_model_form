from django.shortcuts import render

# relative import of forms
from .models import Blog
from .forms import BlogForm
from django.shortcuts import (get_object_or_404,
							render,
							HttpResponseRedirect)


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = BlogForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)



def list_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = Blog.objects.all()
		
	return render(request, "list_view.html", context)

# pass id attribute from urls
def detail_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["data"] = Blog.objects.get(id = id)
		
	return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):

	context ={}

	# fetch the object related to passed id
	obj = get_object_or_404(Blog, id = id)

	# pass the object as instance in form
	form = BlogForm(request.POST or None, instance = obj)

	# save the data from the form and
	# redirect to detail_view
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)

	# add form dictionary to context
	context["form"] = form

	return render(request, "update_view.html", context)



# delete view for details
def delete_view(request, id):
	
	context ={}

	# fetch the object related to passed id
	obj = get_object_or_404(Blog, id = id)


	if request.method =="POST":
		# delete object
		obj.delete()
		# after deleting redirect to
		# home page
		return HttpResponseRedirect("/")

	return render(request, "delete_view.html", context)




