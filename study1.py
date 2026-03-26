import requests
import random
import sys
import string
#Studying Python basics
#name = input("input example: ")
"""
Dito sa part na ito ay kung paano gagamitin ang tuple sa python
So ang tuple ay isang data structure na ginagamit para magstore ng multiple values sa isang variable.
"""
#a = "Garcia"
#b = 20
#c = "Laguna"
#infoExample = (a, b, c)

#print(infoExample)
"""
Dito sa part na ito ay kung paano gagamtin ang .split() function
So ang .split() function ay ginagamit para hatiin ang intpu ng user na multiple values.
"""
#x, y, z = input(f"multiple input example: ").split()
#print(f"Firstname for x: ", x)
#print(f"Secondname for y: ", y)
#print(f"Thirdname for z: ", z)
#num = 10.5
#print(num)

"""
Dito naman sa part na ito ay kung paano ginagamit ang type conversion sa python
Specifically ay yung type() function with an example of float conversion
ang magiging output nito ay String since ang default data type ng input() function ay String.
"""
#floatExample = (input("price of apple: "))
#print(type(floatExample))

"""
Since case sensitive ang python, dapat magingat sa pagtype ng mga functions at variables
Meaning ay hindi pwedeng magkapareho ang pangalan ng variable at function.
"""

#a = "Hello"
#A = 'World'
#Ang a at A ay magkaibang variable dahil sa case sensitivity pati na rin ang String na gamit

#x = 5
#x = "nigga"
"""
Dito naman, ang x ay nagkaroon ng unang automatic na data type as integer
tapos nagbago ang data type nito as String dahil sa reassignment
at ang ipiprint na output ay ang latest changes sa variable x which is nigga
"""
#x = str(5)
#y = int(5)
#z = float(5)

"""
Dito naman ay kung ipiprint ang mga ito ay makikita ang iba't ibang data types
like kung ipiprint ang x ay magkakaroon ng output na String dahil sa str() conversion
Ganon din para sa iba dahil sa kanilang data type casting functions
"""

#variable1 = ("Hello World")
#variable_1 = ("Hello World")
#VARIABLE1 = ("Hello World")
#variable1_= ("Hello World")
"""
Ang mga ito ay ang mga legal types of identifiers sa python
Marami pang legal types of identifiers sa python tulad ng:
1. Pwedeng gumamit ng mga letters (a-z, A-Z)
2. Pwedeng gumamit ng mga numbers (0-9) basta't hindi magsisimula sa number
3. Pwedeng gumamit ng underscore (_)
"""
#1variable = "Hello World"
#variable-1 = "Hello World"
#variable 1 = "Hello World"
"""
Ito naman ang mga illegal types of identifiers sa python
1. Hindi pwedeng magsimula sa number
2. Hindi pwedeng gumamit ng special characters tulad ng hyphen (-) at space
"""
#x = y = z = "Orange"
#a, b, c = 'apple', 'banana', 'cherry'
#print(x, y, z)
#print(x)
#print(y)
#print(z)
#print(a, b, c)
"""
Dito namana ay yung simpleng assigning ng multiple variables sa isang line
Gamit ang parehong value or iba't ibang values, or multiple values, multiple variables 1 line
"""

#a = "Hello"
#b = 5
#c = "!"
#print (a, b, c)
"""
Dito naman ay yung simpleng pagprint ng multiple variables sa isang line
Gamit ang comma (,) para paghiwalayin ang mga variables
"""

#name = "Ashley" #Global variable

#def pangalan():
    #global name
    #name = "Jazmar" #Local variable
    #print("Global variable: ", name) # Printing the global variable inside the function
    #print("Local variable: ", name) # Printing the local variable inside the function
#pangalan()

#print("Outside global print: ", name)# Printing the global variable outside the function

#def myfunc():
    #global nigga
    #nigga = "Me"
    #print("local to global variable inside def: ", nigga)
#myfunc()

#print("local to global variable: ", nigga)
"""
Dito is ineexplore natin yung global keyword with the use of def()
tulad ng pagpapalit ng value ng global variable sa loob ng function
at pag gagamit ng local variable at global variable gamit ang print() function
"""

