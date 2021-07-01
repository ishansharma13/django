# from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import operator
def home(request):
    return render(request, 'home.html')

def success(request):
    x = request.GET['fulltext']
    c = Counter(x.split())
    key_l = list(c.keys())
    val_l = list(c.values())
    max_val = max(val_l)
    max_k = key_l[val_l.index(max_val)]
    sor = sorted(c.items(),key=operator.itemgetter(1),reverse=True)
    data = {'text':x,'max_text':max_k,'max_count':max_val,'items':sor}
    return render(request, 'success.html',data)
    # return render(request, 'success.html',data)
def about(request):
    return render(request,'about.html')
