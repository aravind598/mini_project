from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox
import pickle

list_of_days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
date_track = datetime.date.today()
day_track = date_track.weekday()
# other_date = datetime.date.today()
# other_day = 0
time_track = datetime.datetime.now().time()
str_time_track = time_track.strftime("%H:%M:%S")

#import pickled menu file
in_menus = open('menus','r+b')
menus = pickle.load(in_menus)
in_menus.close()

#import pickled menu file
in_times = open('times','r+b')
times = pickle.load(in_times)
in_times.close()

def back_1():
    global m, back_button, day_track
    m.choose_label.forget()
    for i in m.stalls:
        if day_track in i:
            for j in range(len(m.stalls[i])):
                m.stalls[i][j].forget()
    back_button.forget()
    m.welcome_message.pack()
    m.B1.pack(pady=10)
    m.B2.pack()
    m.B3.pack(side=BOTTOM, fill=X, pady=15)


def back_2():
    global m, back_button
    m.choose_date.grid_forget()
    m.year_label.grid_forget()
    m.year_entry.grid_forget()
    m.month_label.grid_forget()
    m.month_entry.grid_forget()
    m.day_label.grid_forget()
    m.day_entry.grid_forget()
    m.hour_label.grid_forget()
    m.hour_entry.grid_forget()
    m.minute_label.grid_forget()
    m.minute_entry.grid_forget()
    m.enter_button.grid_forget()
    m.blank.grid_forget()
    back_button.grid_forget()
    m.blank2.grid_forget()
    m.enter_button.grid_forget()
    m.welcome_message.pack()
    m.B1.pack(pady=10)
    m.B2.pack()
    m.B3.pack(side=BOTTOM, fill=X, pady=15)
    back_button = Button(m.frame, text="Back", bg="BLUE", width=10,
                         command=lambda: back_to_prev_page(1))


def back_3():
    global m, back_button, other_day
    m.choose_label.pack_forget()
    for i in m.stalls:
        if input_day in i:
            for j in range(len(m.stalls[i])):
                m.stalls[i][j].forget()
    back_button.pack_forget()
    m.choose_date.grid(row=0, column=0, columnspan=6)
    m.blank.grid(row=1)
    m.day_label.grid(row=2, column=0)
    m.day_entry.grid(row=2, column=1)
    m.month_label.grid(row=2, column=2)
    m.month_entry.grid(row=2, column=3)
    m.year_label.grid(row=2, column=4)
    m.year_entry.grid(row=2, column=5)
    m.hour_label.grid(row=4, column=0)
    m.hour_entry.grid(row=4, column=1)
    m.minute_label.grid(row=4, column=2)
    m.minute_entry.grid(row=4, column=3)
    m.blank2.grid(row=5)
    m.enter_button.grid(row=6, column=0, columnspan=6)
    back_button = Button(m.frame, text="Back", bg="BLUE", width=10,
                         command=lambda: back_to_prev_page(2))
    back_button.grid(row=7, column=0, columnspan=6)


def back_4():
    global m, back_button, input_day, input_time
    back_button = Button(m.frame, text="Back", bg="BLUE", width=10,
                         command=lambda: back_to_prev_page(1))
    m.choose_label.pack()
    # for i in m.stalls:
    #     if day_track in i:
    #         for j in range(len(m.stalls[i])):
    #             m.stalls[i][j].pack(pady=5, fill=X)
    m.which_menu()
    back_button.pack(pady=10, fill=X)


def back_5():
    global m, back_button, input_day, input_time
    back_button = Button(m.frame, text="Back", bg="BLUE", width=10,
                         command=lambda: back_to_prev_page(3))
    m.choose_label.pack()
    # for i in m.stalls:
    #     if day_track in i:
    #         for j in range(len(m.stalls[i])):
    #             m.stalls[i][j].pack(pady=5, fill=X)
    m.which_menu()
    back_button.pack(pady=10, fill=X)