#string = str("Hello World") 'str()' is the datatype
#integer = int(10) 'int()' is the datatype
#floatation = float(10.10) 'float()' is the datatype
#complexion = complex(100, 10.101) 'complex(j)' is the datatype
#lister = list(("Ashley", "Jazmar", "Clyde")) 'list[]' is the datatype
#tupler = tuple(("unarranged", "group", "set")) 'tuple()' is the datatype
#ranger = range(10) 'range()' is the datatype
#dictionary = dict(name = "Ashley", age = 20) 'dict{}' is the datatype
#setter = set(("apple", "banana", "cherry")) 'set{}' is the datatype
#frozen = frozenset(("apple", "banana", "cherry")) 'frozenset()' is the datatype
#boolean = bool(10) 'bool()' is the datatype
#byter = bytes(5) 'byte()' is the datatype
#byterray = bytearray(7) 'bytearray()' is the datatype
#MemoryViewBytes = memoryview(bytes(20)) 'memoryview(bytes())' is the datatype
#print(complexion)
"""
So dito naman ay nilibot ko yung iba't-ibang klase ng data types sa python
"""
#chapter 3
"""
Adding = 5 + 5  
Subbing = 10 - 5
Multiplying = 10 * 10
Dividing = 10 / 2
Moduling = 50 % 6 # So balee dito ang formula is 50 / 6 = 8, 6 * 8 = 48, 50 - 48 = 2 yung 2 is yung sagot 
Exponing = 4 ** 2 # Has a formula like this 2 x 2 = 4 x 2 = 8 x 2 = 16 meaning ito yung may power sa Math
print(Exponing)
"""
"""
#Pinapaliwang dito ay yung iba ibang klase ng Boolean operators nag sumasagot ng True or False
print(1 == 5) #Is Equal to
print(1 != 5) #Not Equal to
print(5 > 1) #Is greater than
print(5 >= 1) #Is Greater than Or Equal to
print(1 < 5) #Is less than
print(1 <= 5) #Is Less than Or Equal to
"""

"""
#Lazy Operators
number_1 = 14
number_1 += 27
print(number_1)
"""
"""
Name_Test = input("What is your name: ")
print(f"Hi {Name_Test} this is an input test")

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
print(f"{num_1} + {num_2} = {int(num_1) + int(num_2)}")
"""
#Chapter 3 Exercises
"""

#Mini exercises
print("Ashley")
print("Ashley" * 10)

appleQuestion = input("How many apples you would like to buy: ")
apple = 100
print(f"You like to purchase {appleQuestion} from {apple} apples, there would be {int(apple) - int(appleQuestion)} apples left")
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
print(f'Hello {firstName} {lastName}')

name = input("What is your name: ")
location = input("Where do you live: ")
phoneNumber = input("What is your phone number: ")
favColor = input("What is your favorite color: ")
print(f"So your info is this:\nname: {name}\nlocation: {location}\nphone number: {phoneNumber}\nfavorite color: {favColor}")
"""
"""
def ifelse_example():
    global x
    x = input('Enter name: ')
    if x == "Ashley":
        print('x is Ashley!')
    elif x == "Sairylle":
        print('x is Sairylle!')
    else:
        print(f"Your name is: {x}")
        #print('x does equal to Ashley!')
ifelse_example()
 #String Manipulation Examples
print(f'This is the .lower() function example: {x.lower()}') #ashley jazmar clyde l. garcia
print(f'This is the .upper() function example: {x.upper()}') #ASHLEY JAZMAR CLYDE L. GARCIA
print(f'This is the .capitalize() function example: {x.capitalize()}') #Ashley jazmar clyde l. garcia
print(f'This is the .title() function example: {x.title()}') #Ashley Jazmar Clyde L. Garcia
print(f'This is the .swapcase() function example: {x.swapcase()}') #aSHLEY jAZMAR cLYDE l. gARCIA
print(f'This is the .len() function example: {len(x)}') #26
print(f'This is the .rstrip() function example: {x.rstrip("Garcia")}') #Ashley Jazmar Clyde L.
"""
#def ifelse_example():
"""
#Left or Right Game
print("Welcome to Left or Right Game!")
name = input("enter your name: ")
name = name.title()
print(f"Hello {name}!, let us start the game...")
choice = input("Choose a path, Left or Right: ")
choice = choice.lower()
if choice == "left":
    print(f"Correct {name}!, you've chosen the right path!")
    print("Now answer this math game to continue throught the path...")
    MathGame = int(input("What is 10 * 5 / 2 + 10 - 10: "))
    if MathGame == 25:
        print(f"Correct {name}, you may continue your path to success!")
    else:
        print(f"Wrong answer {name}, you lost the game!")
elif choice == "right":
    print(f"That is the wrong path to succeed {name}, you will be eaten by a Python!")
    print("Game Over!")
else:
    print(f"Invalid choice {name}, wag nigga!")
"""
#ifelse_example()
#Chapter 4 Exercise
"""

mathProblem = int(input("What is 10 % 5: ")) #Modulus DMS
if mathProblem == 0:
    print("Ang galing mo nigga!")
else:
    print("Mali kang nigga ka!")

name = input("What is your full name: ").upper()
print(name)
print(f"Ito yung dami ng letters sa name mo: {len(name)}")
"""

