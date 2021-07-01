from tkinter import Tk,IntVar,Label,Button,Radiobutton
from tkinter import messagebox
from os import system


class app:
	def __init__(self):
		self.bg = "#081828"
		self.fg = "#FFFFFF"
		self.versions = ["Home","Home N","Professional","Professional N","Education","Education N","Enterprise","Enterprise N","Home Single Language","Home Country Specific"]
		self.activation_codes = ["TX9XD-98N7V-6WMQ6-BX7FG-H8Q99","3KHY7-WNT83-DGQKR-F7HPR-844BM","W269N-WFGWX-YVC9B-4J6C9-T83GX","MH37W-N47XK-V7XM9-C7227-GCQG9","NW6C2-QMPVW-D7KKK-3GKT6-VCFB2","2WH4N-8QGBV-H22JP-CT43Q-MDWWJ","NPPR9-FWDCX-D2C8J-H872K-2YT43","DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4","7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH","PVMJN-6DFY6-9CCP6-7BKTT-D3WVR"]

		self.window()

	def activate(self):
		version = self.selection.get()
		proceed = messagebox.askyesno("activation",f"are you sure the version of windows you have installed on your system is 'Windows 10 {self.versions[version]}'?")
		activation_key = self.activation_codes[version]
		if proceed:
			system(f"slmgr /ipk {activation_key}")
			system("slmgr /skms kms10.msguides.com")
			system("slmgr /ato")
		self.root.destroy()

	def window(self):
		self.root = Tk()
		self.root.config(bg=self.bg)
		self.root.title("windows activation")
		self.root.geometry("390x270")
		self.widgets()
		self.root.mainloop()

	def widgets(self):
		self.selection = IntVar()
		title="select your windows version"
		self.title = Label(self.root,text=title,bg=self.bg,fg=self.fg,font=20)
		self.radio_home = Radiobutton(self.root,text=self.versions[0],variable=self.selection,value=0,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_home_n = Radiobutton(self.root,text=self.versions[1],variable=self.selection,value=1,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_pro = Radiobutton(self.root,text=self.versions[2],variable=self.selection,value=2,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_pro_n = Radiobutton(self.root,text=self.versions[3],variable=self.selection,value=3,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_education = Radiobutton(self.root,text=self.versions[4],variable=self.selection,value=4,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_education_n = Radiobutton(self.root,text=self.versions[5],variable=self.selection,value=5,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_enterprise = Radiobutton(self.root,text=self.versions[6],variable=self.selection,value=6,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_enterprise_n = Radiobutton(self.root,text=self.versions[7],variable=self.selection,value=7,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_home_single_language = Radiobutton(self.root,text=self.versions[8],variable=self.selection,value=8,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)
		self.radio_home_country_specific = Radiobutton(self.root,text=self.versions[9],variable=self.selection,value=9,bg=self.bg,fg=self.fg,highlightbackground=self.bg,activebackground=self.bg,activeforeground="#00FF00",selectcolor=self.bg,font=12)

		self.activate_button = Button(self.root,text="Activate",bg=self.bg,fg=self.fg,font=14,command=self.activate)

		self.title.grid(row=0,column=0,columnspan=2,sticky="EW",pady=10)
		self.activate_button.grid(row=6,column=0,columnspan=2,sticky="EW",padx=10,pady=30)

		self.radio_home.grid(row=1,column=0,sticky="W")
		self.radio_home_n.grid(row=1,column=1,sticky="W")
		self.radio_pro.grid(row=2,column=0,sticky="W")
		self.radio_pro_n.grid(row=2,column=1,sticky="W")
		self.radio_education.grid(row=3,column=0,sticky="W")
		self.radio_education_n.grid(row=3,column=1,sticky="W")
		self.radio_enterprise.grid(row=4,column=0,sticky="W")
		self.radio_enterprise_n.grid(row=4,column=1,sticky="W")
		self.radio_home_single_language.grid(row=5,column=0,sticky="W")
		self.radio_home_country_specific.grid(row=5,column=1,sticky="W")



app()