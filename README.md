# qr-link

A small desktop app that turns any link into a **QR code image**. Paste a URL, choose where to save it,
and the PNG is ready — the folder opens automatically.

## Usage

### Windows (no installation)
Download `qr_link.exe` from the [Releases](https://github.com/CestnyTR/qr-link/releases/latest) page and run it.

### With Python (Windows / macOS / Linux)
```bash
pip install "qrcode[pil]"
python qr_link.py
```
Tkinter ships with Python. On Linux, if it's missing: `sudo apt install python3-tk`

## How it works
1. Enter a URL.
2. Click **Generate QR Code** and pick a file name (`qr_code.png` by default).
3. The QR code is saved as a PNG and the folder opens.

## Build the executable yourself
```bash
pip install pyinstaller "qrcode[pil]"
pyinstaller --onefile --windowed qr_link.py
```
The output is `dist/qr_link.exe`.

## Tech stack
Python 3 · Tkinter · [qrcode](https://pypi.org/project/qrcode/)
