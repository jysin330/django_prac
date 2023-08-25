from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # perms = {'name': 'jyoti', 'place': 'india'}
    # return render(request, 'index.html', perms)

    return render(request, 'index.html')


def analyse(request):
    # get the text
    text = request.POST.get('text', "enter your text")
    # checkbox
    removepunc = request.POST.get('removepunc', "off")
    uppercase = request.POST.get('uppercase', "off")
    newlineremover = request.POST.get('newlineremover', "off")
    extraspaceremover = request.POST.get('extraspaceremover', "off")
    charcount = request.POST.get("charcount", "off")
    # print(removepunc)
    # print(text)
    # analyse the text

    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        sent = ""
        for char in text:
            if char not in punctuation:
                sent += char
        perms = {'purpose': 'remove punctuation', 'analyse_text': sent}
        text = sent

    if (uppercase == "on"):
        character = ''
        for char in text:
            character += char.upper()
        perms = {'purpose': 'remove lowercase', 'analyse_text': character}
        text = character

    if (newlineremover == "on"):
        line = ''
        for char in text:
            if (char != '\n' and char != "\r"):
                line += char

        perms = {'purpose': 'new line remover', 'analyse_text': line}
        text = line

    if (extraspaceremover == 'on'):
        line = ''
        for index, char in enumerate(text):
            if not (text[index] == ' ' and text[index+1] == ' '):
                line += char

        perms = {'purpose': 'extra space remover', 'analyse_text': line}
        text = line

    if (charcount == 'on'):
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        count = 0
        for i in text:
            if i not in punctuation:
                count += 1

        perms = {'purpose': "character count", 'analyse_text': count}

    if (extraspaceremover != 'on' and newlineremover != "on" and uppercase != "on" and removepunc != "on"):
        return HttpResponse("please select any of the option and try again")

    return render(request, 'analyse.html', perms)
