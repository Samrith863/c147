from tkinter import *
root=Tk()
root.title("Ascii")
root.geometry("400x400")
input_1=Entry(root)
input_1.place(relx=0.5,rely=0.4,anchor=CENTER)
label_1=Label(root,text="Name in Ascii:",bg="light cyan",fg="black")
label_1.place(relx=0.5,rely=0.5,anchor=CENTER)
label_2=Label(root,text="Encrypted Name:",bg="light cyan",fg="black")
label_2.place(relx=0.5,rely=0.7,anchor=CENTER)

def asciiConverter():
    get_word=str(input_1.get())
    for letter in get_word:
        label_1['text']+=str(ord(letter))+"  "
        ascii=int(ord(letter))
        ascii=ascii-5
        label_2['text']+=str(chr(ascii))+"  "
    


btn=Button(root,text="Show Ascii Value",bg="royalblue",fg="white",command=asciiConverter)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()

