"""This program is based on C programming ide Which is provide you a interface to write to the code and compile.
In this ide you can also run your c++ ,python,c programme ,the date of making this programme is 2 july 2020 Himanshu Sharma """

"""Importing all modules for the project"""

# filetypes=(("All files","*.*"),("c files","*.c"),("txt files","*.txt"),("c++ files","*.cpp"))

from tkinter import *
import tkinter.messagebox as show
import time
import datetime
import os
from tkinter.ttk import Menubutton,OptionMenu
from tkinter import filedialog
from tkinter import colorchooser
import random
import webbrowser


"""Some global variables that will be used in different functions"""
ReadFileNAme="You did not save your file yet!!"
TextFile=None
fileno=0
file=None
"""==================================================="""
#some basic work before it start function
if os.path.isdir("Unsaved Files") is False:

     os.mkdir("Unsaved Files")

# after compile and run the this directory will contain all data
if os.path.isdir("bin") is False:
    os.mkdir("bin")



"""======================================================"""
"""now the functions will start from here"""
"""fontStyle function"""
def fontStyle():

    def tellFont():


        CodeText.config(font=f"{fontStylelist.get(ACTIVE)} {fontsizeList.get(ACTIVE)}")

    os.chdir("D:\\python projects\\C programming IDE\\Ide")
    root1=Tk()
    root1.title("Select the font option")
    root1.iconbitmap("font.ico")
    root1.maxsize(height=250,width=300)

    fontList=["Chiller","Latin","Mistral ","InkFree","jokerman","MvBoli","Times","Aprajita","ARCHRISTY","Fixedsys","Gillsans","Algerian","Elephant","ArDelaney","Arial","Broadway","ComicSansMs","Cooper","Corbel"]
    fontsize=[10,12,13,15,28,18,20,22,24,26,30,48,72,36]
    frameForFont=Frame(root1,relief=SUNKEN,bd=2)
    frameForFont.pack()
    fontstyleLabel=Label(frameForFont,text="Font-Family",font="times 16 bold",fg="green")
    fontstyleLabel.pack()
    fontStylelist=Listbox(frameForFont)
    fontStylelist.pack(side=LEFT,padx=10,pady=10)
    for i in fontList:
        fontStylelist.insert(END,i)

    fontsizeList=Listbox(frameForFont)
    fontsizeList.pack(side=LEFT,padx=10,pady=10)

    for fontlenth in fontsize:
        fontsizeList.insert(END,fontlenth)
    fontButton=Button(root1,command=tellFont,text="Apply" ,bd=3,relief=SUNKEN,width=20)
    fontButton.pack()
    root1.mainloop()

    """End of function which was for the font style and size================================"""


"""To print date time from menu bar"""


def printDatetime():

    CodeText.insert(END,str(time.asctime(time.localtime(time.time()))))

"""====================================================================="""


"""For new window from menu bar"""
def newWindow():
    choice=show.askokcancel("Warning..","If You Open New Window All Content In Previous Window Will Be Cleared. Are You Sure To Open New Window ?")
    if choice==True:
        CodeText.delete(1.0,END)
        root.title("CodeView _*untitled")
    else:
        pass
"""====================================================================="""

"""for the clear all text and delete all the text from menu bar"""
def clearText():
    CodeText.delete(1.0,END)

"""====================================================================="""

"""For set the theme"""
def changebackgroundColor():
    chosenColor=colorchooser.askcolor(title="Background Color")
    CodeText.config(bg=f"{chosenColor[1]}")

def changeforgroundColor():
     chosenColor1=colorchooser.askcolor(title="Text Color")
     CodeText.config(fg=f"{chosenColor1[1]}")

"""====================================================================="""

"""For saving the file"""

def saveasFile(*args):
    global TextFile
    global ReadFileNAme
    files=[('c file','*.c'),("text file","*.txt"),('c++ file','*.cpp'),('headerfile','*.h'),("All files","*.*")]

    try:
        TextFile = filedialog.asksaveasfile(filetypes=files, defaultextension=files, title="Select path (Himanshu sharma)",)
        # root.title(f"CodeView {TextFile.name}")
        # ReadFileNAme = TextFile.name
        with open(f"{TextFile.name}", "w") as saveAllData:
            saveAllData.write(f"{CodeText.get(1.0, END)}")
    except Exception as savingError:
        pass


        # file.write(CodeText.get(1.0,END))
"""============================================================================="""

"""for saving te file ...."""

