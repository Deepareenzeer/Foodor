import tkinter as tk
from tkinter import ttk,messagebox,Label
from tkinter.scrolledtext import ScrolledText
from tkinter import *

# Function Insert ScrollText
def addCombo() :
    st.insert('1.0',varSubj.get()+'\n')

# Function Clear ScrollText
def clear() :
    # ลบบรรทัดที่1 ถึงจุดสุดท้าย
    st.delete('1.0','end')
    st.focus()

def deltopline() :
    # ลบบรรทัดที่1 ถึงบรรทัดที่2
    st.delete('1.0',"2.0")

# Function แสดงรายละเอียดและการจ่ายเงิน
def chkClicked():
    st1.delete('1.0','end')
    thetext=f"{varChk1.get()} {varChk2.get()} {varChk3.get()}"
    thetext1=f"{varSize.get()}"
    st1.insert('1.0',f'{thetext }\n')
    st1.insert('2.0',f'{thetext1} \n')
    
def clear_selection():
    # ล้าง CheckBox และ RadioButton
    
    varChk1.set(False)  # ล้าง CheckBox
    varChk1.set('Not Selected')
    varChk2.set(False)
    varChk2.set('')
    varChk3.set(False)
    varChk3.set('')
    st1.delete('1.0','end')
    varSize.set("เงินสด")  # รีเซ็ต RadioButton ไปยัง Option 1
    chkClicked()  # อัปเดตการแสดงผลใน ScrolledText
    
# Main Program
root = tk.Tk()
root.title("Food Order")
root.geometry('600x400+200+100')

btn1=ttk.Entry(root)
btn1.place(x=10,y=10)
btn1.bind('<Return>',addCombo)

# สร้าง ComboBox
# สร้าง List ข้อมูล
foodlist=['ข้าวขาหมู','ข้าวหมูแดง','ข้าวมันไก่']
# สร้างตัวแปรสำหรับ Widget
varSubj=tk.StringVar()
# สร้าง Combobox + ผูกกับตัวแปร
cmbSubj=ttk.Combobox(root,textvariable=varSubj)
# โยนค่าในList ไปให้ Combobox
cmbSubj['values']=foodlist
cmbSubj.place(x=10,y=10)

# สร้างปุ่มบันทึกรายการอาหาร
btn1=ttk.Button(root,text='บันทึกรายการ',command=addCombo)
btn1.place(x=200,y=10)

# สร้างปุ่มลบรายการอาหาร
btn1=ttk.Button(root,text='ลบรายการ',command=deltopline)
btn1.place(x=200,y=50)

# สร้างปุ่มล้างรายการอาหาร
btn2=ttk.Button(root,text='ล้างรายการ',command=clear)
btn2.place(x=200,y=90)

# สร้าง ScrolledText รายการอาหาร
st=ScrolledText(root, width=33 ,height=11)
st.place(x=300,y=10)

# สร้าง Checkbox รายละเอียด
varChk1=tk.StringVar()
chk1=ttk.Checkbutton(root,text="อุ่น",variable=varChk1,onvalue='อุ่น',offvalue="",command=chkClicked)
chk1.place(x=30,y=220)
varChk1.set('อุ่น')

varChk2=tk.StringVar()
chk1=ttk.Checkbutton(root,text="รับถุง",variable=varChk2,onvalue='รับถุง',offvalue="",command=chkClicked)
chk1.place(x=115,y=220)
varChk2.set('รับถุง')

varChk3=tk.StringVar()
chk1=ttk.Checkbutton(root,text="รับช้อน",variable=varChk3,onvalue='รับช้อน',offvalue="",command=chkClicked)
chk1.place(x=200,y=220)
varChk3.set('รับช้อน')

# สร้าง Radio การจ่ายเงิน
varSize=tk.StringVar()
rdo1=ttk.Radiobutton(root,text='เงินสด',value='เงินสด',variable=varSize,command=chkClicked)
rdo1.place(x=30,y=270)
varSize.set('เงินสด')

varSize1=tk.StringVar()
rdo2=ttk.Radiobutton(root,text='เงินโอน',value='เงินโอน',variable=varSize,command=chkClicked)
rdo2.place(x=120,y=270)
varSize1.set('เงินโอน')

# สร้าง ScrolledText รายละเอียด
st1=ScrolledText(root, width=33 ,height=9)
st1.place(x=300,y=220)

# ปุ่มสำหรับล้าง CheckBox และ RadioButton
btn3=ttk.Button(root,text='ล้างรายการ',command=clear_selection)
btn3.place(x=200,y=265)

tk.mainloop()