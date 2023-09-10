import datetime
import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
from tkinter import ttk
import tkintermapview


def update_duration(event):
    """ updates the duration after finding the duration """
    duration = vid_player.video_info()["duration"]
    end_time["text"] = str(datetime.timedelta(seconds=duration))
    progress_slider["to"] = duration

def update_scale(event):
    progress_value.set(vid_player.current_duration())

def load_video():
    file_path = filedialog.askopenfilename()

    if file_path:
        vid_player.load(file_path)

        progress_slider.config(to=0, from_=0)
        play_pause_btn["text"] = "Play"
        progress_value.set(0)


def seek(value):
    vid_player.seek(int(value))


def skip(value: int):
    vid_player.seek(int(progress_slider.get())+value)
    progress_value.set(progress_slider.get() + value)


def play_pause():
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"

    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"


def video_ended(event):
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    progress_slider.set(0)

filename = "file.txt"
data = []
with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # удаление лишних пробелов и символов переноса строки
            if line:  # проверка, что строка не пустая
                name, x, y = line.split(',')  # разделение строки по запятым
                data.append([name, float(x), float(y)])  # добавление данных в двумерный массив
result = data
num_rows = len(result)

root = tk.Tk()
root.title("File_creat_zero")
root.geometry('950x720')
root.columnconfigure(0,weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=1)

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")
# s

but_win = ttk.Label(root)#######################3

vid_player = TkinterVideo(scaled=1, master=root,borderwidth = 1, relief="solid")
vid_player.set_size((385,615))
vid_player.grid(column = 0, row  = 0, columnspan = 2, sticky="NSEW", padx = 7,pady = 2)



load_btn = ttk.Button(root, text="Load",style="Accent.TButton", command=load_video)
load_btn.grid(column = 0, row  = 1, columnspan = 2,padx = 5,sticky="NSEW")

play_pause_btn = ttk.Button(root, text="Play",style="Accent.TButton", command=play_pause)
play_pause_btn.grid(column = 0, row  = 2, columnspan = 2,padx = 5,pady = 5,sticky="NSEW")

skip_plus_5sec = ttk.Button(root, text="Skip -5 sec",style="Accent.TButton", command=lambda: skip(-5))
skip_plus_5sec.grid(column = 0, row  = 3, columnspan = 2,padx = 5,pady = 5,sticky="NSEW")


progress_value = tk.IntVar(root)

progress_slider = tk.Scale(root, variable=progress_value, from_=0, to=0, orient="horizontal", command=seek)

progress_slider.grid(column = 0, row  = 4, columnspan = 2,padx = 5,pady = 5,sticky="NSEW")


vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended )

end_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
end_time.grid()

skip_plus_5sec = ttk.Button(root, text="Skip +5 sec",style="Accent.TButton", command=lambda: skip(5))
skip_plus_5sec.grid(column = 0, row  = 5, columnspan = 2,padx = 5,pady = 5,sticky="NSEW")


vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended )

# e
but_win.grid(column=0, row=0, columnspan = 2 ,ipadx=10, ipady=10, sticky="NSEW")


map_GPS = ttk.Label(root, text="                     ", borderwidth = 1, relief="solid")
map_widget = tkintermapview.TkinterMapView(map_GPS, width=600, height=720, corner_radius=0)
map_widget.set_address("59.971636, 30.386398")
map_widget.set_zoom(18)
map_widget.grid()
map_GPS.grid(column = 2, row = 0, rowspan = 7,padx = 5,pady = 5,sticky="NSEW")



for i in range(0, num_rows):
  name1 = data[i][0]
  x1 = data[i][1]
  y1 = data[i][2]

  if name1 == "pit":
    newmarker = map_widget.set_marker(x1, y1, text = "Яма")

  if name1 == "crack":
    newmarker = map_widget.set_marker(x1, y1, text = "Трещина")

  if name1 == "fill":
    newmarker = map_widget.set_marker(x1, y1, text = "Заплатка")


root.mainloop()