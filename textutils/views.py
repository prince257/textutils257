# i have created this file -prince


from django.http import HttpResponse
from django.shortcuts import  render # for templates bnaane ke liye
# def index1(request): # ek request argument dena he hoga...taaki hmm isse web use kr ske
#     # return HttpResponse("hello prince")
#     return HttpResponse("<h1>prince</h1>")
# # aur view hmee ab http response deta h...return m..isliye hmme Httpresponse chaiye hota h
#
# def about(request): # ek request argument dena he hoga...taaki hmm isse web use kr ske
#     return HttpResponse("about hello prince ")
#
# def notes(request):
#     with open('aishehe.txt') as f:
#         yo=f.read()
#     return HttpResponse(yo)
#
# def sitesname(request):
#     return HttpResponse('''to open <a href="https://timesofindia.indiatimes.com/"> Times Of India</a><br>
#     to open <a href="https://www.youtube.com/"> Youtube</a><br>
#     to open <a href="https://www.myntra.com/"> Myntra</a><br>''')

#ye ab tutes7 chl raha h


def index(request):
    return render(request,'index.html')

# ye render use krte h template bnnane ke liye
    # return HttpResponse("Home")

# def removepunc(request):
#     djtext=(request.GET.get('text','default')) # ye aapko text return karegi..agr text nhi mila to default value le lega
#     print(djtext)
#     return HttpResponse('''remove punc
#      for go to back page click <a href='/'> BACK </a><br>''') # ab back ho jaayega ek page
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse('''new line remove
#     for go to back page click <a href='/'> BACK </a><br>''')
#
# def spaceremove(request):
#     return HttpResponse('''space remover
#      for go to back page click <a href='/'> BACK </a><br>''')
#
# def charcount(request):
#     return HttpResponse('''charcount
#      for go to back page click <a href='/'> BACK </a><br>''')


def analyze(request):
    djtext=(request.POST.get('text','default')) # ye aapko text return karegi..agr text nhi mila to default value le lega
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))
    charcount = (request.POST.get('charcount', 'off'))

    # print(removepunc)
    # print(djtext)
    # check checkbox values

    if removepunc=="on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@$%^*_&'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        # return HttpResponse('''remove punc
        #  for go to back page click <a href='/'> BACK </a><br>''') # ab back ho jaayega ek page
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed


    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove new lines', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtex=analyzed

    if extraspaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed + char
        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed


    if charcount=="on":
        analyzed = ""
        i=0
        for char in djtext:
            i=i+1
        analyzed=i
        params = {'purpose': 'character count', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    if(removepunc!="on" and newlineremover!="on" and charcount!="on" and fullcaps!="on" and extraspaceremover!="on"):
        return HttpResponse("please selesct any operation and try again")

    return render(request,'analyze.html',params)

# post request m hmm..aise cheeze bhejte h jo private ho...jaise ki password
# aur jab hmm get request se data ko bhejte h to...yaani ki url ke form to uski ek max length
# hoti h.....agr jaada data bhej diya to error aa jaayega




