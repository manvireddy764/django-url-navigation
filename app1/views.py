from django.shortcuts import render

# Create your views here.
def first1(request):
    return render(request,'first.html',context={'name':'kanoo','wishes':'noohin'})


def second1(request):
    return render(request,'second.html',context={'name':'manvi','wishes':'noohin'})