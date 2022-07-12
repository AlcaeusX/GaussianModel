####### Creator : Alkaios Lamprakis ########
####### For questions/bugs or just say thanks ---> alkaios.lmp@gmail.com ######


import tkinter
from tkinter import *
import numpy as np
from scipy.stats import norm
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

####################ARXIKES TIMES################
global is_on
is_on = False

beamWaist = 0
scanningSpeed = 0
pulseFreq = 0



##################################################



def solve_now():
#    ans0 = float(10/float(entry2.get()) * math.log((float(entry3.get()) / float(entry4.get()))))
#    print(ans0)
#    l0.config(text="Fluence (J/cm2): " + str(ans0))
    
    beamWaist = float(entry1.get())
    scanningSpeed =  float(entry5.get())
    pulseFreq = float(entry6.get())

    ans1 = float(10/float(entry2.get()) * math.log(float(entry3.get()) / float(entry4.get())))
    print(ans1)
    l7.config(text="MAX Ablation depth (mm): " + str(ans1))
    
    ans2 = float((1 - float(entry5.get()) / (2 * float(entry1.get()) * float(entry6.get())))*100)
    print(ans2)
    l8.config(text="Pulse overlap %: " + str(ans2))
    
    ans3 = float(2 * float(entry1.get()) * float(entry6.get()) / float(entry5.get()))
    print(ans3)
    l9.config(text="Effective pulse number: " + str(ans3))
    
    ans4 = float(float(entry1.get()) * np.sqrt((0.2*float(entry2.get()) * float(ans1))))
    print(ans4)
    l10.config(text="Ablation width (mm): " + str(ans4))    
    
#####sto ans1 evala 10/a anti 1/a wste na vgei to depth se mm    
   


#####sto ans4 evala 0,2 anti 2 (ekana to a apo cm-1 se 10mm-1) wste na vgoun swsta oi monades 
    
    ##########PLOT#####

    window = tkinter.Tk()
    window.wm_title("Plot")
    

    DN= float(scanningSpeed)/ float(pulseFreq)
    ###print("DN " +str(DN))
    ###print("beamWaist " +str(beamWaist))
   

    # scale_factor = 5

    # xmin, xmax = plt.xlim()
    # ymin, ymax = plt.ylim()

    # plt.xlim(xmin * scale_factor, xmax * scale_factor)
    # plt.ylim(ymin * scale_factor, ymax * scale_factor)



    # Creating the distribution (sto x/data vazw -loc,3*loc,0.00...loc kai sto y/pdf vazw data, loc , scale opou scale=beamwaist/2 oxi loc/2 giati scale=sigma)
    data = np.arange(-beamWaist, 6*beamWaist, beamWaist* 0.01)
    pdf = norm.pdf(data , loc = beamWaist , scale = beamWaist/2 )

      ###print("data " +str(data[0]))
      ###print("pdf " +str(pdf))
    
    data1 = np.arange(-beamWaist, 6*beamWaist, beamWaist* 0.01)
    pdf1 = norm.pdf(data1 , loc =  DN + beamWaist , scale = beamWaist/2 )

    data2 = np.arange(-beamWaist, 6*beamWaist,beamWaist* 0.01)
    pdf2 = norm.pdf(data , loc = 2*DN + beamWaist , scale = beamWaist/2 )
    
    print('Pulse Centers Distance=' + str(DN))
        
      #ολη η διασπορα μου ειναι ιση με το beamwaist, ενώ το ΔΝ=v/f
    
      ############## KIKLOI #########################
       
  
    fig1, axes = plt.subplots(figsize=(8,5)) 
    cc1 = plt.Circle(( beamWaist , 0.5 ), beamWaist, color = 'r', alpha=0.5 ) 
    cc2 = plt.Circle(( DN + beamWaist , 0.5 ), beamWaist, color = 'r', alpha=0.5 ) 
    cc3 = plt.Circle(( 2*DN + beamWaist , 0.5 ), beamWaist, color = 'r', alpha=0.5 ) 
     
      # axes.set_aspect( 1 ) 
    axes.add_artist(cc1) 
    axes.add_artist(cc2) 
    axes.add_artist(cc3) 
    plt.title( 'Pulse Overlap Visualization' ) 
    plt.xlim(0,2*DN + 2*beamWaist)
    plt.axis('off')
     
      # plt.title( 'Pulse Overlap Visualization' ) 
   
 
      #################################################
    
    fig = plt.figure(figsize=(14,8))
    ax1 = fig.add_subplot(111).plot(data, pdf, data1, pdf1, data2, pdf2)
    plt.title('Distribution')
      # ax2 = fig.add_subplot(212).plot(x, y , x1, y1 , x2, y2)
      # fig = Figure(figsize=(8, 6), dpi=120)
      #fig.add_subplot(111).plot(data, pdf, data1, pdf1, data2, pdf2, x, y , x1, y1 , x2, y2)
    
    
    ###########CANVAS#################################
    canvas = FigureCanvasTkAgg(fig1, master=window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack()
    

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()
    
   ####################################################
    exit_button = Button(window, text="Exit", command=window.destroy)
    exit_button.pack()
        
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)


    canvas.mpl_connect("key_press_event", on_key_press)


