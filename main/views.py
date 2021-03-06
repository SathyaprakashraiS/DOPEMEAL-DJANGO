from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Paleo
from .models import Vegetarian
from .models import Food
from .models import Vegan
from .models import Ketogenic
from .models import Mediterranean
from .models import review
from .models import drop
from .models import foodrequest
from .models import shopper
from .models import Book
from .forms import ContactForm
from itertools import chain
import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser


def comment(request):
	obj = review.objects.all()
	return render(request,"review.html",{'obj':obj})


def add_comment(request):
	p = request.GET['head']
	c = request.GET['review']
	review.objects.create(name=p,comment=c)
	return HttpResponseRedirect("/")

def food_request(request):
	p = request.GET['foodname']
	foodrequest.objects.create(foodname=p)
	return HttpResponseRedirect("/")



def basic(request):
	return render(request,"basic.html")

def result(request):
	return render(request,"calory.html",{})

def callcalcal(request):
	return render(request,"calcal.html",{})

def test(request):
	return render(request,"dropdown.html",{})

def okay(request):
#	if request.method =='POST':
#		form=YourForm(request.POST)
#	if form.is_valid():
#		answer=form.cleaned_data['value']
	banswer=request.GET['breakfast']
	lanswer=request.GET['lunch']
	sanswer=request.GET['snack']
	danswer=request.GET['dinne']
	return render(request,"ama.html",{'banswer':banswer,'lanswer':lanswer,'sanswer':sanswer,'danswer':danswer})


def fo(request):
	obj = Food.objects.all()
	pal=Paleo.objects.all()
	veg=Vegetarian.objects.all()
	vag=Vegan.objects.all()
	ket=Ketogenic.objects.all()
	med=Mediterranean.objects.all()
	return render(request,"fo.html",{'obj':obj,'pal':pal,'veg':veg,'vag':vag,'ket':ket,'med':med})


def pybot(request):
    query = request.GET.get('query')

    
    try:
        client = wolframalpha.Client("<--Your API key-->")
        res = client.query(query)
        ans = next(res.results).text
        return render(request,"pybot.html", {'ans': ans, 'query': query})

            
    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request,"pybot.html", {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request,"pybot.html", {'ans': ans, 'query': query})


