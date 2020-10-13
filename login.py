from tkinter import *
from PIL import ImageTk
from tkinter import messagebox




class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Hi, I Create Software")
        self.root.geometry('1080x670+360+180')
        self.root.resizable(False, False)
        
        #Background Image
        
        self.bg=ImageTk.PhotoImage(file="images/pexels-photo-1445416.jpeg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        #login Frame
        LogFr = Frame(self.root,bg='white')
        LogFr.place(x = 570, y = 180, height= 340, width=440)
        

        title = Label(LogFr, text="Login Here",font=("Poppins",20,"bold"),fg="#41aea9",bg="white").place(x=50,y=20)

        lbl_user = Label(LogFr, text="Username",font=("Calibri",8,"bold"),fg="#000",bg="white").place(x=50,y=90)
        self.txt_user = Entry(LogFr, font=("Poppins",9), bg="#fbf7f0",borderwidth = 0)
        self.txt_user.place(x = 50, y = 110, width=300, height=35)
        
        lbl_user = Label(LogFr, text="Password",font=("Calibri",8,"bold"),fg="#000",bg="white").place(x=50,y=160)
        self.txt_pass = Entry(LogFr, font=("Poppins",9), bg="#fbf7f0",borderwidth = 0)
        self.txt_pass.place(x = 50, y = 180, width=300, height=35)
        
        
        forget = Button(LogFr,text= "Forget Password?",bd= 0 , bg="white",fg="#41aea9").place(x = 50, y = 220)
        login_btn = Button(LogFr,command=self.login, text="Login",cursor ="hand2" ,border=0, bg="#41aea9").place(x=50,y =270, width=300, height=35)
        
        
    def login(self):
        
       
        
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get()!="admin" or self.txt_user.get()!="admin":
            messagebox.showerror("Error", "Invalid Password", parent=self.root)
        else:
            root.destroy()
            dsh.dashboard(self)
            
        
            
        

    
root = Tk()
obj = Login(root)
root.mainloop()



        