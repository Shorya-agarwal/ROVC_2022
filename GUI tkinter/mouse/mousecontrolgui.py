from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import pigpio

# Create an instance of TKinter Window or frame
app = Tk()

# Set the size of the window
app.geometry("990x850")

# Create thvalue[0] Label to capture the Video frames
label =Label(app )
# label.place(relwidth=1, relheight=0.45, rely=0.03)
label.place(x  = 25 , y = 5 , height= 450 , width= 900)
# label.grid(row=0, column=0, columnspan=5, padx = 20 , pady=40)
cap= cv2.VideoCapture(0)

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

#show_frames()

thruster_one = 10    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_two = 7    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_three = 3  #Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_four = 27  #Enter the PIN Number to Which Thrsuter 4 is coonected

thruster_pins = [thruster_one, thruster_two, thruster_three, thruster_four]

pi = pigpio.pi()

for item in thruster_pins:
    pi.set_servo_pulsewidth(item,1500)



thvalue = [1500, 1500,1500,1500]

def forward():
   if thvalue[0] < 1650 and thvalue[1]<1650:
      thvalue[0] = thvalue[0] + 50
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])

   if thvalue[0] > 1500 and thvalue[1] > 1500:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving forward with " + \
      str(abs(1500-thvalue[0])) +  " unit speed \n" + \
            "Thruster 2 is moving forward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   elif thvalue[0] == 1500 and thvalue[1] == 1500:
      result_str = "ROV IS AT REST"

   else:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving backward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving backward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"
   
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)


def backward():
   if thvalue[0] > 1350 and thvalue[1] > 1350:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] - 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])

   if thvalue[0] > 1500 and thvalue[1] > 1500:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving forward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving forward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   elif thvalue[0] == 1500 and thvalue[1] == 1500:
      result_str = "ROV IS AT REST"

   else:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving backward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving backward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)

def down():
   if thvalue[2] <= 1800 and thvalue[2]>1200:
      thvalue[2] = thvalue[2] - 50
      thvalue[3] = thvalue[3] - 50
      pi.set_servo_pulsewidth(thruster_three, thvalue[2])
      pi.set_servo_pulsewidth(thruster_four, thvalue[3])

   if thvalue[2] > 1500:
      result_str = "Rov is going up with " + str(abs(1500-thvalue[2])) + " unit speed"
   elif thvalue[2] == 1500:
      result_str = "Vertical Motion Of Rov has Stopped"
   else:
      result_str = "Rov is going down with " + str(abs(1500-thvalue[2])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)

def upward():
   if thvalue[2]>=1200 and thvalue[2]<1800:
      thvalue[2] = thvalue[2] + 50
      thvalue[3] = thvalue[3] + 50
      pi.set_servo_pulsewidth(thruster_three, thvalue[2])
      pi.set_servo_pulsewidth(thruster_four, thvalue[3])

   if thvalue[2] > 1500:
      result_str = "Rov is going up with " + str(abs(1500-thvalue[2])) + " unit speed"
   elif thvalue[2] == 1500:
      result_str = "Vertical Motion Of Rov has Stopped"
   else:
      result_str = "Rov is going down with " + str(abs(1500-thvalue[2])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)

def left():
   if thvalue[0] > 1500:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning left and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   elif thvalue[0] == 1500:
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Left Thruster is Stopped and Rov is turning left\n and speed of right thruster is " + \
         str(abs(1500-thvalue[1])) + " unit"

   else:
      thvalue[0] = thvalue[0] + 50
      thvalue[1] = thvalue[1] - 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning right and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   # time.sleep(1)
   # thvalue[1] = 1500
   # thvalue[0] = 1500
   # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
   # pi.set_servo_pulsewidth(thruster_two, thvalue[1]) 

