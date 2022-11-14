import psutil
from time import sleep
from win10toast import ToastNotifier

LOW_BATTERY_LEVEL = 40
TIME_INTERVALS = 60

def check_battery(low):
    battery = psutil.sensors_battery()
    #print(f'battery : {battery}')

    is_laptop = False
    notify = False
    title, message = '', ''
    if battery is not None:
        is_laptop = True
        is_charging = battery.power_plugged
        percent = battery.percent
        # print(f'is charging : {is_charging}')
        # print(f'battery percent : {percent} %')

        if percent <= low and not is_charging:
            title = 'Low Battery Level'
            message = f'battery level is {percent} %'
            notify = True

    else:
        title = 'No battery'
        message = 'battery is none, not using laptop'
        notify = True
    
    return is_laptop, notify, title, message

# One-time initialization
toaster = ToastNotifier()
while True:
    is_laptop, notify, title, message = check_battery(LOW_BATTERY_LEVEL)
    if notify:
        toaster.show_toast(title, message, threaded=True,
                        icon_path=None, duration=5)
    if is_laptop:
        sleep(TIME_INTERVALS)
    else:
        break