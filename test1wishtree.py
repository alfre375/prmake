import webbrowser

print("there are 6 questions")
grade = int(input("default grade: "))
name = input("Name: ")
maxGrade = int(input("maximum grade: "))

def p(txt):
    print(txt)

"""def lp(txt):
    txt.lower()
    print(txt)

lp('TesTing')
"""

difficulty = input("dificulty: ")

if difficulty == "" or difficulty == "main" or difficulty == "default":
    difficulty = "nonSillyBlookie"

if difficulty == "nonSillyBlookie":
    print("#1 why did they decide not to cut Red down?")
    #
    print("a. The tree cutters were too lazy")
    #
    print("b. The tree talks")
    #
    print("c. The tree was important to Francesca's family")
    #
    print("d. Maeve loves life")
    #
    res = input("correct answer(type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d.)")
    #
    if res == "C" or res == "c":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#2 True/False: Red got cut down")
    #
    print("a. True")
    #
    print("b. False")
    #
    res = input("correct answer(type 'A' for a. Type 'B' for b.)")
    #
    if res == "B" or res == "b":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#3 Which one best discribes bongo")
    #
    print("a. Optimistic")
    #
    print("b. A Minecrafter")
    #
    print("c. Pesimistic")
    #
    res = input("correct answer(type 'A' for a. Type 'B' for b. Type 'C' for c.)")
    #
    if res == "C" or res == "c":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#4 Red is a wishtree who receives many wishes daily, especially on wishing day. When is wishing day?")
    #
    print("a. May 1st")
    #
    print("b. May 31st")
    #
    print("c. Friday")
    #
    print("d. June 1st")
    #
    res = input("correct answer(type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d.)")
    #
    if res == "A" or res == "a":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#5 What is red's job? Why is red's name red?")
    #
    print("a. Red is a bird who is very friendly, she is a cardinal and that is where she gets her name")
    #
    print("b. Red is a farmer, her name came from a tractor brand")
    #
    print("c. Red is the boy that lives in the blue house, and he's named after the color of his hair")
    #
    print("d. Red is a wishtree, her name is also her color in fall")
    res = input("correct answer(type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d)")
    #
    if res == "D" or res == "d":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#6 Who is in the story?")
    #
    print("a. Red, Bongo, Samar, Stephen, Maeve, Francesca")
    #
    print("b. Dr. Ferullo, Been, Soop, His stuff, Minecraft")
    #
    print("c. FreshBakedBread, RosePetal, Harold, Squibbles")
    #
    print("d. You, You, You")
    #
    print("e. B, C, D are correct answers")
    #
    print("f. A, C are correct answers")
    #
    print("g. A, C, D are correct answers")
    #
    res = input("correct answer(type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d. Type 'E' for e. Type 'D' for d. Type 'E' for e. Type 'F' for f. Type 'G' for g.)")
    #
    if res == "G" or res == "g":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#7 Which best describes Red?")
    #
    print("a. Optimistic")
    #
    print("b. Minecrafter")
    #
    print("c. Pesimistic")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c.)")
    #
    if res == "A" or res == "a":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    print("#8 What animal's name is HariySpider?")
    #
    p("a. a spider")
    #
    p("b. an opossum")
    #
    p("c. a racoon")
    #
    p("d. a squirel")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d.)")
    #
    if res == "B" or res == "b":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#9 What was the relationship between Amadora and Maeve?")
    #
    p("a. Maeve was the mom")
    p("b. Maeve was the dad")
    p("c. Maeve was the daughter")
    p("d. Maeve was the son")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d)")
    #
    if res == "A" or res == "a":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#10 What was the relationship between Ama and Francesca?")
    #
    p("a. They were neighbors")
    p("b. They were frenimies")
    p("c. Ama was Francesca's great grandma")
    p("d. They were best friends")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d)")
    #
    if res == "C" or res == "c":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#11 What word/phrase was written on the trunk of the tree?")
    #
    p("a. Maeve loves Red xD")
    p("b. Stay")
    p("c. Leave")
    p("d. Hope")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d)")
    #
    if res == "C" or res == "c":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#12 What were the animals named after?")
    #
    p("a. Smells they enjoyed")
    p("b. Things they feared")
    p("c. Common names")
    p("d. All of the above")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d)")
    #
    if res == "D" or res == "d":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#13 What things were placed in the hollows?")
    #
    p("a. A loaf of bread")
    p("b. Letters")
    p("c. A baby")
    p("d. All of the above")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d)")
    #
    if res == "D" or res == "d":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#14 What was Maeve's wish?")
    #
    p("a. To get an invisible robot that did homework")
    p("b. For a true love")
    p("c. To never get the tree cut down")
    p("d. To go to the bathroom")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d)")
    #
    if res == "B" or res == "b":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #
    #
    #
    print("#15 What was Samar's wish?")
    #
    p("a. To get an invisible robot that did homework")
    p("b. For someone to love")
    p("c. All of the above")
    p("d. None of the above")
    #
    res = input("correct answer(Type 'A' for a. Type 'B' for b. Type 'C' for c. Type 'D' for d)")
    #
    if res == "D" or res == "d":
        print("correct, +1 points")
        grade = grade+1
    else:
        print("incorrect, -1 points")
        grade = grade-1
    #vocab
    p("#16 VOCAB")
    p("a. notoriously     1. odd, puzzled")
    p("b. boisterously    2. to injure severely")
    p("c. mangled         3. somebody or something well known for a bad thing")
    p("d. inquisitive     4. to pluck")
    p("e. twitching       5. person eager for knowledge")
    p("f. quizzical       6. something noisy")
    res = input("correct answer(Enter the numbers for the definitions of a,b,c,d,e and f in order separated by commas.)")
    res = res.split(',')
    correct = ['3', '6', '2', '5', '4', '1']
    names = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        if res[i].strip() == correct[i]:
            p(names[i] + ' is correct')
            grade = grade + 1
        else:
            p(names[i] + ' is incorrect')
            grade = grade-1
    #ESSAY
    idValue = str(129847)#randrange(100000, 10000000, 2)
    print("#17 use forms for this:")
    webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSc3UEZo8vRXLAUpcWT4bvUztFr6rvuOI1qUfmpX-kIFtgsdxw/viewform")
    print("id: " + idValue)
else:
    print("invalid difficulty")
if grade < 0:
    grade = 0


if grade > maxGrade:
    grade = maxGrade
if grade == 1:
    pts = " point"
else:
    pts = " points"
grade = str(grade)
maxGrade = str(maxGrade)
print("you got " + grade + pts)
