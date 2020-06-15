import logger
import subprocess
import pkg_resources
import sys
import keyboard

def checkModules():
    missing = False
    logger.log("Checking for required modules...")
    try:
        import tkinter
        import keyboard
    except:
        missing = True

    if missing:
        logger.log("Missing required module(s).")

        logger.log("Downloading...")
        try:
            subprocess.check_call(['pip', 'install', "-U", *missing], stdout=subprocess.DEVNULL)
        except Exception as e:
            # Always subprocess error
            print("\nError:\n{0}\nPlease download required modules: {1}".format(e, required))
            sys.exit(-1)
