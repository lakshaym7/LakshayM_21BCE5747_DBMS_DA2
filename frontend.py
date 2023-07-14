#Frontend

from tkinter import *
import tkinter.messagebox
import backend

class Vehicle:
	def __init__(self, root):
		self.root=root
		self.root.title("Online Vehicle Ticket Booking System")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="black")

		
		VehicleID=StringVar()
		Manufacturer=StringVar()
		Model=StringVar()
		Year=StringVar()
		Type=StringVar()
		Mileage=StringVar()
		EngineCapacity=StringVar()
		Availability=StringVar()
		
		
		#Fuctions
		def iExit():
			iExit=tkinter.messagebox.askyesno("Online Vehicle Booking System", "Are you sure???")
			if iExit>0:
				root.destroy()
			return

		def clcdata():
			self.txtVehicleID.delete(0,END)
			self.txtManufacturer.delete(0,END)
			self.txtModel.delete(0,END)
			self.txtYear.delete(0,END)
			self.txtType.delete(0,END)
			self.txtMileage.delete(0,END)
			self.txtAvailability.delete(0,END)
			self.txtEngineCapacity.delete(0,END)

		def adddata():
			if(len(VehicleID.get())!=0):
				backend.AddVehicleRec(VehicleID.get(),Manufacturer.get(),Model.get(),Year.get(),Type.get(),Mileage.get(),EngineCapacity.get(),Availability.get())
				VehicleList.delete(0,END)
				VehicleList.insert(END,(VehicleID.get(),Manufacturer.get(),Model.get(),Year.get(),Type.get(),Mileage.get(),EngineCapacity.get(),Availability.get()))

		def disdata():
			VehicleList.delete(0,END)
			for row in backend.ViewVehicleData():
				VehicleList.insert(END, row, str(""))

		def vehiclerec(event):
			global sd
			searchvehicle=VehicleList.curselection()[0]
			sd=VehicleList.get(searchvehicle)

			self.txtVehicleID.delete(0,END)
			self.txtVehicleID.insert(END,sd[0])
			self.txtManufacturer.delete(0,END)
			self.txtManufacturer.insert(END,sd[1])
			self.txtModel.delete(0,END)
			self.txtModel.insert(END,sd[2])
			self.txtYear.delete(0,END)
			self.txtYear.insert(END,sd[3])
			self.txtType.delete(0,END)
			self.txtType.insert(END,sd[4])
			self.txtMileage.delete(0,END)
			self.txtMileage.insert(END,sd[5])
			self.txtEngineCapacity.delete(0,END)
			self.txtEngineCapacity.insert(END,sd[6])
			self.txtAvailability.delete(0,END)
			self.txtAvailability.insert(END,sd[7])

		def deldata():
			if(len(VehicleID.get())!=0):
				backend.DeleteVehicleRec(sd[0])
				clcdata()
				disdata()

		def searchdb():
			VehicleList.delete(0,END)
			for row in backend.SearchVehicleData(VehicleID.get(),Manufacturer.get(),Model.get(),Year.get(),Type.get(),Mileage.get(),EngineCapacity.get(),Availability.get()):
				VehicleList.insert(END, row, str(""))

		def updata():
			if(len(VehicleID.get())!=0):
				backend.DeleteVehicleRec(sd[0])
			if(len(VehicleID.get())!=0):
				backend.AddVehicleRec(VehicleID.get(),Manufacturer.get(),Model.get(),Year.get(),Type.get(),Mileage.get(),EngineCapacity.get(),Availability.get())
				VehicleList.delete(0,END)
				VehicleList.insert(END,(VehicleID.get(),Manufacturer.get(),Model.get(),Year.get(),Type.get(),Mileage.get(),EngineCapacity.get(),Availability.get()))

		#Frames
		MainFrame=Frame(self.root, bg="black")
		MainFrame.grid()

		TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
		TFrame.pack(side=TOP)

		self.TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="ONLINE VEHICLE BOOKING SYSTEM", bg="black", fg="orange")
		self.TFrame.grid() 

		BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
		BFrame.pack(side=BOTTOM)

		DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
		DFrame.pack(side=BOTTOM)

		DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Vehicle Info_\n", fg="white")
		DFrameL.pack(side=LEFT)

		DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Vehicle Details_\n", fg="white")
		DFrameR.pack(side=RIGHT)

		#Labels & Entry Box

		self.lblVehicleID=Label(DFrameL, font=('Arial', 18, 'bold'), text="Vehicle ID:", padx=2, pady=2, bg="black", fg="orange")
		self.lblVehicleID.grid(row=0, column=0, sticky=W)
		self.txtVehicleID=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=VehicleID, width=39, bg="black", fg="white")
		self.txtVehicleID.grid(row=0, column=1) 

		self.lblManufacturer=Label(DFrameL, font=('Arial', 18, 'bold'), text="Manufacturer", padx=2, pady=2, bg="black", fg="orange")
		self.lblManufacturer.grid(row=1, column=0, sticky=W) 
		self.txtManufacturer=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Manufacturer, width=39, bg="black", fg="white")
		self.txtManufacturer.grid(row=1, column=1)

		self.lblModel=Label(DFrameL, font=('Arial', 18, 'bold'), text="Model:", padx=2, pady=2, bg="black", fg="orange")
		self.lblModel.grid(row=2, column=0, sticky=W) 
		self.txtModel=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Model, width=39, bg="black", fg="white")
		self.txtModel.grid(row=2, column=1)

		self.lblYear=Label(DFrameL, font=('Arial', 18, 'bold'), text="Year:", padx=2, pady=2, bg="black", fg="orange")
		self.lblYear.grid(row=3, column=0, sticky=W) 
		self.txtYear=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Year, width=39, bg="black", fg="white")
		self.txtYear.grid(row=3, column=1)

		self.lblType=Label(DFrameL, font=('Arial', 18, 'bold'), text="Type:", padx=2, pady=2, bg="black", fg="orange")
		self.lblType.grid(row=4, column=0, sticky=W) 
		self.txtType=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Type, width=39, bg="black", fg="white")
		self.txtType.grid(row=4, column=1)

		self.lblMileage=Label(DFrameL, font=('Arial', 18, 'bold'), text="Mileage (miles per gallon):", padx=2, pady=2, bg="black", fg="orange")
		self.lblMileage.grid(row=5, column=0, sticky=W) 
		self.txtMileage=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Mileage, width=39, bg="black", fg="white")
		self.txtMileage.grid(row=5, column=1)

		self.lblEngineCapacity=Label(DFrameL, font=('Arial', 18, 'bold'), text="EngineCapacity (Litres):", padx=2, pady=2, bg="black", fg="orange")
		self.lblEngineCapacity.grid(row=6, column=0, sticky=W) 
		self.txtEngineCapacity=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=EngineCapacity, width=39, bg="black", fg="white")
		self.txtEngineCapacity.grid(row=6, column=1)

		self.lblAvailability=Label(DFrameL, font=('Arial', 18, 'bold'), text="Availability (Yes/No):", padx=2, pady=2, bg="black", fg="orange")
		self.lblAvailability.grid(row=7, column=0, sticky=W) 
		self.txtAvailability=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Availability, width=39, bg="black", fg="white")
		self.txtAvailability.grid(row=7, column=1)

		#ListBox & ScrollBar
		sb=Scrollbar(DFrameR)
		sb.grid(row=0, column=1, sticky='ns')

		VehicleList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
		VehicleList.bind('<<ListboxSelect>>', vehiclerec)
		VehicleList.grid(row=0, column=0, padx=8)
		sb.config(command=VehicleList.yview)

		#Buttons
		self.btnadd=Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=adddata)
		self.btnadd.grid(row=0, column=0)

		self.btndis=Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=disdata)
		self.btndis.grid(row=0, column=1)

		self.btnclc=Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=clcdata)
		self.btnclc.grid(row=0, column=2)

		self.btnse=Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=searchdb)
		self.btnse.grid(row=0, column=3)

		self.btndel=Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=deldata)
		self.btndel.grid(row=0, column=4)

		self.btnup=Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=updata)
		self.btnup.grid(row=0, column=5)

		self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=iExit)
		self.btnx.grid(row=0, column=6)


if __name__=='__main__':
	root=Tk()
	datbase=Vehicle(root)
	root.mainloop()
