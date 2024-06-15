import tkinter as tk
from mapmy_processManager import *
import mapmy_processManager 
from tkinter import messagebox
import threading


class myGUI (object):
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("1280x720")
        self.state = True
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # self.GUI_Manager()
        self.Create_GUI_Screen()
        
    

    def Create_GUI_Screen(self) :
        print("GUI screen created\n")
        # UseGlobals()
        # global Label2_vehicleID
        # root.geometry("1280x720")

        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure(1, weight=4)
        self.root.columnconfigure(2, weight=4)
        self.root.columnconfigure(3, weight=4)

        self.root.rowconfigure(0, weight=4)
        self.root.rowconfigure(1, weight=2)
        self.root.rowconfigure(2, weight=3)
        self.root.rowconfigure(3, weight=1)

        # set default screen color
        screenTheme = 'darkgrey'
        fontBG = 'white'
        fontSIZE = 12


        #--------------------------------------------------------------------------------------------
        # vehicles  rectangle_1
        rectangle_1 = tk.Frame(self.root, bg="green")
        rectangle_1.grid(row=0, column=0,rowspan=2,padx=(3, 30), pady=3, sticky="NSEW")


        rectangle_1.columnconfigure(0, weight=50)
        rectangle_1.columnconfigure(1, weight=1)
        rectangle_1.rowconfigure(0, weight=1)
        rectangle_1.rowconfigure(1, weight=4)

        rect_1 = tk.Frame(rectangle_1, bg="green")
        rect_1.grid(row=0, column=0,padx=0, pady=0,columnspan=2, sticky="NSEW")
        rect_1_Heading = tk.Label(rect_1, 
                            text = "Vehicles",font=('Helvetica', 15, 'bold','underline'),bg="green").place(relx=0.5, rely=0.5, anchor='center')

        # sb = Scrollbar(rectangle_1,orient="vertical")
        # text = Text(rectangle_1, width=1, height=1, yscrollcommand=sb.set,padx=3, pady=3, bg='silver', relief=FLAT)
        # text.grid(row=1, column=0,padx=(3,0), pady=1, sticky="NSEW")
        # sb.grid(row=1, column=1,padx=(0,1), pady=1, sticky="NSEW")
        # sb.config(command=text.yview)

        # sb.pack(side="right",fill="both")
        # text.pack(side="top",fill="both",expand=False)


        rect_2 = tk.Frame(rectangle_1, bg="green")
        rect_2.grid(row=1, column=0,padx=0, pady=2, sticky="NSEW")

        rect_2.columnconfigure(0, weight=1)
        rect_2.rowconfigure(0, weight=1)

        sb = tk.Scrollbar(rectangle_1,orient="vertical")
        text = tk.Text(rect_2, width=1, height=1, yscrollcommand=sb.set,padx=0, pady=0, bg='silver', relief=tk.FLAT)
        text.grid(row=0, column=0,padx=(3,0), pady=0, sticky="NSEW")
        # text.tag_configure("center", justify='center')
        # text.tag_add("center", 1.0, "end")
        sb.grid(row=1, column=1,padx=(0,2), pady=2, sticky="NSEW")
        sb.config(command=text.yview)
        # sb.pack(side=RIGHT,fill =Y)


        for i in range(3):
            cb = tk.Button(rect_2,text="checkbutton %s" % i,padx=5,pady=5,bd=5, justify='center', relief='groove', anchor='c')
            text.window_create("end", window=cb)
            text.insert("end", "\n")




        #--------------------------------------------------------------------------------------------
        # vehicleDetail  rectangle_2
        rectangle_2 = tk.Frame(self.root, bg="blue")
        rectangle_2.grid(column=1, row=0, rowspan=3,padx=3, pady=3, sticky="NSEW")
        
        rectangle_2.columnconfigure(0, weight=1)
        rectangle_2.columnconfigure(1, weight=1)
        rectangle_2.rowconfigure(0, weight=1)
        rectangle_2.rowconfigure(1, weight=1)
        rectangle_2.rowconfigure(2, weight=1)
        rectangle_2.rowconfigure(3, weight=1)
        rectangle_2.rowconfigure(4, weight=1)
        rectangle_2.rowconfigure(5, weight=1)
        rectangle_2.rowconfigure(6, weight=1)
        rectangle_2.rowconfigure(7, weight=1)
        rectangle_2.rowconfigure(8, weight=1)
        rectangle_2.rowconfigure(9, weight=1)
        
        # rect_200 = tk.Frame(rectangle_2, bg="white")
        # rect_200.grid(row=1, column=0,padx=2, pady=2, rowspan=6, columnspan=2, sticky="NSEW")

        # rect_201 = tk.Frame(rectangle_2, bg="white")
        # rect_201.grid(row=0, column=1,padx=2, pady=2, sticky="NSEW")

        rect_210 = tk.Frame(rectangle_2, bg="white")
        rect_210.grid(row=1, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_211 = tk.Frame(rectangle_2, bg="white")
        rect_211.grid(row=1, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_220 = tk.Frame(rectangle_2, bg="white")
        rect_220.grid(row=2, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_221 = tk.Frame(rectangle_2, bg="white")
        rect_221.grid(row=2, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_230 = tk.Frame(rectangle_2, bg="white")
        rect_230.grid(row=3, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_231 = tk.Frame(rectangle_2, bg="white")
        rect_231.grid(row=3, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_240 = tk.Frame(rectangle_2, bg="white")
        rect_240.grid(row=4, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_241 = tk.Frame(rectangle_2, bg="white")
        rect_241.grid(row=4, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_250 = tk.Frame(rectangle_2, bg="white")
        rect_250.grid(row=5, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_251 = tk.Frame(rectangle_2, bg="white")
        rect_251.grid(row=5, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_260 = tk.Frame(rectangle_2, bg="white")
        rect_260.grid(row=6, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_261 = tk.Frame(rectangle_2, bg="white")
        rect_261.grid(row=6, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_270 = tk.Frame(rectangle_2, bg="white")
        rect_270.grid(row=7, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_271 = tk.Frame(rectangle_2, bg="white")
        rect_271.grid(row=7, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_280 = tk.Frame(rectangle_2, bg="white")
        rect_280.grid(row=8, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_281 = tk.Frame(rectangle_2, bg="white")
        rect_281.grid(row=8, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_290 = tk.Frame(rectangle_2, bg="white")
        rect_290.grid(row=9, column=0,padx=3, pady=(0,3), columnspan=2, sticky="NSEW")
        
        # vehicleDetail = tk.Label(rectangle_2,text = "vehicleDetail",font=('Helvetica', 12, 'bold'),bg="red").place(x = 110,y = 60)
        _rectangle_2_Heading = tk.Label(rectangle_2, 
                            text = "Vehicle Detail",font=('Helvetica', 15, 'bold','underline'),bg="blue").place(x=80, y=25)
        self.Label2_vehicleID = tk.StringVar(value="text")
        _vehicleID = tk.Label(rect_210, text = "Vehicle ID:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 100)
        Label2_vehicleID = tk.Label(rect_211,textvariable=self.Label2_vehicleID,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 100) 
        # self.labelText.set("EVID0001")
        # print(type(Label2_vehicleID))
        self.Label2_origin = tk.StringVar(value="text")
        _origin = tk.Label(rect_220,text="Origin:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 140) 
        Label2_origin = tk.Label(rect_221,textvariable=self.Label2_origin,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 140)     

        self.Label2_destination = tk.StringVar(value="text")
        _destination = tk.Label(rect_230,text="Destination:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 180) 
        Label2_destination = tk.Label(rect_231,textvariable=self.Label2_destination,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 180) 

        self.Label2_priority = tk.StringVar(value="text")
        _priority = tk.Label(rect_240,text="Priority:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 220) 
        Label2_priority = tk.Label(rect_241,textvariable=self.Label2_priority,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 220) 

        self.Label2_vehicleNumber = tk.StringVar(value="text")
        _vehicleNumber = tk.Label(rect_250,text="Vehicle Num.:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 260)
        Label2_vehicleNumber = tk.Label(rect_251,textvariable=self.Label2_vehicleNumber,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 260)  

        self.Label2_extraInfo1 = tk.StringVar(value="text")
        _DriverName = tk.Label(rect_260,text="Driver Name:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 300)
        Label2_extraInfo1 = tk.Label(rect_261,textvariable=self.Label2_extraInfo1,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 300)  

        self.Label2_extraInfo2 = tk.StringVar(value="text")
        _ContactNum = tk.Label(rect_270,text="Contact Num.:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 340)
        Label2_extraInfo2 = tk.Label(rect_271,textvariable=self.Label2_extraInfo2,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 340)  

        self.Label2_extraInfo3 = tk.StringVar(value="text")
        _extraInfo = tk.Label(rect_280,text="Extra Info:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 380)
        Label2_extraInfo3 = tk.Label(rect_281,textvariable=self.Label2_extraInfo3,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 380)  






        #--------------------------------------------------------------------------------------------
        # vehicleDetail  rectangle_2
        rectangle_3 = tk.Frame(self.root, bg="red")
        rectangle_3.grid(column=2, row=0, padx=3, pady=3, sticky="NSEW")


        rectangle_3.columnconfigure(0, weight=1)
        rectangle_3.columnconfigure(1, weight=1)
        rectangle_3.rowconfigure(0, weight=1)
        rectangle_3.rowconfigure(1, weight=1)
        rectangle_3.rowconfigure(2, weight=1)
        rectangle_3.rowconfigure(3, weight=1)
        rectangle_3.rowconfigure(4, weight=1)


        rect_310 = tk.Frame(rectangle_3, bg="white")
        rect_310.grid(row=1, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_311 = tk.Frame(rectangle_3, bg="white")
        rect_311.grid(row=1, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_320 = tk.Frame(rectangle_3, bg="white")
        rect_320.grid(row=2, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_321 = tk.Frame(rectangle_3, bg="white")
        rect_321.grid(row=2, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_330 = tk.Frame(rectangle_3, bg="white")
        rect_330.grid(row=3, column=0,padx=3, pady=(0,3),columnspan=2, rowspan=2, sticky="NSEW")

        # rect_311 = tk.Frame(rectangle_2, bg="white")
        # rect_311.grid(row=1, column=1,padx=(0,3), pady=0, sticky="NSEW")



        _LabelCurrentStatus = tk.Label(rectangle_3, 
                        text = "Current Status",font=('Helvetica', 15, 'bold','underline'),bg="red").place(x = 80, y = 25)

        self.Label3_present_Coords = tk.StringVar(value="text")
        _present_Coords = tk.Label(rect_310, text = "Pres Coords:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 100)
        Label3_present_Coords = tk.Label(rect_311,textvariable=self.Label3_present_Coords,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 100)

        self.Label3_presCoord_name = tk.StringVar(value="text")
        # nearby place name  (famous name)
        _present_Coord_name = tk.Label(rect_320,text="Landmark(any):",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 140) 
        Label3_presCoord_name = tk.Label(rect_321,textvariable=self.Label3_presCoord_name,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 140)     

        # _duration_to_upcoming_Signal = tk.Label(rectangle_3,text="Destination:",font=('Helvetica', 12, 'bold'),bg="red").place(x = 8,y = 180) 
        # Label3_duration = tk.Label(rectangle_3,textvariable=self.Label2_vehicleID,font=('Helvetica', 10, 'bold'),bg="blue").place(x = 120,y = 180) 

        # _duration_to_upcoming_Signal = tk.Label(rectangle_3,text="Priority:",font=('Helvetica', 12, 'bold'),bg="red").place(x = 8,y = 220) 
        # Label3_priority = tk.Label(rectangle_3,textvariable=self.Label2_vehicleID,font=('Helvetica', 10,  'bold'),bg="blue").place(x = 120,y = 220) 

        # _extraInfo = tk.Label(rectangle_3,text="extraInfo:",font=('Helvetica', 12, 'bold'),bg="red").place(x = 8,y = 260)
        # Label3_extraInfo = tk.Label(rectangle_3,textvariable=self.Label2_vehicleID,font=('Helvetica', 10, 'bold'),bg="blue").place(x = 120,y = 260)  





        #--------------------------------------------------------------------------------------------
        # vehicleDetail  rectangle_2
        rectangle_6 = tk.Frame(self.root, bg="gold")
        rectangle_6.grid(column=2, row=1, rowspan=2, padx=3, pady=3, sticky="NSEW")

        rectangle_6.columnconfigure(0, weight=1)
        rectangle_6.columnconfigure(1, weight=1)
        rectangle_6.rowconfigure(0, weight=1)
        rectangle_6.rowconfigure(1, weight=1)
        rectangle_6.rowconfigure(2, weight=1)
        rectangle_6.rowconfigure(3, weight=1)
        rectangle_6.rowconfigure(4, weight=1)
        rectangle_6.rowconfigure(5, weight=1)
        

        rect_610 = tk.Frame(rectangle_6, bg="white")
        rect_610.grid(row=1, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_611 = tk.Frame(rectangle_6, bg="white")
        rect_611.grid(row=1, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_620 = tk.Frame(rectangle_6, bg="white")
        rect_620.grid(row=2, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_621 = tk.Frame(rectangle_6, bg="white")
        rect_621.grid(row=2, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_630 = tk.Frame(rectangle_6, bg="white")
        rect_630.grid(row=3, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_631 = tk.Frame(rectangle_6, bg="white")
        rect_631.grid(row=3, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_640 = tk.Frame(rectangle_6, bg="white")
        rect_640.grid(row=4, column=0,padx=(3,0), pady=0, sticky="NSEW")

        rect_641 = tk.Frame(rectangle_6, bg="white")
        rect_641.grid(row=4, column=1,padx=(0,3), pady=0, sticky="NSEW")

        rect_650 = tk.Frame(rectangle_6, bg="white")
        rect_650.grid(row=5, column=0,padx=3, pady=(0,3), rowspan=2, columnspan=2, sticky="NSEW")

        # rect_651 = tk.Frame(rectangle_6, bg="white")
        # rect_651.grid(row=2, column=1,padx=(0,3), pady=0, sticky="NSEW")
        


        _signalstatus = tk.Label(rectangle_6, 
                        text = "Upcoming signal status",font=('Helvetica', 15, 'bold','underline'),bg="gold").place(x=30,y=10)

        self.Label6_signal_ID = tk.StringVar(value="text")
        _upcoming_signal_ID = tk.Label(rect_610, text = "Upcoming \nSignal ID:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 100)
        Label6_signal_ID = tk.Label(rect_611,textvariable=self.Label6_signal_ID,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 100)

        self.Label6_signal_name = tk.StringVar(value="text")
        _upcoming_signal_name = tk.Label(rect_620, text = "Upcoming \nSignal Name:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 140+10)
        Label6_signal_name = tk.Label(rect_621,textvariable=self.Label6_signal_name,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 140+10)

        self.Label6_distance = tk.StringVar(value="text")
        _distance_to_upcoming_Signal = tk.Label(rect_630,text="Distance:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 180+20) 
        Label6_distance = tk.Label(rect_631,textvariable=self.Label6_distance,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 180+20)     

        self.Label6_duration = tk.StringVar(value="text")
        _duration_to_upcoming_Signal = tk.Label(rect_640,text="Duration:",font=('Helvetica', 12, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 8,y = 220+20) 
        Label6_duration = tk.Label(rect_641,textvariable=self.Label6_duration,font=('Helvetica', fontSIZE, 'bold'),bg=fontBG).place(relx=0.5, rely=0.5, anchor='center')  #(x = 120,y = 220+20) 






        #--------------------------------------------------------------------------------------------
        # vehicleDetail  rectangle_2
        rectangle_8 = tk.Frame(self.root, bg="silver")
        rectangle_8.grid(column=1, row=3,columnspan=2, padx=3, pady=(20,3), sticky="NSEW")





        #--------------------------------------------------------------------------------------------
        # vehicleDetail  rectangle_2
        '''    '''
        rectangle_4 = tk.Frame(self.root, bg="SlateBlue1")
        rectangle_4.grid(column=3, row=0, rowspan=2, padx=(30,3), pady=3, sticky="NSEW")

        rectangle_4.columnconfigure(0, weight=50)
        rectangle_4.columnconfigure(1, weight=1)
        rectangle_4.rowconfigure(0, weight=1)
        rectangle_4.rowconfigure(1, weight=6)

        rect_4 = tk.Frame(rectangle_4, bg="SlateBlue1")
        rect_4.grid(row=0, column=0,padx=0, pady=0,columnspan=2, sticky="NSEW")
        LabelSignal = tk.Label(rect_4, 
                            text = "Signals",font=('Helvetica', 15, 'bold','underline'),bg="SlateBlue1").place(relx=0.5, rely=0.5, anchor='center')


        self.listbox = tk.Listbox(rectangle_4,width=1,height=1, font=('Helvetica', 11, 'bold'),justify=tk.CENTER, relief=tk.FLAT)
        self.listbox.grid(column=0, row=1, padx=(3,0), pady=3, sticky="NSEW")

        scrollRect = tk.Frame(rectangle_4)
        scrollRect.grid(column=1, row=1, padx=(0,3), pady=3, sticky="NSEW")

        self.scrollbar = tk.Scrollbar(scrollRect) #, padx=3, pady=3, sticky="NSEW")
        # scrollbar.grid(column=4, row=0)
        self.scrollbar.pack(side=tk.RIGHT,fill =tk.Y)
        for values in range(5):
            self.listbox.insert(tk.END, values)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        '''  '''




        #--------------------------------------------------------------------------------------------
        # vehicleDetail  rectangle_2
        rectangle_5 = tk.Frame(self.root, bg="firebrick1")
        rectangle_5.grid(column=0, row=2, rowspan=2, padx=(3, 30), pady=3, sticky="NSEW")

        rectangle_5.columnconfigure(0, weight=1)

        rectangle_5.rowconfigure(0, weight=1)
        rectangle_5.rowconfigure(1, weight=1)
        rectangle_5.rowconfigure(2, weight=1)
        rectangle_5.rowconfigure(3, weight=1)
        rectangle_5.rowconfigure(4, weight=1)
        rectangle_5.rowconfigure(5, weight=1)
        
        rect_51 = tk.Frame(rectangle_5, bg="firebrick1")
        rect_51.grid(column=0, row=0, padx=20, pady=(12,0), sticky='NSEW')


        self.rect_52 = tk.Frame(rectangle_5, bg="lightgrey")
        self.rect_52.grid(column=0, row=1, padx=40, pady=(12,0), sticky='NSEW')

        self.rect_53 = tk.Frame(rectangle_5, bg="lightgrey")
        self.rect_53.grid(column=0, row=2, padx=40, pady=(12,0), sticky='NSEW')

        self.rect_54 = tk.Frame(rectangle_5, bg="lightgrey")
        self.rect_54.grid(column=0, row=3, padx=40, pady=(12,0), sticky='NSEW')

        self.rect_55 = tk.Frame(rectangle_5, bg="lightgrey")
        self.rect_55.grid(column=0, row=4, padx=40, pady=(12,0), sticky='NSEW')

        self.rect_56 = tk.Frame(rectangle_5, bg="lightgrey")
        self.rect_56.grid(column=0, row=5, padx=40, pady=12, sticky='NSEW')



        signlstatus = tk.Label(rect_51, 
                            text = "System Status",font=('Helvetica', 15, 'bold','underline'),bg="firebrick1").place(relx=0.5, rely=0.5, anchor='center')

        self.InternetStatus = tk.Label(self.rect_52, 
                            text = "Internet",font=('Helvetica', 12, 'bold')).place(relx=0.5, rely=0.5, anchor='center')
        self.MMI_Status = tk.Label(self.rect_53, 
                            text = "MMI Input",font=('Helvetica', 12, 'bold')).place(relx=0.5, rely=0.5, anchor='center')
        self.InternetStatus = tk.Label(self.rect_54, 
                            text = "Firebase",font=('Helvetica', 12, 'bold')).place(relx=0.5, rely=0.5, anchor='center')
        # self.MMI_Status = tk.Label(self.rect_55, 
        #                     text = "MMI Input",font=('Helvetica', 12, 'bold'),bg="green3").place(relx=0.5, rely=0.5, anchor='center')





        #--------------------------------------------------------------------------------------------
        # vehicleDetail  rectangle_2
        '''    '''
        rectangle_7 = tk.Frame(self.root, bg="green3")
        rectangle_7.grid(column=3, row=2, rowspan=2, padx=(30,3), pady=3, sticky="NSEW")

        rectangle_7.columnconfigure(0, weight=50)
        rectangle_7.columnconfigure(1, weight=1)
        rectangle_7.rowconfigure(0, weight=1)
        rectangle_7.rowconfigure(1, weight=6)

        rect_7 = tk.Frame(rectangle_7, bg="green3")
        rect_7.grid(row=0, column=0,padx=0, pady=0,columnspan=2, sticky="NSEW")
        _terminal = tk.Label(rect_7, 
                            text = "Terminal",font=('Helvetica', 15, 'bold','underline'),bg="green3").place(relx=0.5, rely=0.5, anchor='center')


        self.Terminal_listbox = tk.Listbox(rectangle_7,width=1,height=1,justify=tk.CENTER, relief=tk.FLAT)
        self.Terminal_listbox.grid(column=0, row=1, padx=(3,0), pady=3, sticky="NSEW")

        scrollRect = tk.Frame(rectangle_7)
        scrollRect.grid(column=1, row=1, padx=(0,3), pady=3, sticky="NSEW")

        scrollbar = tk.Scrollbar(scrollRect) #, padx=3, pady=3, sticky="NSEW")
        # scrollbar.grid(column=4, row=0)
        scrollbar.pack(side=tk.RIGHT,fill =tk.Y)
        # for values in range(5):
        #     self.Terminal_listbox.insert(tk.END, values)
        self.Terminal_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Terminal_listbox.yview)

        '''  '''



    
    
    def Update_GUI_Variables(self) :
        # global conditon1
        # # global EVIDs
        # online_vehicle_manager()   
         
        
        if mapmy_processManager.FBS_Status :     self.rect_54.config(bg='blue')  
        else  :             self.rect_54.config(bg='red') 

        try :
            if mapmy_processManager.defaultVariable.Internet_Flag :     self.rect_52.config(bg='blue')  
            else  :             self.rect_52.config(bg='red3')  
            
            if mapmy_processManager.defaultVariable.MMIKeyFlag :     self.rect_53.config(bg='blue')  
            else  :             self.rect_53.config(bg='red3') 
            
            if mapmy_processManager.update_Status :     self.rect_54.config(bg='blue')  
            else  :             self.rect_54.config(bg='red3')  

        except Exception as e:
            # print(f"flag show exception : {e}")      # flag show exception : 'NoneType' object has no attribute 'Internet_Flag'
            pass
        
        # if mapmy_processManager.defaultVariable.class_Status :     self.rect_56.config(bg='blue')  
        # else  :             self.rect_56.config(bg='red')  
        

        # print(mapmy_processManager.defaultVariable.origin)
        # print(mapmy_processManager.EVIDs)
        # mapmy_processManager.defaultVariable.get_signals_in_route()
        # print(mapmy_processManager.defaultVariable.sigSeqList)
        try:
                
            self.Label2_vehicleID.set(mapmy_processManager.defaultVariable.ID)
            self.Label2_origin.set(mapmy_processManager.defaultVariable.origin)
            self.Label2_destination.set(mapmy_processManager.defaultVariable.destin)
            self.Label2_priority.set(mapmy_processManager.defaultVariable.priority)
            #
            self.Label2_vehicleNumber.set("EV 01 ID 0003")
            self.Label2_extraInfo1.set("ManSukh Driver")
            self.Label2_extraInfo2.set("9851645453")
            self.Label2_extraInfo3.set("emergency case")

     

            self.Label3_present_Coords.set(mapmy_processManager.defaultVariable.presnt)
            self.Label3_presCoord_name.set("")



            # self.Label6_signal_name.set("SIG00001")
            self.Label6_signal_ID.set(mapmy_processManager.SignalHardware[mapmy_processManager.Signal_count])
            self.Label6_signal_name.set(mapmy_processManager.defaultVariable.next_signal_name)
            self.Label6_distance.set(str(mapmy_processManager.defaultVariable.signal_distance) + " m")
            self.Label6_duration.set(str(mapmy_processManager.defaultVariable.exp_arrival_time) + " mins")
        




            # def Update_Signals_List(self):
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", end='')
            # print(mapmy_processManager.SignalsUpdated)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", end='')
            # print(len(mapmy_processManager.defaultVariable.sigSeqList))
            if mapmy_processManager.SignalsUpdated and len(mapmy_processManager.defaultVariable.sigSeqList)>0 :
                if mapmy_processManager.condition1 :
                    print("waiting for signaals~~~~~~~~~~")
                    self.listbox.delete(0,'end')
                    for _signal in mapmy_processManager.defaultVariable.sigSeqList:
                        # self.listbox.config(font=('Helvetica', 11, 'bold'))
                        self.listbox.insert('end', _signal)   # position = tk.END
                        # self.listbox.config(font=('Helvetica', 9, 'bold'))
                        self.listbox.insert('end', '')   # position = tk.END

                    print("Signals Updated in Screen")
                    print(mapmy_processManager.defaultVariable.sigSeqList)
                    mapmy_processManager.SignalsUpdated = True
                    mapmy_processManager.condition1 = False
                


            
            




            # def GUI_Terminal(self):
            # if (condition2)
            # for values in range(5):
            #     self.Terminal_listbox.delete(values)
            if mapmy_processManager.terminal_item_available :
                self.Terminal_listbox.insert('end', mapmy_processManager.terminal_item)   # position = tk.END
                mapmy_processManager.terminal_item_available = False

        except :
            pass

        self.root.after(20,self.Update_GUI_Variables)
  

 



    def run(self):
        # self.grid()
        self.root.after(20,self.Update_GUI_Variables)
        self.root.mainloop()

    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"Total MMI Requests (MMI_request_counter) : {mapmy_processManager.defaultVariable.MMI_request_counter} \n\n")
            self.root.destroy()




# online_vehicle_manager() 
# mapmy_processManager.defaultVariable.get_signals_in_route()

# print(mapmy_processManager.defaultVariable.sigSeqList)



if __name__=='__main__':
    t1 = threading.Thread(target=Vehicle_Manager)    
    t1.start()

    # Vehicle_Manager()

    
    t2 = threading.Thread(target=start_journey_and_switch_signals_2, args=(mapmy_processManager.defaultVariable, ))
    t2.start()

    # start_journey_and_switch_signals_2(mapmy_processManager.defaultVariable)

    t3 = threading.Thread(target=myGUI().run())
    t3.start()
    
    


    # t1.join()
    # t2.join()
    # t3.join()
    


    







'''
ask_new_url()  self.mapmyResponse : 
{'routes': [{'duration': 192, 'distance': 1998.8, 'legs': [{'summary': 'Naroda Link Road, Naroda Link Road', 'duration': 192, 'distance': 1998.8, 'weight': 192, 'steps': [{'duration': 1.7, 'mode': 'driving', 'distance': 22.7, 'destinations': 'Bharat Ratna Vinobabhave Railway Over Bridge', 'name': 'Bharat Ratna Vinobabhave Railway Over Bridge', 'weight': 1.7, 'geometry': '{rgkCiqfzLQi@', 'driving_side': 'left', 'intersections': [{'entry': [True], 'bearings': [65], 'location': [72.619894, 22.981742], 'out': 0}], 'maneuver': {'modifier': 'left', 'bearing_after': 65, 'location': [72.619894, 22.981742], 'bearing_before': 0, 'type': 'depart'}}, {'duration': 190.3, 'mode': 'driving', 'distance': 1976.1, 'destinations': 'Naroda Link Road', 'name': 'Naroda Link Road', 'weight': 190.3, 'geometry': 'msgkCsrfzL_AmCs@{Bu@{Bu@{BO[IKKOmAaBg@o@gAsA}AoBMMg@k@MQiAiAa@_@i@k@}@aAiBmBeAiAcAiAgAgAeAgAoAoAQUwA{AoAqAKOu@u@cAgAcBeBgAiAkAcAwAmAgAw@oBoAs@g@ECKGMIe@Qy@_@uAc@uAc@', 'driving_side': 'left', 'intersections': [{'entry': [True, False], 'bearings': [60, 240], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.620095, 22.981828], 'out': 0}, {'entry': [True, False, False, True], 'bearings': [45, 120, 240, 300], 'in': 2, 'lanes': [{'valid': True, 'indications': ['straight', 'left']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.622805, 22.983028], 'out': 0}, {'entry': [True, True, False, False], 'bearings': [45, 120, 225, 300], 'in': 2, 'lanes': [{'valid': True, 'indications': ['straight', 'left']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.622946, 22.98314], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 
225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.623435, 
22.983531], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': 
True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, 
{'valid': True, 'indications': ['straight']}], 'location': [72.623679, 22.983727], 'out': 0}, {'entry': [True, 
False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.625407, 22.985273], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.625571, 22.985436], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.62579, 22.985654], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.626117, 22.985963], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.626669, 22.986485], 'out': 
0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.627408, 22.987184], 'out': 0}, {'entry': [True, False, False, True], 'bearings': [45, 120, 225, 300], 'in': 2, 'location': [72.628529, 22.988285], 'out': 0}, {'entry': [True, True, False], 'bearings': [45, 120, 225], 'in': 2, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.628636, 22.98838], 'out': 0}, {'entry': [True, False, True], 'bearings': 
[45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.629098, 22.988819], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.629514, 22.989216], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.629858, 22.989546], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': 
True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.630215, 22.989889], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'location': [72.631096, 
22.990749], 'out': 0}, {'entry': [True, False, False, True, True], 'bearings': [30, 135, 210, 225, 315], 'in': 
2, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.632705, 22.99275], 'out': 0}, {'entry': [True, True, False, False], 'bearings': [30, 135, 210, 315], 'in': 2, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.632821, 22.992908], 'out': 0}, {'entry': [True, True, True, False], 'bearings': [0, 30, 120, 210], 'in': 3, 'lanes': [{'valid': True, 'indications': ['straight', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight', 'slight right', 'uturn']}], 'location': [72.632914, 22.993095], 'out': 1}], 'maneuver': {'modifier': 'straight', 'bearing_after': 63, 'location': [72.620095, 22.981828], 'bearing_before': 64, 'type': 'new name'}}, {'duration': 0, 'mode': 'driving', 'ref': 'NH 48', 'distance': 0, 'destinations': 'Naroda Link Road', 'name': 'Naroda Link Road', 'weight': 0, 'geometry': 'aajkC}eizL', 'driving_side': 'left', 'intersections': [{'entry': [True], 'bearings': [201], 'in': 0, 'location': [72.633426, 22.994247]}], 'maneuver': {'modifier': 'right', 'bearing_after': 0, 'location': [72.633426, 22.994247], 'bearing_before': 21, 'type': 'arrive'}}]}], 'weight_name': 'routability', 'weight': 192, 'geometry': '{rgkCiqfzLaGgQgJkLkf@qg@cJsGkGyB'}], 'code': 'Ok', 'Server': 'Adv-5400', 'waypoints': [{'distance': 0.976255, 'hint': 'Rzk7gv___38cAAAALQAAAOwAAAAAAAAAyTAeQtqjtUGZH6NDAAAAABwAAAAtAAAA7AAAAAAAAACOAAAAdhdUBG6sXgFyF1QEdqxeAQQAHwT6XhXQ', 'name': 'Bharat Ratna Vinobabhave Railway Over Bridge', 'location': [72.619894, 22.981742]}, {'distance': 9.538476, 'hint': 'rqcJgP___38AAAAAVwAAAKEAAABXAAAAAAAAAN9ilUIYCwpD0yyVQgAAAABXAAAAoQAAAFcAAACOAAAAUkxUBEfdXgGmTFQEIt1eAQMAHwH6XhXQ', 'name': 'Naroda Link Road', 'location': [72.633426, 22.994247]}], 'version': '202104.19.5222'}

get_signals_in_route()   Recieved json from URL :
{'routes': [{'duration': 192, 'distance': 1998.8, 'legs': [{'summary': 'Naroda Link Road, Naroda Link Road', 'duration': 192, 'distance': 1998.8, 'weight': 192, 'steps': [{'duration': 1.7, 'mode': 'driving', 'distance': 22.7, 'destinations': 'Bharat Ratna Vinobabhave Railway Over Bridge', 'name': 'Bharat Ratna Vinobabhave Railway Over Bridge', 'weight': 1.7, 'geometry': '{rgkCiqfzLQi@', 'driving_side': 'left', 'intersections': [{'entry': [True], 'bearings': [65], 'location': [72.619894, 22.981742], 'out': 0}], 'maneuver': {'modifier': 'left', 'bearing_after': 65, 'location': [72.619894, 22.981742], 'bearing_before': 0, 'type': 'depart'}}, {'duration': 190.3, 'mode': 'driving', 'distance': 1976.1, 'destinations': 'Naroda Link Road', 'name': 'Naroda Link Road', 'weight': 190.3, 'geometry': 'msgkCsrfzL_AmCs@{Bu@{Bu@{BO[IKKOmAaBg@o@gAsA}AoBMMg@k@MQiAiAa@_@i@k@}@aAiBmBeAiAcAiAgAgAeAgAoAoAQUwA{AoAqAKOu@u@cAgAcBeBgAiAkAcAwAmAgAw@oBoAs@g@ECKGMIe@Qy@_@uAc@uAc@', 'driving_side': 'left', 'intersections': [{'entry': [True, False], 'bearings': [60, 240], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.620095, 22.981828], 'out': 0}, {'entry': [True, False, False, True], 'bearings': [45, 120, 240, 300], 'in': 2, 'lanes': [{'valid': True, 'indications': ['straight', 'left']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.622805, 22.983028], 'out': 0}, {'entry': [True, True, False, False], 'bearings': [45, 120, 225, 300], 'in': 2, 'lanes': [{'valid': True, 'indications': ['straight', 'left']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.622946, 22.98314], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 
225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.623435, 
22.983531], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': 
True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, 
{'valid': True, 'indications': ['straight']}], 'location': [72.623679, 22.983727], 'out': 0}, {'entry': [True, 
False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.625407, 22.985273], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.625571, 22.985436], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.62579, 22.985654], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.626117, 22.985963], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.626669, 22.986485], 'out': 
0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.627408, 22.987184], 'out': 0}, {'entry': [True, False, False, True], 'bearings': [45, 120, 225, 300], 'in': 2, 'location': [72.628529, 22.988285], 'out': 0}, {'entry': [True, True, False], 'bearings': [45, 120, 225], 'in': 2, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.628636, 22.98838], 'out': 0}, {'entry': [True, False, True], 'bearings': 
[45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.629098, 22.988819], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.629514, 22.989216], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.629858, 22.989546], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'slight left']}, {'valid': 
True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight']}], 'location': [72.630215, 22.989889], 'out': 0}, {'entry': [True, False, True], 'bearings': [45, 225, 315], 'in': 1, 'location': [72.631096, 
22.990749], 'out': 0}, {'entry': [True, False, False, True, True], 'bearings': [30, 135, 210, 225, 315], 'in': 
2, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.632705, 22.99275], 'out': 0}, {'entry': [True, True, False, False], 'bearings': [30, 135, 210, 315], 'in': 2, 'lanes': [{'valid': True, 'indications': ['straight', 'sharp left', 'left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight', 'right', 'uturn']}], 'location': [72.632821, 22.992908], 'out': 0}, {'entry': [True, True, True, False], 'bearings': [0, 30, 120, 210], 'in': 3, 'lanes': [{'valid': True, 'indications': ['straight', 'slight left']}, {'valid': True, 'indications': ['straight']}, {'valid': True, 'indications': ['straight', 'slight right', 'uturn']}], 'location': [72.632914, 22.993095], 'out': 1}], 'maneuver': {'modifier': 'straight', 'bearing_after': 63, 'location': [72.620095, 22.981828], 'bearing_before': 64, 'type': 'new name'}}, {'duration': 0, 'mode': 'driving', 'ref': 'NH 48', 'distance': 0, 'destinations': 'Naroda Link Road', 'name': 'Naroda Link Road', 'weight': 0, 'geometry': 'aajkC}eizL', 'driving_side': 'left', 'intersections': [{'entry': [True], 'bearings': [201], 'in': 0, 'location': [72.633426, 22.994247]}], 'maneuver': {'modifier': 'right', 'bearing_after': 0, 'location': [72.633426, 22.994247], 'bearing_before': 21, 'type': 'arrive'}}]}], 'weight_name': 'routability', 'weight': 192, 'geometry': '{rgkCiqfzLaGgQgJkLkf@qg@cJsGkGyB'}], 'code': 'Ok', 'Server': 'Adv-5400', 'waypoints': [{'distance': 0.976255, 'hint': 'Rzk7gv___38cAAAALQAAAOwAAAAAAAAAyTAeQtqjtUGZH6NDAAAAABwAAAAtAAAA7AAAAAAAAACOAAAAdhdUBG6sXgFyF1QEdqxeAQQAHwT6XhXQ', 'name': 'Bharat Ratna Vinobabhave Railway Over Bridge', 'location': [72.619894, 22.981742]}, {'distance': 9.538476, 'hint': 'rqcJgP___38AAAAAVwAAAKEAAABXAAAAAAAAAN9ilUIYCwpD0yyVQgAAAABXAAAAoQAAAFcAAACOAAAAUkxUBEfdXgGmTFQEIt1eAQMAHwH6XhXQ', 'name': 'Naroda Link Road', 'location': [72.633426, 22.994247]}], 'version': '202104.19.5222'}

number of signals = 3

try 0000000000000000000000000000000000000000000  ok
hekkkkkkoookkkjhh
Got these values for firebase :
ID = EVID003
Origin = ['22.98175', '72.61989']
Destin = ['22.99421', '72.63351']
Presnt = ['22.99683', '72.62227']
Prirty = 5
Object attributes update

'''