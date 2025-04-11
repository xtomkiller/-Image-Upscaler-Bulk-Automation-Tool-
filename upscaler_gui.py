import os
import time
import threading
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

image_folder = ""
selected_ratio = None

def choose_folder():
    global image_folder
    image_folder = filedialog.askdirectory()
    folder_label.config(text=f"📁 Selected: {image_folder}")

def run_automation(mode, ratio_value):
    if not image_folder:
        print("❌ Please select an image folder first!")
        return

    files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    if not files:
        print("❌ No image files found in the folder.")
        return

    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("prefs", {"download.prompt_for_download": False})

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://imgupscaler.com/")
    time.sleep(5)

    driver.execute_script("window.open('https://imgupscaler.com/', '_blank');")
    extra_tab = driver.window_handles[-1]

    i = 0
    while i < len(files):
        tab_files = files[i:i + 10]
        tabs = []

        for index, f in enumerate(tab_files):
            driver.execute_script("window.open('https://imgupscaler.com/', '_blank');")
            new_tab = driver.window_handles[-1]
            tabs.append(new_tab)
            driver.switch_to.window(new_tab)
            print(f"[Tab {index+1}] Uploading: {f}")

            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
                ).send_keys(os.path.join(image_folder, f))
                print(f"[Tab {index+1}] ✅ File uploaded.")
            except Exception as e:
                print(f"[Tab {index+1}] ❌ File upload failed: {e}")
                driver.save_screenshot(f"upload_error_tab{index+1}.png")
                continue

            # Ratio selection
            try:
                if ratio_value == "2":
                    driver.find_element(By.XPATH, "//input[@value='2']").click()
                elif ratio_value == "4":
                    driver.find_element(By.XPATH, "//input[@value='4']").click()
            except:
                print(f"[Tab {index+1}] ⚠️ Ratio selection skipped.")

            # Start button
            try:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start')]"))
                ).click()
                print(f"[Tab {index+1}] ▶️ Start clicked.")
            except:
                print(f"[Tab {index+1}] ❌ Could not click Start.")
                driver.save_screenshot(f"start_error_tab{index+1}.png")

        print("⏳ Waiting 40 seconds for processing...")
        time.sleep(40)

        for index, tab in enumerate(tabs):
            driver.switch_to.window(tab)
            print(f"[Tab {index+1}] 🔄 Checking for Download button...")

            try:
                download_btn = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Download']]"))
                )
                download_btn.click()
                print(f"[Tab {index+1}] ✅ Download clicked.")
            except Exception as e:
                print(f"[Tab {index+1}] ❌ Download failed: {e}")
                driver.save_screenshot(f"download_error_tab{index+1}.png")

        print("⏳ Waiting 120 seconds after downloads...")
        time.sleep(120)

        for tab in tabs:
            driver.switch_to.window(tab)
            driver.close()

        driver.switch_to.window(extra_tab)
        i += 10

def start_process(mode):
    threading.Thread(target=lambda: run_automation(mode, selected_ratio.get()), daemon=True).start()

# GUI
root = tk.Tk()
root.title("Image Upscaler Bot")
root.geometry("400x300")

tk.Button(root, text="📁 Choose Image Folder", command=choose_folder).pack(pady=10)
folder_label = tk.Label(root, text="No folder selected")
folder_label.pack()

selected_ratio = tk.StringVar(value="2")
tk.Label(root, text="Select Ratio:").pack()
tk.Radiobutton(root, text="2x", variable=selected_ratio, value="2").pack()
tk.Radiobutton(root, text="4x", variable=selected_ratio, value="4").pack()

tk.Button(root, text="Fast Mode (Bulk)", command=lambda: start_process("fast")).pack(pady=20)

root.mainloop()
