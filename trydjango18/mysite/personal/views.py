from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')
def contact(request):
	return render(request, 'personal/basic.html',{ 'content':['if u lyk me email me','krutam@gmail.com'] })

