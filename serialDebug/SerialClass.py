'''
@ author: summer
@ editor: Ali
@ tools: VSCode 
@ content: Serial communication implementation class
@ date: 2023.2.19
'''
import serial
import serial.tools.list_ports

class SerialAchieve:
    def __init__(self,band=9600,check="no check digit",data=8,stop=1):
        self.port = None
        # Get available serial ports
        self.port_list = list(serial.tools.list_ports.comports())
        assert (len(self.port_list) != 0),"no serial port available"

        self.bandRate = band
        self.checkbit = check
        self.databit = data
        self.stopbit = stop

        # read and write data
        self.read_data = None
        self.write_data = None

        pass
    def show_port(self):
        for i in range(0,len(self.port_list)):
            print(self.port_list[i])

    def show_other(self):
        print("Baud rate:"+self.bandRate)
        print("Check Digit:" + self.checkbit)
        print("Data bits:" + self.databit)
        print("stop bit:" + self.stopbit)
    # return serial port
    def get_port(self):
        return self.port_list
    # open serial port
    def open_port(self,port):
        self.port = serial.Serial(port, self.bandRate,timeout = None)

    def delete_port(self):
        if self.port != None:
            self.port.close()
            print("Close the serial port to complete")
        else:
            pass

    def Read_data(self):   # self.port.read(self.port.in_waiting) Indicates that all receive data in the serial port
        self.read_data = self.port.read(self.port.in_waiting)   # read data
        return self.read_data.decode("utf-8")

    def Write_data(self,data):
        if self.port.isOpen() == False:
            print("serial port open error")
        else:
            self.port.write(data.encode("utf-8"))  # Returns the number of bytes written

if __name__ == '__main__':
    myser = SerialAchieve()
    myser.open_port("COM7")
    myser.delete_port()
    myser.show_port()



