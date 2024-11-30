from tkinter import *
from tkinter import messagebox
import random
# Functionality Part
def clear():
    sunscreenEntry.insert(0,END)
    nightcreamEntry.insert(0,END)
    serumEntry.insert(0,END)
    foamEntry.insert(0,END)
    tonerEntry.insert(0,END)
    maskEntry.insert(0,END)
   
   
    riceEntry.insert(0,END)
    oilEntry.insert(0,END)
    saltEntry.insert(0,END)
    sugarEntry.insert(0,END)
    butterEntry.insert(0,END)
    teaEntry.insert(0,END)
    
   
    coffeeamericanoEntry.insert(0,END)
    pistachiolatteEntry.insert(0,END)
    masalachaiEntry.insert(0,END)
    cinnamondolceLatteEntry.insert(0,END)
    peppermintmochaEntry.insert(0,END)
    lattemacchiatoEntry.insert(0,END)
    
    
    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    coffeetaxEntry.delete(0,END)
    
   
    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    coffeepriceEntry.delete(0,END)
    
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    
    textarea.delete(0,END)

    
    

billnumber=random.randint(500,1000)
def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error', 'Customer Details are required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and coffeepriceEntry.get()=='':
         messagebox.showerror('Error', 'No Products are selected')
    elif cosmeticpriceEntry.get()=='0$' and grocerypriceEntry.get()=='0$'and coffeepriceEntry.get()=='0$':
        messagebox.showerror('Error', 'No Products are selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, '\t**Welcome Customer**')
        textarea.insert(END, f'\nBill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}')
        textarea.insert(END,'\n*****************************************')
        textarea.insert(END, 'Product\t\tQuantity\t\tPrice')
        textarea.insert(END,'\n*****************************************')
        if sunscreenEntry.get()!='0':
            textarea.insert(END,f'\nSunscreen\t\t{sunscreenEntry.get()}\t\t{sunscreenprice} $')
        if nightcreamEntry.get()!='0':
            textarea.insert(END,f'\nNightcream\t\t{nightcreamEntry.get()}\t\t{nightcreamprice} $')
        if serumEntry.get()!='0':
            textarea.insert(END,f'\nSerum\t\t{serumEntry.get()}\t\t{serumprice} $')
        if foamEntry.get()!='0':
            textarea.insert(END,f'\nfoam\t\t{foamEntry.get()}\t\t{foamprice} $')
        if tonerEntry.get()!='0':
            textarea.insert(END,f'\nToner\t\t{tonerEntry.get()}\t\t{tonerprice} $')
        if maskEntry.get()!='0':
            textarea.insert(END,f'\nMask\t\t{maskEntry.get()}\t\t{maskprice} $')
            
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t{riceEntry.get()}\t\t{riceprice} $')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t{oilEntry.get()}\t\t{oilprice} $')
        if saltEntry.get()!='0':
            textarea.insert(END,f'\nSalt\t\t{saltEntry.get()}\t\t{saltprice} $')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t{sugarEntry.get()}\t\t{sugarprice} $')
        if butterEntry.get()!='0':
            textarea.insert(END,f'\nButter\t\t{butterEntry.get()}\t\t{butterprice} $')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t{teaEntry.get()}\t\t{teaprice} $')
            
        if coffeeamericanoEntry.get()!='0':
            textarea.insert(END,f'\nCoffee Americano\t\t{coffeeamericanoEntry.get()}\t\t{coffeeamericanoprice} $')
        if pistachiolatteEntry.get()!='0':
            textarea.insert(END,f'\nPistachioLatte\t\t{pistachiolatteEntry.get()}\t\t{pistachiolatteprice} $')
        if masalachaiEntry.get()!='0':
            textarea.insert(END,f'\nMasalachai\t\t{masalachaiEntry.get()}\t\t{masalachaiprice} $')
        if cinnamondolceLatteEntry.get()!='0':
            textarea.insert(END,f'\nCinnamon DolceLatte\t\t{cinnamondolceLatteEntry.get()}\t\t{cinnamondolceLatteprice} $')
        if peppermintmochaEntry.get()!='0':
            textarea.insert(END,f'\nPepper Mintmocha\t\t{peppermintmochaEntry.get()}\t\t{peppermintmochaprice} $')
        if lattemacchiatoEntry.get()!='0':
            textarea.insert(END,f'\nLatte Macchiato\t\t{lattemacchiatoEntry.get()}\t\t{lattemacchiatoprice} $')
        
        textarea.insert(END, '\n----------------------------------------')
        
        
        if cosmetictaxEntry.get()!='0.0$':
            textarea.insert(END, f'\n Cosmetic Tax\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0$':
            textarea.insert(END, f'\n Grocery Tax\t\t{grocerytaxEntry.get()}')
        if coffeetaxEntry.get()!='0.0$':
            textarea.insert(END, f'\n Coffee Tax\t\t{coffeetaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill\t\t\t\t\t{totalbill}')
        




















#cosmetic price calculator
def total():
    global sunscreenprice,nightcreamprice,serumprice,foamprice,tonerprice,maskprice
    global riceprice,oilprice,saltprice,sugarprice,butterprice,teaprice
    global coffeeamericanoprice,pistachiolatteprice,masalachaiprice,cinnamondolceLatteprice,peppermintmochaprice,lattemacchiatoprice
    global totalbill
    sunscreenprice=int(sunscreenEntry.get()) * 12
    nightcreamprice=int(nightcreamEntry.get()) * 8
    serumprice=int(serumEntry.get()) * 13
    foamprice=int(foamEntry.get())* 10
    tonerprice=int(tonerEntry.get()) * 11
    maskprice=int(maskEntry.get())*  5
    
    totalcosmeticprice=float(sunscreenprice+nightcreamprice+serumprice+foamprice+tonerprice+maskprice)
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} $')
    
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax) + '$')
    
    
#grocery price calculator
    riceprice=int(riceEntry.get())* 30
    oilprice=int(oilEntry.get())* 14
    saltprice=int(saltEntry.get())* 2
    sugarprice=int(sugarEntry.get())* 3
    butterprice=int(butterEntry.get())* 4
    teaprice=int(teaEntry.get())* 6
    totalgroceryprice=float(riceprice+oilprice+saltprice+sugarprice+butterprice+teaprice)
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} $')
    
    
    grocerytax=totalgroceryprice*0.12
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax) + '$')
    
    
    
