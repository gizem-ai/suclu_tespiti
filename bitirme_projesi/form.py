from tkinter import * 
from tkinter import messagebox

"""def show_msg():
    messagebox.showinfo("Message","Hey There! I hope you are doing well.")"""

form = Tk()   
form.geometry("350x250")  
sucluAdi = Label(form, text = "Adı: ").place(x = 40,y = 30)
sucluAdi_input_area = Entry(form,width = 30).place(x = 110,y = 30)
sucluSoyad = Label(form,text = "Soyadı: ").place(x = 40,y = 70)
sucluSoyad_entry_area = Entry(form,width = 30).place(x = 110,y = 70)
veriEkle = Button(form,text = "Veri Ekle").place(x = 40,y = 110)
submit_button = Button(form,text = "Kaydet").place(x = 140,y = 110)
aramaButonu = Button(form,text = "Arama Yap").place(x = 40,y = 145)
cikis = Button(form,text = "Çıkış", command=form.destroy).place(x = 140,y = 145)
form.mainloop() 