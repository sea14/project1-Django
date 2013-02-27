# Create your views here.
from django.shortcuts import render

def home(request):
	context = {
		'member_count': Member.objects.count(),
	}
	return render(request, "base.html", context)
