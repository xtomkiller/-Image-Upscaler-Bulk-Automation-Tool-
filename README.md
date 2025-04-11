#  Image Upscaler Bulk-Automation-Tool
 A fully automated Python tool that bulk uploads images to imgupscaler.com, upscales them using AI (2x or 4x), and downloads the enhanced results — all through a clean GUI. Perfect for designers, AI artists, and photographers needing quick batch enhancement.Anyone who needs to upscale multiple images efficiently, this tool saves hours of manual work.

# 🔧 Features

    ✅ Uploads multiple .png, .jpg, and .jpeg images
    ✅ Supports 2x and 4x upscale ratios
    ✅ Opens multiple tabs for parallel processing (10 at a time)
    ✅ Automatically downloads enhanced images
    ✅ Includes GUI (Graphical User Interface)
    ✅ Error handling with screenshots for debugging
    ✅ Optional delay between processing for performance and rate-limiting

#📦 Requirements

   Python 3.x
   Google Chrome installed
   ChromeDriver matching your Chrome version
   selenium library
   tkinter (included in standard Python on most platforms)



> ✅ This approach keeps your system clean, avoids `externally-managed-environment` errors, and follows best practices for Python development on Kali Linux.

---

Let me know if you also want me to prepare a `.sh` script to automate all of this setup in one command!

## 🚀 Installation

    sudo apt update
    sudo apt install python3-tk
    git clone https://github.com/xtomkiller/Image_Upscaler_Bulk_Automation-Tool
    cd Image_Upscaler_Bulk_Automation-Tool
    pip install -r requirements.txt

## 🚀 How to Run

    python3 upscaler_gui.py
---

## ⚙️ Setup Instructions

To run this project safely on Kali Linux or any system with Python restrictions (PEP 668), follow these steps using a virtual environment.

### 🛠️ Step 1: Create a Virtual Environment

```bash
python3 -m venv .venv
```

> 💡 If you get an error like `No module named 'venv'`, run:
```bash
sudo apt install python3-venv
```

---

### 🚀 Step 2: Activate the Virtual Environment

```bash
source .venv/bin/activate
```

You should now see your terminal prompt change like this:
```bash
(.venv) hacker@kali:~/your-project-folder$
```

---

### 📦 Step 3: Install All Required Packages

```bash
pip install -r requirements.txt
```

This will install everything listed in `requirements.txt`.

---

### ▶️ Step 4: Run the Tool

```bash
python3 main.py
```

---

### ❌ Step 5: Exit the Virtual Environment

When you're done:

```bash
deactivate
```

---

## 💻 GUI Instructions

    Click 📁 Choose Image Folder to select your image folder.
    Select 2x or 4x as upscaling ratio.
    Click Fast Mode (Bulk) to begin automated uploading and downloading.
    The script processes 10 images at a time, opens new browser tabs, and downloads results after AI processing is complete.

# 📁 Folder Structure
"""
image-upscaler-bot/
│
├── upscaler_gui.py         # Main script with GUI and automation
├── README.md               # Project documentation
├── upload_error_tabX.png   # (Optional) Error screenshots for upload issues
├── download_error_tabX.png # (Optional) Error screenshots for download issues """

## 📷 Screenshots


## 📌 Notes

    The script uses imgupscaler.com which offers free and fast AI image upscaling.

    Make sure Chrome and ChromeDriver are the same version.

    Processed files are downloaded to the browser's default Downloads folder.

    Tab-wise screenshot handling helps in identifying failed tabs.