def back_to_prev_page(x):
    global m, back_button

    if x == 1:
        back_1()

    elif x == 2:
        back_2()

    elif x == 3:
        back_3()

    elif x == 4:
        m.mcd.Welcome.grid_forget()
        m.date_text.grid_forget()
        for key, value in m.mcd.menu.items():
            m.mcd.menu[key].grid_forget()
            key.grid_forget()
        back_button.grid_forget()
        m.mcd.menubar.destroy()
        if m.choice == 1:
            back_4()
        else:
            back_5()

    elif x == 5:
        m.sub.Welcome.grid_forget()
        m.date_text.grid_forget()
        for key, value in m.sub.menu.items():
            m.sub.menu[key].grid_forget()
            key.grid_forget()
        back_button.grid_forget()
        m.sub.menubar.destroy()
        if m.choice == 1:
            back_4()
        else:
            back_5()

    elif x == 6:
        m.piz.Welcome.grid_forget()
        m.date_text.grid_forget()
        for key, value in m.piz.menu.items():
            m.piz.menu[key].grid_forget()
            key.grid_forget()
        back_button.grid_forget()
        m.piz.menubar.destroy()
        if m.choice == 1:
            back_4()
        else:
            back_5()

    elif x == 7:
        m.kfc.Welcome.grid_forget()
        m.date_text.grid_forget()
        for key, value in m.kfc.menu.items():
            m.kfc.menu[key].grid_forget()
            key.grid_forget()
        back_button.grid_forget()
        m.kfc.menubar.destroy()
        if m.choice == 1:
            back_4()
        else:
            back_5()

    elif x == 8:
        m.swg.Welcome.grid_forget()
        m.date_text.grid_forget()
        for key, value in m.swg.menu.items():
            m.swg.menu[key].grid_forget()
            key.grid_forget()
        back_button.grid_forget()
        m.swg.menubar.destroy()
        if m.choice == 1:
            back_4()
        else:
            back_5()


# Class deifinition for the main page