#coffee price calculator
    coffeeamericanoprice=int(coffeeamericanoEntry.get())* 4
    pistachiolatteprice=int(pistachiolatteEntry.get())* 5
    masalachaiprice=int(masalachaiEntry.get())* 6
    cinnamondolceLatteprice=int(cinnamondolceLatteEntry.get())* 8
    peppermintmochaprice=int(peppermintmochaEntry.get())* 7
    lattemacchiatoprice=int(lattemacchiatoEntry.get())* 10
    totalcoffeeprice=float(coffeeamericanoprice+pistachiolatteprice+masalachaiprice+cinnamondolceLatteprice+peppermintmochaprice+lattemacchiatoprice)
    coffeepriceEntry.delete(0,END)
    coffeepriceEntry.insert(0,f'{totalcoffeeprice} $')   

    coffeetax=totalcoffeeprice*0.12
    coffeetaxEntry.delete(0,END)
    coffeetaxEntry.insert(0,str(coffeetax) + '$')
    
    totalbill=totalcosmeticprice+totalgroceryprice+totalcoffeeprice+cosmetictax+grocerytax+coffeetax








#GUI Part
root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
headingLabel=Label(root,text='Retail Billing System', font=('times new roman', 30, 'bold')
                   ,bg='gray9',fg='red2',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('time new roman',15, 'bold')
                                  ,fg='red2',bd=8,relief=GROOVE,bg='gray9')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row='0',column='1',padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row='0',column='3',padx=8)




productsFrame=Frame(root)
productsFrame.pack()

cosmeticFrame=LabelFrame(productsFrame,text='Cosmetics',font=('time new roman',15, 'bold')
                                  ,fg='red2',bd=8,relief=GROOVE,bg='gray9')
cosmeticFrame.grid(row=0,column=0)

