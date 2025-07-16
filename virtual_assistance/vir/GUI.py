from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("Gen")
root.geometry("500x700")

root.resizable(False, False)
root.config(bg="#22938d")

def ask():
    user_val=speech_to_text.speech_to_text()
    bot_val=action.action(user_val)
    text.insert(END,'User--->'+ user_val+"\n")
    if bot_val!=None:
        text.insert(END,"Bot<---"+str(bot_val)+"\n")
    if bot_val=="ok sir":
        root.destroy()    
    
    
def send():
    send = entry.get()
    bot = action.action(send)
    text.insert(END,'User--->'+ send+"\n")
    if bot!=None:
        text.insert(END,"Bot<---"+str(bot)+"\n")
    if bot=="ok sir":
        root.destroy() 

    
def del_text():
    text.delete('1.0',"end")


frame = LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised" , bg="#22938d", fg="white", font=("Cosmic sans ms", 20))
frame.config(bg="#042337", fg="white")
frame.grid(row=0, column=1, padx=55, pady=10)

text_label = Label(frame,text = "Gen", font = ("Consmic sans ms", 20,"bold"), bg="#042337", fg="white")
text_label.grid(row=0,column=0,padx=20,pady=10)



# image 
original_image = Image.open("image/cute-smiling-robot-virtual-assistant-in-your-device-future-robotic-technology-artificial-intelligence-mascot-ai-chat-bot-vector.jpg")

resized_image = original_image.resize((180, 180), Image.LANCZOS)  # Use LANCZOS for high-quality downsampling

image = ImageTk.PhotoImage(resized_image)
image_label = Label(frame, image=image, bg="#042337")
image_label.grid(row=1, column=0, pady=20)

# adding text 
# Remove text.place(...) and use grid instead
text = Text(root, font=('courier 1 bold '), bg="#5fd6c1", fg="white")
text.grid(row=2, column=0)
text.place(x=65,y=375,width=375,height=100)


# entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=75,y=500,width=350,height=50)

# button
Button1 = Button(root, text="Ask",bg="#11B59C",pady=16,padx=40,borderwidth=3 , relief=SOLID,command = ask)
Button1.place(x=50, y=575)

Button2 = Button(root, text="Send",bg="#11B59C",pady=16,padx=40,borderwidth=3 , relief=SOLID,command = send)
Button2.place(x=350, y=575)

Button3 = Button(root, text="Delete",bg="#11B59C",pady=16,padx=40,borderwidth=3 , relief=SOLID,command = del_text)
Button3.place(x=195, y=575)


# Make sure the root window expands properly
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
