from decimal import Rounded
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import pigpio

# Create an instance of TKinter Window or frame
app = Tk()
# app.configure(bg='#F5FF90')
app.title("ROVC-team HUSTLERS")
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
# Set the size of the window
app.geometry("%dx%d" % (width, height))

# Create a Label to capture the Video frames
# label =Label(app )
# label.place(relwidth=1, relheight=0.45, rely=0.03)
# label.place(x  = 25 , y = 5 , height= 450 , width= 900)
# label.grid(row=0, column=0, columnspan=5, padx = 20 , pady=40)
# cap= cv2.VideoCapture(0)

# Define function to show frame
# def show_frames():
#    # Get the latest frame and convert into Image
#    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
#    img = Image.fromarray(cv2image)
#    # Convert image to PhotoImage
#    imgtk = ImageTk.PhotoImage(image = img)
#    label.imgtk = imgtk
#    label.configure(image=imgtk)
#    # Repeat after an interval to capture continiously
#    label.after(1, show_frames)

# show_frames()

thruster_one = 10    #Enter the PIN Number to Which Thrsuter 1 is coonected
thruster_two = 7    #Enter the PIN Number to Which Thrsuter 2 is coonected
thruster_three = 3  #Enter the PIN Number to Which Thrsuter 3 is coonected
thruster_four = 27  #Enter the PIN Number to Which Thrsuter 4 is coonected

thruster_pins = [thruster_one, thruster_two, thruster_three, thruster_four]

# pi = pigpio.pi()

# for item in thruster_pins:
#      pi.set_servo_pulsewidth(item,1500)



thvalue = [1500, 1500,1500,1500]

def forward(eve):
   if thvalue[0] < 1850 and thvalue[1]<1850:
      thvalue[0] = thvalue[0] + 10
      thvalue[1] = thvalue[1] + 10
      # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      # pi.set_servo_pulsewidth(thruster_two, thvalue[1])

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
   if thvalue[2]<1500:
      more_str = " \nROV IS moving Vertically Down with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)
   if thvalue[2]>1500:
      more_str = " \nROV IS moving Vertically UP with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)


def backward(eve):
   if thvalue[0] > 1150 and thvalue[1] > 1150:
      thvalue[0] = thvalue[0] - 10
      thvalue[1] = thvalue[1] - 10
      # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      # pi.set_servo_pulsewidth(thruster_two, thvalue[1])

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
   if thvalue[2]<1500:
      more_str = " \nROV IS moving Vertically Down with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)
   if thvalue[2]>1500:
      more_str = " \nROV IS moving Vertically UP with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)

def down(eve):
   if thvalue[2] <= 1800 and thvalue[2]>1200:
      thvalue[2] = thvalue[2] - 10
      thvalue[3] = thvalue[3] - 10
      # pi.set_servo_pulsewidth(thruster_three, thvalue[2])
      # pi.set_servo_pulsewidth(thruster_four, thvalue[3])

   if thvalue[2] > 1500:
      result_str = "Rov is going up with " + str(abs(1500-thvalue[2])) + " unit speed"
   elif thvalue[2] == 1500:
      result_str = "Vertical Motion Of Rov has Stopped"
   else:
      result_str = "Rov is going down with " + str(abs(1500-thvalue[2])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[0]!=1500 or thvalue[1] != 1500:
      more_str =  "\n ROV Is also in Horizontal Forward Motion " + \
          "You can Press Enter to Stop It "
      ele.insert(INSERT, more_str)

def upward(eve):
   if thvalue[2]>=1200 and thvalue[2]<1800:
      thvalue[2] = thvalue[2] + 10
      thvalue[3] = thvalue[3] + 10
      # pi.set_servo_pulsewidth(thruster_three, thvalue[2])
      # pi.set_servo_pulsewidth(thruster_four, thvalue[3])

   if thvalue[2] > 1500:
      result_str = "Rov is going up with " + str(abs(1500-thvalue[2])) + " unit speed"
   elif thvalue[2] == 1500:
      result_str = "Vertical Motion Of Rov has Stopped"
   else:
      result_str = "Rov is going down with " + str(abs(1500-thvalue[2])) + " unit speed"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[0]!=1500 or thvalue[1] != 1500:
      more_str =  "\n ROV Is also in Horizontal Forward Motion " + \
          "You can Press Enter to Stop It "
      ele.insert(INSERT, more_str)

def left(eve):
   if thvalue[0] > 1500:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] + 50
      # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      # pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning left and speed of thruster 1 is " + \
          str(abs(1500-thvalue[0])) + \
          " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   elif thvalue[0] == 1500:
      thvalue[1] = thvalue[1] + 10
      # pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Left Thruster is Stopped and Rov is turning left" + \
         "and speed of right thruster is " + \
         str(abs(1500-thvalue[1])) + " unit"

   else:
      thvalue[0] = thvalue[0] + 10
      thvalue[1] = thvalue[1] - 10
      # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      # pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning right and speed of thruster 1 is " + \
         str(abs(1500-thvalue[0])) + \
          " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[2]<1500:
      more_str = " \nROV IS moving Vertically Down with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)
   if thvalue[2]>1500:
      more_str = " \nROV IS moving Vertically UP with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)

