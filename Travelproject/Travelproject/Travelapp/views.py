
from django.shortcuts import render

from.models import states
from.models import ourteam
#
# # Create your views here.
def demo(request):
    obj1=states.objects.all()
    obj2=ourteam.objects.all()
    return render(request,'index.html',{'out1':obj1,'out2':obj2})