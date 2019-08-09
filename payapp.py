import datetime
import time
from tkinter import*

from tkinter import messagebox

root = Tk()
root.title("Payroll Systems")
root.geometry('1350x650+0+0')

Tops = Frame(root,width = 1350,height=50,bd=8,relief="raise")
Tops.pack(side = TOP)
f1 = Frame(root,width = 600,height = 600,bd=8,relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root,width = 300,height = 700,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1,width=600,height=200,bd=20,relief="raise")
f1a.pack(side=TOP)
f1b = Frame(f1,width=600,height=600,bd=20,relief="raise")
f1b.pack(side=TOP)

lblinfo = Label(Tops,font=('arial',60,'bold'),text="    Payroll Management System     ",bd=10)
lblinfo.grid(row=0,column=0)


def iExit():
    qExit = messagebox.askquestion("Payroll System","Do you want to exit the system?")
    if qExit =='yes':
        root.destroy()
        return

def Reset():
    Name.set("")
    Address.set("")
    Employer.set("")
    NINumber.set("")
    HoursWorked.set("")
    HourlyPay.set("")
    Tax.set("")
    Overtime.set("")
    GrossPay.set("")
    NetPay.set("")
    txtPaySlip.delete("1.0",END)
    return

def EnterInfo():
    txtPaySlip.delete("1.0",END)
    txtPaySlip.insert(END,"\t\tPay Slip\n\n")
    txtPaySlip.insert(END,"Name: \t\t"+Name.get()+"\n\n")
    txtPaySlip.insert(END,"Address: \t\t"+Address.get()+"\n\n")
    txtPaySlip.insert(END,"Employer: \t\t"+Employer.get()+"\n\n")
    txtPaySlip.insert(END,"E-Number: \t\t"+NINumber.get()+"\n\n")
    txtPaySlip.insert(END,"Hours Worked: \t\t"+HoursWorked.get()+"\n\n")
    txtPaySlip.insert(END,"Net Payable: \t\t"+GrossPay.get()+"\n\n")
    txtPaySlip.insert(END,"Wages per hour: \t\t"+HourlyPay.get()+"\n\n")
    txtPaySlip.insert(END,"Tax Paid: \t\t"+Tax.get()+"\n\n")
    txtPaySlip.insert(END,"Payable: \t\t"+NetPay.get()+"\n\n")
    return


def Weeklywages():
    HoursWorkedPerWeek= float(HoursWorked.get())*5
    WagesPerHours= float(HourlyPay.get())

    paydue = WagesPerHours * HoursWorkedPerWeek
    PaymentDue= "INR", str('%.2f' %(paydue))
    GrossPay.set(PaymentDue)

    tax = paydue*0.1
    Taxables = "INR",str('%.2f'%(tax))
    Tax.set(Taxables)

    netpay = paydue-tax
    NetPays = "INR",str('%.2f' %(netpay))
    NetPay.set(NetPays)

    if HoursWorkedPerWeek>40:
        OverTimeHours = (HoursWorkedPerWeek - 40)* WagesPerHours*0.5
        OverTimehrs = "INR", str('%.2f' %(OverTimeHours))
        Overtime.set(OverTimehrs)
    elif HoursWorkedPerWeek<=40:
        OverTimePay = 0
        OverTimehrs = "INR", str('%.2f' %(OverTimePay))
        Overtime.set(OverTimehrs)
    return
    

Name= StringVar()
Address= StringVar()
Employer= StringVar()
NINumber= StringVar()
HoursWorked= StringVar()
HourlyPay= StringVar()
Tax= StringVar()
Overtime= StringVar()
GrossPay= StringVar()
NetPay= StringVar()
TimeOfOrder = StringVar()
DateOfOrder = StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

lblName=Label(f1a,text="Name",font=('arial',16,'bold'),bd=20)
lblName.grid(row=0,column=0)
lblAddress=Label(f1a,text="Address",font=('arial',16,'bold'),bd=20)
lblAddress.grid(row=0,column=2)
lblEmployer=Label(f1a,text="Employer",font=('arial',16,'bold'),bd=20)
lblEmployer.grid(row=1,column=0)
lblNINumber=Label(f1a,text="E-Number",font=('arial',16,'bold'),bd=20)
lblNINumber.grid(row=1,column=2)
lblHoursWorked=Label(f1a,text="HoursWorked",font=('arial',16,'bold'),bd=20)
lblHoursWorked.grid(row=2,column=0)
lblHourlyPay=Label(f1a,text="Hourly Pay",font=('arial',16,'bold'),bd=20)
lblHourlyPay.grid(row=2,column=2)
lblTax=Label(f1a,text="Tax",font=('arial',16,'bold'),bd=20)
lblTax.grid(row=3,column=0)
lblOvertime=Label(f1a,text="OverTime",font=('arial',16,'bold'),bd=20)
lblOvertime.grid(row=3,column=2)
lblGrossPay=Label(f1a,text="Gross Pay",font=('arial',16,'bold'),bd=20)
lblGrossPay.grid(row=4,column=0)
lblNetPay=Label(f1a,text="Net Pay",font=('arial',16,'bold'),bd=20)
lblNetPay.grid(row=4,column=2)

etxtName= Entry(f1a,textvariable=Name,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=0,column=1)

etxtAddress= Entry(f1a,textvariable=Address,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=0,column=3)

etxtEmployer= Entry(f1a,textvariable=Employer,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=1,column=1)

etxtNINumber= Entry(f1a,textvariable=NINumber,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=1,column=3)

etxtHoursWorked= Entry(f1a,textvariable=HoursWorked,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=2,column=1)

etxtHourlyPay= Entry(f1a,textvariable=HourlyPay,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=2,column=3)

etxtTax= Entry(f1a,textvariable=Tax,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=3,column=1)

etxtOvertime= Entry(f1a,textvariable=Overtime,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=3,column=3)

etxtGrossPay= Entry(f1a,textvariable=GrossPay,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=4,column=1)

etxtNetPay= Entry(f1a,textvariable=NetPay,font=('arial',16,'bold'),bd=16,width=22,justify='left').grid(row=4,column=3)


lblPaySlip = Label(f2,textvariable=DateOfOrder,font=('arial',21,'bold')).grid(row=0,column=0)
txtPaySlip = Text(f2,height=22,width=34,bd=16,font=('arial',12,'bold'))
txtPaySlip.grid(row=1,column=0)


btnSalary=Button(f1b,text='Weekly Salary',command=Weeklywages,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=14,height=1).grid(row=0,column=0)
btnReset=Button(f1b,text='Reset',command=Reset,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=14,height=1).grid(row=0,column=1)
btnPaySlip=Button(f1b,text='View Payslip',command=EnterInfo,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=14,height=1).grid(row=0,column=2)
btnExit=Button(f1b,text='Exit System',command=iExit,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=14,height=1).grid(row=0,column=3)


root.mainloop()
