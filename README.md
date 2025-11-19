# Pico W: The Physical Button for Your Alexa Routines

Have you ever wished you had a single, satisfying physical button to trigger your smart home routines—not just a voice command? I did. I wanted one button for "Movie Night," one for "Good Night," and so on, without having to yell at Alexa.

This project uses a **Raspberry Pi Pico W** and a beautiful **Pimoroni Pico Scroll Pack** to turn that wish into a reality. It's a simple, **four-button remote** that connects to your Wi-Fi and fires off pre-set **Alexa routines** with a single press by using webhooks.

![image](https://github.com/jegamboafuentes/Pico-W-Alexa-Routine-Trigger/blob/main/assets/Images/alexaremotedemo.gif) 

---

## ✨ Features: More Than Just Buttons

-   **Your 4-Button Smart Remote:** Each of the four buttons (A, B, X, Y) is programmed to trigger a different, unique smart home action, giving you instant physical control.
    
-   **Alexa Routines Made Physical:** The **Pico W** sends a web request (a simple URL call) that **Alexa** can recognize via services like `virtualsmarthome.xyz` or **IFTTT**. This lets you connect a physical button press directly to any Alexa Routine you create.
    
-   **MicroPython & Wi-Fi Connected:** It runs on **MicroPython** and connects reliably to your **2.4GHz** network, giving you a full IoT remote control.
    
-   **Visual Feedback on the Scroll Pack:** The Pimoroni Pico Scroll display provides live status updates, showing messages like "Connecting to Wi-Fi..." and confirming which routine was triggered (e.g., "TV Time").
    
-   **Safety First Boot:** Includes a built-in **5-second delay** on startup. This gives you plenty of time to interrupt the script in Thonny, avoiding that annoying "USB device not recognized" error.
    
![image](https://github.com/jegamboafuentes/Pico-W-Alexa-Routine-Trigger/blob/main/assets/Images/WhatsApp%20Image%202025-11-18%20at%2020.03.58_3144cb89.jpg) 
---

## Hardware You'll Need

This is a clean, modular build. The Scroll Pack sits neatly right on top of the Pico W's header pins.

-   **[Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico-w/)** (Must be the "W" model for Wi-Fi!)
    
-   **[Pimoroni Pico Scroll Pack](https://shop.pimoroni.com/products/pico-scroll-pack)**
    
-   A Micro-USB cable
    
![image](https://github.com/jegamboafuentes/Pico-W-Alexa-Routine-Trigger/blob/main/assets/Images/WhatsApp%20Image%202025-11-18%20at%2020.03.52_51d8a99e.jpg) 
---

## ⚙️ Software & Setup

To get those cool scrolling messages and button inputs working, you need the custom Pimoroni MicroPython firmware.

### 1\. Install Pimoroni Firmware

1.  Download the latest "Pimoroni-flavored" MicroPython `.uf2` file. You can find it on this repo or their GitHub releases page: **[https://github.com/pimoroni/pimoroni-pico/releases](https://github.com/pimoroni/pimoroni-pico/releases)**
    
2.  Hold the **BOOTSEL** button on your Pico W while plugging it into your computer.
    
3.  Drag and drop the downloaded `.uf2` file onto the `RPI-RP2` drive that appears. The Pico will reboot and be ready to go.
    

### 2\. Install Thonny

1.  Download and install **[Thonny IDE](https://thonny.org/)**. (It's the easiest tool for working with MicroPython.)
    
2.  Open Thonny and connect to your Pico (it should be listed in the bottom-right).
    

### 3\. Upload Project Files

1.  Download the `main.py` and `urequests.py` files from this repository.
    
2.  In Thonny, open each file and go to **File > Save As...**
    
3.  Choose **"Raspberry Pi Pico"** and save them with their original names (`main.py` and `urequests.py`).
    

---

## 🚀 How to Connect with Alexa

The magic happens when the **Pico W** calls a unique URL (a **webhook**) that you have configured to start an **Alexa Routine**.

Open `main.py` in Thonny and find the **`# --- 1. SETTINGS ---`** section at the top.

### 1\. Configure Wi-Fi

Change these values to match your home Wi-Fi network. **Note: The Pico W only works on 2.4GHz networks.**

Python

```
WIFI_SSID = "Your_2.4GHz_Network_Name"
WIFI_PASSWORD = "Your_Wi-Fi_Password"
```

### 2\. Add Your Webhook URLs

You need to get a unique URL for each button. I used `virtualsmarthome.xyz` for this project, which easily turns a simple URL into an Alexa trigger.

Replace the example URLs in `main.py` with your real ones:

Python

```
# These are the unique URLs that trigger your Alexa Routines
ROUTINE_A_URL = "https://your.unique.webhook.com/trigger/buttonA"
ROUTINE_B_URL = "https://your.unique.webhook.com/trigger/buttonB"
# ...and so on for X and Y
```

### 3\. Create the Alexa Routine

Once your Pico is programmed, you go into your **Alexa app** and create a new Routine for each button:

1.  **Select 'When this happens'** and choose the option to trigger by **Webhook** (or the name of the service you used, like `Virtual Smart Home`).
    
2.  **Select 'Add action'** and choose what you want Alexa to do (e.g., set volume, turn off lights, start a playlist, etc.).
    
3.  When you press the button on the Pico, the device sends the URL, the webhook service catches it, and **Alexa** runs your Routine!

![image](https://github.com/jegamboafuentes/Pico-W-Alexa-Routine-Trigger/blob/main/assets/Images/WhatsApp%20Image%202025-11-18%20at%2020.04.03_a557dbdb.jpg) 
