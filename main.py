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
    global filename, colors
    filetypes = (
        ("Image files", "*.jpg *.jpeg *.png"),
        ("All files", "*.*")
    )
    filename=fd.askopenfilename(title='Select IMG', initialdir='/', filetypes=filetypes)
    # print(filename)
    place_image(filename)
    #read colors from that image
    dominants.image_path=filename
    dominants.dominant_colors(10)
    #print out result

    for index, item in enumerate(dominants.colors):

        print(f"Top {index+1} with proportion: {round((dominants.proportions[index] * 100),2)}% \ncolor as RGB: {item}\nas #HEX: {_from_rgb(item)}")
        colors[index].config(text=_from_rgb(item),bg=_from_rgb(item), fg='black')

def place_image(path):
    global picture,start_picture_img
    picture = Image.open(path)
    picture = picture.resize((300, 300))
    picture = ImageTk.PhotoImage(picture)
    start_picture_img.config(image=picture)

window=tk.Tk()
window.title('Image to Color Palette')
window.geometry("500x600")
window.resizable(True, True)
window.config(bg='#F3F0CA')
label=tk.Label(text='THIS SIMPLE APP HELPS YOU TO EXTRACT \n TOP 10 COLORS '
                    'FROM ANY PICTURE',font=('Courier',10,'bold'))
label.grid(row=0,column=0,pady=20,padx=100)

select_button=tk.Button(window, text='Select Image',command=select)
select_button.grid(row=1,column=0,pady=20)

start_picture=Image.open('start_picture.jpg')
start_picture=start_picture.resize((300,300))
start_picture=ImageTk.PhotoImage(start_picture)

start_picture_img=tk.Label(image=start_picture)
start_picture_img.grid(row=2,column=0)

frame=tk.Frame(window,width=300,height=50,bg='grey')
frame.grid(row=3,column=0,pady=20)

colors=[]
for _ in range(10):
    label_=tk.Label(frame,text="Color",bg='#F3F0CA',fg='#F3F0CA')
    label_.grid(row=0,column=_, padx=0)
    colors.append(label_)

window.mainloop()