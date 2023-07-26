from defs import choices, linha, color, find_answer_in_string
from time import sleep
import time
from fractions import Fraction
from sql.entities.ENEM import EnemAnswers_Repository
from sql.entities.SAT import SatAnswer_Repository

repo_enem = EnemAnswers_Repository()
repo_sat = SatAnswer_Repository()

while True:
    linha()
    print(color("""GABARITECH""", "Blue").center(69))
    print("""Which test mode do you want??
(1) - ENEM
(2) - SAT 
(3) - Timer """) 
    linha()
    chosen1 = choices(3)

    #MODELO ENEM
    if chosen1 == 1: 
        while True:
            linha()
            print(color("""MODELO ENEM""", "Blue").center(69))
            print("What do you wanna do??")
            print("""(1) - See the test answers
(2) - Create a new test answer
(3) - Check the results
(4) - Back""")
            linha()
            chosen2 = choices(4)
            
            #See all the test anwers
            if chosen2 == 1:
                linha()
                test_answers = repo_enem.select()
                if test_answers == []: #Checking how many test answers saves have
                    print(color("You did'nt save any test yet", "Red").center(69))
                    sleep(3)
                    continue
                else:   
                    print("Do you want see the result of which test??")
                    for test in test_answers:
                        print(f"{test.id} - {test.title}")
                    test_choice = choices(len(test_answers))

                #Showing the gabarito
                while True:
                    linha()
                    answers = repo_enem.select_question(test_choice)
                    answers = answers.split(",")
                    cont = 0
                    for answer in answers:
                        cont += 1
                        print(f"({cont}) - {answer}")

                    print("""\n
(1) - Repair
(2) - Continue\n""")
                    chosen4 = choices(2)
                    
                    #Repair the test answer
                    if chosen4 == 1:
                        while True:
                            try:
                                error_line = int(input("(?): "))
                                break
                            except:
                                print(color("Please, only numbers!!", "Red"))
                                sleep(1)
                                continue
                        repair = input(f"({error_line}) - :")
                        repo_enem.update(error_line, repair)
                                               
                    if chosen4 == 2:
                        break
            
            #Save test gabarito in data
            elif chosen2 == 2:
                linha()
                results = []
                test_title = str(input("Choose a title to the test answer: "))
                
                #Inputing the gabarito of the test
                for i in range(5):
                    while True:
                        question = str(input(f"Question {i+1}: ")).upper()
                        Anwers_options = ["A", "B", "C", "D", "E"]
                        if question in (Anwers_options):
                            results.append(question)
                            break
                        else:
                            print(color("Please, only choice A, B, C, D or E", "Red").center(69))
                            continue
                
                #Saving the data
                joined_results = ",".join(results)
                repo_enem.insert(test_title, joined_results)
                continue
            
            #Check the results with the test in data
            elif chosen2 == 3:
                linha()
                results = []
                answers = repo_enem.select()
                if answers == []:
                    print(color("You did'nt save any test yet", "Red").center(69))
                    sleep(3)
                    continue
                else:
                    print("Do you wanna check the results of which test??")
                    for answer in answers:
                        print(answer)
                test_choice = choices(len(answers))
                
                #Inputing the results of the test
                for i in range(5):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                linha()
                sleep(1)
                print("$ = Correct\nX = Wrong\n\n")
                sleep(2)
                
                #Colecting the gabarito as a list
                gabarito = repo_enem.select_question(test_choice) #Respostas | if marcadas == respostas: (correct)
                for i in range(5):
                    if results[i] in gabarito[i]:
                        print(f"({i+1}) = {results[i]} - {color('$', 'Green')}")
                    else:
                        print(f"({i+1}) = {results[i]} - {color('X', 'Red')} [{find_answer_in_string(gabarito[i])}]")
                linha()
                sleep(4)
                break
            
            #back
            elif chosen2 == 4:
                break
    
    
    #MODELO SAT
    elif chosen1 == 2:
        while True:
            linha()
            print(color("""MODELO SAT""", "Blue").center(69))
            print("What do you wanna do??")
            print("""(1) - See the test answers 
(2) - Create a new test answer
(3) - Check the results
(4) - Back""")
            linha()
            chosen3 = choices(4)
            
            #See all test answers
            if chosen3 == 1: 
                linha()
                
                #Checking how many test answers saves have
                test_answers = repo_sat.select()
                
                if test_answers == []:
                    print(color("You did'nt save any test yet", "Red").center(69))
                    sleep(3)
                    continue
                
                else:
                    if len(test_answers) == 1:
                        repo_sat.fix_id(test_answers[0].id)
                    sleep(1)
                    print("Do you want see the result of which test??")
                    for test in test_answers:
                        print(f"{test.id} - {test.title}")
                    test_choice = choices(len(test_answers))

                #Showing the gabarito
                while True:
                    linha()
                    answers = repo_sat.select_question(test_choice)
                    answers = answers.split(",")
                    cont = 0
                    show_cont = 0
                    print(color("READING", "Yellow").center(69))
                    
                    for answer in answers:
                        cont += 1
                        show_cont += 1
                        
                        if cont == 52:
                            print(color("WRITING", "Yellow").center(69))
                            show_cont = 1
                        
                        if cont == 96:
                            print(color("MATH", "Yellow").center(69))
                            show_cont = 1
                        
                        if cont == 116:
                            print(color("MATH WITH CALCULATOR", "Yellow").center(69))
                            show_cont = 1
                        
                        print(f"({show_cont}) - {answer}")

                    print("""\n
(1) - Continue
(2) - Delete\n""")
                    chosen4 = choices(2)

                    #Deleting the test answer (Here is better delete, because there is a lot of issues involved)
                    #Consider put in a next version a repair in the SAT Test Answer Save!
                    if chosen4 == 1: 
                        break
                
                    if chosen4 == 2:
                        repo_sat.delete(test_choice)
                        print(color("\nSucessfull Deleted!", "Green".center(69)))
                        linha()
                        break
            
            #Save a test answers
            if chosen3 == 2: 
                linha()
                reading = []
                writing = []
                math = []
                mathC = []
                
                #Inputing the title of the test answer
                sat_title = input("What is the name of this test: ")
                linha()
                
                #Inputing the gabarito of the test
                print(color("READING", "Yellow").center(69))
                for i in range(52):
                    while True:
                        question = str(input(f"Question {i+1}: ")).upper()
                        question_options = ["A", "B", "C", "D"]
                        if question in question_options:
                            reading.append(question)
                            break
                        else:
                            print(color("Please, only choice A, B, C, D", "Red").center(69))
                            continue
                
                print(color("WRITING", "Yellow").center(69))
                for i in range(44):
                    while True:
                        question = str(input(f"Question {i+1}: ")).upper()
                        question_options = ["A", "B", "C", "D"]
                        if question in question_options:
                            writing.append(question)
                            break
                        else:
                            print(color("Please, only choice A, B, C, D", "Red").center(69))
                            continue
                
                print(color("MATH", "Yellow").center(69))
                for i in range(20):
                    if i < 15:
                        while True:
                            question = str(input(f"Question {i+1}: ")).upper()
                            question_options = ["A", "B", "C", "D"]
                            if question in question_options:
                                math.append(question)
                                break
                            else:
                                print(color("Please, only choice A, B, C, D", "Red").center(69))
                                continue
                    else:
                        while True: #Tratamento de erro liberal
                            try:
                                question = input(f"Question {i+1}: ")  
                                math.append(question)
                                break   
                            except:
                                print(color("Please, only float and fractions numbers in this part of section!", "Red").center(69))        
                                continue

                print(color("MATH - CALCULATOR", "Yellow").center(69))
                for i in range(38):
                    if i < 30:
                        while True:
                            question = str(input(f"Question {i+1}: ")).upper()
                            question_options = ["A", "B", "C", "D"]
                            if question in question_options:
                                mathC.append(question)
                                break
                            else:
                                print(color("Please, only choice A, B, C, D", "Red").center(69))
                                continue
                    else:
                        while True:
                            try:
                                question = input(f"Question {i+1}: ")
                                mathC.append(question)
                                break   
                            except:
                                print(color("Please, only float and fractions numbers in this part of section!", "Red").center(69))        
                                continue
                
                data = []
                
                #Saving the all the data
                for line in reading:
                    data.append(line)

                for line in writing:
                    data.append(line)

                for line in math:
                    data.append(line)

                for line in mathC:
                    data.append(line)

                joined_data = ",".join(data)
                repo_sat.insert(sat_title, joined_data)
           
           #Check the results with the test in data
            elif chosen3 == 3: 
                linha()
                results = []
                
                #Checking how many tests saves have
                answers = repo_sat.select()
                if answers == []:
                    print(color("You did'nt save any test yet", "Red").center(69))
                    sleep(3)
                    continue
                else:
                    if len(answers) == 1:
                        repo_sat.fix_id(answers[0].id)
                    print("Do you wanna check the results of which test??")
                    for answer in answers:
                        print(answer)
                test_choice = choices(len(answers))
                
                #Inputing the results of the test
                print(color("READING", "Yellow").center(69))
                for i in range(52):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                print(color("WRITING", "Yellow").center(69))
                
                for i in range(44):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                print(color("MATH", "Yellow").center(69))
                
                for i in range(20):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                print(color("MATH - CALCULATOR", "Yellow").center(69))
                
                for i in range(38):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                
                linha()
                sleep(1)
                print("$ = Correct\nX = Wrong\n\n")
                sleep(2)
                
                #Colecting the gabarito as a list
                gabarito = repo_sat.select_question(test_choice)
                gabarito = gabarito.split(",") #Respostas | if marcadas == respostas: (correct)
                for i in range(154):
                    if i == 0:
                        print(color("READING", "Yellow").center(69))
                    elif i == 52:
                        print(color("WRITING", "Yellow").center(69))
                    elif i == 96:
                        print(color("MATH", "Yellow").center(69))
                    elif i == 116:
                        print(color("MATH - CALCULATOR", "Yellow").center(69))
                    elif results[i] in gabarito[i]:
                        print(f"({i+1}) = {results[i]} - {color('$', 'Green')}")
                    else:
                        print(f"({i+1}) = {results[i]} - {color('X', 'Red')} [{find_answer_in_string(gabarito[i])}]")
                linha()
                sleep(4)
                break
            
            #back
            elif chosen3 == 4:
                break
    
    
    #Timer
    elif chosen1 == 3:
        linha()
        print(color("SAT TIMER", "Blue").center(69))
        datas = []
        while True:
            start_time = 0
            true_break = False
            end_time = 0
            running = False
            
            while True:
                input_key = input("Press 'enter' to start/stop the timer and 'x' to finish!: ")
                if input_key == "x":
                    linha()
                    print(color("Avarege time", "Green").center(69))
                    print('\n')
                    total = 0
                    for data in datas:
                        print(data)
                        only_number = float(data.replace("Elapsed time: ", "").replace("seconds.", ""))
                        total += only_number
                    totaln = len(datas)
                    if totaln == 0:
                        totaln = 1
                    mean = total/totaln
                    print("\n")
                    print("Mean Time: "+  color("{:.2f}", "Green").format(mean))
                    sleep(5)
                    true_break == True
                    break  
                
                else: 
                    if not running:
                        running = True
                        start_time = time.time()
                        print("Timer started.")
                    else:
                        running = False
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        print("Timer stopped. Elapsed time:  " + color("{:.2f}", "Green").format(elapsed_time) + " seconds...")
                        datas.append("Elapsed time: {:.2f} seconds.".format(elapsed_time))
                        break
            if true_break:
                break
        