####################################
# FP1-S01 Dictionaries Program
# Reid A. Martin
# 13 October 2021
####################################

import random

subject_list = {}
#overall_avg = subject_list.values()
class_list = {}

good = ["Keep up the great work!", "Don't let your marks drop!", "Look at you go, SUPERSTAR!!!"]
bad = ["Let's try harder on the next go...", "C'mon, I know you can do better.", "Maybe you could get a little more help."]



def add_subject():
    done = False
    while done == False:
        subject = input("What class would you like to add? Type 'done' when you have added the classes.\n>").lower() #key variable
        if subject == "done": # if true goes back to menu
            done = True
        elif subject != "done":
            grade = False
            while grade == False:
                class_avg = float(input("What is the class' average? IN PERCENT WITHOUT THE SIGN\n>")) #class average
                avg_mark = input("Is your average already calculated?\n>").lower()
                if avg_mark == "yes" or avg_mark == "y":
                    average = float(input("Please enter your mark as a number WITH NO PERCENT SIGN. Ex. 89.3\n>")) #pre done average
                    print("Adding", subject, "with an average of", average, "%")
                    subject_list[subject] = average # adds values to dicts
                    class_list[subject] = class_avg # adds values to dicts
                    #print(subject_list)
                    grade = True
                elif avg_mark == "no" or avg_mark == "n": # calculates class average with individual marks
                    total = 0
                    print("no")
                    multiple = int(input("How many marks are you entering?\n>"))
                    for i in range(multiple):
                        mult_mark = float(input("Please enter your mark as a number WITH NO PERCENT SIGN. Ex. 89.3\n>"))
                        total = total + mult_mark
                        average = total/multiple
                    print("Adding", subject, "with an average of", average, "%")
                    subject_list[subject] = average
                    class_list[subject] = class_avg
                    #print(subject_list)
                    grade = True
                    #done1 = True
                else:
                    print("Please type yes or no.")
        else:
            print("That's not an option.")
    
    
def remove_class(): #iff the class is in a dictionary it is then removed, if not if won't 
    done = False
    while done == False:
        #for subject in subject_list:
        view_personal()
           # print(subject)
        rmv_class = input("What class would you like to delete?\n>").lower()
        if rmv_class in subject_list:
            subject_list.pop(rmv_class, None)
            class_list.pop(rmv_class, None)
            view_personal()
            #print(subject_list)
            done = True
        else:
            print("Please pick a class in the list")
    
def view_personal():# states classes and averages
    for key in subject_list:
        print ("In", key, ", your average is...", subject_list[key])
        
def view_class():# states classes and the class' averages
    for key in class_list:
        print ("In", key, ", the class' average is...", class_list[key])

def personal_avg(): #total personal average
     all_add = subject_list.values()
     total = sum(all_add)
     p_avg = float(total / len(subject_list))
     return p_avg

def class_avg(): #total class average
     all_add = class_list.values()
     total = sum(all_add)
     c_avg = float(total / len(class_list))
     return c_avg


def main():
    done1 = False
    print(f"**********************************************\nWelcome to the Class Program!\nWhat would you like to do?")
    while done1 == False: #select a function
        print("**********************************************")
        choice = input("""1. Input subjects
2. Remove a subject
3. Check your scores
4. Check the class score
5. See your overall average
6. See the class' overall average
7. Exit
>""")
    
        if choice == "1":
            add_subject() #add
          #  done1 = True
        elif choice == "2" and len(subject_list) > 0: #there has to be classes for this to work
            remove_class()#remove
            
        elif choice == "3" and len(subject_list) > 0:#there has to be classes for this to work
            view_personal() #view classes and averages
            
        elif choice == "4" and len(subject_list) > 0:#there has to be classes for this to work
            view_class()#view classes and the class avgs
            
        elif choice == "5" and len(subject_list) > 0:#there has to be classes for this to work
            print("Your overall average is", personal_avg()) #overall average with random message
            if personal_avg() < 69:
                print(random.choice(bad))
            elif personal_avg() > 69:
                print(random.choice(good))
            elif personal_avg() == 69:
                print("you have won at life.")
                
        elif choice == "6" and len(subject_list) > 0:#there has to be classes for this to work
            print("The class' overall average is", class_avg()) #overall class avg
            
        elif choice == "7":
            if len(subject_list) > 0:
                print("Your average is", personal_avg()) #if classes in list then prints avg
            print("See You!")
            done1 = True #breaks while loop
        else:
            print("Please pick a real option or add subjects")
         
         
################################         
main() #main code

#add_subject()
#print (subject_list)
#view_class()

#remove_class()