class MainPage:
    def __init__(self, master):
        global back_button, day_track, date_track, str_time_track, list_of_days, input_day, input_time
        self.frame = Frame(master)
        back_button = Button(self.frame, text="Back", bg="BLUE", command=lambda: back_to_prev_page(1))
        self.date_text = Label(self.frame, text = list_of_days[day_track] + ", " + str(date_track)
                                                  + ", " + str(str_time_track), bg="black", fg="white")

        self.welcome_message = Label(self.frame, text="Nanyang Technological University"
                                                      "\nWelcome to Canteen A Menu System ")
        self.B1 = Button(self.frame, text="View Today's stores", command=self.display_today_stalls, width=20,
                         activebackground="Yellow", bg="grey")
        self.B2 = Button(self.frame, text="View stores by other dates", width=20, command=self.get_other_day_stall,
                         activebackground="Yellow", bg="grey")
        self.B3 = Button(self.frame, text="Quit", bg="red", command=self.frame.quit)

        self.choice = 1

        self.mc_donalds = Button(self.frame, text="McDonalds", command=self.create_mcd)
        self.subway = Button(self.frame, text="Subway", command=self.create_subway)
        self.pizza_hut = Button(self.frame, text="Pizza Hut", command=self.create_pizza_hut)
        self.kfc = Button(self.frame, text="KFC", command=self.create_kfc)
        self.sandwich_guys = Button(self.frame, text="The Sandwich Guys", command=self.create_sandwich_guys)

        self.stalls = {(0, 1, 2, 3, 4, 5, 6): [self.mc_donalds, self.subway, self.pizza_hut, self.kfc], (0, 1, 2, 3, 4, 5): [self.sandwich_guys]}

        self.year_label = Label(self.frame, text = " / ")
        self.year_entry = ttk.Combobox(self.frame, values = [x for x in range(2019,2024)], width=5)
        self.month_label = Label(self.frame, text = " / ")
        self.month_entry = ttk.Combobox(self.frame, values = [x for x in range(1,13)], width=5)
        self.day_label = Label(self.frame, text = "Date: ")
        self.day_entry = ttk.Combobox(self.frame, values = [x for x in range(1,32)], width=5)
        self.hour_label = Label(self.frame, text = "Time: ")
        self.hour_entry = ttk.Combobox(self.frame, values = [x for x in range(0,24)], width=5)
        self.minute_label = Label(self.frame, text = " : ")
        self.minute_entry = ttk.Combobox(self.frame, values = ['{:02d}'.format(x) for x in range(0, 60)], width=5)
        self.enter_button = Button(self.frame, text=" ENTER ", command=self.check, activebackground="Green", width=10)

        self.error_label = Label(self.frame, text="INVALID !!!", fg="RED")

        self.back_button = Button(self.frame, text="Back", bg="BLUE", command=lambda: back_to_prev_page(1))
        self.choose_label = Label(self.frame, text="  Choose a store")
        self.choose_date = Label(self.frame, text=" Type in date/time or select from the dropdown boxes: ")
        self.blank = Label(self.frame, text="  ")
        self.blank2 = Label(self.frame, text="  ")
        self.display_mainpage()

    def display_mainpage(self):
        self.frame.pack()
        self.welcome_message.pack()
        self.B1.pack(pady=10)
        self.B2.pack()
        self.B3.pack(side=BOTTOM, fill=X, pady=15)

    def display_today_stalls(self):
        global back_button, day_track, date_track, str_time_track, list_of_days, input_day, input_date, input_time
        self.date_text = Label(self.frame, text=list_of_days[day_track] + ", " + str(date_track) + ", " + str(str_time_track), bg="black", fg="white")
        self.choice = 1
        self.B1.forget()
        self.B2.forget()
        self.B3.forget()
        self.welcome_message.forget()
        self.choose_label.pack()
        input_day = day_track
        input_date = date_track
        input_time = time_track
        self.which_menu()
        back_button.pack(side=BOTTOM, fill=X, pady=15)


    def no_input_stalls(self):
        global back_button, input_day, input_time,input_date, day_track, date_track, time_track
        self.choose_date.grid_forget()
        self.blank.grid_forget()
        self.blank2.grid_forget()
        self.enter_button.grid_forget()
        self.year_label.grid_forget()
        self.year_entry.grid_forget()
        self.month_label.grid_forget()
        self.month_entry.grid_forget()
        self.day_label.grid_forget()
        self.day_entry.grid_forget()
        self.hour_label.grid_forget()
        self.hour_entry.grid_forget()
        self.minute_label.grid_forget()
        self.minute_entry.grid_forget()
        self.enter_button.grid_forget()
        back_button.grid_forget()
        back_button = Button(self.frame, text="Back", bg="BLUE", width=10, command=lambda: back_to_prev_page(3))
        self.choose_label.pack()
        input_day = day_track
        input_date = date_track
        input_time = time_track
        self.which_menu()
        back_button.pack(pady=10, fill=X)

    def get_other_day_stall(self):
        global back_button
        self.choice = 2
        self.B1.forget()
        self.B2.forget()
        self.B3.forget()
        self.welcome_message.forget()
        self.choose_date.grid(row=0, column=0, columnspan=6)
        self.blank.grid(row=1)
        self.day_label.grid(row=2, column=0)
        self.day_entry.grid(row=2, column=1)
        self.month_label.grid(row=2, column=2)
        self.month_entry.grid(row=2, column=3)
        self.year_label.grid(row=2, column=4)
        self.year_entry.grid(row=2, column=5)
        self.hour_label.grid(row=4, column=0)
        self.hour_entry.grid(row=4, column=1)
        self.minute_label.grid(row=4, column=2)
        self.minute_entry.grid(row=4, column=3)
        self.blank2.grid(row=5)
        self.enter_button.grid(row=6, column=0, columnspan=6)
        back_button = Button(self.frame, text="Back", bg="BLUE", width=10, command=lambda: back_to_prev_page(2))
        back_button.grid(row=7, column=0, columnspan=6)

    def check(self):
        global input_date, input_day, input_time, day_track, date_track, time_track
        valid_date = True
        try:
            input_date = datetime.date(int(self.year_entry.get()), int(self.month_entry.get()), int(self.day_entry.get()))
            input_time = datetime.time(int(self.hour_entry.get()), int(self.minute_entry.get()))
            integer_year = int(self.year_entry.get())
            try:
                if integer_year < 2000:
                    valid_date = False
            except:
                pass

        except:
            if not self.year_entry.get() and not self.month_entry.get() and not self.day_entry.get() and not self.hour_entry.get() and not self.month_entry.get():
                valid_date = True
            else:
                valid_date = False

        if valid_date:
            if not self.year_entry.get() or not self.month_entry.get() or not self.day_entry.get() or not self.hour_entry.get() or not self.month_entry.get():
                self.no_input_stalls()
            else:
                input_day = input_date.weekday()
                self.display_other_day_stalls()
        else:
            try:
                if integer_year < 1950:
                    messagebox.showinfo("INVALID !!!", 'Select a valid year')
            except:
                messagebox.showinfo("INVALID !!!", "Select a valid date")

    def display_other_day_stalls(self):
        global back_button, input_day, input_time
        self.choose_date.grid_forget()
        self.blank.grid_forget()
        self.blank2.grid_forget()
        self.enter_button.grid_forget()
        self.year_label.grid_forget()
        self.year_entry.grid_forget()
        self.month_label.grid_forget()
        self.month_entry.grid_forget()
        self.day_label.grid_forget()
        self.day_entry.grid_forget()
        self.hour_label.grid_forget()
        self.hour_entry.grid_forget()
        self.minute_label.grid_forget()
        self.minute_entry.grid_forget()
        self.enter_button.grid_forget()
        back_button.grid_forget()
        back_button = Button(self.frame, text="Back", bg="BLUE",width=10, command=lambda: back_to_prev_page(3))
        self.choose_label.pack()
        self.which_menu()
        back_button.pack(pady=10,fill=X)

    def which_menu(self):
        global input_day, input_date, input_time
        for i in self.stalls:
            if input_day in i:
                pass
                for j in range(len(self.stalls[i])):
                    for stall in times:
                        if input_day in range(0,5):
                            if times[stall][0][1] == datetime.time(0,0):
                                if datetime.datetime.combine(input_date,times[stall][0][0]) <= datetime.datetime.combine(input_date,input_time) <= datetime.datetime.combine(input_date+datetime.timedelta(days=1),times[stall][0][1]):
                                    self.stalls[i][j].pack(pady=5, fill=X)
                                else:
                                    # pass
                                    getattr(self,stall).forget()
                            else:
                                if datetime.datetime.combine(input_date,times[stall][0][0]) <= datetime.datetime.combine(input_date,input_time) <= datetime.datetime.combine(input_date,times[stall][0][1]):
                                    self.stalls[i][j].pack(pady=5, fill=X)
                                else:
                                    getattr(self,stall).forget()

                        elif input_day == 5:
                            if times[stall][1]:
                                # if times[stall][1][0] <= input_time <= times[stall][1][1]
                                if times[stall][1][1] == datetime.time(0,0):
                                    if datetime.datetime.combine(input_date,times[stall][1][0]) <= datetime.datetime.combine(input_date,input_time) <= datetime.datetime.combine(input_date+datetime.timedelta(days=1),times[stall][1][1]):
                                        self.stalls[i][j].pack(pady=5, fill=X)
                                    else:
                                        getattr(self,stall).forget()
                                else:
                                    if datetime.datetime.combine(input_date,times[stall][1][0]) <= datetime.datetime.combine(input_date,input_time) <= datetime.datetime.combine(input_date,times[stall][1][1]):
                                        self.stalls[i][j].pack(pady=5, fill=X)
                                    else:
                                        getattr(self,stall).forget()
                        else:
                            if times[stall][2]:
                                if times[stall][2][0] <= input_time <= times[stall][2][1]:
                                    self.stalls[i][j].pack(pady=5, fill=X)
                                else:
                                    getattr(self,stall).forget()


    def create_mcd(self):
        self.mcd = McDonald(self.frame)

    def create_pizza_hut(self):
        self.piz = PizzaHut(self.frame)

    def create_subway(self):
        self.sub = SubWay(self.frame)

    def create_kfc(self):
        self.kfc = KFC(self.frame)

    def create_sandwich_guys(self):
        self.swg = SandwichGuys(self.frame)

