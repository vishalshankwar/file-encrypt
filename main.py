from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
import tkinter
from tkinter import filedialog
from cryptography.fernet import Fernet
import time
import os
from tkinter import ttk

key=""
filepath=""


#==================== EXIT FUNCTION ====================


def bahar():
    bahar=tkinter.messagebox.askyesno("FICRYPT","DO YOU WANT TO EXIT ?")
    if bahar>0:
        main_window.destroy()
        
        
#======================== HELPDESK FUNCTION ===================================

        
def help_wind():
    win=Toplevel()
    win.geometry("1920x1080")
    win.grab_set()
    tlbl=Label(win,text="HELPDESK",font=("times new roman",37,"bold"),bg="white",fg="red")
    tlbl.place(x=0,y=0,width=1530,height=60)
    
    img_top=Image.open(r'D:\Final Year Project\photos')
    img_top=img_top.resize((1920,1080))
    photoimg_top=ImageTk.PhotoImage(img_top)
    
    flbl=Label(win,image=photoimg_top)
    flbl.place(x=0,y=55,width=1920,height=1080) 
    
    e_lbl=Label(flbl,text="EMAIL",font=("times new roman",40,"bold"),fg="blue",bg="white")
    e_lbl.place(x=680,y=100)
    
    r_lbl=Label(flbl,text="rohitjadli03@gmail.com",font=("times new roman",40,"bold"),fg="blue",bg="white")
    r_lbl.place(x=510,y=300)
        
    v_lbl=Label(flbl,text="shankhwarvishal2001@gmail.com",font=("times new roman",40,"bold"),fg="blue",bg="white")
    v_lbl.place(x=410,y=450)

    win.wm_iconbitmap(r'D:\Final Year Project\photos')
    win.mainloop()
    
    
    
#========================= DECRYPTION WINDOW ===================================


def prg_dcr():

    root = Tk()
    root.title('FICRYPT')
    root.geometry("720x300+400+220")
    win.destroy()
    

    def run2():
        button1.destroy()
  
  #======== PROGRESSBAR FUNC ============================
        
        progressBar['maximum'] = 100
        global g
        for i in range(1,101):
            time.sleep(0.01)
            progressBar["value"] = i
            progressBar.update()
            g=i
            lbl=Label(frame,font=("times new roman",20,"bold"),fg="green",bg="black")
            lbl.place(x=350,y=150,height=50)
            lbl.config(text=str(g)+"%")
        
        messagebox.showinfo("SUCCESS","FILE DECRYPT SUCCESSFULLY")
        
            
            
        def dec(filepath):
                
            global key

            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
    
            fernet = Fernet(key)

            with open(filepath, 'rb') as enc_file:
                encrypted = enc_file.read()
                        
            decrypted = fernet.decrypt(encrypted)

            with open(filepath, 'wb') as dec_file:
                dec_file.write(decrypted)
        
        
        dec(filepath)
        
        root.destroy()

    
    

    

    
    
    

  
#================= FRAME =======================
    
    frame=Frame(root,bg="black")
    frame.place(x=0,y=0,width=720,height=300)

    plbl=Label(root,text="PROCESS",font=("times new roman",37,"bold"),bg="blue",fg="red")
    plbl.place(x=0,y=0,width=720,height=70)

  
    button1 = Button(frame,text="START",command=run2,font=("times new roman",22,"bold"),fg="white",bg="red")
    button1.place(x=313,y=210,width=120)



    progressBar = ttk.Progressbar(frame,orient="horizontal", length=680,mode="determinate")
    progressBar.place(x=17,y=120)
    
    root.wm_iconbitmap(r'D:\Final Year Project\photos')
    root.mainloop()
    







        