#Chapter 5
#def listfunc_example():
"""
ex_1 = "Garcia"
list_numbers = [25, 256, 300]
names = ["Ashley", ex_1, "Sairylle", "Jazmar", "Clyde", list_numbers, "Dela Cruz", 30, {1, 2, 3, 4}]
names.extend(["Jaea", "Nigga"]) #Ito naman is malinis na pag add ng new list sa existing list which is names
#imbis na idadagdag sya with braces, ilalagay sya ng malinis bilang part talaga ng list, pero sa dulong parte sya ilalagay
names.append("Cindy") #Inaadd nito yung word na "Cindy" sa dulo ng list, after list_numbers.
names.insert(4, "Santiago") #Dito naman ay nagaadd ng word na "Santiago" sa index 4
#meaning madadagdag sya after Jazmar at before Clyde.
names.remove("Jazmar") #Ibig sabihin ireremove yung word "Jazmar" sa list pagkaprint
names.pop(3)#Dito naman is tatanggalin nito yung nakalagay sa index 3 which is "Santiago"

print(names)
print(len(names))

emptyList = ["Zero item", "First item", "Second item", [1, 2, 3, 4]]
#emptyList.extend(["Third item", "Fourth item", "Fifth item"])
print(emptyList[3] [2]) #Dito naman is ipiprint lng na bagay ay yung nasa loob ng [1, 2, 3, 4] na may index number na 2 which is yung 3
"""
#def listfunc_example():
#chatpter 5 exercise
"""

KnownNames = ["Ashley", "Sairylle", "Jazmar", "Cindy", "Clyde"]
print(KnownNames [1])
ListWithMath = [1 + 1, "Nigga", 30, 10.5, "Chatgpt"]
print(ListWithMath [0]) #Dito is piniprint na agad yung sagot which is 2 sa OUtput

MultiDimensionalList = [["Ashley", "Niggasan street", 20, "Philippines"], ["Jazmar", "Ellilora Kingdom", 19, "Philippnies"], ["Clyde", "Stamburt Street", 25, "Philippines"], ["Laquian", "Danayan Subdivision", 23, "Philippines"]]
print(MultiDimensionalList [1]) #Dito nmn is ipiprint yung "Jazmar" list
print(MultiDimensionalList [2] [2]) #Ipiprint dito is yung nasa loob ng pangatlong list which is yung number 25
"""

#chapter 6
#While Loop Example

