from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pylsl import StreamInfo, StreamOutlet
import logging
import time
import sys

def main():
    print('cmd entry:', sys.argv[1])
    filename = sys.argv[1] + '.csv'
    # Set up LabStreamingLayer stream.
    info = StreamInfo(name='inputListener', type='Markers', channel_count=1,
                        channel_format='string', source_id='Exp_InputStream_001')
    outlet = StreamOutlet(info)  # Broadcast the stream.

    # log file settings
    logging.basicConfig(filename=filename, level=logging.INFO, filemode='a', format='%(asctime)s:%(message)s')
    
    # Define keyboard listener functions
    # Get keyboard press. This will register both when press and press and hold
    def on_press(key):
        marker = "{0}_press_{1}".format(key, time.time_ns())
        outlet.push_sample([marker])
        logging.info(marker)
        print(marker)

    # Get keyboard release.
    def on_release(key):
        # marker = key.char + "_release_" + str(time.time_ns())
        marker = "{0}_release_{1}".format(key, time.time_ns())
        outlet.push_sample([marker])
        logging.info(marker)
        print(marker)

    # Define mouse listener functions
    # Get mouse x y when the mouse moves
    def on_move(x, y):
        marker = str(x) + "_" + str(y) + str(time.time_ns())
        outlet.push_sample([marker])
        logging.info(marker)
        print(marker)
        # print("Mouse moved to ({0}, {1}) at {3}".format(x, y, time.time_ns()))

    # Get mouse button click. currently register which button and coordinate
    def on_click(x, y, button, pressed):
        if pressed:
            marker = str(x) + "_" + str(y) + "_" + str(button) + "_click_" + str(time.time_ns())
            outlet.push_sample([marker])
            logging.info(marker)
            print(marker)
            # print('Mouse clicked at ({0}, {1}) with {2} at {3}'.format(x, y, button, time.time_ns()))
        else:
            marker = str(x) + "_" + str(y) + "_" + str(button) + "_release_" + str(time.time_ns())
            outlet.push_sample([marker])
            logging.info(marker)
            print(marker)
            # print('Mouse released at ({0}, {1}) with {2} at {3}'.format(x, y, button, time.time_ns()))Q

    # Get mouse scroll.
    def on_scroll(x, y, dx, dy):
        marker = str(x) + "_" + str(y) + "_" + str(dx) + "_" + str(dy) + "_" + str(time.time_ns())
        outlet.push_sample([marker])
        logging.info(marker)
        print(marker)
        # print('Mouse scrolled at ({0}, {1})({2}, {3}) at {4}'.format(x, y, dx, dy, time.time_ns()))

    # Setup the keyboard listener threads, remove any unwanted listening items
    # keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
    keyboard_listener = KeyboardListener(on_press=on_press)

    # Setup the mouse listener threads, remove any unwanted listening functions
    # mouse_listener = MouseListener(on_click=on_click, on_scroll=on_scroll, on_move=on_move)
    mouse_listener = MouseListener(on_click=on_click)

    # initiate logging
    keyboard_listener.start()
    mouse_listener.start()

    # adding log.INGO into the log file
    keyboard_listener.join()
    mouse_listener.join()

if __name__ == "__main__":
    main()