def saveFile(event=""):
    global file,ReadFileNAme
    if file==None:
        file=filedialog.asksaveasfilename(initialfile="untitled.c",filetypes=(("All files","*.*"),("c files","*.c"),("txt files","*.txt"),("c++ files","*.cpp")),title="Select folder _Himi")
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(f"{CodeText.get(1.0,END)}")
            f.close()
            root.title(os.path.basename(file) + " " + "CodeView")
    else:
        f = open(file, "w")
        f.write(f"{CodeText.get(1.0, END)}")
        f.close()


    ReadFileNAme=file




"""==================================================================================="""

"""open  file delete all the previous text areas"""
def openFiletoCodetext(*args):
    global file,ReadFileNAme
    file=filedialog.askopenfilename(defaultextension="*.*",initialdir="C:\\Users\\himan\\Onedrive\\Desktop",title="open file_Himanshu",filetypes=(("All files","*.*"),("c files","*.c"),("txt files","*.txt"),("c++ files","*.cpp")))
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " " + "-CodeView")
        CodeText.delete(1.0,END)
        f=open(file,"r")
        CodeText.insert(1.0,f.read())
        f.close()

    ReadFileNAme=file

"""========================================================================================"""

"""To open File Form file  dialouge but this will keep previous all text inside text area"""
def FileOpenwindow():
    try:

        input=filedialog.askopenfile(initialdir="C:/Users/himan/Onedrive/Desktop",title="Open (Himanshi)")

        CodeText.insert(0.1,f"{input.read()}")
    except Exception as Error:
         CodeText.insert(END,Error)


"""================================================================================================"""

"""Tell the file information"""
def TellFileInfo(event=""):
    sayinfo=show.showinfo("File Info",f"File Location : {ReadFileNAme} ")

"""Cut copy Paste functions"""
def DoCut():
    CodeText.event_generate(("<<Cut>>"))
def DoCopy():
    CodeText.event_generate(("<<Copy>>"))
def DoPaste():
    CodeText.event_generate(("<<Paste>>"))
def DoUndo():
    CodeText.event_generate(("<<Undo>>"))
def DoSelect():
    CodeText.event_generate(("<<SelectAll>>"))
def deleteSelectedArea():
    try:
        CodeText.delete('sel.first','sel.last')
    except Exception as hima:
        pass
"""============================================================"""

"""Open New File Just liKe Delete All And clear Text Function"""
def OpenNew(event=""):
    global fileno

    firstrandom=random.randint(0,100)
    secondrandom=random.randint(100,1000)*3
    fileno=firstrandom+secondrandom*2
    os.chdir("D:\\python projects\\C programming IDE\\Ide")



    try:
        with open(f'Unsaved Files\\File id..{fileno}.txt' ,'w') as writeinFile:

            writeinFile.write(f"{CodeText.get(1.0,END)}")
    except Exception as FilewriteError:
         show.showerror("Error_404",FilewriteError)
         #print statement here latar we will remove it just for debugging..

    CodeText.delete(1.0,END)
    root.title("CodeView _*untitled")
    """==================================================================="""

"""for help menu go to the site """
def gototheSite():
    if os.path.isfile("D:\\python projects\\C programming IDE\\Ide\\hello.html") is True:
        site= 'D:\\python projects\\C programming IDE\\Ide\\hello.html'
        webbrowser.open_new_tab(site)
    else:
        show.showerror("Error ","404 Error it seems that file has been removed plz check once..")
    """===================================================================================="""

"""most important part here for only compile function with help of gcc compiler and command prompt"""

def docompile():
    cfileId=random.randint(0,1000)
    with open(f"D:/python projects/C programming IDE/Ide/bin/{cfileId}.c","w") as docompilee:
        docompilee.write(f'{CodeText.get(1.0,END)}')

    os.chdir('D:/python projects/C programming IDE/Ide/bin')
    os.system('cmd /c "mode 1000"')
    os.system(f'cmd /c "gcc {cfileId}.c"')
"""======================================================================="""

"""after compilation programme will execute file """
def runCode():
    os.chdir('D:/python projects/C programming IDE/Ide/bin')
    try:
        os.system('cmd /c "mode 1000"')
        print(os.popen("a.exe").read())

    except Exception as codeError:
        show.showerror("Error ",f"{codeError}")
"""========================================================================"""

"""this th combination of above two function compile and run only"""