##########FORMULAS BUTTON#############################

# Define our switch function
def switch():
    
	global is_on
	# Determin is on or off
	if is_on:
		on_button.config(text='FORMULAS')
		my_label.config(text='')
		is_on = False
	else:
		on_button.config(text='HIDE')
		my_label.config(bg = 'white', text="MAX Ablation depth: D=1/a * ln (Fp/Fth) \n Pulse overlap % : (1- v / 2 w f) 100 % \n Effective pulse number: 2 w f / v \n Ablation width: S = w √(2aD) \n Fluence: 2Ep/πw^2 \n Depth of focus (b) is equal to 2Zr (Rayleigh range) \n or b = 2 * π n w/λ, where n is the ri of the medium (for air nair=1).\n Ablation depth <= depth of focus.\n Beam waist is calculated at I/e^2")
		is_on = True
  
# Define Our Texts
on = 'FORMULAS'
off = 'HIDE'








#####################################################################

window = tkinter.Tk()
window.title("AblationTron")
window.geometry("600x600")

l1 = Label(window, text="Enter Beam waist (w in mm)")
l1.pack()
entry1 = Entry(window, )
entry1.pack()


l2 = Label(window, text="Enter Absorptivity (a in cm-1)")
l2.pack()
entry2 = Entry(window)
entry2.pack()

##l3 = Label(window, text="Enter Peak Fluence Fp in J/cm2")
l3 = Label(window, text="Enter Pulse Energy (Ep in mJ)")
l3.pack()
entry3 = Entry(window, )
entry3.pack()

##l4 = Label(window, text="Enter Threshold Fluence Fth in J/cm2")
l4 = Label(window, text="Enter Threshold Pulse Energy (Eth in mJ)")
l4.pack()
entry4 = Entry(window, )
entry4.pack()


l5 = Label(window, text="Enter Scanning Speed (v in mm/s)")
l5.pack()
entry5 = Entry(window, )
entry5.pack()

l6 = Label(window, text="Enter Pulse Frequency (f in Hz)")
l6.pack()
entry6 = Entry(window, )
entry6.pack()
b1 = Button(window, text="SOLVE",
command=solve_now)
b1.pack()



l7 = Label(window)
l7.pack()

l8 = Label(window)
l8.pack()

l9 = Label(window)
l9.pack()

l10 = Label(window)
l10.pack()

l16 = Label(window)
l16.pack()



# l15 = Label(window,bg='white', text="FORMULAS")
# l15.pack()
on_button = Button(window, text=on, command=switch)
on_button.pack()

my_label = Label(window,text="")
my_label.pack()



# lc = Label(window, text='MAX Ablation depth: D=1/a * ln (Fp/Fth) \n Pulse overlap % : (1- v / 2 w f) 100 % \n Effective pulse number: 2 w f / v \n Ablation width: S = w √(2aD) \n Fluence: 2Ep/πw^2 \n Depth of focus (b) is equal to 2Zr (Rayleigh range) \n or b = 2 * π n w/λ, where n is the ri of the medium (for air nair=1).\n Ablation depth <= depth of focus.\n Beam waist is calculated at I/e^2')
# lc.pack()

# l11 = Label(window, text="MAX Ablation depth: D=1/a * ln (Fp/Fth)" )
# l11.pack()

# l12 = Label(window,bg='white', text="Pulse overlap % : (1- v / 2 w f) 100 %")
# l12.pack()

# l13 = Label(window, text="Effective pulse number: 2 w f / v")
# l13.pack()

# l14 = Label(window,bg='white', text="Ablation width: S = w √(2aD)")
# l14.pack()

# l115 = Label(window, text="Fluence: 2Ep/πw^2")
# l115.pack()

# l116 = Label(window, bg='white', text="Depth of focus (b) is equal to 2Zr (Rayleigh range) \n or b = 2 * π n w/λ, where n is the ri of the medium (for air nair=1)\n Ablation depth <= depth of focus\n Beam waist is calculated at I/e^2")
# l116.pack()





exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.pack(side = BOTTOM)


window.mainloop()