def right(eve):
   if thvalue[1] > 1500:
      thvalue[1] = thvalue[1] - 50
      thvalue[0] = thvalue[0] + 50
      # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      # pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning right and speed of thruster 1 is " + str(abs(1500-thvalue[0])) + \
          " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"

   elif thvalue[1] == 1500:
      thvalue[0] = thvalue[0] + 10
      # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      result_str = "right Thruster is Stopped and Rov is turning right\n and speed of left thruster is " + \
          str(abs(1500-thvalue[0])) + " unit"

   else:
      thvalue[0] = thvalue[0] - 50
      thvalue[1] = thvalue[1] + 50
      # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
      # pi.set_servo_pulsewidth(thruster_two, thvalue[1])
      result_str = "Rov is turning left and speed of thruster 1 is " + str(abs(1500-thvalue[0])) +  \
         " unit and thruster 2 is " + str(abs(1500-thvalue[1])) + " unit"
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)
   if thvalue[2]<1500:
      more_str = " \nROV IS moving Vertically Down with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)
   if thvalue[2]>1500:
      more_str = " \nROV IS moving Vertically UP with " + str(abs(1500 - thvalue[2])) + " unit speed"
      ele.insert(INSERT, more_str)

def reset(eve):
   thvalue[0] = 1500
   thvalue[1] = 1500
   thvalue[2] = 1500
   thvalue[3] = 1500
   # pi.set_servo_pulsewidth(thruster_one, thvalue[0])
   # pi.set_servo_pulsewidth(thruster_two, thvalue[1])
   # pi.set_servo_pulsewidth(thruster_three, thvalue[2])
   # pi.set_servo_pulsewidth(thruster_four, thvalue[3])
   result_str = "ROV IS AT REST"
   ele.delete("1.0","end")
   ele.insert(INSERT, result_str)




result = "Rov is not in Motion \nAll The thrusters aare in Idle State"

e =0

left_bImage = PhotoImage(file='left.png')
right_bImage = PhotoImage(file='right.png')
up_bImage = PhotoImage(file='up.png')
down_bImage = PhotoImage(file='down.png')
Vup_bImage = PhotoImage(file='Vup.png')
Vdown_bImage = PhotoImage(file='Vdown.png')
reset_bimage = PhotoImage(file='reset.png')

logo = ImageTk.PhotoImage(Image.open("logo.png"))

lb1 = Label(app,image=logo , borderwidth=0)
lb1.image = logo #keep a reference to it
# lb1.pack()

lb1.place(x=1080, y=80)

button_forward =Button(app, image=up_bImage , padx=40, pady=20 , command = lambda : forward(e), borderwidth=0).place(x = 210 , y= 410)
button_backward = Button(app, image=down_bImage , padx=40, pady=20,command = lambda : backward(e), borderwidth=0).place(x=210,y=505 )
button_left = Button(app, image=left_bImage , padx=40, pady=20 ,command = lambda : left(e), borderwidth=0).place(x=100, y=505 )
button_right = Button(app, image=right_bImage , padx=40, pady=20,command = lambda : right(e), borderwidth=0).place(y =505, x = 320  )
button_up = Button(app, image = Vup_bImage, padx=40, pady=20,command = lambda : upward(e), borderwidth=0).place(x = 430,  y= 410 )
button_down = Button(app, image = Vdown_bImage , padx=40, pady=20,command = lambda : down(e), borderwidth=0).place(x = 430 , y= 505 ) 
button_reset = Button(app, image = reset_bimage, padx=40, pady=20 , command = lambda : reset(e), borderwidth=0).place(x = 200, y  = 605)


team_name = Label(app, text="TEAM HUSTLERS" , font=(('comic sans ms'), 72), borderwidth=0)
team_name.place(x = 50, y= 225)


app.bind('<Key-Up>',backward)
# app.bind('<KeyRelease-Up>',reset)
app.bind('<Key-Left>',right)
# app.bind('<KeyRelease-Left>',reset)
app.bind('<Key-Down>',forward)
# app.bind('<KeyRelease-Down>',reset)
app.bind('<Key-Right>',left)
# app.bind('<KeyRelease-Right>',reset)
app.bind('<Key-c>',down)
# app.bind('<KeyRelease-c>',reset)
app.bind('<Key-e>',upward)
# app.bind('<KeyRelease-e>',reset)
app.bind('<Return>', reset)




ele = Text(app ,bg="#4146DA",foreground="white",font=(('monospace'), 28), borderwidth=5 )
ele.place(relwidth=0.43 , relheight=0.32 , relx=0.48, rely = 0.55)
ele.insert(INSERT, result)
app.mainloop()