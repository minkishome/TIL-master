from django.shortcuts import render, redirect
from art import *
from . import hangulutils as hg

# Create your views here.



def index(request):
    return render(request, 'utils/index.html')


def art(request):
    fonts = ['3d_diagnoal', 'alpha', 'acrobatic', 'avatar', 'cards']
    return render(request, 'utils/art.html', {
        'fonts' : fonts,
    })

def output(request):
    # print(request.POST)
    user_input = request.GET.get('user-input')
    user_font = request.GET.get('user-font')
    
    if user_input:
        result = text2art(user_input, font = user_font)
        return render(request, 'utils/output.html',{
            'result' : result
        })
    else:
        return redirect('/utils/art/')

def throw(request):
 
    return render(request, 'utils/throw.html')

def catch(request):
    input1 = request.GET.get('user-input1')
    input2 = request.GET.get('user-input2')
    

    char_1 = [hg.KorChar(char).countstrokes() for char in input1]
    char_2 = [hg.KorChar(char).countstrokes() for char in input2]
    
    if not len(char_1) ==3 and len(char_2)==3:
        return redirect('/utils/throw/') 

    char_mix = []
    for i in range(3):
        char_mix.append(char_1[i])
        char_mix.append(char_2[i])
    map(int, char_mix)
    while len(char_mix) != 2:
        for i in range(len(char_mix)):
            if i == len(char_mix)-1:
                break
            char_mix[i] += char_mix[i+1]
            if char_mix[i] >= 10:
                char_mix[i] = char_mix[i] - 10
        char_mix.pop()
    alpha = char_mix[0]*10 + char_mix[1]
    if alpha <30:
        result = f'{alpha}점은 포기가 빨라요....'
    if alpha <60:
        result = f'{alpha}점은 가망이 없네요....'
    if alpha <90:
        result = f'{alpha} 점수가 높다고 뭐가 달라질까요?'
    if alpha <=99:
        result = f'{alpha} 점수는 높네요! 하지만 그게 다죠'

    
    return render(request, 'utils/catch.html', {
        'result' : result,
        'input1' : input1,
        'input2' : input2,
    })
