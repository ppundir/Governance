from django.http import HttpResponse
from django.shortcuts import render
from forum.models import State, Constituency

#def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
def index(request):
    a = Constituency.objects.all()
    context = {'const_list': a}
    return render(request, 'forum/index.html', context)


def state(request, statecode):	
	b = State.objects.get(id = statecode)
	a = Constituency.objects.filter(state_id=statecode)
	context = {'state_const': a, 'state': b}
	return render(request, 'forum/state.html', context)
