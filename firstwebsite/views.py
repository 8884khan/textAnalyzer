# Ihave created this File :- Shahbaz Khan
from django.http import HttpResponse
from django.shortcuts import render


# below line is for render
def index(request):
    return render(request, 'index.html')


def analyze(request):

    # Get the text
    djtext = request.GET.get('text', 'default')

    #check box value
    removepunc=request.GET.get('removepunc','off')
    capletter =request.GET.get('capletter','off')
    newlineremover =request.GET.get('newlineremover','off')
    extraspaceremover =request.GET.get('extraspaceremover','off')




    # analyzed=djtext


    # check
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        return render(request,'analyzed.html',params)

    #for capital---------------------------
    elif  (capletter == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': "change to upper case ", 'analyzed_text': analyzed}
        return render(request, 'analyzed.html', params)

# new line remover ---------------------

    elif newlineremover == "on":
        analyzed = ""
        for  char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text

        return render(request, 'analyzed.html', params)


 # space remover ------------------

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyzed.html', params)


    else:
        return HttpResponse("error")