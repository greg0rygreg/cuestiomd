# the question format is: [["question", "A", "B", "C", "D", "correct option (from A-D)"]]
import random, json

def clear():
    print("\x1B[2J\x1B[H")

def sep():
    print("-" * 75)

clear()
welcomeMSGS = ["hi Vro, welcome to", "hey, welcome to CuestioMD", "welcome to CuestioMD! also, try DRAWscii!", "...", ":3", "*snoring*", "hi", "welcome to", "hey google, how to spell QeustionmD"]
byeMSGS = ["study more", "bye!", f"please tell me you got 100{"%"} on the last quizz you played", "we're planning to add an option to encrypt quizzes made with this app to prevent cheating", "bye Vro", "*snoring*", "bye"]
print(random.choice(welcomeMSGS))
print(""" ██████╗██╗   ██╗███████╗███████╗████████╗██╗ ██████╗ ███╗   ███╗██████╗ 
██╔════╝██║   ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗ ████║██╔══██╗
██║     ██║   ██║█████╗  ███████╗   ██║   ██║██║   ██║██╔████╔██║██║  ██║
██║     ██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╔╝██║██║  ██║
╚██████╗╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚═╝ ██║██████╔╝
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ """)
while True:
    mainMenu = input("""options:
(1) make a quizz
(2) open a quizz
(3) info
(0) quit

(?) >> """)
    try:
        mainMenu = int(mainMenu)
    except ValueError:
        pass
    if mainMenu == 1:
        clear()
        questions = []
        while True:
            print(""" █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
███████║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝""")
            actions = input("(1) add a question\n(0) save and exit\n\n(?) >> ")
            try:
                actions = int(actions)
            except ValueError:
                pass
            if actions == 1:
                clear()
                options = []
                question = input("question: ")
                options.append(question)
                for i in range(4):
                    options.append(input(f"option {"ABCD"[i]}: "))
                cOption = input("correct option (A-D): ").upper()
                if cOption in "ABCD" and len(cOption) == 1:
                    options.append(cOption.upper())
                else:
                    options.append(random.choice("ABCD"))
                questions.append(options)
                clear()
                if cOption not in "ABCD" and len(cOption) > 1:
                    print(f"the answer to the question you just made was incorectly formatted so we chose option {options[5]} for you : )")
                    sep()
            if actions == 0:
                clear()
                filename = input("save to (no file extension): ")
                with open(f"{filename}.qcmd", "w") as f:
                    json.dump(questions, f)
                clear()
                print(f"quizz saved to {filename}.qcmd successfully")
                sep()
                break
    if mainMenu == 2:
        clear()
        filename = input("open (no file extension): ")
        with open(f"{filename}.qcmd", "r") as f:
            questions = json.load(f)
        correct = 0
        for i, question in enumerate(questions):
            clear()
            msg = f"question {i+1}/{len(questions)}: {question[0]}\n"
            for i in range(4):
                msg += f"({"ABCD"[i]}) {question[i+1]}\n"
            msg += "\n(?) >> "
            answer = input(msg).upper()
            if answer == question[5]:
                correct += 1
        clear()
        grade = round((correct / len(questions)) * 100, 2)
        print(f"! ! ! RESULTS ARE IN ! ! !\nquestions you got correct: {correct}\nquestions you got wrong: {len(questions) - correct}\nyour final grade is {grade}%\n\n! YOU {"WIN" if grade >= 50 else "LOSE"} !")
        sep()
    if mainMenu == 0:
        clear()
        print(random.choice(byeMSGS))
        exit()
    if mainMenu == 3:
        clear()
        print("""CuestioMD v1 - made by greg with love and patience in Python 3.12
licensed under GPL v3.0 - you're allowed to redistribute as long as you credit me""")
        sep()