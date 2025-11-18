def sylvia():
    window1= Toplevel()
    window1.geometry("400x600")
    window1.config(bg="white")
    window1.image=PhotoImage(file="C:\\Users\\jtees\\Documents\\Python GUI Projects\\poems generator\\red bow.png")
    label1=Label(window1,text="Mad Girl's Love Song",font=("ink free",15,"bold"),fg="#deb2c5",bg="white")
    label1.config(image=window1.image,compound="left")
    label1.pack()
    text = Text(window1, wrap=WORD, font=("ink free", 12,"bold"),fg="white",bg="#deb2c5")
    text.pack(expand=True, fill="both")

    poem = """    I shut my eyes and all the world drops dead; 
    I lift my lids and all is born again.
    (I think I made you up inside my head.)
    
    The stars go waltzing out in blue and red, 
    And arbitrary blackness gallops in.
    I shut my eyes and all the world drops dead.
    I dreamed that you bewitched me into bed  
    And sung me moon-struck, 
    kissed me quite insane.
    (I think I made you up inside).
     
    God topples from the sky, hell's fires fade:
    Exit seraphim and Satan's men:
    I shut my eyes and all the world drops dead
    I fancied you'd return the way you said,
    But I grow old and I forget your name.
    (I think I made you up inside my head.)

    I should have loved a thunderbird instead;
    "At least when spring comes they roar back again.
    I shut my eyes and all the world drops dead.
    (I think I made you up inside my head.)"""

    text.insert(END, poem)
def mahmood():
    window2=Toplevel()
    window2.geometry("400x400")
    window2.config(bg="white")
    window2.image2=PhotoImage(file="C:\\Users\\jtees\\Documents\\Python GUI Projects\\poems generator\\broken heart.png")
    label2=Label(window2,text="The War will End",font=("ink free",15,"bold"),bg="white",fg="#410d0d")
    label2.config(image=window2.image2,compound="left")
    label2.pack()
    text = Text(window2, wrap=WORD, font=("ink free", 12,"bold"),fg="white",bg="#410d0d")
    text.pack(expand=True, fill="both")

    poem ="""       The war will end and the leaders will shake hands,
        and that old woman will remain waiting for her martyred son,
        and that girl will wait for her beloved husband, 
        and the children will wait for their heroic father,
        I do not know who sold the homeland but I know who paid the price."""

    text.insert(END, poem)
def albert():
    window3=Toplevel()
    window3.geometry("400x400")
    window3.config(bg="white")
    window3.image3=PhotoImage(file="C:\\Users\\jtees\\Documents\\Python GUI Projects\\poems generator\\clock.png")
    label3=Label(window3,text="The Myth of Sisyphus and Other Essays",font=("ink free",15,"bold"),bg="white",fg="#9cbb85")
    label3.config(image=window3.image3,compound="bottom")
    label3.pack()
    text = Text(window3, wrap=WORD, font=("ink free", 12,"bold"),fg="white",bg="#9cbb85")
    text.pack(expand=True, fill="both")

    poem ="""       There's no tragedy in having to start again,
          as long as you start again."""

    text.insert(END, poem)
def kafka():
    window4=Toplevel()
    window4.geometry("400x500")
    window4.config(bg="white")
    window4.image4=PhotoImage(file="C:\\Users\\jtees\\Documents\\Python GUI Projects\\poems generator\\cup.png")
    label4=Label(window4,text="Letters to Milena",font=("ink free",15,"bold"),bg="white",fg="black")
    label4.config(image=window4.image4,compound="bottom")
    label4.pack()
    text = Text(window4, wrap=WORD, font=("ink free", 12,"bold"),fg="white",bg="black")
    text.pack(expand=True, fill="both")

    poem ="""       Dear Milena,
        I wish the world were ending tomorrow.
        Then I could take the next train, arrive at your doorstep in Vienna, and say: 
        “Come with me, Milena. We are going to love each other without scruples or fear or restraint. 
        Because the world is ending tomorrow.” 
        Perhaps we don’t love unreasonably because we think we have time, or have to reckon with time. 
        But what if we don't have time? Or what if time, as we know it, is irrelevant?
        Ah, if only the world were ending tomorrow. We could help each other very much."""

    text.insert(END, poem)
def give_poem():
    selection = listbox.curselection()  # returns tuple of selected indices
    if selection:
        author = listbox.get(selection[0])  # get author name
        author_functions[author]() 

author_functions = {
    "Sylvia Plath": sylvia,
    "Mahmood Darwaish": mahmood,
    "Albert Camus": albert,
    "Franz Kafka": kafka
}
authors=list(author_functions.keys())

from tkinter import *
from tkinter import ttk
window=Tk()
window.config(bg="white")
label= Label(window,text="Poems for You",font=("ink free",20,"bold"),bg="white",fg="#97d0dd")
label.pack()

image= PhotoImage(file="C:\\Users\\jtees\\Documents\\Python GUI Projects\\poems generator\\blue flowers.png")
label.config(image=image,compound="bottom")

listbox=Listbox(window,font=("ink free",15,"bold"),bg="white",fg="#97d0dd")
listbox.pack(anchor="center")
for author in authors:
    listbox.insert(END,author)

submitbutton=Button(window,text="Give a poem",compound="bottom",font=("ink free",15,"bold"),fg="white",bg="#97d0dd"
                    ,activeforeground="#97d0dd",command=give_poem)

submitbutton.pack(anchor="center")

window.mainloop()