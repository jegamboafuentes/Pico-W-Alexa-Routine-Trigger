# Pico W Alexa Routine Trigger

A MicroPython project that turns a Raspberry Pi Pico W and a Pimoroni Pico Scroll Pack into a physical, Wi-Fi connected remote. Pressing buttons (A, B, X, Y) triggers pre-set Alexa routines by calling their unique URLs.



---

## ✨ Features

* **4-Button Remote:** Triggers four different smart home actions.
* **Wi-Fi Connected:** Connects to your 2.4GHz Wi-Fi network.
* **Visual Feedback:** Uses the Pico Scroll display to show status (e.g., "Connecting...", "TV Time").
* **Alexa/IFTTT Ready:** Calls any webhook or URL, perfect for Alexa routines (via services like `virtualsmarthome.xyz`) or IFTTT.
* **Safe Boot:** Includes a 5-second delay on startup, giving you time to interrupt the script in Thonny and preventing the "USB device not recognized" error.

---

## Hardware Required

* [**Raspberry Pi Pico W**](https://www.raspberrypi.com/products/raspberry-pi-pico-w/)
* [**Pimoroni Pico Scroll Pack**](https://shop.pimoroni.com/products/pico-scroll-pack)
* A Micro-USB cable

---

## ⚙️ Software & Setup

This project requires a specific MicroPython firmware from Pimoroni to work, as it includes the necessary `picoscroll` libraries.

### 1. Install Pimoroni Firmware

1.  Download the latest "Pimoroni-flavored" MicroPython `.uf2` file. You can find it on their GitHub releases page:
    **[https://github.com/pimoroni/pimoroni-pico/releases](https://github.com/pimoroni/pimoroni-pico/releases)**
2.  Hold the **BOOTSEL** button on your Pico W while plugging it into your computer.
3.  Drag and drop the downloaded `.uf2` file onto the `RPI-RP2` drive that appears. Your Pico will reboot.

### 2. Install Thonny

1.  Download and install [**Thonny IDE**](https://thonny.org/).
2.  Open Thonny and connect to your Pico (it should be listed in the bottom-right).

### 3. Upload Project Files

1.  Download the `main.py` and `urequests.py` files from this repository.
2.  In Thonny, open each file and go to **File > Save As...**
3.  Choose **"Raspberry Pi Pico"** and save them with their original names (`main.py` and `urequests.py`).

---

## 🚀 How to Use

The only file you need to edit is `main.py`.

Open `main.py` in Thonny and find the **`# --- 1. SETTINGS ---`** section at the top.

### 1. Configure Wi-Fi

Change these values to match your home Wi-Fi network. **This must be a 2.4GHz network.**

```python
WIFI_SSID = "Your_2.4GHz_Network_Name"
WIFI_PASSWORD = "Your_Wi-Fi_Password"