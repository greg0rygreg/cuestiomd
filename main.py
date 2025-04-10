# the question format is: [["question", "A", "B", "C", "D", "correct option (from A-D)"]]
import random, json, time, base64

def clear():
    print("\x1b[2J\x1b[H",end="") # that's all i needed to do????

def sep():
    print("-" * 75)

def error(text:str, more:str=None):
    if more is not None:
        print(f"\x1b[1;31merror:\x1b[0m\x1b[1m {text}\n\x1b[0m{more}")
    else:
        print(f"\x1b[1;31merror:\x1b[0m\x1b[1m {text}\x1b[0m")

def warning(text:str, more:str=None):
    if more is not None:
        print(f"\x1b[1;33mwarning:\x1b[0m\x1b[1m {text}\n\x1b[0m{more}")
    else:
        print(f"\x1b[1;33mwarning:\x1b[0m\x1b[1m {text}\x1b[0m")

clear()
welcomeMSGS = ["hi Vro, welcome to", "hey, welcome to CuestioMD", "welcome to CuestioMD! also, try DRAWscii!", "...", ":3", "*snoring*", "hi", "welcome to", "hey google, how to spell QeustionMD"]
byeMSGS = ["study more", "bye!", f"please tell me you got 100{"%"} on the last quizz you played", "bye Vro", "*snoring*", "bye"]
print(random.choice(welcomeMSGS))
logo = """ ██████╗██╗   ██╗███████╗███████╗████████╗██╗ ██████╗ ███╗   ███╗██████╗ 
██╔════╝██║   ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗ ████║██╔══██╗
██║     ██║   ██║█████╗  ███████╗   ██║   ██║██║   ██║██╔████╔██║██║  ██║
██║     ██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╔╝██║██║  ██║
╚██████╗╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚═╝ ██║██████╔╝
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ """
while True:
    mainMenu = input(f"""{logo}
options:
(1) make a quizz
(2) open a quizz
(3) edit a quizz [WIP]
(4) info
(0) quit

(?) >> """)
    try:
        mainMenu = int(mainMenu)
    except ValueError:
        clear()
    if mainMenu == 1:
        clear()
        questions = []
        while True:
            print(f""" █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
███████║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
you have {len(questions)} question{"" if len(questions) == 1 else "s"}""")
            actions = input("(1) add a question\n(0) save and exit\n\n(?) >> ")
            try:
                actions = int(actions)
            except ValueError:
                clear()
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
                if cOption not in "ABCD" or len(cOption) > 1:
                    #print(f"the answer to the question you just made was incorrectly formatted so we chose option {options[5]} for you : )")
                    error("incorrectly formatted answer", f"{options[5]} was automatically chosen")
                    sep()
            if actions == 0:
                clear()
                filename = input("save to (no file extension): ")
                try:
                    with open(f"{filename}.qcmd", "w") as f:
                        stred = json.dumps(questions)
                        stred = base64.b64encode(bytes(stred, encoding="utf-8"))
                        stred = stred[::-1]
                        _temp = []
                        for char in stred.decode(encoding="utf-8"):
                            _temp.append(chr(ord(char) << 2))
                        f.write("".join(_temp))
                    clear()
                    print(f"quizz saved to {filename}.qcmd successfully")
                except PermissionError:
                    with open(f"backup_{time.strftime("%d_%m_%Y", time.gmtime())}.qcmd", "w") as f:
                        json.dump(questions, f)
                    clear()
                    #print(f"quizz failed to save to {filename}.qcmd so we've created a backup for you")
                    error(f"failed to save to {filename}.qcmd", "backup has been created in the current folder")
                sep()
                break
    if mainMenu == 2:
        clear()
        filename = input("open (no file extension): ")
        try:
            with open(f"{filename}.qcmd", "r") as f:
                _temp = []
                for char in f.read():
                    _temp.append(chr(ord(char) >> 2))
                stred = "".join(_temp)[::-1]
                stred = base64.b64decode(bytes(stred, encoding="utf-8"))
                questions = json.loads(stred.decode(encoding="utf-8"))
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
        except FileNotFoundError:
            clear()
            #print("quizz not found")
            error(f"quizz {filename}.qcmd was not found")
            sep()
        
    if mainMenu == 0:
        clear()
        print(random.choice(byeMSGS))
        exit()
    if mainMenu == 4:
        clear()
        print("""CuestioMD v0.2 - made by greg with love and patience in Python 3.12
licensed under the MIT license - you're allowed to redistribute as long as you credit me""")
        sep()
    if mainMenu == 3:
        clear()
        #print("work in progess - come back later!")
        warning("work in progress", "come back later!")
        sep()