def decrypt_wind():
    global win
    win=Toplevel()
    win.geometry("720x320+400+220")
    win.grab_set()
    
    def bahar():
        bahar=tkinter.messagebox.askyesno("FICRYPT","DO YOU WANT TO EXIT ?")
        if bahar>0:
            win.destroy()
        
    def openfile():
        global filepath
        filepath=filedialog.askopenfilename(title="Select File For Decryption",filetypes=[("All Files","*.*")])
        lbl_enc=Label(win,text=filepath,font=("times new roman",16,"bold"),bg="black",fg="white")
        lbl_enc.place(x=60,y=115,width=600,height=50)
        #return filepath
    
    def rmvfile():
        lbl_enc=Label(win,text="",font=("times new roman",16,"bold"),bg="black",fg="white")
        lbl_enc.place(x=60,y=115,width=600,height=50)
    
    tlbl=Label(win,text="Selecting File For Decryption",font=("times new roman",37,"bold"),bg="blue",fg="red")
    tlbl.place(x=0,y=0,width=720,height=70)
        
    frame3=Frame(win,bg="black")
    frame3.place(x=0,y=70,width=720,height=383)
    
    rmv_btn=Button(frame3,text="REMOVE FILE",command=rmvfile,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
    rmv_btn.place(x=520,y=180,width=150,height=50)
        
    dcr_btn=Button(frame3,text="DECRYPT",command=prg_dcr,font=("times new roman",21,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
    dcr_btn.place(x=240,y=110,width=200,height=50)
        
    add_btn=Button(frame3,text="ADD FILE",command=openfile,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
    add_btn.place(x=30,y=180,width=150,height=50)

    ext_btn=Button(frame3,text="EXIT",command=bahar,font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
    ext_btn.place(x=265,y=180,width=150,height=50)
    
    win.wm_iconbitmap(r'D:\Final Year Project\photos')
    win.mainloop()
    
    
    
    
#======================= ENCRYPTION ==================================

# PROGRESS BAR AND ENCRYPTION FUNCTION WITH WINDOW

def prg_enc():

    root = Tk()
    root.title('FICRYPT')
    root.geometry("720x300+400+220")
    win.destroy()
    
    
    def run1():
        button1.destroy()
        
        progressBar['maximum'] = 100
        global g
        for i in range(1,101):
            time.sleep(0.01)
            progressBar["value"] = i
            progressBar.update()
            g=i
            lbl=Label(frame,font=("times new roman",20,"bold"),fg="green",bg="black")
            lbl.place(x=350,y=150,height=50)
            lbl.config(text=str(g)+"%")
        messagebox.showinfo("SUCCESS","FILE ENCRYPT SUCCESSFULLY")
        root.destroy()
        enc(filepath)
            
            
    def enc(filepath):
                
        global key

        key = Fernet.generate_key()
                
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
                    
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        with open(filepath, 'rb') as file:
            original = file.read()
	
        encrypted = fernet.encrypt(original)

        with open(filepath, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        '''my_file="{}".format(filepath)
        base = os.path.splitext(my_file)[0]
        os.rename(my_file, base + '.enc')'''

              
#================= FRAME =======================
    
    frame=Frame(root,bg="black")
    frame.place(x=0,y=0,width=720,height=300)

    plbl=Label(root,text="PROCESS",font=("times new roman",37,"bold"),bg="blue",fg="red")
    plbl.place(x=0,y=0,width=720,height=70)

  
    button1 = Button(frame,text="START",command=run1,font=("times new roman",22,"bold"),fg="white",bg="red")
    button1.place(x=313,y=210,width=120)



    progressBar = ttk.Progressbar(frame,orient="horizontal", length=680,mode="determinate")
    progressBar.place(x=17,y=120)
    
    root.wm_iconbitmap(r'D:\Final Year Project\photos')
    root.mainloop()
    







#========================== ENCRYPTION WINDOW ==========================

 

def encrypt_wind():
    global win
    win=Toplevel()
    win.geometry("720x320+400+220")
    win.grab_set()
    
    def bahar():
        bahar=tkinter.messagebox.askyesno("FICRYPT","DO YOU WANT TO EXIT ?")
        if bahar>0:
            win.destroy()
        
    def openfile():
        global filepath
        filepath=filedialog.askopenfilename(title="Select File For Encryption",filetypes=[("All Files","*.*")])
        lbl_enc=Label(win,text=filepath,font=("times new roman",16,"bold"),bg="black",fg="white")
        lbl_enc.place(x=60,y=115,width=600,height=50)
    
    def rmvfile():
        lbl_enc=Label(win,text="",font=("times new roman",16,"bold"),bg="black",fg="white")
        lbl_enc.place(x=60,y=115,width=600,height=50)


    tlbl=Label(win,text="Selecting File For Encryption",font=("times new roman",37,"bold"),bg="blue",fg="red")
    tlbl.place(x=0,y=0,width=720,height=70)
        
    frame2=Frame(win,bg="black")
    frame2.place(x=0,y=70,width=720,height=383)
        
    rmv_btn=Button(frame2,text="REMOVE FILE",command=rmvfile,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
    rmv_btn.place(x=520,y=180,width=150,height=50)
        
    enr_btn=Button(frame2,text="ENCRYPT",command=prg_enc,font=("times new roman",21,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
    enr_btn.place(x=240,y=110,width=200,height=50)
        
    add_btn=Button(frame2,text="ADD FILE",command=openfile,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
    add_btn.place(x=30,y=180,width=150,height=50)

    ext_btn=Button(frame2,text="EXIT",command=bahar,font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
    ext_btn.place(x=265,y=180,width=150,height=50)

    win.wm_iconbitmap(r'D:\Final Year Project\photos')
    win.mainloop()
    




main_window=Tk()


#=========== BACKGROUND IMAGE =========================


bg1=Image.open(r"D:\Final Year Project\photos")
bg1=bg1.resize((1920,1080))
bgimg1=ImageTk.PhotoImage(bg1)
        
bg_lbl=Label(main_window,image=bgimg1)
bg_lbl.place(x=0,y=0,width=1920,height=1080)


#=========== UPPER LABEL ================================


tlbl=Label(bg_lbl,text="FICRYPT - FILE ENCRYPTION SOFTWARE",font=("times new roman",40,"bold"),bg="black",fg="red")
tlbl.place(x=0,y=0,width=1530,height=70)


#================ ENCRYPTION BUTTON =========================

         
img1=Image.open(r'D:\Final Year Project\photos')
img1=img1.resize((160,140))
fotoimg1=ImageTk.PhotoImage(img1)
        
b1=Button(bg_lbl,image=fotoimg1,cursor="hand2",command=encrypt_wind)
b1.place(x=100,y=300,width=220,height=220)
        
b1_1=Button(bg_lbl,text="ENCRYPT",cursor="hand2",command=encrypt_wind,font=("times new roman",20,"bold"),bg="black",fg="red")
b1_1.place(x=100,y=480,width=220,height=60)


#==================== DECRYPTION BUTTON ==========================
        
                
img2=Image.open(r'D:\Final Year Project\photos')
img2=img2.resize((220,220))
fotoimg2=ImageTk.PhotoImage(img2)
        
b2=Button(bg_lbl,image=fotoimg2,cursor="hand2",command=decrypt_wind)
b2.place(x=450,y=300,width=220,height=220)
        
b2_1=Button(bg_lbl,text="DECRYPT",cursor="hand2",command=decrypt_wind,font=("times new roman",19,"bold"),bg="black",fg="red")
b2_1.place(x=450,y=480,width=220,height=60)


#=================== HELPDESK BUTTON ===========================

        
img3=Image.open(r'D:\Final Year Project\photos')
img3=img3.resize((210,180))
fotoimg3=ImageTk.PhotoImage(img3)
    
b3=Button(bg_lbl,image=fotoimg3,cursor="hand2",command=help_wind)
b3.place(x=800,y=300,width=220,height=220)
        
b3_1=Button(bg_lbl,text="HELPDESK",cursor="hand2",command=help_wind,font=("times new roman",19,"bold"),bg="black",fg="red")
b3_1.place(x=800,y=480,width=220,height=60)


#==================== EXIT BUTTON ================================

        
img4=Image.open(r'D:\Final Year Project\photos')
img4=img4.resize((160,140))
fotoimg4=ImageTk.PhotoImage(img4)
        
b4=Button(bg_lbl,image=fotoimg4,cursor="hand2",command=bahar)
b4.place(x=1150,y=300,width=220,height=220)
        
b4_1=Button(bg_lbl,text="EXIT",cursor="hand2",command=bahar,font=("times new roman",19,"bold"),bg="black",fg="red")
b4_1.place(x=1150,y=480,width=220,height=60)






main_window.geometry("1920x1080")
main_window.title("Ficrypt - File Encryption Software")
main_window.wm_iconbitmap(r'D:\Final Year Project\photos')
main_window.mainloop()
