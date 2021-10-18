def download_link_script():

    from configparser import ConfigParser
    from tkinter import PhotoImage

    # yt-dlb default download link
    # this MUST be a direct link to 'yt-dlp.exe'
    yt_dlp_download_link = 'https://github.com/yt-dlp/yt-dlp/releases/download/2021.10.10/yt-dlp.exe'

    # FFMPEG default download link
    # this link needs to be a '.7z' archive with 'ffmpeg.exe' inside of it
    ffmpeg_download_link = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z'

    download_links_config = 'Runtime/downloadlinks.ini'  # Creates (if doesn't exist) and defines location of config.ini
    config = ConfigParser()
    config.read(download_links_config)

    # creates each section/value upon first launch of the program
    if not config.has_section('ffmpeg_link'):
        config.add_section('ffmpeg_link')
    if not config.has_option('ffmpeg_link', 'link'):
        config.set('ffmpeg_link', '# information', 'link needs to be a ".7z" archive with "ffmpeg.exe" inside of it')
        config.set('ffmpeg_link', 'link', ffmpeg_download_link)
    if not config.has_section('youtubedl_link'):
        config.add_section('youtubedl_link')
    if not config.has_option('youtubedl_link', 'link'):
        config.set('youtubedl_link', '# information', 'this MUST be a direct link to "yt-dlp.exe"')
        config.set('youtubedl_link', 'link', yt_dlp_download_link)
    try:
        # writes to the downloadlinks.ini file
        with open(download_links_config, 'w') as configfile:
            config.write(configfile)
    except:
        # Error window in the event that you could not create the downloadlinks.ini file
        from tkinter import Tk, Button, Label, PhotoImage
        main = Tk()
        main.title("Error!")
        error_window_icon = PhotoImage(file='Runtime/Images/Youtube-DL-Gui.png')
        main.iconphoto(False, error_window_icon)
        main.configure(background="#434547")
        window_height = 250
        window_width = 450
        screen_width = main.winfo_screenwidth()
        screen_height = main.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        main.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        label = Label(main, text='Unable to create "downloadlink.ini"\nPlease report this on the tracker'
                                    '\nhttps://github.com/jlw4049/Youtube-DL-GUI/issues\n\n\nThe '
                                    'auto downloader will not work \nwhen missing "downloadlink.ini"')
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        button = Button(main, text="OK", command=lambda: main.destroy())
        button.pack(side="bottom", fill="none", expand=True)
        main.mainloop()