#def while_exampel():
"""
    num1 = int(input('Enter number zero here: '))
    while num1 < 10:
        #Kung yung += ay tinanggal ay mag-yayari sa while loop ay endless loop
        num1 += 1 #Ibig sabihin nito ay kung ano man ilagay ko sa input ay pag pinrint ay mag + 1 sya
        #Pag andito yung += statement ay ang mangyayari ay magsisimula sa 1 ang pagprint
        print(f"You have entered 0 that is why the output is {num1}")
        #Pero pag yung += statement ay nilgay dito ay ang mangyayari ay magsisimula sa 0 ang pagprint
"""
#Break Statement Example
"""
    num2 = 20
    while num2 < 40:
        num2 += 5 #ang use nitong += ay pra mag add ng lima sa 20 every loop
        print(f"The number is now: {num2}")
        if num2 == 35:
            num2 += 1 #Tapos itong += naman ay mag aadd ng 1 pag yung loop ay malapit na sa 35 at ipiprint yung mismong number na 35
            break #Gamit ang break statement ay mapuputol ang while loop pag naabot ang condition na totoo
"""
#Continue Statement Example
"""
    num3 = 5
    while num3 < 50:
        num3 += 5
        if num3 == 25:
            continue
            #So dito sa part na ito, ang ginawa ng continue statement ay pag umabot sa 25 yung num3
            #ay lalaktawan nya yung loop sa 25th na number at magsisimula ulit sa 30
        print(f"The number is now: {num3}")
"""
#while_exampel()

#def for_example():
    #For loop through a range
"""
    for num in range(1, 10): #ibig sabihin nito ay magsisimula sa 1 yung bilang hanggang 9, pag walang 1 dito ay magisismula sa 0
        print(num)
        if num == 1: #Dito naman is kung yung loop daw ay tumapat sa 1 mag piprint ng message
            print(f"the number starts with {num}")
        if num == 9: #Tapos dito, pag tumapat ng 9 yung loop ay mag piprint ng message
            num += 1 #Pero mag plus 1 pra lumabas yung 10 sa output
            print(f"The number ends with {num}")
"""
    #For loop through a list
"""
    nigga = ["mahal", "ako", "hanggang", "arawaraw", "lagi", " ", "kitang", "iniisip", "tunay", "ako"]
    for n in nigga:
        print(n [0]) #Ang gingagwa nito is kinukuha yung mga index ng mga words sa list,
        #Kasi yung n ay yung name ng mga words sa list
        #yung nasa print() na number is yung equivalent nung mga n bilang index
        #so kinuha ko yung mga index ng mga letters sa loob ng words na may index din
        # n = mahal, ako, etc
        #[] = a, b, c, d, e,
"""
    #Basic for looops
"""
    for i in range(5):
        i += 1
        print(i) #piprint ng hanggang 5 dahil sa += statement
    else:
        print("Tis done") #after ng numerical na prints ay ito ang huling lalabas sa output

    for x in range(5):
        pass #Ito ay mag rarun pero ang output ay blanko
"""
    #FIZZBUZZ CODE
"""
    for x in range (1, 101):
        print(x)
        if x % 3 == 0: # So dito kaya doble ang operator dito ay ganto:
            print(f"{x} FIZZ") #Kung yung number daw sa loop(==) ay pwede idivide(%) sa 3 print daw ng FIZZ
        elif x % 5 == 0: # Dito naman is kung yung number sa loop(==) 
            print(f" {x} BUZZ") #ay pwede idivide(%) sa 5 print daw ng BUZZ
        elif x % 3 == 0 and x % 5 == 0: #Dito is kung yung number ay pwede idivide sa 3 at 5
            print(f" {x} FIZZBUZZ")
"""
    #Improved FIZZBUZZ CODE
"""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0: #Much better dito dahil walang duplicate na print statement
            print(f"{i} FIZZBUZZ")
        elif i % 3 == 0:
            print(f"{i} FIZZ") #Mga print dito ay nkaayos yung pagkakasunod sunod ng condition
        elif i % 5 == 0:
            print(f"{i} BUZZ")
        else:
            print(i)
"""
#for_example()

