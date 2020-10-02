# Imports--------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter import filedialog, StringVar
import subprocess
import tkinter as tk
import pathlib
import tkinter.scrolledtext as scrolledtextwidget
from TkinterDnD2 import *
from tkinter import messagebox
from tkinter import scrolledtext

# Main Gui & Windows --------------------------------------------------------

root = TkinterDnD.Tk()
root.title("Youtube-DL-Gui Beta v1.0")
# root.iconphoto(True, PhotoImage(file="Runtime/Images/topbar.png"))
root.configure(background="#434547")
window_height = 300
window_width = 801
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)
# root.grid_columnconfigure(3, weight=1)
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)
# root.grid_rowconfigure(3, weight=1)

# Bundled Apps ---------------------------------------------------------------

youtube_dl_cli = '"' + "Apps\youtube-dl\youtube-dl.exe" + '"'
ffmpeg_location = ' --ffmpeg-location "Apps/ffmpeg/ffmpeg.exe" '

# --------------------------------------------------------------- Bundled Apps

# Menu Items and Sub-Bars ---------------------------------------------------------------------------------------------
my_menu_bar = Menu(root, tearoff=0)
root.config(menu=my_menu_bar)

file_menu = Menu(my_menu_bar, tearoff=0, activebackground='dim grey')
my_menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Exit', command=root.quit)

options_menu = Menu(my_menu_bar, tearoff=0, activebackground='dim grey')
my_menu_bar.add_cascade(label='Options', menu=options_menu)

options_submenu = Menu(root, tearoff=0, activebackground='dim grey')
options_menu.add_cascade(label='Shell Options', menu=options_submenu)
shell_options = StringVar()
shell_options.set('Default')
options_submenu.add_radiobutton(label='Shell Closes Automatically', variable=shell_options, value="Default")
options_submenu.add_radiobutton(label='Shell Stays Open (Debug)', variable=shell_options, value="Debug")

tools_submenu = Menu(my_menu_bar, tearoff=0, activebackground='dim grey')
my_menu_bar.add_cascade(label='Tools', menu=tools_submenu)
tools_submenu.add_command(label="Open MediaInfo") #command=mediainfogui)

help_menu = Menu(my_menu_bar, tearoff=0, activebackground="dim grey")
my_menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About") #command=openaboutwindow)


# --------------------------------------------------------------------------------------------- Menu Items and Sub-Bars


def apply_link():
    global download_link
    print(text_area.get(1.0, END))
    download_link = text_area.get(1.0, END)
    text_area.delete(1.0, END)


# File Output ---------------------------------------------------------------------------------------------------------
def file_save():
    global VideoOutput
    VideoOutput = filedialog.askdirectory()
    if VideoOutput:
        print(VideoOutput)
        # output_entry.configure(state=NORMAL)  # Enable entry box for commands under
        # output_entry.delete(0, END)  # Remove current text in entry
        # output_entry.insert(0, VideoOutput)  # Insert the 'path'
        # output_entry.configure(state=DISABLED)  # Disables Entry Box

# --------------------------------------------------------------------------------------------------------- File Output

def start_job():
    command = '"' + youtube_dl_cli + ffmpeg_location + '--audio-quality 0 ' + '-x ' + '-o ' + '"' + VideoOutput + '/%(title)s.%(ext)s' \
              + '" ' + download_link + '"'
    print(command)
    subprocess.Popen('cmd /k' + command)



text_area_label = Label(text='Paste Link:', font=("Times New Roman", 12))
text_area_label.grid(row=0, column=0, columnspan=1, pady=(15,1), padx=10, sticky=W)
text_area = scrolledtext.ScrolledText(root, wrap=WORD, width=69, height=1, font=("Times New Roman", 14))
text_area.grid(row=1, column=0, columnspan=3, pady=(1,5), padx=10)
apply_btn = Button(root, text="Add Link", command=apply_link)
apply_btn.grid(row=2, column=2, columnspan=1, padx=5, pady=5, sticky=N + S + E + W)

save_btn = Button(root, text="Save Location", command=file_save)
save_btn.grid()

start_job_btn = Button(root, text="Start Job", command=start_job)
start_job_btn.grid()


# End Loop ------------------------------------------------------------------------------------------------------------
root.mainloop()
