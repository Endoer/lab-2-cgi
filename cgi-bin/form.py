#!/usr/bin/env python3
from asyncio import constants
import cgi
import math
import random
import html


Min = 1
Max = 100
Attemps= math.ceil(math.log(Max-Min+1) / math.log(2))
GameOver=False

form = cgi.FieldStorage()

inputValue = form.getfirst("inputValue", None)
leftAttemps=form.getfirst("leftAttemps", Attemps+1)
statusHistory=form.getfirst("statusHistory","")
computerNumber=form.getfirst("computerNumber", None)

if(computerNumber==None):
    computerNumber=round(random.uniform(Min, Max))

if(inputValue!=None):
    statusHistory =f""" Ваше число {inputValue} моё число {"больше" if inputValue < computerNumber else "меньше"}\n """ + statusHistory

if(int(leftAttemps) == 1):
    statusHistory="К сожалению у вас закончились попытки и вы проиграли\n"
    GameOver=True

if (inputValue == computerNumber):
    statusHistory="Поздравляю вы победили!\n"
    GameOver=True

def printHead():
    print("Content-type: text/html\n")
    print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="windows-1251">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/styles/style.css"> 
    <link rel="stylesheet" href="/styles/bootstrap_css/bootstrap.css">
    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">    -->

</head>

<body>
    <div class="gameBlock">
    <form action="/cgi-bin/form.py" class ="gameForm">
        <div class="h1" >Игра угадай число</div>""")

def printGreeting():
    print(f"""<div class="form-label" id="greating">Комьютер загадал число от {Min} до {Max} и у вас есть {Attemps} попыток чтобы его отгадать<hr></div>""")

def printInputArea():
    print(f"""<div class="inputButton">
            <input class="form-control" id="answerNumber" type="number" name="inputValue" {"disabled" if GameOver else ""} autofocus>
            <button class="btn btn-primary" id="checkButton" {"disabled" if GameOver else ""}>Проверить</button>
            <a class="btn btn-primary" type="button" href="/">Заново</a>
            <input style="display:none" name="leftAttemps" value={int(leftAttemps)-1}>
            <input style="display:none" name="statusHistory" value="">
            <input style="display:none" name="computerNumber" value={computerNumber}>
        </div>"""
    )
#{statusHistory != None if html.escape(statusHistory) else None}
def printStatus():
    
    print(f"""<div class="form-label" id="status"> <hr>{statusHistory if statusHistory != "" else "Я только что загадал новое число"} </div>""")

def printTail():
    print("""</form>
</div>
</body>

</html>""")

def printPage():
    printHead()
    printGreeting()
    printInputArea()
    printStatus()
    printTail()    

printPage()