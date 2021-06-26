# Convolution Reverb

## 前言  
* **Convolution Reverb---卷積混響**市面上與之相關的Plug-ins也會稱為**IR Reverb(Impluse Response Reverb 脈衝響應混響)**，這個演算法是利用**Fast Fourier transform 快速傅立葉轉換**得出音頻頻率，再利用**Convolution 卷積**的數學運算方法，得出Audio在IR中的頻率分布，並將運算結果寫出。
---
## Usage  
下圖此演算法的GUI: 
* Step 1 : **輸入Dry Audio路徑**  
在Dry Audio的欄位中輸入欲處理的Wav檔案路徑。  
* Step 2 : **輸入IR路徑**  
在Impulse Response的欄位中輸入IR的Wav檔案路徑。
* Step 3 : **按下Deliver**  
檔案路徑會傳入演算法中，*Please Put Audio File Path In Entry*會變成*Please Enter the Process*。
* Step 4 : **按下Processr**  
此時演算法將會處理音訊，此步驟運算會稍微久一點，等到GUI可以正常運作就代表完成，並會出現*Audio have been Processed*。
* Step 5 : **按Play播放音訊，Dry/Wet Slider調整乾濕度**  
按下Play即可聽到處理完的音訊，並且可以調整Dry/Wet，調整你要音色。
* Step 6 : **輸出Audio**  
調整完後即可輸出成Wav檔，看到*Wav_File Output*表示輸出完成，**輸出的檔案會根據Slider目前的位置為準，請務必檢查清楚**。  
* 備註 :  
    * Dry.wav為未處理的
    * Wet.wav為演算後的
    * Final.wav為經Dry/Wet調整後的  
![image](https://github.com/LILRAY0826/Convolution_Reverb/blob/main/Pic/GUI.jpg?raw=true)  

---  
## 技術應用
### 開發工具
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
演算法中此行代碼為主要，**快速傅立葉轉換FFT**&**卷積Cvolution**在此完成，也是按下Process時，需要等候的原因。  
#### 平行處理
Dry/Wet Slider的調控是利用混音上平行壓縮Parallel Compression的想法，將Dry的信號加上Wet的信號，再做輸出。

---
## 總結  
**在Convolution_Reverb.py的程式碼中，都有標註詳細用途，不懂的人可以看後面的標註，有助於理解演算法過程。**  
此演算法可以優化的地方有很多 :
* 增加演算速度，這次是使用scipy.signal.convolve的函式，那在未來可以自己寫一個傅立葉的轉換以及卷積過程。
* 增加功能，可以再加上Low High pass Filiter 或者 Gain, Pre-Delay等功能
* Plug-in化，可以使用MSP編程，寫成Plug-in，這也是我正在學習當中的技能，未來也會將Plug-in的內容放置網站上。
