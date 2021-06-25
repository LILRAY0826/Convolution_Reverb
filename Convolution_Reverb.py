import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
from scipy.signal import convolve

def main(sample_path, reverb_path):
    #   OPENING TEST WAV FILE   #

    wav_file = wave.open(sample_path, 'r')
    frame_rate = wav_file.getframerate()           # 得到音檔的取樣率
    num_samples_sample = wav_file.getnframes()     # 227328偵
    num_channels_sample = wav_file.getnchannels()  # 2
    sample = wav_file.readframes(num_samples_sample) # 會以16進位tuple的方式讀取成buffer
    total_samples_sample = num_samples_sample * num_channels_sample # 454656偵
    wav_file.close()

    wav_file = wave.open(reverb_path, 'r')
    num_samples_reverb = wav_file.getnframes()     # 49465偵
    num_channels_reverb = wav_file.getnchannels()  # 2
    reverb = wav_file.readframes(num_samples_reverb) # 會以16進位tuple的方式讀取成buffer
    total_samples_reverb = num_samples_reverb * num_channels_reverb # 98930偵
    wav_file.close()

    sample = struct.unpack('{n}h'.format(n=total_samples_sample), sample) # 將16進位的tuple unpack成'h'->short int  len_sample=454656
    sample = np.array([sample[0::2], sample[1::2]], dtype=np.float64)     # 因為是雙聲道所以拆成兩個單聲道處理 len_sample[0]=len_sample[1]=227328
    sample[0] /= np.max(np.abs(sample[0]))                                # 將音訊量化，因為16-bit的訊號範圍[-32768,+32767]
    sample[1] /= np.max(np.abs(sample[1]))                                # 將音訊量化，因為16-bit的訊號範圍[-32768,+32767]

    reverb = struct.unpack('{n}h'.format(n=total_samples_reverb), reverb) # 將16進位的tuple unpack成'h'->short int   len_reverb=98930
    reverb = np.array([reverb[0::2], reverb[1::2]], dtype=np.float64)     # 因為是雙聲道所以拆成兩個單聲道處理 len_reverb[0]=len_reverb[1]=49465
    reverb[0] /= np.max(np.abs(reverb[0]))                                # 將音訊量化，因為16-bit的訊號範圍[-32768,+32767]
    reverb[1] /= np.max(np.abs(reverb[1]))                                # 將音訊量化，因為16-bit的訊號範圍[-32768,+32767]

    #   MAIN PART OF THE ALGORITHM   #

    gain_dry = 1
    gain_wet = 1
    output_gain = 0.05

    reverb_out = np.zeros([2, np.shape(sample)[1] + np.shape(reverb)[1] - 1], dtype=np.float64)        # len_reverb_out = 276792
    reverb_out[0] = output_gain * (convolve(sample[0] * gain_dry, reverb[0] * gain_wet, method='fft')) # 進行傅立葉變換再進行卷積
    reverb_out[1] = output_gain * (convolve(sample[1] * gain_dry, reverb[1] * gain_wet, method='fft')) # 進行傅立葉變換再進行卷積

    #   WRITING TO FILE   #

    reverb_integer = np.zeros((reverb_out.shape))
    reverb_integer[0] = (reverb_out[0] * int(np.iinfo(np.int16).max)).astype(np.int16)  # int(np.iinfo(np.int16).max)=32767，是位元深度16-bit的每個訊號大小
    reverb_integer[1] = (reverb_out[1] * int(np.iinfo(np.int16).max)).astype(np.int16)  # int(np.iinfo(np.int16).max)=32767，是位元深度16-bit的每個訊號大小

    reverb_to_render = np.empty((reverb_integer[0].size + reverb_integer[1].size), dtype=np.int16)
    reverb_to_render[0::2] = reverb_integer[0]
    reverb_to_render[1::2] = reverb_integer[1]

    nframes = total_samples_sample
    comptype = "NONE"
    compname = "not compressed"
    nchannels = 2
    sampwidth = 2

    wav_file_write = wave.open('Wet.wav', 'w')
    wav_file_write.setparams((nchannels, sampwidth, int(frame_rate), nframes, comptype, compname))

    for s in range(nframes):
        wav_file_write.writeframes(struct.pack('h', reverb_to_render[s])) # 將short int寫回16進位的tuple

    wav_file_write.close()

    #   PLOTTING THE RESULTS   #

    plt.figure()
    plt.subplot(4, 1, 1)
    plt.plot(sample[0])
    plt.xlim(0, num_samples_sample)
    plt.grid(True)
    plt.subplot(4, 1, 2)
    plt.plot(sample[1])
    plt.xlim(0, num_samples_sample)
    plt.grid(True)
    plt.subplot(4, 1, 3)
    plt.plot(reverb_out[0])
    plt.xlim(0, num_samples_sample)
    plt.grid(True)
    plt.subplot(4, 1, 4)
    plt.plot(reverb_out[1])
    plt.xlim(0, num_samples_sample)
    plt.grid(True)
    plt.show()
'''
if __name__ == "__main__":

    sample_path = 'Dry.wav'
    reverb_path = 'C:/Users/ray89/Desktop/python/Audio_algorithm/Reverb_Impluse/Nice Drum Room.wav'
    main(sample_path, reverb_path)
'''