def schemeselection(request):
	h=float(request.GET['height'])
	w=float(request.GET['weight'])
	h=h/100
	b=w/(h*h)
	m=int(request.GET['meal'])
	c=int(request.GET['cals'])
	finder=int(request.GET['choices'])
	banswer=request.GET['breakfast']
	lanswer=request.GET['lunch']
	sanswer=request.GET['snack']
	danswer=request.GET['dinne']
	#anyfood=bool(request.post.get(['ANY']))
	#paleofood=bool(request.post.GET(['PALEO']))
	#vegfood=bool(request.post.GET(['VEG']))
	#veganfood=bool(request.GET(['VEGAN']))
	#banswer=request.GET['breakfast']
	#lanswer=request.GET['lunch']
	#sanswer=request.GET['snack']
	#danswer=request.GET['dinne']
	if(m==3 and(c>6900 or c<300)):
		return render(request,"calory.html",{})
	if(m==4 and (c>9200 or c<400)):
		return render(request,"calory.html",{})
	else:
		#return render(request,"findfood.html",{})
		#obj =Food.objects.get(calories=c)
		partedcalo=c/m
		minpartedcalo=partedcalo-(partedcalo/5)
		ofatav=20#16.246
		ufatav=5
		if(finder==1):
			if(b>25):
				if(partedcalo<300):
					obj =Food.objects.all().filter(calories__lte=partedcalo)
					pal=Paleo.objects.all().filter(calories__lte=partedcalo)
					veg=Vegetarian.objects.all().filter(calories__lte=partedcalo)
					vag=Vegan.objects.all().filter(calories__lte=partedcalo)
					ket=Ketogenic.objects.all().filter(calories__lte=partedcalo)
					med=Mediterranean.objects.all().filter(calories__lte=partedcalo)
					result=list(chain(obj,pal,veg,vag,ket,med))
					return render(request,"fooddisplaycheck.html",{'result':result,'pal':pal,'veg':veg,'vag':vag,'ket':ket,'med':med,'meal':m,'c':c,'banswer':banswer,'lanswer':lanswer,'sanswer':sanswer,'danswer':danswer})
					#return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m,'BOOLVALUEPASSED':choice})
				else:
					obj =Food.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					pal=Paleo.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					veg=Vegetarian.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					vag=Vegan.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					ket=Ketogenic.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					med=Mediterranean.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					result=list(chain(obj,pal,veg,vag,ket,med))
					return render(request,"fooddisplaycheck.html",{'obj':result,'pal':pal,'veg':veg,'vag':vag,'ket':ket,'med':med,'meal':m,'banswer':banswer,'lanswer':lanswer,'sanswer':sanswer,'danswer':danswer})
			if(b<18.5):
				if(partedcalo<300):
					obj =Food.objects.all().filter(calories__lte=partedcalo)
					pal=Paleo.objects.all().filter(calories__lte=partedcalo)
					veg=Vegetarian.objects.all().filter(calories__lte=partedcalo)
					vag=Vegan.objects.all().filter(calories__lte=partedcalo)
					ket=Ketogenic.objects.all().filter(calories__lte=partedcalo)
					med=Mediterranean.objects.all().filter(calories__lte=partedcalo)
					result=list(chain(obj,pal,veg,vag,ket,med))
					return render(request,"fooddisplaycheck.html",{'obj':result,'pal':pal,'veg':veg,'vag':vag,'ket':ket,'med':med,'meal':m,'banswer':banswer,'lanswer':lanswer,'sanswer':sanswer,'danswer':danswer})
				else:
					obj =Food.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					pal=Paleo.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					veg=Vegetarian.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					vag=Vegan.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav).filter(calories__lte=partedcalo,fat__gte=ufatav).filter(calories__lte=partedcalo,fat__gte=ufatav)
					ket=Ketogenic.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav).filter(calories__lte=partedcalo,fat__gte=ufatav)
					med=Mediterranean.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					result=list(chain(obj,pal,veg,vag,ket,med))
					return render(request,"fooddisplaycheck.html",{'obj':result,'pal':pal,'veg':veg,'vag':vag,'ket':ket,'med':med,'meal':m,'banswer':banswer,'lanswer':lanswer,'sanswer':sanswer,'danswer':danswer})
			if(b>=18.5 and b<=25):
				obj =Food.objects.all().filter(calories__lte=partedcalo)
				pal=Paleo.objects.all().filter(calories__lte=partedcalo)
				veg=Vegetarian.objects.all().filter(calories__lte=partedcalo)
				vag=Vegan.objects.all().filter(calories__lte=partedcalo)
				ket=Ketogenic.objects.all().filter(calories__lte=partedcalo)
				med=Mediterranean.objects.all().filter(calories__lte=partedcalo)
				result=list(chain(obj,pal,veg,vag,ket,med))
				return render(request,"fooddisplaycheck.html",{'obj':result,'pal':pal,'veg':veg,'vag':vag,'ket':ket,'med':med,'meal':m,'banswer':banswer,'lanswer':lanswer,'sanswer':sanswer,'danswer':danswer})
	
		if(finder==2):
			if(b>25):
				if(partedcalo<300):
					obj =Paleo.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Paleo.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b<18.5):
				if(partedcalo<300):
					obj =Paleo.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Paleo.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b>=18.5 and b<=25):
				obj =Paleo.objects.all().filter(calories__lte=partedcalo)
				return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})

		if(finder==3):
			if(b>25):
				if(partedcalo<300):
					obj =Vegetarian.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Vegetarian.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b<18.5):
				if(partedcalo<300):
					obj =Vegetarian.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Vegetarian.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b>=18.5 and b<=25):
				obj =Vegetarian.objects.all().filter(calories__lte=partedcalo)
				return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
	#	if(b>25):
	#		obj =Vegetarian.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
	#		return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
	#	if(b<18.5):
	#		obj =Vegetarian.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
	#		return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
	#	if(b>=18.5 and b<=25):
	#		obj =Vegetarian.objects.all().filter(calories__lte=partedcalo)
	#		return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})

