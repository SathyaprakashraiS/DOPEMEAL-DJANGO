from django.db import models

# Create your models here.
class Food(models.Model):#anything is Food
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images', default='static/images/DIET3.jpg')

class Paleo(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images',default='static/images/DIET3.jpg')

class Vegetarian(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images' ,default='images/DIET3.jpg')

class Vegan(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images' ,default='static/images/DIET3.jpg')

class Ketogenic(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images', default='static/images/DIET3.jpg')

class Mediterranean(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images', default='static/images/DIET3.jpg')


class review(models.Model):
	name=models.CharField(max_length=30)
	comment=models.CharField(max_length=500)

class foodrequest(models.Model):
	foodname=models.CharField(max_length=30)

class drop(models.Model):
	mealchoice =(
		('light meal','light meal'),
		('medium meal','medium meal'),
		('heavy meal','heavy meal')
		)
	choicename= models.CharField(max_length=120,choices= mealchoice)

class shopper(models.Model):
	productname=models.CharField(max_length=1000)
	productlink=models.CharField(max_length=1000,default="NO LINK AVAILABLE")
	productimage=models.ImageField(upload_to='images', default='images/dlogo.jpeg')
	productprice=models.FloatField(default='0.0')

class Book(models.Model):
	bookname=models.CharField(max_length=100)
	bookauthor=models.CharField(max_length=100)
	booklink=models.CharField(max_length=1000)
	bookimage=models.ImageField(upload_to='images',default='images/dlogo.jpeg')

class Contact(models.Model):
	FIRSTNAME=models.CharField(max_length=100)
	LASTNAME=models.CharField(max_length=100)
	SUBJECT=models.CharField(max_length=1000)