# Class definition for McDonalds
class McDonald:
    def __init__(self, frame):
        # self.op_hours = {0: ("8:00am - 11:00pm"), 1: ("8:00am - 11:00pm"), 2: ("8:00am - 11:00pm"), 3: ("8:00am - 11:00pm"),
        #                4: ("8:00am - 11:00pm"), 5: ("9:00am - 9:00pm"), 6: ("8:00am - 6:00pm")}
        self.Welcome = Label(frame, text="Welcome to McDonald's")
        global m, window, back_button, day_track, other_day

        m.choose_label.forget()
        back_button.forget()
        for i in m.stalls:
            if input_day in i:
                for j in range(len(m.stalls[i])):
                    m.stalls[i][j].forget()

        # self.item_1 = Label(frame, text="Fries")
        # self.item_2 = Label(frame, text="McSpicy")
        # self.price_item_1 = Label(frame, text="$ 1.00")
        # self.price_item_2 = Label(frame, text="$ 2.00")
        # self.menu = menus['mc_donalds']
        self.menubar = Menu(window)
        self.showmenu(frame)

    def showmenu(self, frame):
        global m, window, back_button

        window.config(menu=self.menubar)
        self.menubar.add_cascade(label="Operating Hours", command=self.showtime)
        self.menubar.add_cascade(label="Waiting Time", command=self.get_waiting_time)
        m.date_text.grid(row=0, column=0, columnspan=10)
        self.Welcome.grid(row=1, column=1)
        self.menu = {}
        if input_time <= datetime.time(11):
          for key, value in menus['mc_donalds'][0].items():
              updater = {Label(frame, text=key):
              Label(frame, text=value)}
              self.menu.update(updater)
          i = 2
          for key, value in self.menu.items():
              key.grid(row=i, column=0, sticky=W)
              value.grid(row=i, column=2)
              i += 1
        else:
            for key, value in menus['mc_donalds'][1].items():
                updater = {Label(frame, text=key):
                Label(frame, text=value)}
                self.menu.update(updater)
            i = 2
            for key, value in self.menu.items():
                key.grid(row=i, column=0, sticky=W)
                value.grid(row=i, column=2)
                i += 1
        back_button = Button(frame, text="Back", bg="BLUE", width=10, command=lambda: back_to_prev_page(4))
        back_button.grid(row=i, column=1)

    def showtime(self):
        t_weekday = "Weekdays: " + times['mc_donalds'][0][0].strftime("%I:%M %p").lower() + " - " + times['mc_donalds'][0][1].strftime("%I:%M %p").lower() + "\n\n"
        if times['mc_donalds'][1] is not None:
            t_saturday = "Saturday: " + times['mc_donalds'][1][0].strftime("%I:%M %p").lower() + " - " + times['mc_donalds'][1][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_saturday = "Saturday: Closed"
        if times['mc_donalds'][2] is not None:
            t_sunday = "Sunday: " + times['mc_donalds'][2][0].strftime("%I:%M %p").lower() + " - " + times['mc_donalds'][2][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_sunday = "Sunday: Closed"
        string = t_weekday + t_saturday + t_sunday

        messagebox.showinfo("Stall Information", string)

    def get_waiting_time(self):
        box = Toplevel()
        box.title("Waiting Time")
        label = Label(box, text="Enter the number of people queuing:")
        label.pack()
        entry = Entry(box, width=12)
        entry.pack()
        button = Button(box, text="Enter", width=10, command=lambda:self.calc_waiting_time(box, label, entry, button,
                                                                                           quit_box))
        button.pack()
        quit_box = Button(box, text="Cancel", width=10, command=box.destroy)
        quit_box.pack()


    def calc_waiting_time(self, box, label, entry, button, quit_box):
        number = entry.get()
        if number.isnumeric() and 0 <= int(number):
            label.destroy()
            entry.destroy()
            button.destroy()
            quit_box.destroy()
            Label(box, text="Estimated Waiting time : "+str(2*(int(number)+1))+" minutes").pack()
            Button(box, text="OK", command=box.destroy).pack()
        else:
            messagebox.showerror("INVALID", "Enter a Valid Number!")

# Class definition for Subway stall
class SubWay:
    def __init__(self, frame):
        # self.op_hours = {0: ("8:00am - 11:00pm"), 1: ("8:00am - 11:00pm"), 2: ("8:00am - 11:00pm"), 3: ("8:00am - 11:00pm"),
        #                4: ("8:00am - 11:00pm"), 5: ("9:00am - 9:00pm"), 6: ("8:00am - 6:00pm")}
        self.Welcome = Label(frame, text="Welcome to Subway")
        global m, window, back_button, day_track, other_day

        m.choose_label.forget()
        back_button.forget()
        for i in m.stalls:
            if input_day in i:
                for j in range(len(m.stalls[i])):
                    m.stalls[i][j].forget()

        # self.item_1 = Label(frame, text="Fries")
        # self.item_2 = Label(frame, text="McSpicy")
        # self.price_item_1 = Label(frame, text="$ 1.00")
        # self.price_item_2 = Label(frame, text="$ 2.00")
        # self.menu = menus['subway']
        self.menubar = Menu(window)
        self.showmenu(frame)

    def showmenu(self, frame):
        global m, window, back_button

        window.config(menu=self.menubar)
        self.menubar.add_cascade(label="Operating Hours", command=self.showtime)
        self.menubar.add_cascade(label="Waiting Time", command=self.get_waiting_time)
        m.date_text.grid(row=0, column=0, columnspan=10)
        self.Welcome.grid(row=1, column=1)
        self.menu = {}
        for key, value in menus['subway'].items():
            updater = {Label(frame, text=key):
            Label(frame, text=value)}
            self.menu.update(updater)
        i = 2
        for key, value in self.menu.items():
            key.grid(row=i, column=0, sticky=W)
            value.grid(row=i, column=2)
            i += 1
        back_button = Button(frame, text="Back", bg="BLUE", width=10, command=lambda: back_to_prev_page(5))
        back_button.grid(row=i, column=1)

    def showtime(self):
        t_weekday = "Weekdays: " + times['subway'][0][0].strftime("%I:%M %p").lower() + " - " + times['subway'][0][1].strftime("%I:%M %p").lower() + "\n\n"
        if times['subway'][1] is not None:
            t_saturday = "Saturday: " + times['subway'][1][0].strftime("%I:%M %p").lower() + " - " + times['subway'][1][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_saturday = "Saturday: Closed"
        if times['subway'][2] is not None:
            t_sunday = "Sunday: " + times['subway'][2][0].strftime("%I:%M %p").lower() + " - " + times['subway'][2][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_sunday = "Sunday: Closed"
        string = t_weekday + t_saturday + t_sunday

        messagebox.showinfo("Stall Information", string)

    def get_waiting_time(self):
        box = Toplevel()
        box.title("Waiting Time")
        label = Label(box, text="Enter the number of people queuing:")
        label.pack()
        entry = Entry(box, width=12)
        entry.pack()
        button = Button(box, text="Enter", width=10, command=lambda:self.calc_waiting_time(box, label, entry, button,
                                                                                           quit_box))
        button.pack()
        quit_box = Button(box, text="Cancel", width=10, command=box.destroy)
        quit_box.pack()


    def calc_waiting_time(self, box, label, entry, button, quit_box):
        number = entry.get()
        if number.isnumeric() and 0 <= int(number):
            label.destroy()
            entry.destroy()
            button.destroy()
            quit_box.destroy()
            Label(box, text="Estimated Waiting time : "+str(2*(int(number)+1))+" minutes").pack()
            Button(box, text="OK", command=box.destroy).pack()
        else:
            messagebox.showerror("INVALID", "Enter a Valid Number!")


class PizzaHut:
    def __init__(self, frame):
        # self.op_hours = {0: ("8:00am - 11:00pm"), 1: ("8:00am - 11:00pm"), 2: ("8:00am - 11:00pm"), 3: ("8:00am - 11:00pm"),
        #                4: ("8:00am - 11:00pm"), 5: ("9:00am - 9:00pm"), 6: ("8:00am - 6:00pm")}
        self.Welcome = Label(frame, text="Welcome to Pizza Hut")
        global m, window, back_button, day_track, other_day

        m.choose_label.forget()
        back_button.forget()
        for i in m.stalls:
            if input_day in i:
                for j in range(len(m.stalls[i])):
                    m.stalls[i][j].forget()

        # self.item_1 = Label(frame, text="Fries")
        # self.item_2 = Label(frame, text="McSpicy")
        # self.price_item_1 = Label(frame, text="$ 1.00")
        # self.price_item_2 = Label(frame, text="$ 2.00")
        # self.menu = menus['pizza_hut']
        self.menubar = Menu(window)
        self.showmenu(frame)

    def showmenu(self, frame):
        global m, window, back_button

        window.config(menu=self.menubar)
        self.menubar.add_cascade(label="Operating Hours", command=self.showtime)
        self.menubar.add_cascade(label="Waiting Time", command=self.get_waiting_time)
        m.date_text.grid(row=0, column=0, columnspan=10)
        self.Welcome.grid(row=1, column=1)
        self.menu = {}
        for key, value in menus['pizza_hut'].items():
            updater = {Label(frame, text=key):
            Label(frame, text=value)}
            self.menu.update(updater)
        i = 2
        for key, value in self.menu.items():
            key.grid(row=i, column=0, sticky=W)
            value.grid(row=i, column=2)
            i += 1
        back_button = Button(frame, text="Back", bg="BLUE", width=10, command=lambda: back_to_prev_page(6))
        back_button.grid(row=i, column=1)

    def showtime(self):
        t_weekday = "Weekdays: " + times['pizza_hut'][0][0].strftime("%I:%M %p").lower() + " - " + times['pizza_hut'][0][1].strftime("%I:%M %p").lower() + "\n\n"
        if times['pizza_hut'][1] is not None:
            t_saturday = "Saturday: " + times['pizza_hut'][1][0].strftime("%I:%M %p").lower() + " - " + times['pizza_hut'][1][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_saturday = "Saturday: Closed"
        if times['pizza_hut'][2] is not None:
            t_sunday = "Sunday: " + times['pizza_hut'][2][0].strftime("%I:%M %p").lower() + " - " + times['pizza_hut'][2][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_sunday = "Sunday: Closed"
        string = t_weekday + t_saturday + t_sunday

        messagebox.showinfo("Stall Information", string)

    def get_waiting_time(self):
        box = Toplevel()
        box.title("Waiting Time")
        label = Label(box, text="Enter the number of people queuing:")
        label.pack()
        entry = Entry(box, width=12)
        entry.pack()
        button = Button(box, text="Enter", width=10, command=lambda:self.calc_waiting_time(box, label, entry, button,
                                                                                           quit_box))
        button.pack()
        quit_box = Button(box, text="Cancel", width=10, command=box.destroy)
        quit_box.pack()


    def calc_waiting_time(self, box, label, entry, button, quit_box):
        number = entry.get()
        if number.isnumeric() and 0 <= int(number):
            label.destroy()
            entry.destroy()
            button.destroy()
            quit_box.destroy()
            Label(box, text="Estimated Waiting time : "+str(2*(int(number)+1))+" minutes").pack()
            Button(box, text="OK", command=box.destroy).pack()
        else:
            messagebox.showerror("INVALID", "Enter a Valid Number!")

class KFC:
    def __init__(self, frame):
        # self.op_hours = {0: ("8:00am - 11:00pm"), 1: ("8:00am - 11:00pm"), 2: ("8:00am - 11:00pm"), 3: ("8:00am - 11:00pm"),
        #                4: ("8:00am - 11:00pm"), 5: ("9:00am - 9:00pm"), 6: ("8:00am - 6:00pm")}
        self.Welcome = Label(frame, text="Welcome to KFC")
        global m, window, back_button, day_track, other_day

        m.choose_label.forget()
        back_button.forget()
        for i in m.stalls:
            if input_day in i:
                for j in range(len(m.stalls[i])):
                    m.stalls[i][j].forget()

        # self.item_1 = Label(frame, text="Fries")
        # self.item_2 = Label(frame, text="McSpicy")
        # self.price_item_1 = Label(frame, text="$ 1.00")
        # self.price_item_2 = Label(frame, text="$ 2.00")
        # self.menu = menus['kfc']
        self.menubar = Menu(window)
        self.showmenu(frame)

    def showmenu(self, frame):
        global m, window, back_button

        window.config(menu=self.menubar)
        self.menubar.add_cascade(label="Operating Hours", command=self.showtime)
        self.menubar.add_cascade(label="Waiting Time", command=self.get_waiting_time)
        m.date_text.grid(row=0, column=0, columnspan=10)
        self.Welcome.grid(row=1, column=1)
        self.menu = {}
        for key, value in menus['kfc'].items():
            updater = {Label(frame, text=key):
            Label(frame, text=value)}
            self.menu.update(updater)
        i = 2
        for key, value in self.menu.items():
            key.grid(row=i, column=0, sticky=W)
            value.grid(row=i, column=2)
            i += 1
        back_button = Button(frame, text="Back", bg="BLUE", width=10, command=lambda: back_to_prev_page(7))
        back_button.grid(row=i, column=1)

    def showtime(self):
        t_weekday = "Weekdays: " + times['kfc'][0][0].strftime("%I:%M %p").lower() + " - " + times['kfc'][0][1].strftime("%I:%M %p").lower() + "\n\n"
        if times['kfc'][1] is not None:
            t_saturday = "Saturday: " + times['kfc'][1][0].strftime("%I:%M %p").lower() + " - " + times['kfc'][1][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_saturday = "Saturday: Closed"
        if times['kfc'][2] is not None:
            t_sunday = "Sunday: " + times['kfc'][2][0].strftime("%I:%M %p").lower() + " - " + times['kfc'][2][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_sunday = "Sunday: Closed"
        string = t_weekday + t_saturday + t_sunday

        messagebox.showinfo("Stall Information", string)

    def get_waiting_time(self):
        box = Toplevel()
        box.title("Waiting Time")
        label = Label(box, text="Enter the number of people queuing:")
        label.pack()
        entry = Entry(box, width=12)
        entry.pack()
        button = Button(box, text="Enter", width=10, command=lambda:self.calc_waiting_time(box, label, entry, button,
                                                                                           quit_box))
        button.pack()
        quit_box = Button(box, text="Cancel", width=10, command=box.destroy)
        quit_box.pack()


    def calc_waiting_time(self, box, label, entry, button, quit_box):
        number = entry.get()
        if number.isnumeric() and 0 <= int(number):
            label.destroy()
            entry.destroy()
            button.destroy()
            quit_box.destroy()
            Label(box, text="Estimated Waiting time : "+str(2*(int(number)+1))+" minutes").pack()
            Button(box, text="OK", command=box.destroy).pack()
        else:
            messagebox.showerror("INVALID", "Enter a Valid Number!")

class SandwichGuys:
    def __init__(self, frame):
        # self.op_hours = {0: ("8:00am - 11:00pm"), 1: ("8:00am - 11:00pm"), 2: ("8:00am - 11:00pm"), 3: ("8:00am - 11:00pm"),
        #                4: ("8:00am - 11:00pm"), 5: ("9:00am - 9:00pm"), 6: ("8:00am - 6:00pm")}
        self.Welcome = Label(frame, text="Welcome to The Sandwich Guys")
        global m, window, back_button, day_track, other_day

        m.choose_label.forget()
        back_button.forget()
        for i in m.stalls:
            if input_day in i:
                for j in range(len(m.stalls[i])):
                    m.stalls[i][j].forget()

        # self.item_1 = Label(frame, text="Fries")
        # self.item_2 = Label(frame, text="McSpicy")
        # self.price_item_1 = Label(frame, text="$ 1.00")
        # self.price_item_2 = Label(frame, text="$ 2.00")
        # self.menu = menus['sandwich_guys']
        self.menubar = Menu(window)
        self.showmenu(frame)

    def showmenu(self, frame):
        global m, window, back_button

        window.config(menu=self.menubar)
        self.menubar.add_cascade(label="Operating Hours", command=self.showtime)
        self.menubar.add_cascade(label="Waiting Time", command=self.get_waiting_time)
        m.date_text.grid(row=0, column=0, columnspan=10)
        self.Welcome.grid(row=1, column=1)
        self.menu = {}
        for key, value in menus['sandwich_guys'].items():
            updater = {Label(frame, text=key):
            Label(frame, text=value)}
            self.menu.update(updater)
        i = 2
        for key, value in self.menu.items():
            key.grid(row=i, column=0, sticky=W)
            value.grid(row=i, column=2)
            i += 1
        back_button = Button(frame, text="Back", bg="BLUE", width=10, command=lambda: back_to_prev_page(8))
        back_button.grid(row=i, column=1)

    def showtime(self):
        t_weekday = "Weekdays: " + times['sandwich_guys'][0][0].strftime("%I:%M %p").lower() + " - " + times['sandwich_guys'][0][1].strftime("%I:%M %p").lower() + "\n\n"
        if times['sandwich_guys'][1] is not None:
            t_saturday = "Saturday: " + times['sandwich_guys'][1][0].strftime("%I:%M %p").lower() + " - " + times['sandwich_guys'][1][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_saturday = "Saturday: Closed"
        if times['sandwich_guys'][2] is not None:
            t_sunday = "Sunday: " + times['sandwich_guys'][2][0].strftime("%I:%M %p").lower() + " - " + times['sandwich_guys'][2][1].strftime("%I:%M %p").lower() + "\n\n"
        else:
            t_sunday = "Sunday: Closed"
        string = t_weekday + t_saturday + t_sunday

        messagebox.showinfo("Stall Information", string)

    def get_waiting_time(self):
        box = Toplevel()
        box.title("Waiting Time")
        label = Label(box, text="Enter the number of people queuing:")
        label.pack()
        entry = Entry(box, width=12)
        entry.pack()
        button = Button(box, text="Enter", width=10, command=lambda:self.calc_waiting_time(box, label, entry, button,
                                                                                           quit_box))
        button.pack()
        quit_box = Button(box, text="Cancel", width=10, command=box.destroy)
        quit_box.pack()


    def calc_waiting_time(self, box, label, entry, button, quit_box):
        number = entry.get()
        if number.isnumeric() and 0 <= int(number):
            label.destroy()
            entry.destroy()
            button.destroy()
            quit_box.destroy()
            Label(box, text="Estimated Waiting time : "+str(2*(int(number)+1))+" minutes").pack()
            Button(box, text="OK", command=box.destroy).pack()
        else:
            messagebox.showerror("INVALID", "Enter a Valid Number!")



window = Tk()
window.title("Canteen System")
window.geometry("500x500")

back_button = Button(window, text="Back", bg="blue", command=lambda: back_to_prev_page(1))

image = PhotoImage(file="NTU.png")
image_label = Label(window, image=image)
image_label.pack()


m = MainPage(window)
window.mainloop()