#from .models import Vegan
		if(finder==4):
			if(b>25):
				if(partedcalo<300):
					obj =Vegan.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Vegan.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b<18.5):
				if(partedcalo<300):
					obj =Vegan.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Vegan.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b>=18.5 and b<=25):
				obj =Vegan.objects.all().filter(calories__lte=partedcalo)
				return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})


		if(finder==5):
			if(b>25):
				if(partedcalo<300):
					obj =Ketogenic.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Ketogenic.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b<18.5):
				if(partedcalo<300):
					obj =Ketogenic.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Ketogenic.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b>=18.5 and b<=25):
				obj =Ketogenic.objects.all().filter(calories__lte=partedcalo)
				return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})

		if(finder==6):
			if(b>25):
				if(partedcalo<300):
					obj =Mediterranean.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Mediterranean.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b<18.5):
				if(partedcalo<300):
					obj =Mediterranean.objects.all().filter(calories__lte=partedcalo)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
				else:
					obj =Mediterranean.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
					return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
			if(b>=18.5 and b<=25):
				obj =Mediterranean.objects.all().filter(calories__lte=partedcalo)
				return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
        
		if(finder>=7 or finder==0):
			return render(request,"calory.html",{})
	#	if(b>25):
	#		obj =Vegan.objects.all().filter(calories__lte=partedcalo,fat__lte=ofatav)
	#		return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
	#	if(b<18.5):
	#		obj =Vegan.objects.all().filter(calories__lte=partedcalo,fat__gte=ufatav)
	#		return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})
	#	if(b>=18.5 and b<=25):
	#		obj =Vegan.objects.all().filter(calories__lte=partedcalo)
	#		return render(request,"fooddisplaycheck.html",{'obj':obj,'meal':m})

def calcal(request):
	n=request.GET['Foodname'];
	n=n.upper()
	#obj =Food.objects.all().filter(name=n)
	obj =Food.objects.all().filter(name=n)
	pal=Paleo.objects.all().filter(name=n)
	veg=Vegetarian.objects.all().filter(name=n)
	vag=Vegan.objects.all().filter(name=n)
	ket=Ketogenic.objects.all().filter(name=n)
	med=Mediterranean.objects.all().filter(name=n)
	if((obj.exists())):
		obj =Food.objects.all().filter(name=n)
		return render(request,"calcalculated.html",{'obj':obj,'n':n})
	if((pal.exists())):
		pal=Paleo.objects.all().filter(name=n)
		return render(request,"calcalculated.html",{'obj':pal,'n':n})
	if((veg.exists())):
		veg=Vegetarian.objects.all().filter(name=n)
		return render(request,"calcalculated.html",{'obj':veg,'n':n})
	if((vag.exists())):
		vag=Vegan.objects.all().filter(name=n)
		return render(request,"calcalculated.html",{'obj':vag,'n':n})
	if((ket.exists())):
		ket=Ketogenic.objects.all().filter(name=n)
		return render(request,"calcalculated.html",{'obj':ket,'n':n})
	if((med.exists())):
		med=Mediterranean.objects.all().filter(name=n)
		return render(request,"calcalculated.html",{'obj':med,'n':n})
	else:
		#obj ="ERROR"
		return render(request,"calcalculatednone.html",)
def aboutus(request):
	return render(request,"aboutus.html")
def testpage(request):
	return render(request,"newtest.html")
def dopestop(request):
	item=shopper.objects.all()
	return render(request,"dopestop.html",{'item':item})
def book(request):
	obj=Book.objects.all()
	return render(request,"book.html",{'obj':obj})
#def contactus(request):
#	return render(request,"contactus.html")
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saveconfirmed = form.instance
            return render(request, 'contactus.html', {'form': form,'saveconfirmed':saveconfirmed})
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})