def right():
   if thvalue[1] > 1500:
      thvalue[1] = thvalue[1] - 50
      thvalue[0] = thvalue[0] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning right and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   elif thvalue[1] == 1500:
      thvalue[0] = thvalue[0] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      result_str = "right Thruster is Stopped and Rov is turning right\n and speed of left thruster is " + str(abs(1500-thvalue[0])) + " unit"

   else:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning left and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   # time.sleep(1)
   # thvalue[0] = 1500
   # thvalue[1] = 1500
   # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
   # pi.set_servo_pulsewidth(thruster_two, thvalue[1])    

def reset():
   thvalue[0] = 1500
   thvalue[1] = 1500
   thvalue[2] = 1500
   thvalue[3] = 1500
   pi.set_servo_pulsewidth(thruster_one, thvalue[0])
   pi.set_servo_pulsewidth(thruster_two, thvalue[1])
   pi.set_servo_pulsewidth(thruster_three, thvalue[2])
   pi.set_servo_pulsewidth(thruster_four, thvalue[3])
   result_str = "ROV IS AT REST"
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)




result = "Rov is not in Motion \nAll The thrusters aare in Idle State"


button_forward = Button(app, text="↑" , padx=40, pady=20 , command = forward).place(x = 160 , y= 510)
button_backward = Button(app, text="↓" , padx=40, pady=20,command = backward).place(x=160,y=575 )
button_left = Button(app, text="←" , padx=40, pady=20 ,command = left).place(x=50, y=575 )
button_right = Button(app, text="→" , padx=40, pady=20,command = right).place(y =575, x = 270  )
button_up = Button(app, text="UP" , padx=40, pady=20,command = upward).place(x = 380,  y= 510 )
button_down = Button(app, text="Down" , padx=40, pady=20,command = down).place(x = 380 , y= 575 ) 
button_reset = Button(app, text="RESET" , padx=40, pady=20 , command = reset).place(x = 100, y  = 650)

ele = Text(app, width=65, height = 5 ,borderwidth=5)
ele.place(relwidth=0.42 , relheight=0.25 , relx=0.54, rely = 0.63)
ele.insert(INSERT, result)
app.mainloop()
from tkinter import *
#from PIL import Image, ImageTk
#import cv2
import time
import pigpio

# Create an instance of TKinter Window or frame
app = Tk()

# Set the size of the window
app.geometry("990x850")

# Create thvalue[0] Label to capture the Video frames
#label =Label(app )
# label.place(relwidth=1, relheight=0.45, rely=0.03)
#label.place(x  = 25 , y = 5 , height= 450 , width= 900)
# label.grid(row=0, column=0, columnspan=5, padx = 20 , pady=40)
#cap= cv2.VideoCapture(0)

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

#show_frames()

thruster_one = 10    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_two = 7    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_three = 3  #Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_four = 27  #Enter the PIN Number to Which Thrsuter 4 is coonected

thruster_pins = [thruster_one, thruster_two, thruster_three, thruster_four]

pi = pigpio.pi()

for item in thruster_pins:
    pi.set_servo_pulsewidth(item,1500)



thvalue = [1500, 1500,1500,1500]

def forward():
   if thvalue[0] < 1650 and thvalue[1]<1650:
      thvalue[0] = thvalue[0] + 50
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])

   if thvalue[0] > 1500 and thvalue[1] > 1500:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving forward with " + \
      str(abs(1500-thvalue[0])) +  " unit speed \n" + \
            "Thruster 2 is moving forward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   elif thvalue[0] == 1500 and thvalue[1] == 1500:
      result_str = "ROV IS AT REST"

   else:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving backward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving backward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"
   
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)


def backward():
   if thvalue[0] > 1350 and thvalue[1] > 1350:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] - 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])

   if thvalue[0] > 1500 and thvalue[1] > 1500:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving forward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving forward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   elif thvalue[0] == 1500 and thvalue[1] == 1500:
      result_str = "ROV IS AT REST"

   else:
      result_str = "ROV IS IN MOTION \n" + "Thruster 1 is moving backward with " + \
      str(abs(1500-thvalue[0])) + " unit speed \n" + \
            "Thruster 2 is moving backward with " + \
               str(abs(1500-thvalue[1])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)

