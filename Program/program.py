""" This sketch utilizes the buzzer to play songs. The Raspberry's 'freq()' command plays notes of a 
given frequency, while 'duty_u16()' set the current duty cycle of the 
PWM output as an unsigned 16-bit value in the range 0 to 65535 inclusive.

There's a function that takes note characters
and returns the corresponding frequency from this table:

  note 	frequency
  c     262 Hz
  d     294 Hz
  e     330 Hz
  f     349 Hz
  g     392 Hz
  t     415 Hz
  a     440 Hz
  b     494 Hz
  h     494 Hz
  C     523 Hz
  D     587 Hz
  S     622 Hz
  U     622 Hz
  E     659 Hz
  F     698 Hz
  J     740 Hz
  G     784 Hz
  A     880 Hz
  V     1047 Hz
  
super mario theme song link: https://youtu.be/NTa6Xbzfq1U?si=ocevOTef4G9sJV_Z
For more information, see https://docs.micropython.org/en/latest/library/machine.PWM.html """


from machine import Pin, PWM
from time import sleep

tempo = 100
notes = "EE E CE G g C g e a h bagEG AFG E CDh C g e a h bagEG AFG E CDh  GJFS E taC aCD GJFS E V VV  GJFS E taC aCD U D C  GJFS E taC aCD GJFS E V VV  GJFS E taC aCD U D C"
songLength = 93
beats = [1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,2,6,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,2,6]

frequencies = {
    'c': 262, 'd': 294, 'e': 330, 'f': 349, 'g': 392, 't': 415, 'a': 440,
    'b': 466, 'h': 494, 'C': 523, 'D': 587, 'S': 622, 'E': 659, 'F': 698,
    'J': 740, 'G': 784, 'A': 880, 'V': 1047, 'U': 622
}
buzzer = PWM(Pin()) # Buzzer pin on board
    
def playSong():
    notesList = list(notes)
  
    for i in range(songLength):
        duration = beats[i] * tempo / 800
        if notesList[i] == ' ':       
            sleep(duration)
        else:           
            buzzer.freq(frequency(notesList[i]))
            buzzer.duty_u16(1000)    
            sleep(duration)
            buzzer.duty_u16(0) 
    sleep(tempo) 

def frequency(note):
    for key, value in frequencies.items():
        if key == note:
            return value
    return 0

playSong()
