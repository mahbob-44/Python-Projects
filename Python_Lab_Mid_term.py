import time as tm
class Star_Cinema:
    __hall_list=[]
    def entry_hall(self):
        self.__hall_list.append(self)

class Hall(Star_Cinema):
    __seats={}
    __show_list=[]
    def print_line(self,num):
        for i in range(num):
            if i<num-1:
                print("-",end="")
            else:
                print("-")

    def __init__(self,rows,cols,hall_no):
        self.__row=rows
        self.__col=cols
        self.hall_no=hall_no
        super().__init__()
        self.entry_hall()

    def seat_availability(self,id):
        for i in range(0,self.__row):
            for j in range(0,self.__col):
                if self.__seats[id][i][j]==0:
                    return True
        return False

    def entry_show(self,id,movie_name,time):
        tuple=(id,movie_name,time)
        self.__show_list.append(tuple)
        list=[[0 for i in range(self.__row)] for j in range(self.__col)]
        self.__seats[id]=list

    def book_seats(self,name,phone,show_id,tup):
        __flag=0
        self.print_line(100)
        if tup[0]<self.__row and tup[0]>=0 and tup[1]-1<self.__col and tup[1]-1>=0:
            if show_id in self.__seats:
                if self.__seats[show_id][tup[0]][tup[1]-1]==0:
                    self.__seats[show_id][tup[0]][tup[1]-1]=1
                    print(f"The seat {chr(tup[0]+65)}{tup[1]} booking is successfull!!!")
                    print(f'Name:{name}\t\t\t\t\tShow ID:{show_id}\nContact NO: {phone}\t\t\t\t\t',end='')
                    for i in range(len(self.__show_list)):
                        for j in range(len(self.__show_list[i])):
                            if self.__show_list[i][0]==show_id:
                                print(f"Show name: {self.__show_list[i][1]}\nSeat Number:{chr(tup[0]+65)}{tup[1]}\t\t\t\t\t\tShow starting time: {self.__show_list[i][2]}")
                                __flag=1
                                break
                        if __flag==1:
                            break
                else:
                    print(f"Sorry {name}! The seat {chr(tup[0]+65)}{tup[1]} is already booked")
            else:
                print(f"Sorry {name}! the show id {show_id} is not in the show list")
        else:
            print(f"Sorry {name}! the seat {chr(tup[0]+65)}{tup[1]} is not valid.")
        self.print_line(100)

    def view_show_list(self):
        print('')
        self.print_line(100)
        print("The show list of today is given below.")
        for i in self.__show_list:
            print(f"Show ID:{i[0]}\t\t\tShow name: {i[1]}\t\t\tSarting time: {i[2]}")
        self.print_line(100)

    def view_available_seats(self,id):
        print('\n')
        self.print_line(97)
        if id in self.__seats:
            print(f"The available seats for show {id} is shown below.\n")
            print("Note: Unavailable seats are marked as (>^.^<)")
            self.print_line(97)
            for i in range(0,self.__row):
                for j in range(0,self.__col):
                    if self.__seats[id][i][j]==0:
                        if j ==0:
                            print(f"|\t{chr(i+65)}{j+1}\t|",end='\t')
                        else:
                            print(f"{chr(i+65)}{j+1}\t|",end='\t')
                    elif self.__seats[id][i][j]==1:
                        if j ==0:
                            print(f"|\t(>^.^<)\t|",end='\t')
                        else:
                            print(f"(>^.^<)\t|",end='\t')
                print('')
                self.print_line(97)
            self.print_line(97)
        else:
            self.print_line(97)
            print("The show id you entered is invalid. Please enter a valid show id")
            self.print_line(97)
            
def print_line(num):
    for i in range(num):
        if i<num-1:
            print("-",end="")
        else:
            print("-")

Dhaka_hall=Hall(6,6,505)

Dhaka_hall.entry_show("5005","SHUTTER ISLAND","10:00 am")
Dhaka_hall.entry_show("6006","TENET","12:00 pm")
Dhaka_hall.entry_show("7007","INTERSTELLAR","2:00 pm")

running=True
wrong_choice_count=1
print_line(100)
print("\t\tWellcome to the Ticket booking system of DHAKA CINEMA HALL")
print_line(100)
while running:
    print_line(23)
    print("1.View all shows today.")
    print('2.View available seats.')
    print("3.Book seat")
    print("4.Exit")
    print_line(23)
    choice=int(input("Choose an option: "))
    print_line(100)
    if choice==1:
        Dhaka_hall.view_show_list()
    elif choice==2:
        id=input("Enter the id of show to see the available seats of that show: ")
        Dhaka_hall.view_available_seats(id)
    elif choice==3:
        name=input(f"Enter your name: ")
        phone=input(f"Enter your phone number: ")
        number_of_seats=int(input("How many ticket do you want to buy?\nEnter your answer here: "))
        show_id=input(f"Enter the show id: ")
        if Dhaka_hall.seat_availability(show_id):
            Dhaka_hall.view_available_seats(show_id)
            for i in range(0,number_of_seats):
                seat=input("Enter the seat number: ")
                row=ord(seat[0])-ord('A')
                col=ord(seat[1])-ord('0')
                Dhaka_hall.book_seats(name,phone,show_id,(row,col))
        else:
            print_line(81)
            print(f"Sorry {name}! There are no seat available of your required show.")
            print_line(81)
            continue
    elif choice==4:
        break
    else:
        print_line(100)
        if wrong_choice_count==5:
            print("You have entered wrong choice 5 times. No body is allowed to insert wrong choice more than five times.\nSo we are taking you out  from this ticket booking system.")
            print_line(100)
            break
        else:
            if wrong_choice_count==4 or wrong_choice_count==3:
                print("You are choosing wrong option multiple times. Be carefull! You are allowed to give wrong choice for \n5 times.")
            else:
                print(f"{choice} is not a valid option please select a valid option.")
            wrong_choice_count+=1
        print_line(100)
