import storage
import usb_cdc
import usb_hid
import digitalio
import board

button = digitalio.DigitalInOut(board.GP8)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

usb_cdc.enable()    
if (button.value):
    storage.disable_usb_drive()

usb_hid.enable(()) 
# usb_midi.enable()
# storage.remount("/", readonly=False)