#Chapter 6 Exercises
"""
for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} FIZZBUZZ")
    elif i % 3 == 0 or i % 5 == 0:
        print(f"{i} FIZZ" if i % 3 == 0 else f"{i} BUZZ")
    else: print(i)

first = ["Ashley", "Nigga street", 273659, "Cindy"]
second = ["Jazmar", "Ligga street", 283659, "Sairylle"]
third = ["Clyde", "Bigga street", 6237890, "Dela"]
fourth = ["Garcia", "Whigga street", 2369529, "Cruz"]
fifth = [first, second, third, fourth]
for num in fifth:
    print(num [2]) #Dito naman is piniprint ay yung mga integers lng or yung may index number 2 sa loob ng mga lists
                #first, second, third lists na ang index 2 ay yung mga numbers kaya ayun ang kukunin
                #"1" = 0_index, "2" = 1_index 3 = 2_index
for num in fifth:
    print(fifth[1], fifth[3])#Ang ipiprint nito ay yung second[] at yung fourth[] sa loob ng fifth [[], []]
    break #Pra isang print lang lalabas
"""
# Chapter 7
# Function()
"""
def myfunc(): #Dito is kung ilalagay natin yung i na variable dito is makakapag print tayo ng specific number sa end line ng myfunc()
    print("Function testing")
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f" {i} FIZZBUZZ")
        elif i % 3 == 0 or i % 5 == 0:
            print(f"{i} FIZZ"if i % 3 == 0 else f"{i} BUZZ")
        else:
            print(f"{i} is not divisible to 3 or 5")
myfunc()#so kung maglalagay tayo sa loob ng number within the range() ay yun lng ang ipiprint
"""
"""
def input_example(): #Tinry ko lng kung gagana ito, easy to understand ito so get nyo na yan
    is_True = True
    is_False = False
    x = int(input('Enter a number: ')) 
    if x % 2:
        print(f"The {x} is {is_True}") 
    else:
        print(f"The {x} is {is_False}") 
input_example()

def bool_xmpl(x): #Dito is nilagyan ng item na variable yung function na bool_xmpl()
    if x % 2 == 0: #Simula dito ay conditional statement lng pra sa print() statement
        return True
    else:
        return False
my_var = bool_xmpl(88)
print(my_var)#Ang ipiprint nito ay yung boolean equivalent ng number na nakalagay sa my_var = bool_xmpl()
#print(bool_xmpl(10)) #Dito is yung pag print na gamit ang function
# bool_xmpl(582) Pero pag ito ay mag piprint ng blank output dahil hindi nagpiprint tlga yung function eh, box lng sya
"""
"""
#Dito is later on sa code nilgyan ng value yung item which is sa names() rather than def names()
def names(first, second): #Dito is tinest yung multiple items sa loob ng isang function()
    print(f"2 names in function test {first} and {second}") #tapos dito ay tinest yung laman ng items gamit yung names() function
names("Ashley", "Jazmar") #Dito is nilgyan ng laman yung first at second na item ng subitem.

def namer(first = "Ashley", second = "Jazmar"): #Ito is gumagamit ng default na subitem pra sa items na first at second
    print(f"first item: {first}")
    print(f"second item: {second}")
namer("Nigga")# Di tulad sa upper block of code, itong code na ito ay may value na agad yung items sa loob ng namer() function
#Pag dito sa namer() ay isa lng nilagay mo, ang ipiprint ay mababago yung first which is unang print() statement
#Then pag blanko or kulang yung value ng namer() ay kukuha sa default value ng second
"""
# Chapter 7 exercise

