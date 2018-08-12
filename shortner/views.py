"""
This module performs the core functionality here we take the primary key from the table and then
convert it to base 62 then we store that value in our database. Then we will query that value and
append to our own custom link.
"""
#The Libraries to be imported
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Shortify
from math import floor
import string
# Create your views here.
#Our Main Page
def index(request):
    return render(request,'shortner/index.html')
#We arrive here from the shortenURL link which is present in the index.html
def longURL(request):
    if request.method=='POST':
        if request.POST.get('url'):
            #Creating the object
            addValues=Shortify()
            longURLHere=request.POST.get('url')
            addValues.longURL=longURLHere
            #Saving the value
            addValues.save()
            #Getting the primary key
            num=addValues.pk
            shortenedURL=toBase62(num)
            #Updating The Value Here!
            addShortUrl=Shortify.objects.get(pk=addValues.pk)
            addShortUrl.shortURL=shortenedURL
            addShortUrl.save()
            #Adding A Context Here
            args={'longURL':longURLHere,'shortURL':shortenedURL}
            #Going to the same page again.
            return render(request,'shortner/success.html',args)
        else:
            return render(request,'shortner/failure.html')
    else:
        return render(request,'shortner/failure.html')
#Our function to reverse the short URL to the long URL
def redirectExternal(request,id):
    if Shortify.objects.get(shortURL=id):
        value=Shortify.objects.get(shortURL=id)
        longURLToRedirect=value.longURL
        #The below inline function will check that whether the link is absolute url or not if not it converts it to absolute url
        partToCheck=longURLToRedirect[:4]
        print(partToCheck)
        if 'http' != partToCheck:
            listLink=[]
            listLink.append(longURLToRedirect)
            print(listLink)
            listLink.insert(0,'http://')
            print(listLink)
            absoluteURL=''.join(listLink)
            print(absoluteURL)
        else:
            absoluteURL=longURLToRedirect
        return redirect(absoluteURL)
    else:
        return render(request,'shortner/failure.html')
#Our Function to convert from decimal to the base 62
def toBase62(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q=floor(q / b)
        res = base[int(r)] + res
    return res
#Converting back to the decimal base again for the obvious reasons :P
def toBase10(num, b = 62):
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res