def compileAndCode():
    cfileID=random.randint(10000,50000)
    try:
        with open(f"D:/python projects/C programming IDE/Ide/bin/{cfileID}.c", "w") as cANDr:
            cANDr.write(CodeText.get(1.0,END))
        os.chdir('D:/python projects/C programming IDE/Ide/bin')
        os.system('cmd /c "mode 1000"')
        runValue=os.system(f'cmd /c "gcc {cfileID}.c"')
        if runValue==1:
            """if any error occur in code runValue will return 1, if no error occur it will return 0"""
            pass
        else:
            os.system('cmd /c "mode 1000"')
            os.system('cmd /c "a.exe"')
    except Exception as RunError:
        show.showerror("Error ",RunError)

"""======================================================================================="""




"""coding starts from here"""

root=Tk()
"""root default setting"""
root.iconbitmap('pen.ico')
root.geometry("1000x635")
root.minsize(height='200',width=500)
root.title("CodeView _*untitled")
"""==========================="""
"""main menu work starts from here"""
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New File  (ctrl+N)",command=OpenNew)
m1.add_command(label="open File  (ctrl+O)",command=openFiletoCodetext)
m1.add_command(label="Open File without clear",command=FileOpenwindow )

m1.add_separator()
m1.add_command(label="Save  (ctrl+s)",command=saveFile)
m1.add_command(label="Save As (ctrl+d)",command=saveasFile)
m1.add_command(label="File Info (ctrl+i)",command=TellFileInfo)
m1.add_separator()
m1.add_command(label="Exit",activebackground="black",command=exit)

m2=Menu(root,tearoff=0)
m2.add_command(label="Select")
m2.add_command(label="Select All  ( ctrl+A)",command=DoSelect)
m2.add_separator()
m2.add_command(label="Cut  (ctrl+x)",command=DoCut)
m2.add_command(label="Copy (ctrl+c)",command=DoCopy)
m2.add_command(label="Paste (ctrl+v)",command=DoPaste)
m2.add_command(label="Undo (ctrl+z)",command=DoUndo)
m2.add_separator()
m2.add_command(label='Delete',command=deleteSelectedArea)
m2.add_command(label='Delete All',activebackground="red",command=clearText)
m2.add_command(label='Clear Text',command=clearText)

m3=Menu(root,tearoff=0)
m3.add_command(label="Font Style",command=fontStyle)
m3.add_command(label="Background Theme",command=changebackgroundColor)
m3.add_command(label="Text Color",command=changeforgroundColor)
m3.add_command(label="New Window",command=newWindow)
m3.add_command(label="Date-Time",command=printDatetime)
# m4=Menu(m3,tearoff=0)
# m4.add_command(label="Zoom In")
# m4.add_command(label="Zoom Out")
# m3.add_cascade(label="Zoom" ,menu=m4)

m5=Menu(root,tearoff=0)
m5.add_command(label="Compile",command=docompile)
m5.add_command(label="Run",command=runCode)
m5.add_command(label="Compile And Run",command=compileAndCode)

m6=Menu(root,tearoff=0)
m6.add_command(label="Go To Site",command=gototheSite)

mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Edit" ,menu=m2)
mainmenu.add_cascade(label="Format" ,menu=m3)
mainmenu.add_cascade(label="Execute" ,menu=m5)
mainmenu.add_cascade(label="Help" ,menu=m6)
root.config(menu=mainmenu)
"""menu Work End Here======================="""

"""making the task bar"""
taskBar=Frame(root)
taskBar.pack(side=BOTTOM,anchor=S,fill=X)
Label1=Label(taskBar,text="Coding..",fg="black")
Label1.pack(side=RIGHT,anchor=SE,padx=5,pady=3)
Label2=Label(taskBar,text="C\\C++")
Label2.pack(side=RIGHT,anchor=SE,pady=3,padx=5,)
label3=Label(taskBar,text=str(datetime.datetime.now()))
label3.pack(side=LEFT,anchor=SW)
"""=================================================="""

"""Fixing the scroll bar"""
setScroll=Scrollbar(root,)
setScroll.pack(side=RIGHT,fill=Y)

CodeText=Text(root,yscrollcommand=setScroll.set,font="Times 20",wrap=WORD,bg="blue",fg="yellow",insertofftime=200,insertontime=200,undo=1,insertbackground="red",insertwidth=8)
CodeText.pack(fill=BOTH,expand=1)

"""binding the function for shortcut key for saving the file new file and save as file"""

CodeText.bind('<Control-s>',saveFile)
CodeText.bind('<Control-d>',saveasFile)
CodeText.bind('<Control-n>',OpenNew)
CodeText.bind('<Control-o>',openFiletoCodetext)
CodeText.bind('<Control-i>',TellFileInfo)


setScroll.config(command=CodeText.yview)


root.mainloop()


"""finally it completed on 7/12/2020   Himanshu sharma dwara nirmit ye application mahan hai"""
