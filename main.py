import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image,ImageTk
from read_colors import Read_Colors

dominants=Read_Colors()
filename=None
picture=None
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def select():
    global filename
    filetypes = (
        ("Image files", "*.jpg *.jpeg *.png"),
        ("All files", "*.*")
    )
    filename=fd.askopenfilename(title='Select IMG', initialdir='/', filetypes=filetypes)
    # print(filename)
    place_image(filename)
    dominants.dominant_colors(10)
    # bg = "rgb(0, 255, 0)",
    print(dominants.colors)


def place_image(path):
    global picture,start_picture_img
    picture = Image.open(path)
    picture = picture.resize((300, 300))
    picture = ImageTk.PhotoImage(picture)
    start_picture_img.config(image=picture)

# def dominant_colors(number_of_colors):
#


window=tk.Tk()
window.title('Image to Color Palette')
window.geometry("500x500")
window.resizable(False, False)

label=tk.Label(text='THIS SIMPLE APP HELPS YOU TO EXTRACT \n TOP 10 COLORS '
                    'FROM ANY PICTURE',font=('Courier',10,'bold'))
label.grid(row=0,column=0,pady=20,padx=100)

select_button=tk.Button(window, text='Select Image',command=select)
select_button.grid(row=1,column=0,pady=20)

# start_picture=tk.PhotoImage(file='start_picture.jpg')
# start_picture.

start_picture=Image.open('start_picture.jpg')
start_picture=start_picture.resize((300,300))
start_picture=ImageTk.PhotoImage(start_picture)


start_picture_img=tk.Label(image=start_picture)
start_picture_img.grid(row=2,column=0)


# top_1=tk.Label(text='Top 1',fg="white")
# top_1.grid(row=4,column=0)

window.mainloop()