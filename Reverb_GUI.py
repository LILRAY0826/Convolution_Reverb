import tkinter as tk
import pygame
from pydub import AudioSegment
from Convolution_Reverb import main
# C:\Users\ray89\Desktop\python\Audio_algorithm\Reverb_Impluse\Block Inside.wav

def play():
    global s
    pygame.mixer.init()
    pygame.mixer.music.load('Wet.wav')
    s = pygame.mixer.Sound('Dry.wav')
    s.set_volume(1.0)
    s.play()
    pygame.mixer.music.play()

def volume(current):
    pygame.mixer.music.set_volume(float(current))

def Deliver():
    var1.set('Please Enter the Process')

def Process():
    main(sample_path.get(), reverb_path.get())
    var1.set('Audio have been Processed')

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def output():
    Dry = AudioSegment.from_file("Dry.wav")  # your first audio file
    Wet = AudioSegment.from_file("Wet.wav")  # 載入WAV文件
    db = Wet.dBFS  # 取得WAV文件的聲音分貝值
    wet = match_target_amplitude(Wet, int(db-(abs(db)*(1.0-(pygame.mixer.music.get_volume())))))
    mixed = Dry.overlay(wet)
    mixed.export("Final.wav", format="wav")
    var.set('Wav_File Output')

pygame.mixer.init()

window = tk.Tk()
window.title('Convolution_Reverb')   # 命名視窗名字
window.geometry('500x550')           # 給定視窗大小
sample_path = tk.StringVar()
reverb_path = tk.StringVar()
var = tk.StringVar()
var1 = tk.StringVar()
var.set('')
var1.set('Please Put Audio File Path In Entry')
current = 0.00
sample_label = tk.Label(window, text='Dry Audio', font=('Arial', 14)).pack()
sample = tk.Entry(window, show = None, font=('Arial', 12), textvariable=sample_path).pack()
reverb_label = tk.Label(window, text='Impulse Reponse', font=('Arial', 14)).pack()
reverb = tk.Entry(window, show = None, font=('Arial', 12), textvariable=reverb_path).pack()
Process_Label = tk.Label(window, textvariable=var1, font=('Arial', 10), width=30, height=2).pack()
Deliver_button = tk.Button(window, text="Deliver", command=Deliver, width=30, height=2).pack()
Process_button = tk.Button(window, text="Process", command=Process, width=30, height=2).pack()
Drywet_label = tk.Label(window, text='Dry/Wet(%)', font=('Arial', 14)).pack()
Drywet_slider = tk.Scale(window, from_=0, to=1, resolution=0.05, command=volume, length=200, orient="horizontal", variable=current)
Drywet_slider.pack()
final = tk.Label(window, textvariable=var, font=('Arial', 10), width=30, height=2).pack()
my_button = tk.Button(window, text="Play", command=play, width=30, height=2)
my_button.pack()
tk.Button(window, text="Output", command=output, width=30, height=2).pack()
window.mainloop()