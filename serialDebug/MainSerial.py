'''
@ author: summer
@ editor: Ali
@ tools: VSCode 
@ content: Realize the main class of serial communication
@ date: 2023.2.19
'''
import tkinter
from tkinter import ttk
from SerialClass import SerialAchieve   # Import serial communication class

class MainSerial:
    def __init__(self):
        # Define serial variables
        self.port = None
        self.band = None
        self.check = None
        self.data = None
        self.stop = None
        self.myserial = None

        # Initialize the form
        self.mainwin = tkinter.Tk()
        self.mainwin.title("Serial debugging tool")
        self.mainwin.iconbitmap(r'C:\Users\Ali\Documents\elec\python serial\icon.ico')
        self.mainwin.geometry("600x400")

        # Label
        self.label1 = tkinter.Label(self.mainwin,text = "Serial port:",font = ("Arial",13))
        self.label1.place(x = 5,y = 5)
        self.label2 = tkinter.Label(self.mainwin, text="Baud rate:", font=("Arial", 13))
        self.label2.place(x=5, y=45)
        self.label3 = tkinter.Label(self.mainwin, text="Parity digit:", font=("Arial", 13))
        self.label3.place(x=5, y=85)
        self.label4 = tkinter.Label(self.mainwin, text="Data bits:", font=("Arial", 13))
        self.label4.place(x=5, y=125)
        self.label5 = tkinter.Label(self.mainwin,text = "Stop bits:",font = ("Arial",13))
        self.label5.place(x = 5,y = 165)

        # Text display, clear sending data
        self.label6 = tkinter.Label(self.mainwin, text="send data:", font=("Arial", 13))
        self.label6.place(x=230, y=5)

        self.label7 = tkinter.Label(self.mainwin, text="Receive data:", font=("Arial", 13))
        self.label7.place(x=230, y=200)

        # Serial number
        self.com1value = tkinter.StringVar()  # Text that comes with the form, create a value
        self.combobox_port = ttk.Combobox(self.mainwin, textvariable=self.com1value,
                                          width = 13,font = ("Arial",10))
        # enter selection
        self.combobox_port["value"] = [""]  # Select here first

        self.combobox_port.place(x = 105,y = 5)  # display

        # baud rate
        self.bandvalue = tkinter.StringVar()  # Text that comes with the form, create a value
        self.combobox_band = ttk.Combobox(self.mainwin, textvariable=self.bandvalue, width=13, font=("Arial", 10))
        # enter selection
        self.combobox_band["value"] = ["4800","9600","14400","19200","38400","57600","115200"]  # Select here first
        self.combobox_band.current(6)  # The 0th is selected by default
        self.combobox_band.place(x=105, y=45)  # Display

        # Check Digit
        self.checkvalue = tkinter.StringVar()  # Text that comes with the form, create a value
        self.combobox_check = ttk.Combobox(self.mainwin, textvariable=self.checkvalue, width=13, font=("Arial", 10))
        # enter selection
        self.combobox_check["value"] = ["no check digit"]  # Select here first
        self.combobox_check.current(0)  # The 0th is selected by default
        self.combobox_check.place(x=105, y=85)  # Display

        # data bit
        self.datavalue = tkinter.StringVar()  # Text that comes with the form, create a value
        self.combobox_data = ttk.Combobox(self.mainwin, textvariable=self.datavalue, width=13, font=("Arial", 10) )
        # enter selection
        self.combobox_data["value"] = ["8", "9", "0"]  # Select here first
        self.combobox_data.current(0)  # The 0th is selected by default
        self.combobox_data.place(x=105, y=125)  # Display

        # stop bit
        self.stopvalue = tkinter.StringVar()  # Text that comes with the form, create a value
        self.combobox_stop = ttk.Combobox(self.mainwin, textvariable=self.stopvalue, width=13, font=("Arial", 10))
        # enter selection
        self.combobox_stop["value"] = ["1", "0"]  # Select here first
        self.combobox_stop.current(0)  # The 0th is selected by default
        self.combobox_stop.place(x=105, y=165)  # Display

        # Press Display to open the serial port
        self.button_OK = tkinter.Button(self.mainwin, text="open port",
                                        command=self.button_OK_click, font = ("Arial",10),
                                        width = 10,height = 1)
        self.button_OK.place(x = 5,y = 210)  # Display Control
        # close the serial port
        self.button_Cancel = tkinter.Button(self.mainwin, text="close port",  # Display text
                                 command=self.button_Cancel_click, font = ("Arial",10),
                                 width=10, height=1)
        self.button_Cancel.place(x = 120,y = 210)  # Display Control

        # clear send data
        self.button_Cancel = tkinter.Button(self.mainwin, text="Clear send data",  # Display text
                                            command=self.button_clcSend_click, font=("Arial", 10),
                                            width=13, height=1)
        self.button_Cancel.place(x=400, y=2)  # DisplayControl

        # Clear received data
        self.button_Cancel = tkinter.Button(self.mainwin, text="Clear received data",  # Display text
                                            command=self.button_clcRece_click, font=("Arial", 10),
                                            width=13, height=1)
        self.button_Cancel.place(x=400, y=197)  # DisplayControl

        # send button
        self.button_Send = tkinter.Button(self.mainwin, text="send",  # Display text
                                            command=self.button_Send_click, font=("Arial", 10),
                                            width=6, height=1)
        self.button_Send.place(x=5, y=255)  # DisplayControl

        # receive button
        self.button_Send = tkinter.Button(self.mainwin, text="receive",  # Display text
                                          command=self.button_Rece_click, font=("Arial", 10),
                                          width=6, height=1)
        self.button_Send.place(x=5, y=310)  # DisplayControl

        # Display frame
        # Implement the functional components of Notepad
        self.SendDataView = tkinter.Text(self.mainwin,width = 40,height = 9,
                                         font = ("Arial",10))  # text is actually a text editor
        self.SendDataView.place(x = 230,y = 35)  # Display

        self.ReceDataView = tkinter.Text(self.mainwin, width=40, height=9,
                                         font=("Arial", 10))  # text is actually a text editor
        self.ReceDataView.place(x=230, y=230)  # Display

        # sent content
        test_str = tkinter.StringVar(value="Hello")
        self.entrySend = tkinter.Entry(self.mainwin, width=13,textvariable = test_str,font = ("Arial",13))
        self.entrySend.place(x = 80,y = 260)  # Display

        # get file path
        test_str = tkinter.StringVar(value="Hello")
        self.entrySend = tkinter.Entry(self.mainwin, width=13, textvariable=test_str, font=("Arial", 13))
        self.entrySend.place(x=80, y=260)  # Display

        # Get the parameters of the interface
        self.band = self.combobox_band.get()
        self.check = self.combobox_check.get()
        self.data = self.combobox_data.get()
        self.stop = self.combobox_stop.get()
        print("Baud rate:"+self.band)
        self.myserial = SerialAchieve(int(self.band),self.check,self.data,self.stop)

        # Handle serial port values
        self.port_list = self.myserial.get_port()
        port_str_list = []  # Used to store the cut serial number
        for i in range(len(self.port_list)):
            # Cut out the serial number
            lines = str(self.port_list[i])
            str_list = lines.split(" ")
            port_str_list.append(str_list[0])
        self.combobox_port["value"] = port_str_list
        self.combobox_port.current(0)  # The 0th is selected by default

    def show(self):
        self.mainwin.mainloop()

    def button_OK_click(self):
        '''
        @ Serial port open function
        :return: 
        '''
        if self.port == None or self.port.isOpen() == False:
            self.myserial.open_port(self.combobox_port.get())
            print("Open the serial port successfully")
        else:
            pass

    def button_Cancel_click(self):
        self.myserial.delete_port()
        print("Close the serial port successfully")

    def button_clcSend_click(self):
        self.SendDataView.delete("1.0","end")

    def button_clcRece_click(self):
        self.ReceDataView.delete("1.0", "end")

    def button_Send_click(self):
        try:
            if self.myserial.port.isOpen() == True:
                print("start sending data")
                send_str1 = self.entrySend.get()
                self.myserial.Write_data(send_str1)
                self.SendDataView.insert(tkinter.INSERT, send_str1+" ")
                print("Send data successfully")
            else:
                print("The serial port is not open")
        except:
            print("Failed to send")
    def button_Rece_click(self):
        try:
            readstr = self.myserial.Read_data()
            self.ReceDataView.insert(tkinter.INSERT, readstr + " ")
        except:
            print("read failed")
if __name__ == '__main__':
    my_ser1 = MainSerial()
    my_ser1.show()


