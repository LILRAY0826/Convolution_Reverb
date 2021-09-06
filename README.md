# Convolution Reverb

## Abstract  
* **Convolution Reverb---Convolution Reverb** The relevant Plug-ins on the market are also called **IR Reverb (Impluse Response Reverb)**. This algorithm uses **Fast Fourier transform Fast Fourier Transform** obtains the audio frequency, and then uses the mathematical operation method of **Convolution convolution** to obtain the frequency distribution of Audio in the IR, and write the result of the calculation.
---
## Usage  
The following figure shows the GUI of this algorithm:
* Step 1: **Enter Dry Audio path**
Enter the path of the Wav file to be processed in the Dry Audio field.
* Step 2: **Enter IR path**
Enter the IR Wav file path in the Impulse Response field.
* Step 3: **Press Deliver**
The file path will be passed into the algorithm, and *Please Put Audio File Path In Entry* will become *Please Enter the Process*.
* Step 4: **Press Processor**
At this time, the algorithm will process the audio. This step will take a little longer. When the GUI can operate normally, it will be completed, and *Audio have been Processed* will appear.
* Step 5: **Press Play to play the audio, Dry/Wet Slider to adjust the dry humidity**
Press Play to hear the processed audio, and you can adjust Dry/Wet to adjust the tone you want.
* Step 6: **Output Audio**
After the adjustment, you can output it as a Wav file. Seeing *Wav_File Output* indicates that the output is complete. **The output file will be based on the current position of the Slider. Please be sure to check it clearly**.
* Remarks:
    * Dry.wav is unprocessed
    * Wet.wav is calculated
    * Final.wav is adjusted by Dry/Wet
![image](https://github.com/LILRAY0826/Convolution_Reverb/blob/main/Pic/GUI.jpg?raw=true)  

---  
## Technique
### Development tools
* Python Language
*	PyCharm
*	wave
*	struct
*	matplotlib.pyplot
*	scipy.signal
*	tkinter
*	pygame
*	pydub
#### scipy.signal.convolve  
```python
convolve(sample[0] * gain_dry, reverb[0] * gain_wet, method='fft')  
```  
This line of code in the algorithm is the main one, **Fast Fourier Transform FFT**&**Convolution Revolution** is completed here, which is why you need to wait when you press Process.
#### Impulse Response
IR refers to the response of a piece of audio in a space. Usually, the method of recording IR is to puncture balloons or items that can make a loud instantaneous noise. Record the audio and record the response of the sound.
#### Parallel processing
The control of Dry/Wet Slider is to use the idea of parallel compression Parallel Compression on the mix, adding the signal of Dry to the signal of Wet, and then outputting it.

---
## Sumarize 
**In the code of Convolution_Reverb.py, there are labels for detailed purposes. Those who don’t understand can read the labels at the back to help understand the algorithm process. **
There are many areas where this algorithm can be optimized:
* Increase the calculation speed. This time I use the scipy.signal.convolve function. In the future, you can write a Fourier transformation and convolution process by yourself.
* Add function, you can add Low High pass Filiter or Gain, Pre-Delay and other functions
* Plug-in, you can use MSP programming, written as Plug-in, this is the skill I am learning, and the content of Plug-in will be placed on the website in the future.