#1.
"""
def fizz_buzz(i):
    #for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} FIZZBUZZ")
    elif i % 3 == 0 or i % 5==0:
        print(f"{i} FIZZ"if i % 3 == 0 else f"{i} BUZZ")
    else:
        print(f"{i} not divisible to 3 or 5")
fizz_buzz(int(input("Enter a number: "))) #Ito naman is pinagsama-sama ko na dito sa baba yung output pra madali at di masyado marami code
"""
#2.
"""
def buzz_fizz(n): # About ito kung paano nababasa ni Python yung pagikot ng Loop
    if n % 3 == 0 and n % 5 == 0: #Pero dahil nasa baba yung For loop, dun palang magsisismula yung loop
        print(f"{n} FIZZBUZZ") #Babasahin lang muna ni Python mga upper lines, pero once na nakatungtong si Python sa For Loop line
    elif n % 3 == 0 or n % 5 == 0: #dun lang nya malalaman na nasa loop pala lahat ng nasa buzz_fizz(n)
        print(f"{n} FIZZ" if n % 3 == 0 else f"{n} BUZZ") #At gagawin ni PYthon ay yung n = i sa ibaba which mean renaming the numbers 100 times
    else:
        print(f"{n} is not divisible to 3 or 5")
for i in range(1, 101):
    buzz_fizz(i)
"""
#3.
"""
def things(first = 1, second = 2, third = 3, fourth = 4, fifth = 5, sixth = 6, seventh = 7):#tama ang pagkaprint
    print(f"All values printed {first}, {second}, {third}, {fourth}, {fifth}, {sixth}, {seventh}")#Pero mali pagkalagay ng mga value sa variables
things() #So dito is nagpacheck ako kay ChatGPT, ang pagkakamali is imbis na ilagay ko yung value ng variables sa things()
#Is sinama ko sila sa def things()
"""
#4.
"""
def asker(): #Simpleng use ng function()
    name = input('What is your name: ')
    print(f'Welcome {name}')
asker()
"""
#Self project using Chapters 1-7
#math operators, lazy operators, input, string manipulations, lists, function, for loops, while loops, if/else statements
#Mini project 1
'''
def mini_proj():
    name_list = []
    age_list = []
    correct_answers = []
    wrong_answers = []
    questionnaire = []

    name = input('Enter username: ').lower()
    while not name.isalpha():
          print('Mali ka boi!')
          sys.exit()
    else:
        print(f'Ollaa {name}')
    age = int(input('Enter age: '))
    if age < 18:
        print('You are not eligible for 18+ ')
        sys.exit() #ito ay nalaman ko lng kay AI, now ko lng toh nalaman whashas
    else:
        print('You are eligible for 18+')
    
    name_list.extend([name])
    age_list.extend([age])

    while True:
        answer = input(f'Are you ready to solve queesetions {name} yes/no: ').lower()
        if answer == 'yes':
            print(f'Matapang ka ah, g! {name}')
            break
        elif answer == 'no':
            print(f'Duwag ka ba? {name}')
            sys.exit()
        else:
            print('Ayusin ang sagot!')
            sys.exit()
            
    print(f'Hello! {name} you are to participate in this basic calculator quest')
        
    
    question1 = int(input('What is the answer to this first question, 50 * 4 =  '))
    questionnaire.extend([question1])
    if question1 == 200:
        correct_answers.extend([question1]) 
        print(f'{question1} is correct!, next question')
    else:
        wrong_answers.extend([question1])
        print(f'{question1} is wrong, next question')
    
    question2 = int(input('What is 27 + 83 = '))
    questionnaire.extend([question2])
    if question2 == 110:
        correct_answers.extend([question2]) 
        print(f'{question2} is correct!, next is the last question')
    else:
        wrong_answers.extend([question2])
        print(f'{question2} is wrong, next is the last question')

    question3 = int(input('What is 89 / 6 - 7 = '))
    questionnaire.extend([question3])
    if question3 == 7:
        correct_answers.extend([question3])
        print(f'{question3} is correct!, you earned the score below')
    else:
        wrong_answers.extend([question3])
        print(f'{question3} is wrong, this is the last question')

    print(f'Congrats! {name}, you finished the FIRST TEST')
        
    print(f'Here is your score {len(correct_answers)}/{len(questionnaire)}')

mini_proj()
'''
#Mini project 2
"""
def quiz_calculator():    
        rounds = int(input('How many times would you like to repeat this process: '))
        
        for i in range(rounds):
            num1 = float(input('Enter a number: '))
            operand = input('Select from the choices how you want the math to continue [+, -, /, *, **, %]: ')
            num2 = float(input('Enter a second number: '))
        
            if operand == '+':
                result = num1 + num2
                #print(f'{num1} {operand} {num2} = {num1 + num2}')
            elif operand == '-':
                result = num1 - num2
                #print(f'{num1} {operand} {num2} = {num1 - num2}')
            elif operand == '/':
                result = num1 / num2
                #print(f'{num1} {operand} {num2} = {num1 / num2}')
            elif operand == '*':
                result = num1 * num2
                #print(f'{num1} {operand} {num2} = {num1 * num2}')
            elif operand == '**':
                result = num1 ** num2
                #print(f'{num1} {operand} {num2} = {num1 ** num2}')
            elif operand == '%':
                result = num1 % num2
                #print(f'{num1} {operand} {num2} = {num1 % num2}')
            else:
                print('Invalid input')
                continue

            print(f' Result {i+1}: {num1} {operand} {num2} = {result}')

quiz_calculator()
"""
#So ang improvement dito from AI are the result variable, print() statement, at removal of operand list

