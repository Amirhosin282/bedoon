from config.config import * # importing pips and funcs from config file
os.system(cl())

try:
    chat_id_file = open("data/chat_id/chat_id.txt", "r")
    chat_id = chat_id_file.read()
    chat_id_file.close()
except:
    pass

while True :
    numb_file = open("data/numb/numb.txt", "r") # open, read and close number file (number file is a long term Var)
    numb = numb_file.read()
    numb_file.close()

    os.system(cl())
    print (Fore.GREEN, time)
    print (Fore.WHITE, khat)
    print (Fore.GREEN, "options:\n")
    print (Fore.WHITE, "1) add to todo list \n 2) remove from todo list \n 3) clear todo list \n 4) Mark as done \n 5) send me tasks in telegram")

    print (khat)
    print (Fore.GREEN, "todo list:\n", Fore.WHITE)
    
    for i in range(int(numb)): # show tasks to user
        if str(numb) == '1':
            print("you are not have any task")
            break
        
        if i == 0:
            pass
        else:
            try:
                tasks = open(f"data/TASK{str(i)}", "r")
                print(Fore.GREEN, i, Fore.WHITE, tasks.read())
                tasks.close()
            except:
                print(Fore.RED, "error")

    print (Fore.WHITE, khat)
    option = input ("select option (1...5): ").strip()
    
    if option == '1': # if user select option 1
        todo = input("print your todo text: ").strip()

        todo_file = open(f"data/TASK{numb}", "a+")
        todo_file.write(todo)
        todo_file.close()
        
        os.remove("data/numb/numb.txt")
        numb_file = open("data/numb/numb.txt", "a+")
        numb_file.write(str(int(numb) + 1))
        numb_file.close()
        try:
            send ("new task added:   " + todo, chat_id)
        except:
            pass
    
    elif option == '2':
        todo = input("print task number: ").strip()
        try:
            os.remove(f"data/TASK{todo}")
            os.remove("data/numb/numb.txt")
            numb_file = open("data/numb/numb.txt", "w+")
            numb_file.write(str(int(numb) - 1))
            numb = str(int(numb) - 1)
            numb_file.close()
            
            for i in range(int(numb) + 1):
                if i <= int(todo):
                    pass
                else:
                    os.rename(f"data/TASK{str(i)}", f"data/TASK{str(int(i) - 1)}")

        except:
            print(Fore.RED, f'not have {todo} task')
            sleep(5)
        
    elif option == '3':
        for i in range (int(numb)):
            if i == 0:
                pass
            elif int(numb) == 1:
                print(Fore.RED, "you don't have any tasks")
                sleep(3)
                break
            else:
                os.remove(f"data/TASK{i}")
        os.remove("data/numb/numb.txt")
        numb_file = open("data/numb/numb.txt", "a+")
        numb_file.write("1")
        numb_file.close()

    elif option == '4':
        todo = input("print number of task: ").strip()
        try:
            file = open(f"data/TASK{todo}", "a+")            
            file_titel = file.read()
            file.write(f"{file_titel}    Done ✔")
            file.close()
            
            try:
                file = open (f"data/TASK{todo}", "r")
                send(file.read(), chat_id) # send to user telegram
            except:
                pass

        except:
            print(Fore.RED, "error")
            sleep(5)

    elif option == '5': # give chat id from user 
        print("ok firs start this bot: @Bedon_Todo_Bot")
        sleep(5)
        
        chat_id = input ("print your telegram chat id (give from @RawDataBot): ").strip()
        chat_id_file = open("data/chat_id/chat_id.txt", "a+")
        chat_id_file.write(chat_id)
        chat_id_file.close()
        try:
            send('hi, Your information has been confirmed ;)', chat_id)
            print(Fore.GREEN, "ok, Your information has been confirmed ;). close app and open again", Fore.WHITE)
            sleep(5)
            break
        except:
            print(Fore.RED, "error your chat id is not crract")
            sleep(5)

    elif option == 'exit' or option == 'EXIT' or option == 'e' or option == 'E':
        print(Fore.RED, "good bye")
        sleep(3)
        exit()

    else:
        print(Fore.RED, "invalid command", Fore.WHITE)
        sleep(3)