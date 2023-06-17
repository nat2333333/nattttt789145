import customtkinter
import math
app = customtkinter.CTk()
app.title('ว้ายที่ ขวาที แพลบๆๆๆๆ')
app.geometry("500x500")

answer_text = customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable=answer_text, font=('Aria', 40))
answer_label.pack(pady=(20, 0))



#ความแสดงผล
Iabel = customtkinter.CTkLabel(app,text="plus stuff", font=('Aria',40))
Iabel.pack(pady=(20,0))

#กล่องรับค่า inputs
entry = customtkinter.CTkEntry(app,placeholder_text="ใส่ input ของคุณตรงนี้")
entry.pack(pady=(15,0))

#ปุ่มกดโง่ๆ
def button_event():
    user_input = entry.get()
    answer = (int(user_input)**2) * 3.14 
    answer_text.set(answer) 
    answer_text.pack(pady=(15,0))





Button = customtkinter.CTkButton(app, text="กดกูสิ", command=button_event)
Button.pack(pady=(20, 0))





app.mainloop()