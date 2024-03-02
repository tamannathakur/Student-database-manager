from tkinter import *
from pickle import *
from random import *
from pymysql import *
from tkinter import messagebox
class En:
    def __init__(self,root):
        '''CONNECTING PYTHON TO MYSQL'''
        
        self.con=connect(host="localhost",user="root",password="#mysql123pass#",database="Marks")
        self.cur=self.con.cursor()
        
        #********** MAIN WIND0W **********
        
        self.win=root
        self.win.resizable(width=False,height=False)
        self.win.title("REPORT CARD")
        self.win.config(bg="light blue")
        self.win.geometry('900x600')
        title=Label(self.win,text="  REPORT CARD  GENERATOR",bd=10,relief=GROOVE,bg="yellow",font=("ALGERIAN",30),fg="black").pack(fill=X)

        #**********ENTRY VALUES STORING VARIABLES**********

        self.maths=StringVar()
        self.english=StringVar()
        self.science=StringVar()
        self.social=StringVar()
        self.hindi=StringVar()
        self.name=StringVar()
        self.stndrd=StringVar()
        self.totalmarks=StringVar()
        self.grade=StringVar()
        self.to=StringVar()
        self.academicyear=StringVar()
        self.percentage=IntVar()

        self.nme=StringVar()
        self.entryno=IntVar()
        self.stn=StringVar()
        

        #**********FRAMES USED**********
        rprt=Frame(self.win,bd=15,relief=GROOVE).place(x=200,y=120,height=480,width=800)
        marks=Frame(self.win,bd=15,relief=GROOVE).place(x=0,y=120,height=480,width=320)
        year=Frame(self.win,relief=GROOVE,bd=5,bg="white",height=55).pack(fill = X)

        #**********TEXTBOX USED**********
        
        self.text=Text(self.win,width=500,height=400,bd=5,font=8,relief=SUNKEN)
        self.text.place(x=310,y=143)

        #*********ENTRIES BY THE USER***********

        e1=Entry(self.win,textvariable=self.name,width=11,font="arial 15",bd=7,relief=SUNKEN).place(x=97,y=150)
        #entry e1 takes student's name as an input
        
        e2=Entry(self.win,textvariable=self.stndrd,width=11,font="arial 15",bd=7,relief=SUNKEN).place(x=97,y=200)
        #entry e2 takes student's class as an input
        
        e3=Entry(self.win,textvariable=self.english,width=11,font="arial 15",bd=7,relief=SUNKEN).place(x=97,y=250)
        #entry e3 takes student's english mark as an input
        
        e4=Entry(self.win,textvariable=self.science,width=11,font="arial 15",bd=7,relief=SUNKEN).place(x=97,y=300)
        #entry e4 takes student's science mark as an input
        
        e5=Entry(self.win,width=11,textvariable=self.maths,font="arial 15",bd=7,relief=SUNKEN).place(x=97,y=350)
        #entry e5 allows the user to enter maths marks as an input
        
        e6=Entry(self.win,width=11,textvariable=self.hindi,font="arial 15",bd=7,relief=SUNKEN).place(x=97,y=400)
        #entry e6 allows the user to enter hindi marks as an input
        
        e7=Entry(self.win,width=11,textvariable=self.social,font="arial 15",bd=7,relief=SUNKEN).place(x=97,y=450)
        #entry e5 allows the user to enter social marks as an input
        
        e8=Entry(self.win,width=15,textvariable=self.academicyear,font="arial 15",bg="grey1",fg="white").place(x=146,y=92,width=180)
        #entry e8 takes academic year as an input
        
        #**********ENTRIES USED FOR DISPLAYING TOTAL MARKS AND GRADE***********
        
        e9=Entry(self.win,width=15,font=("arial 15",10),textvariable=self.totalmarks,fg="white",bg="grey1").place(x=20,y=540,width=200,height=39)
        #entry e9 displays the totalmarks of the student when the save_report or report method is called
        
        e10=Entry(self.win,width=15,font="arial 15",textvariable=self.grade,bg="grey1",fg="white").place(x=222,y=540,width=80,height=39)
        #entry e10 displays the grade of the student when the save_report or report method is called

        #**********BUTTONS USED***********
        
        b1=Button(text="Save in file",font=("times new roman",7,"italic","bold"),command=self.save_report).place(x=220,y=505)
        #button b1 lets the user save the report card in the form of a text file in the computer
        
        b2=Button(text="Generate report card",font=("times new roman",7,"bold","italic"),command=self.verify).place(x=69,y=505,width=150)
        #button b2 lets the user generate the student's report card in the textbox
        
        b3=Button(text="Refresh",font=("times new roman",7,"bold","italic"),command=self.refresh).place(x=20,y=505)
        #button b3 lets the user clear the whole textbox with just one click
        
        b4=Button(self.win,text="Save in table",font=("times new roman",10,"bold","italic"),command=self.write).place(x=657,y=85)

        b5=Button(self.win,text="Show marks list",font=("times new roman",10,"bold","italic"),command=self.showwin).place(x=765,y=85)

        b6=Button(self.win,text="Delete student",font=("times new roman",10,"bold","italic"),command=self.delete).place(x=539,y=85)
        
        #**********
        #**********LABELS USED**********
        
        a1=Label(text="Name :",font=("Brush Script MT",12)).place(x=24,y=155)
        a2=Label(text="Class :",font=("Brush Script MT",13)).place(x=20,y=200)
        a3=Label(text="English :",font=("Brush Script MT",12)).place(x=17,y=255)
        a4=Label(text="Science:",font=("Brush Script MT",12)).place(x=20,y=300)
        a5=Label(text="Maths:",font=("Brush Script MT",12)).place(x=20,y=350) 
        a6=Label(text="Hindi:",font=("Brush Script MT",12)).place(x=20,y=400)
        a7=Label(text="Social:",font=("Brush Script MT",12)).place(x=20,y=450)
        a8=Label(text="Academic year:",font=("Brush Script MT",15),bg="white").place(x=12,y=91)
        report_title=Label(text="Report Card",bg="black",font=("arial 15 bold",11),fg="white",bd=5,relief=SUNKEN).place(x=312,y=132,width=588,height=35)

        #self.found variable used so that data is not overwritten

        self.found=0

        
    def write(self):
        
        #INSERTS CURRENT STUDENT'S DATA IN TABLE

         self.verify()
         tab="create table if not exists mark{}(Entry_No integer primary key auto_increment,Name varchar(225),Class integer,English integer,Hindi integer,Science integer,Maths integer,Social integer,Total_Marks integer,Grade varchar(225),Percentage integer)".format(self.stndrd.get())
         self.cur.execute(tab)
         insert="insert into mark{}(Name,Class,English,Hindi,Science,Maths,Social,Total_Marks,Grade,Percentage) values('{}',{},{},{},{},{},{},{},'{}',{})".format(self.stndrd.get(),str(self.name.get()),self.stndrd.get(),self.english.get(),self.hindi.get(),self.science.get(),self.maths.get(),self.social.get(),self.tt,str(self.grade.get()),self.percentage.get())
         self.cur.execute(insert) 
         self.con.commit()

    def delete(self):
        
        #DELETES ENTRY IN TABLE
        
            top=Toplevel(self.win)
            top.geometry('400x120')
            l=Label(top,text="Enter student's Entry no")
            l.place(x=10,y=10)
            l1=Label(top,text="Enter student's Name")
            l1.place(x=10,y=40)
            l2=Label(top,text="Enter student's Class")
            l2.place(x=10,y=70)
            e=Entry(top,textvariable=self.entryno).place(x=200,y=10)
            e1=Entry(top,textvariable=self.nme).place(x=200,y=40)
            e2=Entry(top,textvariable=self.stn).place(x=200,y=70)

            def verification():

                '''this method determines if the data given by the user in entries are valid or not'''

                try:
                    #verifying if the given inputs are valid or not
        
                    check=[self.nme,self.entryno,self.nme]

                    for i in check:

                    #in case if the user forgets to enter marks , this if statement will set that particular subject's marks to 0 so that when we convert this
                    # string to integer, it wont throw any error while the calculation/total func is being executed

                        if len(str(i.get())) == 0 :
                            val=Tk()
                            val.title("Error")
                            val.geometry("500x50")
                            f=Label(val,text="Please give valid inputs",font=("Helvetica",12,"bold")).pack()
                            b=Button(val,text="OK",relief=GROOVE,command=val.destroy).pack(fill=X)
                            val.mainloop()
                            return
                        
                except TclError:
                    messagebox.showerror("ERROR!","PLEASE ENTER VALID INPUTS")
                    return
                    
            def dat():

                '''dat() method determines if the values entered by the user is present in the table or not'''
                
                try:
                    
                    dataa="select entry_no,name,class from mark{}".format(self.stn.get())
                    self.cur.execute(dataa)
                    a=self.cur.fetchall()
                    
                    for i in a:
                        count=0
                        
                        for m in i:
                            if m==self.entryno.get():
                                count=count + 1
                                
                            if m==self.nme.get():
                                count= count + 1
    
                            if m==int(self.stn.get()): 
                                count= count + 1
                            if count==3:
                                return 3
                    return 0
                
                except ProgrammingError:
                    messagebox.showerror("ERROR!","SQL TABLE ERROR")
                    return
                     
            def delfunc():
                '''this method deletes the entry if present'''
                verification()
                count=dat()
                if count!=3:
                    messagebox.showerror("Error!","Entry not in table")
                    return
                dele="delete from mark{} where name = '{}' and entry_no={} ".format(self.stn.get(),self.nme.get(),self.entryno.get())
                self.cur.execute(dele)
                self.con.commit()
                messagebox.showinfo("Deleted","Entry Deleted")
                top.destroy()
                
            
            b=Button(top,text="Done",command=delfunc)
            b.place(x=10,y=97,width=375,height=20)
            top.mainloop()

    def showwin(self):
        
        '''function that lets user see the existing entries of different standards'''

        nw=Toplevel()
        nw.geometry("200x200")
        s1=Button(nw,text="Class 1",command=self.class1,font=("times new roman",7)).place(x=50,y=10,width=50)
        s2=Button(nw,text="Class 2",command=self.class2,font=("times new roman",7)).place(x=50,y=40,width=50)
        s3=Button(nw,text="Class 3",command=self.class3,font=("times new roman",7)).place(x=50,y=70,width=50)
        s4=Button(nw,text="Class 4",command=self.class4,font=("times new roman",7)).place(x=50,y=100,width=50)
        s5=Button(nw,text="Class 5",command=self.class5,font=("times new roman",7)).place(x=50,y=130,width=50)
        s6=Button(nw,text="Class 6",command=self.class6,font=("times new roman",7)).place(x=100,y=10,width=50)
        s7=Button(nw,text="Class 7",command=self.class7,font=("times new roman",7)).place(x=100,y=40,width=50)
        s8=Button(nw,text="Class 8",command=self.class8,font=("times new roman",7)).place(x=100,y=70,width=50)
        s9=Button(nw,text="Class 9",command=self.class9,font=("times new roman",7)).place(x=100,y=100,width=50)
        s10=Button(nw,text="Class 10",command=self.class10,font=("times new roman",7)).place(x=100,y=130,width=50)
        snull=Button(nw,text="Entries with no class",font=("times new roman",5),command=self.classnull).place(x=50,y=160,width=100,height=20)
        nw.mainloop()
        
    '''different class methods shows their specific class details'''
    
    def classnull(self):
        
        try:
            s="select * from marknull"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")
        
    def class1(self):
        try:
            s="select * from mark1"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class2(self):
        try:
            s="select * from mark2"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class3(self):
        try:
            s="select * from mark3"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class4(self):
        try:
            s="select * from mark4"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class5(self):
        try:
            s="select * from mark5"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class6(self):
        try:
            s="select * from mark6"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class7(self):
        try:
            s="select * from mark7"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class8(self):
        try:
            s="select * from mark8"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class9(self):
        try:
            s="select * from mark9"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")

    def class10(self):
        try:
            s="select * from mark10"
            self.cur.execute(s)
            f=self.cur.fetchall()
            nw=Toplevel()
            nw.geometry('870x500')
            nw.title("show win")
            nw.resizable(width=False,height=False)
            col=["Entry_No","Name","Class","English","Hindi","Science","Maths","Social","Total_Marks","Grade","Percentage"]
            a=0
            for i in col:
                 l=Label(nw,text=i,font=("times new roman",10))
                 l.place(x=a,y=0,height=25,width=90)
                 if i  in ("Entry_No","Name","Class","English","Hindi","Science","Maths","Total_Marks"):
                     a+=80
                 elif i in  ("Social","Grade"):
                     a+=70
            nw.config(bg="AntiqueWhite1")
            lst=["pale violet red","RosyBrown1","snow","peach puff","azure3","wheat1","thistle1","salmon1","yellow","purple1"]
            b=25
            for line in f:
                a=0
                for m in range(11):
                    color=choice(lst)
                    label=Label(nw,text=line[m],bg=color).place(x=a,y=b,width=90)
                    a+=80
                b+=21
            nw.mainloop()
        except:

            # in case if table is not found or deleted
            
            messagebox.showerror("ERROR","NO TABLE FOUND")
        
    def verify(self):

        #verifying if the given inputs are valid or not
        
        check=[self.english,self.social,self.hindi,self.science,self.maths]

        nm=[self.name,self.stndrd]

        for m in nm:

            if len(m.get())==0:
                m.set("null")

        for i in check:

            #in case if the user forgets to enter marks , this if statement will set that particular subject's marks to 0 so that when we convert this
            # string to integer, it wont throw any error while the calculation/total func is being executed

            if len(i.get()) == 0 :
                i.set(0)

            #marks should be in digits for further calculations to take place , so if the user enters any other data type this elif statement will
            # inform the user to enter valid inputs in the entries
            
            elif not i.get().isdigit():

               #in case of any error , a window will be displayed to inform the user about the error
            
               val=Tk()
               val.title("Error")
               val.geometry("500x50")
               f=Label(val,text="Please enter valid inputs",font=("Helvetica",12,"bold")).pack()
               b=Button(val,text="OK",relief=GROOVE,command=val.destroy).pack(fill=X)
               val.mainloop()
               return 
               
        self.total()

    def total(self):

        #adding marks of subjects and calculating percentage and grade


        #converting string to integer using built-in "int()" function
        
        self.tt=int(self.english.get())+int(self.maths.get())+int(self.science.get())+int(self.social.get())+int(self.hindi.get())
        self.percentage.set((self.tt/500)*100)
        self.totalmarks.set("Total marks : " +str(self.tt))
        if self.tt>=400 :
            self.grade.set("A")
        elif self.tt>=300 and self.tt<400:
            self.grade.set("B")
        elif self.tt>=200 and self.tt<300:
            self.grade.set("C")
        elif self.tt>=100 and self.tt<200:
            self.grade.set("E")
        elif self.tt<100:
            self.grade.set("F")
        self.gd=self.grade
        self.tot=self.tt
        self.report()
        

    def report(self):

        #report function generates report card in the textbox 

        #Generating report card(inserting text in the textbox)
        
        self.text.insert(END,'\t                 CHRIST JYOTI CONVENT SCHOOL            ')
        self.text.insert(END,"\n")
        self.text.insert(END,"\n Student's Name: "+self.name.get())
        self.text.insert(END,"\n Student's Class:"+self.stndrd.get())
        self.text.insert(END,"\n  ===================================================================   ")
        self.text.insert(END,"\n  -----------------------------"+(self.academicyear.get())+"----------------------------")
        self.text.insert(END,"\n  ===================================================================  ")
        self.text.insert(END,"\n                             ACADEMICS                             ")
        self.text.insert(END,"\n English : "+str(self.english.get()))
        self.text.insert(END,"\n Hindi : "+str(self.hindi.get()))
        self.text.insert(END,"\n Science : "+str(self.science.get()))
        self.text.insert(END,"\n Social : "+str(self.social.get()))
        self.text.insert(END,"\n Maths : "+str(self.maths.get()))
        self.text.insert(END,"\n ")
        self.text.insert(END,"\n Total Marks : "+str(self.tt)+"/500")
        self.text.insert(END,"\n Grade : "+str(self.grade.get()))
        self.text.insert(END,"\n Percentage: "+str(self.percentage.get()))
        self.text.insert(END,"\n")
        if self.tt>=100:
            self.text.insert(END," PASS")
        elif self.tt<=100:
            self.text.insert(END,"\n FAIL")
        
   

            
    def save_report(self):
        #save_report function saves the generated report card in user's computer
        self.found +=1

        # we are calling refresh function so that if the user has already called the generate report card function
        # then refresh function clears the whole textbox so that we wont get 2 report cards mixed up in the same text file

        self.refresh()
        self.verify()
        self.final=self.text.get("1.0",END)
        file=open("C:\\Report"+str(self.found)+"("+str(self.name.get())+").txt","w")
        file.write(self.final)
        file.close()
        l=Label(self.win,text="\"your report card is saved\"",font=("arial",15),bg="alice blue")
        l.pack(fill=X)
        l.pack(pady=200)
        self.win.after(2000,l.destroy)

    def refresh(self):

        #refresh function clears the whole textbox

        self.text.delete('1.0',END)

def run():
    win=Tk()
    obj=En(win)
    win.mainloop()

run()
