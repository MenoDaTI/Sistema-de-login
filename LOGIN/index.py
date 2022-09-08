#Importar bibliotecas
from http.client import IM_USED
from tkinter import ALL, LEFT, RIGHT, Entry, Frame, Label, PhotoImage, Tk
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criar Nossa Janela
jan = Tk()
jan.title("Dp Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="gray")
jan.resizable(width=False, height=False) 
jan.attributes("-alpha", 1.0)
jan.iconbitmap(default="Icons/Logoicon.ico")

#------------- Carregando imagens _-_-_-_______-____---__--__--__---__-___----___
logo = PhotoImage(file='Icons/logo.png')


#---------------- Widgets -_--_-_---_-_------__-----_--__-_-------___------_-_--
LeftFrame = Frame(jan, width=200, height=300, bg="navy blue", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="navy blue", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="navy blue")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("century gothic", 20), bg="navy blue", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

UserPass = Label(RightFrame, text="Password:", font=("century gothic", 20), bg="navy blue", fg="White")
UserPass.place(x=5, y=150)

UserEntryPass = ttk.Entry(RightFrame, width=30)
UserEntryPass.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass = UserEntryPass.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Welcome!")
    except:
        messagebox.showerror(title="Login Error", message="Check your Login Details and Try Again!")    

#Botões _-_-_-_--___-____----__---_-_-__---_---_-___----__--_
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=150, y=200)

def Register():
    # Removendo widgets/Labels de login
    LoginButton.place(x=10000)
    RegisterButton.place(x=10000)
    # Inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name: ", font=("century gothic", 20), bg="navy blue", fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="E-mail: ", font=("century gothic", 20), bg="navy blue", fg="White")
    EmailLabel.place(x=5, y=55)
    EmailEntry = Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = UserEntryPass.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Fill in All Fields")
        else:    
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Account Created Sucessfully")



    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        # Removendo widgets/Labels de Cadastro
        NomeEntry.place(x=10000)
        NomeLabel.place(x=10000)
        EmailEntry.place(x=10000)
        EmailLabel.place(x=10000)
        BackButton.place(x=10000) 
        Register.place(x=10000)

        RegisterButton.place(x=109, y=250)
        LoginButton.place(x=150, y=200)
    
    BackButton = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    BackButton.place(x=130, y=260)

    
RegisterButton = ttk.Button(RightFrame, text="Register", width=45, command=Register)
RegisterButton.place(x=109, y=250)


jan.mainloop()
