from config.config import * # importing pips and funcs from config file
os.system(cl())
time = JalaliDate.today()

send_to_tel = False

# is saved chat id ? (if output = True )
try:
    chat_id_file = open("data/chat_id/chat_id.txt", "r")
    chat_id = chat_id_file.read()
    chat_id_file.close()

    if chat_id != '':
        send_to_tel = False
    else:
        send_to_tel = True
except :
    send_to_tel = True


while True :
    pass
    numb_file = open("data/numb/numb.txt", "r") # open, read and close number file (number file is a long term Var)
    numb = numb_file.read()
    numb_file.close()

    os.system(cl())
    view(time)
    print (Fore.WHITE, khat)
    print (Fore.GREEN, "options:\n")
    
    if send_to_tel == False: 
        print (Fore.WHITE, "1) add to todo list \n 2) remove from todo list \n 3) clear todo list \n 4) Mark as done \n 5) my telegram info")
    else:
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
    
    if send_to_tel == False and option == '5':
        option = '6'
    
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
                send(file.read(), chat_id) # send to telegram of the user
            except:
                pass

        except:
            print(Fore.RED, "error")
            sleep(5)

    # starting opts
    elif option == '5': # give chat id from user 
        if send_to_tel == False:
            print(Fore.RED, "your chat ID is already saved")
            sleep(5)
        else:
            print("ok firs start this bot: @Bedon_Todo_Bot")
            sleep(5)

            chat_id = input ("print your telegram chat id (give from @RawDataBot): ").strip()
            try:
                try:
                    code = random.randint(111112, 999999)
                    redy_for_send_code = str(str(code)[0] + str(code)[1] + str(code)[2] + '-' + str(code)[3] + str(code)[4] + str(code)[5])
                    send_code = (send(f"your confirm code is: {redy_for_send_code}", chat_id))
                    check_code = input('enter sended code in telegram:  ').strip()

                    if check_code == str(code) or check_code == redy_for_send_code:
                        status = (send('hi, Your information has been confirmed ;)', chat_id))
                        if status.status_code == 200:
                            try:
                                chat_id_file = open("data/chat_id/chat_id.txt", "a+")
                                chat_id_file.write(chat_id)
                                chat_id_file.close()
                            except:
                                print(Fore.RED, 'error (saving data, creat a "chat id" folder in /bedoon/bedoon/data/)')
                                sleep(3)
                                break
                                

                            print(Fore.GREEN, status.status_code)
                            print(Fore.GREEN, "ok, Your information has been confirmed ; . close app and open agein)", Fore.WHITE)
                            sleep(5)
                            break

                        else:
                            print(Fore.RED, 'error (internet)')
                            sleep(3)
                    else:
                        print(Fore.RED, 'error (invalid code)')
                        sleep(3)
                except:
                    print(Fore.RED, status.status_code)
                    print(Fore.RED, "error your chat id is not crract or you have internet error")
                    os.remove("data/chat_id/chat_id.txt")
                    sleep(5)
            except:
                print(Fore.RED, "error (we dont know what is prublem but meybe your connectin is denid)")
                sleep(5)


    elif option == '6':

        if send_to_tel == False:
            while True:
                os.system(cl())
                print(Fore.GREEN, time)
                print (Fore.WHITE, khat)
                print (Fore.GREEN, "options:\n")
                print (Fore.WHITE, "1) delet chat id \n 2) replase chat id \n 3) exit")

                print (khat)

                if chat_id == "":
                    print(Fore.RED, "your telegram is not set", Fore.WHITE)
                else:
                    print(chat_id)


                print (Fore.WHITE, khat)
                telegrams_opt = input ("select option (1...3): ").strip()

                if telegrams_opt ==  '1':
                    print(Fore.RED)
                    delet_confirm = input("are you sure ? (y - n):  ").strip()
                    print(Fore.WHITE)

                    if 'y' in delet_confirm.lower():
                        try:
                            os.remove("data/chat_id/chat_id.txt")
                            open ("data/chat_id/chat_id.txt", 'a+')
                            print(Fore.GREEN, 'your chat id deleted')
                            sleep(3)
                            break

                        except:
                            print (Fore.RED, 'error')
                            sleep(3)


                elif telegrams_opt == '2':
                    try:
                        new_chat_id = input('enter new chat id: ').strip()
                        if new_chat_id == chat_id:
                            print (Fore.RED, "this chat id is alredy saved", Fore.WHITE)
                            sleep(3)

                        else:
                            try:
                                try:
                                    code = random.randint(111112, 999999)
                                    redy_for_send_code = str(str(code)[0] + str(code)[1] + str(code)[2] + '-' + str(code)[3] + str(code)[4] + str(code)[5])
                                    send_code = (send(f"your confirm code is: {redy_for_send_code}", new_chat_id))
                                    check_code = input('enter sended code in telegram:  ').strip()

                                    if check_code == str(code) or check_code == redy_for_send_code:
                                        status = (send('hi, Your information has been confirmed ;)', new_chat_id))
                                        if status.status_code == 200:
                                            try:
                                                os.remove("data/chat_id/chat_id.txt")
                                                chat_id_file = open("data/chat_id/chat_id.txt", "a+")
                                                chat_id_file.write(new_chat_id)
                                                chat_id_file.close()
                                            except:
                                                print(Fore.RED, 'error (saving data, creat a "chat id" folder in /bedoon/bedoon/data/)')
                                                sleep(3)
                                                break


                                            print(Fore.GREEN, status.status_code)
                                            print(Fore.GREEN, "ok, Your information has been confirmed ; . close app and open agein)", Fore.WHITE)
                                            resave = True
                                            sleep(5)
                                            break

                                        else:
                                            print(Fore.RED, 'error (internet)')
                                            sleep(3)

                                    else:
                                        print(Fore.RED, 'error (invalid code)')
                                        sleep(3)

                                except:
                                    print(Fore.RED, status.status_code)
                                    print(Fore.RED, "error your chat id is not crract or you have internet error")
                                    os.remove("data/chat_id/chat_id.txt")
                                    sleep(5)
                            except:
                                print(Fore.RED, "error (we dont know what is prublem but meybe your connectin is denid)")
                                sleep(5)
                    except:
                        print(Fore.RED, "error(we dont know)")

                elif telegrams_opt == '3':
                    break

            try:
                if resave == True:
                    break
            except:
                pass


        else:
            print(Fore.RED, "invalid command", Fore.WHITE)
            sleep(3)

    elif option == 'exit' or option == 'EXIT' or option == 'e' or option == 'E':
        print(Fore.RED, "good bye")
        sleep(3)
        exit()

    else:
        print(Fore.RED, "invalid command", Fore.WHITE)
        sleep(3)
