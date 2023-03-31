This script listens to and logs the keyboard and mouse input at the background and also send through them through LabStreamingLayer (LSL). The original intention is for usability, human factors, and psychological experiment which needs to keep track of computer input and generate accurate timestamps for data syncing. The script creates a data stream "inputListener" that can be picked up by LabRecorder or other LSL compatible programs.

How to use
1. Make sure you have Python package pynput and LSL installed (can install through pip install pynput,pylsl)
2. download the script and run with "Python inputListener.py <filename>". (e.g., python inputListener.py P001)
3. Python 3.8 added time.time_ns() which captures more accurate timestamps, so if you are using Python 3.7 or below will have to change time.time_ns() to time.time()
4. There is currently no key to stop logging, it is recommended to run it through cmd and just closeout the window when done
5. If using time_ns() to convert the Unix time in second divide it by 10,000,000