#Chapter 8
#Dictionaries
"""
love_ko = 'Sai'
Favorite_meals = {
    'Ashley': 'Green Mango', #So yung Ashley is yung KEY at yung Greend Mango ay yung VALUE
    love_ko: 20,
    'Jaea': True
}
print(Favorite_meals)
Favorite_meals['Nigga'] = 20.50
print(Favorite_meals)
#Favorite_meals.pop('Jaea')
print(Favorite_meals[love_ko] + 2)
print(Favorite_meals.keys()) #Dito is ipiprint lng ay yung mga KEY sa loob ng dictionary
print(Favorite_meals.values()) #Dito is ipiprint lng ay yung mga VALUES sa loob ng dictionary
for a, b in Favorite_meals.items(): #Dito is ginamitan ng For loop yung pag print ng Key at Values like may label sila pag pinrint
    print(f"Key: {a}, Values: {b}") #Key: Ashley, Values: Green Mango...Hanggang maprint lahat ng nasa Dictionary
"""
#Chapter 8 Exercises
"""
Friends = {
    'ashley': 2908356,
    'marbs': 289734651,
    'riel': 928356,
    'edgie': 6991428,
    'sai': 67285914
}

friend_input = input('What is your name: ').lower()
print(Friends[friend_input])
friend_remove = input('What name would you like to remove Ashley/Marbs/Riel/Edgie/Sai: ').lower()
Friends.pop(friend_remove)
friend_add = input('What name would you like to add?: ').lower()
friend_addNumber = int(input("Input the added friend's number: "))
Friends[friend_add] = friend_addNumber
print(Friends)
for name, number in Friends.items():
    print(f"My friend {name}'s phone number is: {number}")
"""

#Chapter 9
#Flashcard
#Combining all learned, List,Dictionary,Math operators,Lazy operators,Input,String manipulations,Function,For loops,While loops,If/else statements
'''
def flashcard():
    user_dict = {
        'Ashley': 'ASHLEY'
    }

    Operand_list = ['+', '-', '/', '*']

    name = input('Enter name: ')
    password = input('Enter password: ').upper
    if name and password not in user_dict:
        user_dict[name] = password

    print(f'Welcome to Math Flashcard {name}!')

    while True:
        rand_num1 = random.randint(1, 100)
        rand_num2 = random.randint(1, 100)
        operators = input('Choose from the following (+,-,/,*) or type (q) to quit the game: ')
        if operators == 'q':
            print('Duwag!')
            break
        
        if operators not in Operand_list:
            print('INVALID INPUT')
            continue

        if operators == '+':
            result = rand_num1 + rand_num2
            user_input = int(input(f'{rand_num1} + {rand_num2} = '))
            if user_input == result:
                print('Correct!')
            else:
                print(f'MALI KA!, {result} ANG TAMA')
        elif operators == '-':
            result = rand_num1 - rand_num2
            user_input = int(input(f'{rand_num1} - {rand_num2} = '))
            if user_input == result:
                print('CORRECT!')
            else:
                print(f'MALI KA!, {result} ANG TAMA')
        elif operators == '/':
            if rand_num2 == 0:
                print('DIVISION TO ZERO')
                continue
            result = rand_num1 / rand_num2
            resultstr = f'{result:3f}' #May something dito, ayaw gumana ng 3decimals lng, ang 3f dito is katumbas ng apat ng number sa decimals
            #Kahit gaano ka unti ng decimal na gagamitin mong value ay anim na decimal tlga lumalabas
            user_answer_str = input(f'{rand_num1} / {rand_num2} = ')
            if user_answer_str == resultstr:
                print('CORRECT!')
            else:
                print(f'MALI KA!, {resultstr} ANG TAMA')
        elif operators == '*':
            result = rand_num1 * rand_num2
            user_input = int(input(f'{rand_num1} * {rand_num2} = '))
            if user_input == result:
                print('CORRECT!')
            else:
                print(f'MALI KA!, {result} ANG TAMA')
        else:
            print('INVALID INPUT')
            sys.exit()

flashcard()
'''
#Using .replace() method
'''
she = "Sai"
him = "I Love Her"

x = him.replace("Her", "Sai")
print(x)
'''

