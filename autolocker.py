import win32gui
import time
import ctypes
import os


def lock_pc():
    ctypes.windll.user32.LockWorkStation()

def divide():
    log('*-*'*20, icon=None)


def log(log_txt, icon="[+]"):
    full_path = os.getcwd() + '\\autolocker_log.txt'

    if os.path.exists(full_path):
        with open(full_path, 'a') as f:
            if icon is not None:
                f.write(icon + " " + log_txt + "\n")
            else:
                f.write(log_txt + "\n")
    else:
        with open(full_path, 'w') as f:
            if icon is not None:
                f.write(icon + " " + log_txt + "\n")
            else:
                f.write(log_txt + "\n")


def Main():
    divide()
    log(str(time.ctime(time.time())), icon="[<>]")
    divide()
    log("Starting autolocker..")

    orig_cords = win32gui.GetCursorPos()
    log("Original Cords :{}".format(str(orig_cords)))


    checks = 0
    while True:
        new_cords = win32gui.GetCursorPos()

        if new_cords == orig_cords:
            checks += 1
            log("Checks = {}".format(str(checks)))
            if checks > 4:
                log("Locking PC...", icon="[!X!]")
                lock_pc()
                break
            else:
                log("Orig Cords: {}, New Cords: {}".format(str(orig_cords), str(new_cords)))
                log("Sleeping for 15 secs...")
                time.sleep(15)
        else:
            orig_cords = new_cords
            log("Orig cords equals new cords now, {}".format(str(new_cords)))
            log("Sleeping for 15 secs...")
            time.sleep(15)
            checks = 0
            log("Reset checks... Checks = {}".format(str(checks)))

    log("Exiting..")
    divide()
    exit(0)

if __name__ == "__main__":
    Main()