def down():
   if thvalue[2] <= 1800 and thvalue[2]>1200:
      thvalue[2] = thvalue[2] - 50
      thvalue[3] = thvalue[3] - 50
      pi.set_servo_pulsewidth(thruster_three, thvalue[2])
      pi.set_servo_pulsewidth(thruster_four, thvalue[3])

   if thvalue[2] > 1500:
      result_str = "Rov is going up with " + str(abs(1500-thvalue[2])) + " unit speed"
   elif thvalue[2] == 1500:
      result_str = "Vertical Motion Of Rov has Stopped"
   else:
      result_str = "Rov is going down with " + str(abs(1500-thvalue[2])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)

def upward():
   if thvalue[2]>=1200 and thvalue[2]<1800:
      thvalue[2] = thvalue[2] + 50
      thvalue[3] = thvalue[3] + 50
      pi.set_servo_pulsewidth(thruster_three, thvalue[2])
      pi.set_servo_pulsewidth(thruster_four, thvalue[3])

   if thvalue[2] > 1500:
      result_str = "Rov is going up with " + str(abs(1500-thvalue[2])) + " unit speed"
   elif thvalue[2] == 1500:
      result_str = "Vertical Motion Of Rov has Stopped"
   else:
      result_str = "Rov is going down with " + str(abs(1500-thvalue[2])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)

def left():
   if thvalue[0] > 1500:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning left and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   elif thvalue[0] == 1500:
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Left Thruster is Stopped and Rov is turning left\n and speed of right thruster is " + \
         str(abs(1500-thvalue[1])) + " unit"

   else:
      thvalue[0] = thvalue[0] + 50
      thvalue[1] = thvalue[1] - 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning right and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   # time.sleep(1)
   # thvalue[1] = 1500
   # thvalue[0] = 1500
   # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
   # pi.set_servo_pulsewidth(thruster_two, thvalue[1]) 

def right():
   if thvalue[1] > 1500:
      thvalue[1] = thvalue[1] - 50
      thvalue[0] = thvalue[0] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning right and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   elif thvalue[1] == 1500:
      thvalue[0] = thvalue[0] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      result_str = "right Thruster is Stopped and Rov is turning right\n and speed of left thruster is " + str(abs(1500-thvalue[0])) + " unit"

   else:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] + 50
      pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning left and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   # time.sleep(1)
   # thvalue[0] = 1500
   # thvalue[1] = 1500
   # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
   # pi.set_servo_pulsewidth(thruster_two, thvalue[1])    

def reset():
   thvalue[0] = 1500
   thvalue[1] = 1500
   thvalue[2] = 1500
   thvalue[3] = 1500
   pi.set_servo_pulsewidth(thruster_one, thvalue[0])
   pi.set_servo_pulsewidth(thruster_two, thvalue[1])
   pi.set_servo_pulsewidth(thruster_three, thvalue[2])
   pi.set_servo_pulsewidth(thruster_four, thvalue[3])
   result_str = "ROV IS AT REST"
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)




result = "Rov is not in Motion \nAll The thrusters aare in Idle State"


button_forward = Button(app, text="↑" , padx=40, pady=20 , command = forward).place(x = 160 , y= 510)
button_backward = Button(app, text="↓" , padx=40, pady=20,command = backward).place(x=160,y=575 )
button_left = Button(app, text="←" , padx=40, pady=20 ,command = left).place(x=50, y=575 )
button_right = Button(app, text="→" , padx=40, pady=20,command = right).place(y =575, x = 270  )
button_up = Button(app, text="UP" , padx=40, pady=20,command = upward).place(x = 380,  y= 510 )
button_down = Button(app, text="Down" , padx=40, pady=20,command = down).place(x = 380 , y= 575 ) 
button_reset = Button(app, text="RESET" , padx=40, pady=20 , command = reset).place(x = 100, y  = 650)

ele = Text(app, width=65, height = 5 ,borderwidth=5)
ele.place(relwidth=0.42 , relheight=0.25 , relx=0.54, rely = 0.63)
ele.insert(INSERT, result)
app.mainloop()