sunscreenLabel=Label(cosmeticFrame,text='SunScreen',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
sunscreenLabel.grid(row=0,column=0,pady=9,padx=10)

sunscreenEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sunscreenEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
sunscreenEntry.insert(0,0)

nightcreamLabel=Label(cosmeticFrame,text='Night Cream',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
nightcreamLabel.grid(row=1,column=0,pady=9,padx=10)

nightcreamEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
nightcreamEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
nightcreamEntry.insert(0,0)


serumLabel=Label(cosmeticFrame,text='Serum',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
serumLabel.grid(row=2,column=0,pady=9,padx=10)

serumEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
serumEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
serumEntry.insert(0,0)
foamLabel=Label(cosmeticFrame,text='Foam',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
foamLabel.grid(row=3,column=0,pady=9,padx=10)

foamEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
foamEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
foamEntry.insert(0,0)
tonerLabel=Label(cosmeticFrame,text='Toner',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
tonerLabel.grid(row=4,column=0,pady=9,padx=10)

tonerEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
tonerEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
tonerEntry.insert(0,0)
maskLabel=Label(cosmeticFrame,text='Mask',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
maskLabel.grid(row=5,column=0,pady=9,padx=10)

maskEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maskEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
maskEntry.insert(0,0)
groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('time new roman',15, 'bold')
                                  ,fg='red2',bd=8,relief=GROOVE,bg='gray9')
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10)

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
riceEntry.insert(0,0)
oilLabel=Label(groceryFrame,text='Oil',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10)

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
oilEntry.insert(0,0)
saltLabel=Label(groceryFrame,text='Salt',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
saltLabel.grid(row=2,column=0,pady=9,padx=10)

saltEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
saltEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
saltEntry.insert(0,0)
sugarLabel=Label(groceryFrame,text='Sugar',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
sugarLabel.grid(row=3,column=0,pady=9,padx=10)

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
sugarEntry.insert(0,0)
butterLabel=Label(groceryFrame,text='Butter',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
butterLabel.grid(row=4,column=0,pady=9,padx=10)

butterEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
butterEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
butterEntry.insert(0,0)
teaLabel=Label(groceryFrame,text='Tea',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10)

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
teaEntry.insert(0,0)
coffeeFrame=LabelFrame(productsFrame,text='Coffee',font=('time new roman',15, 'bold')
                                  ,fg='red2',bd=8,relief=GROOVE,bg='gray9')
coffeeFrame.grid(row=0,column=2)

coffeeamericanoLabel=Label(coffeeFrame,text='Caffe Americano',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
coffeeamericanoLabel.grid(row=0,column=0,pady=9,padx=10)

coffeeamericanoEntry=Entry(coffeeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
coffeeamericanoEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
coffeeamericanoEntry.insert(0,0)
pistachiolatteLabel=Label(coffeeFrame,text='Pistachio Latte',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
pistachiolatteLabel.grid(row=1,column=0,pady=9,padx=10)

pistachiolatteEntry=Entry(coffeeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pistachiolatteEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
pistachiolatteEntry.insert(0,0)

masalachaiLabel=Label(coffeeFrame,text='Masala Chai',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
masalachaiLabel.grid(row=2,column=0,pady=9,padx=10)

masalachaiEntry=Entry(coffeeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
masalachaiEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
masalachaiEntry.insert(0,0)
cinnamondolceLatteLabel=Label(coffeeFrame,text='Cinnamon DolceLatte',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
cinnamondolceLatteLabel.grid(row=3,column=0,pady=9,padx=10)

cinnamondolceLatteEntry=Entry(coffeeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cinnamondolceLatteEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
cinnamondolceLatteEntry.insert(0,0)

peppermintmochaLabel=Label(coffeeFrame,text='Peppermint Mocha',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
peppermintmochaLabel.grid(row=4,column=0,pady=9,padx=10)

peppermintmochaEntry=Entry(coffeeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
peppermintmochaEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
peppermintmochaEntry.insert(0,0)

lattemacchiatoLabel=Label(coffeeFrame,text='Latte Macchiato',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
lattemacchiatoLabel.grid(row=5,column=0,pady=9,padx=10)

lattemacchiatoEntry=Entry(coffeeFrame,font=('times new roman',15,'bold'),width=10,bd=5)
lattemacchiatoEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
lattemacchiatoEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=17,width=40,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('time new roman',15, 'bold')
                                  ,fg='red2',bd=8,relief=GROOVE,bg='gray9')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=9,padx=10)

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10)

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')


coffeepriceLabel=Label(billmenuFrame,text='Coffee Price',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
coffeepriceLabel.grid(row=2,column=0,pady=9,padx=10)

coffeepriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
coffeepriceEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')

cosmetictaxLabel=Label(billmenuFrame,text='Cosmentic Tax',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=9,padx=10)

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=9,padx=10,sticky='w')

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=9,padx=10)

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=9,padx=10,sticky='w')


coffeetaxLabel=Label(billmenuFrame,text='Coffee Tax',font=('time new roman',15,'bold')
                ,bg='gray9',fg='white')
coffeetaxLabel.grid(row=2,column=2,pady=9,padx=10)

coffeetaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
coffeetaxEntry.grid(row=2,column=3,pady=9,padx=10,sticky='w')

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold')
                  ,bg='gray9',fg='white',bd=5,width=8,pady=10,command=total )
totalButton.grid(row=0,column=0,pady=20,padx=5)


billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold')
                  ,bg='gray9',fg='white',bd=5,width=8,pady=10,command=bill_area )
billButton.grid(row=0,column=1,pady=20,padx=5)


clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold')
                  ,bg='gray9',fg='white',bd=5,width=8,pady=10, command=clear)
clearButton.grid(row=0,column=2,pady=20,padx=5)
























root.mainloop()

