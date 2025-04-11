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

## 🚀 Installation

 git clone https://github.com/your-username/image-upscaler-bot.git
 cd image-upscaler-bot
 pip install selenium

## 🚀 How to Run

python3 upscaler_gui.py

## 💻 GUI Instructions

Click 📁 Choose Image Folder to select your image folder.
Select 2x or 4x as upscaling ratio.
Click Fast Mode (Bulk) to begin automated uploading and downloading.
The script processes 10 images at a time, opens new browser tabs, and downloads results after AI processing is complete.

# 📁 Folder Structure

image-upscaler-bot/
│
├── upscaler_gui.py         # Main script with GUI and automation
├── README.md               # Project documentation
├── upload_error_tabX.png   # (Optional) Error screenshots for upload issues
├── download_error_tabX.png # (Optional) Error screenshots for download issues

## 📷 Screenshots


## 📌 Notes

    The script uses imgupscaler.com which offers free and fast AI image upscaling.

    Make sure Chrome and ChromeDriver are the same version.

    Processed files are downloaded to the browser's default Downloads folder.

    Tab-wise screenshot handling helps in identifying failed tabs.
