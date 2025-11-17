import time
from picoscroll import PicoScroll
import network  # This library is only on the Pico W
import urequests  # This is the file we just added

# --- !! SAFETY DELAY !! ---
# This gives you 5 seconds to press "Stop" in Thonny
# if the Pico is plugged in, *before* this script
# tries to connect to Wi-Fi and lock up.
print("Starting in 5 seconds... (Press STOP in Thonny to interrupt)")
time.sleep(5)
print("Script starting.")


# --- 1. SETTINGS - EDIT THESE! ---
WIFI_SSID = "yourWIFI"
WIFI_PASSWORD = "yourWIFIPASS"

# Brightness for the LED matrix (0-255)
BRIGHTNESS = 60
# Scroll speed (Higher is slower)
SCROLL_SPEED = 66


# Your Alexa Routine URLs
URL_HOME = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=YOUR-TRIGGER-ID"
URL_TV = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=YOUR-TRIGGER-ID"
URL_MOVIE = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=YOUR-TRIGGER-ID"
URL_NIGHT = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=YOUR-TRIGGER-ID"


# --- 2. SETUP ---
scroll = PicoScroll()
wlan = network.WLAN(network.STA_IF) # Station mode (connect TO a network)


# --- 3. HELPER FUNCTIONS ---

def connect_wifi():
    """
    Connects to Wi-Fi.
    Returns True on success, False on failure.
    THIS FUNCTION NO LONGER LOOPS FOREVER.
    """
    print("Connecting to Wi-Fi...")
    
    # We are replacing the custom font drawing with scroll_text,
    # which we know works on your device.
    scroll.scroll_text("Connecting...", BRIGHTNESS, SCROLL_SPEED)
    
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    print(f"Attempting to connect to: {WIFI_SSID}")
    
    # Wait for connection - let's give it 10 seconds
    max_wait = 10
    while max_wait > 0:
        if wlan.isconnected():
            break # Success!
            
        max_wait -= 1
        status = wlan.status()
        print(f"Waiting for connection... Status: {status}")
        
        # Show a simple scrolling "Waiting..."
        # This will now show the status code on the screen!
        scroll.scroll_text(f"Status {status}", BRIGHTNESS, SCROLL_SPEED)
        
        time.sleep(1) # Wait 1s

    if wlan.isconnected():
        print("--- Wi-Fi Connected! ---")
        print(f"IP: {wlan.ifconfig()[0]}")
        
        # Show "Connected" on success
        scroll.scroll_text("Connected!", BRIGHTNESS, SCROLL_SPEED)
        time.sleep(1) # Give time to read message
        return True
        
    else:
        # --- THIS IS THE CRITICAL FIX ---
        # We no longer loop forever.
        # We just show the error, print, and return False.
        final_status = wlan.status()
        print("--- Wi-Fi Connection FAILED ---")
        print(f"Final connection status: {final_status}")
        
        # Give user feedback based on the status code
        if final_status == 2:
            print("ERROR: Wrong Password.")
            scroll.scroll_text("Wrong Pass", BRIGHTNESS, SCROLL_SPEED)
        elif final_status == 3:
            print("ERROR: Access Point (SSID) not found.")
            scroll.scroll_text("No SSID", BRIGHTNESS, SCROLL_SPEED)
        elif final_status < 0:
            print(f"ERROR: Connection failed with code {final_status}.")
            scroll.scroll_text(f"Fail {final_status}", BRIGHTNESS, SCROLL_SPEED)
        else:
            print("ERROR: Unknown failure.")
            scroll.scroll_text("Failed!", BRIGHTNESS, SCROLL_SPEED)
        
        print("Connection failed. Will retry on button press.")
        return False # <-- This is the fix!


def call_url(url):
    """
    Calls a URL. This function is now 'silent' on the display.
    It prints to console only.
    """
    
    # --- NEW SAFETY CHECK ---
    # If Wi-Fi is down, try to reconnect ONCE.
    if not wlan.isconnected():
        print("Wi-Fi is down. Attempting to reconnect...")
        scroll.scroll_text("Reconnecting...", BRIGHTNESS, SCROLL_SPEED)
        
        # Try to reconnect.
        if not connect_wifi(): 
            # If connect_wifi() returned False, give up for this press.
            print("Reconnect failed. Skipping URL call.")
            # The connect_wifi() function already showed the error.
            return # Exit the function
    # --- END SAFETY CHECK ---
    
    
    print(f"Calling URL: {url}")
    
    try:
        # The URL request!
        # Check if we need to fix http/https
        if "https" in url:
             # Check if the 'ussl' module exists before trying to use it
             try:
                 import ussl
             except ImportError:
                print("Replacing https with http to avoid 'ussl' error")
                url = url.replace("https://", "http://")
            
        response = urequests.get(url)
        print(f"Response: {response.status_code}")
        response.close()
        print("URL call successful.")
        
    except Exception as e:
        print(f"URL Failed: {e}")
        
        # This is where the 'ussl' error would be caught.
        # Let's check for it and try to be helpful.
        if "ussl" in str(e):
            print("---")
            print("ERROR: 'ussl' module not found.")
            print("This firmware doesn't support 'https' URLs.")
            print("Trying again with 'http'...")
            # We will now force an http call
            try:
                url = url.replace("https://", "http://")
                response = urequests.get(url)
                print(f"Response (http retry): {response.status_code}")
                response.close()
                print("URL call successful (http retry).")
            except Exception as e2:
                print(f"HTTP retry also failed: {e2}")
                scroll.scroll_text("SSL Error", BRIGHTNESS, SCROLL_SPEED)
        else:
            print(f"Unknown error calling URL: {e}")
            scroll.scroll_text("URL Error", BRIGHTNESS, SCROLL_SPEED)


# --- 4. MAIN PROGRAM ---

# First, try to connect to Wi-Fi.
# This function will no longer crash the Pico if it fails.
connect_wifi()

print("--- System Ready. Waiting for button presses. ---")
# Even if Wi-Fi failed, we safely enter the main loop.

while True:
    if scroll.is_pressed(PicoScroll.BUTTON_A):
        # Home: Full-width bar (17 chars)
        scroll.scroll_text("= = =", BRIGHTNESS, 11) # Quick animation
        call_url(URL_HOME)
        scroll.scroll_text("I'm Home", BRIGHTNESS, SCROLL_SPEED)
        
    elif scroll.is_pressed(PicoScroll.BUTTON_B):
        # TV: 3/4-width bar (13 chars)
        scroll.scroll_text("= = =", BRIGHTNESS, 11) # Quick animation
        call_url(URL_TV)
        scroll.scroll_text("TV Time", BRIGHTNESS, SCROLL_SPEED)

    elif scroll.is_pressed(PicoScroll.BUTTON_X):
        # Movie: 1/2-width bar (8 chars)
        scroll.scroll_text("= = =", BRIGHTNESS, 11) # Quick animation
        call_url(URL_MOVIE)
        scroll.scroll_text("Movie Time", BRIGHTNESS, SCROLL_SPEED)

    elif scroll.is_pressed(PicoScroll.BUTTON_Y):
        # Night: 1/4-width bar (4 chars)
        scroll.scroll_text(" - - -", BRIGHTNESS, 11) # Quick animation
        call_url(URL_NIGHT)
        scroll.scroll_text("Good Night", BRIGHTNESS, SCROLL_SPEED)
        
    # Wait a bit to prevent multiple button reads
    time.sleep(0.1)