#Using match statements instead of if-elif-else statements
'''
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a second number: '))
print('1 = +')
print('2 = -')
print('3 = /')
print('4 = *')
print('5 = quit')
operand = int(input('Choose a number above: '))
match operand:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 / num2)
    case 4:
        print(num1 * num2)
    case 5:
        print('Match statement goodbye!')
        sys.exit()#Cute na kapalit ng if-elif-else statement whahhshas
'''
''''''
'''
reversing_string = "Ashley"
rvrsed_string = reversing_string[::-1]#Itong [::-1] ay yung taga-reverse
print(rvrsed_string) #Dito is yung pag rereverse ng string whashashhas
reversing_intergers = 123456
rvrsed_integers = int(str(reversing_intergers)[::-1]) #Ginawang string yung integer para mareverse
print(rvrsed_integers) #Dito naman is yung pagreverse ng integers
'''
'''
url = input('Enter a URL: ') #Ito ay input about sa URl lng

try: #Gamit itong try-except statement ay hinahandle itong URL na nilagay mo
    response = requests.get(url) #So dito is yung pag rerequest sa URL na nilagay mo
    response.raise_for_status() #Dito naman is yung kung valid ba yung URL na nilagay mo
    if response.status_code == 200:
        print("The URL is valid and accessible.") #Dito sa if statement is yung kung 200 or ok yung response ng site na nilagay mo
    else:
        print(f"Other response status code: {response.status_code}") #Dito naman is yung kung may iba kang reposne code
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}  ") #Dito is yung kung mali yung nilagay mo na URl at mag lalabas sya ng predicted errors
'''

#Dito is gagawa us ng URL shortener 
url_shi = {}#Dito is gagamit tayo ng library para sa pag shoshort

def generate_short_code(length=6): #So dito is yung mga igegenerate na random code ay limited lng 6 digits
    characters = string.ascii_letters + string.digits #Dito is yung characters na gagamtin is both string & num
    return ''.join(random.choice(characters) for _ in range(length)) #Ang ginagagwa dito is yung pag randomize ng num & string sa loob ng length=6
def shorten_url(long_url): #Dito is yung pag aayos ng short code base sa long_url
    short_code = generate_short_code() #Ito yun specifically
    url_shi[short_code] = long_url #Ito ay yung format sa pag sesave ng URL sa dictionary, dict_name[key] = value
    return short_code
def retrieve_url(short_code): #Dito nmn is yung kuha ng short_code sa dict with get() method
    return url_shi.get(short_code, "Short code not found.")

if __name__ == "__main__": #OK, itong part na ito is wala pa ako idea about dito, pagaaralan ko plng dis
    long_url = input("Input the long URL here: ") #Wala ako idea sa Ifstatement, itong mga ito is output lng ito
    short_code = shorten_url(long_url)
    print(f"The shortened URL is: {short_code}")

