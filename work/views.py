from django.shortcuts import render,redirect
from .forms import rgstudent
from .models import student
# Create your views here.
def reg(request):
	if(request.method=='POST'):
		form=rgstudent(request.POST)
		if form.is_valid():
			form.save()
			form=rgstudent()
	else:
		form=rgstudent()
		data=student.objects.all()
		return render(request,'register.html',{'form':form,'data':data})
		
	data=student.objects.all()	
	return render(request,'register.html',{'form':form,'data':data})
	
def delete(request,id):
	if request.method=='POST':
		pi=student.objects.get(pk=id)
		pi.delete()
	return redirect("/")

def update(request,id):
	if request.method=='POST':
		pi=student.objects.get(pk=id)
		form=rgstudent(request.POST,instance=pi)
		if form.is_valid():
			form.save()
			return redirect("/")
	else:
		pi=student.objects.get(pk=id)
		form=rgstudent(instance=pi)
	return render(request,'update.html',{'id':form})
		