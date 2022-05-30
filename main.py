from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
from PIL import Image, ImageDraw, ImageFont

ws = Tk()
ws.title('Water Mark Image')
ws.geometry('400x200')


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpg', '*png'),('Image Files', '*png'),('Image Files', '*jpeg', '*png')])
    if file_path is not None:
        name = str(file_path.name)
        return name


def uploadFiles():
    pb1 = Progressbar(
        ws,
        orient=HORIZONTAL,
        length=300,
        mode='determinate'
    )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)


def watermark_file():
    # Opening Image & Creating New Text Layer
    image_file_name = open_file()
    print(image_file_name)
    img = Image.open(fr"{image_file_name}")
    img = img.convert("RGBA")
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

    # Creating Text
    text = watermark_text_entry.get()
    # print(type(text))
    font = ImageFont.truetype(r'/usr/share/fonts/truetype/Sarai/Sarai.ttf', 50)

    # Creating Draw Object
    d = ImageDraw.Draw(txt)

    # Positioning Text
    width, height = img.size
    textwidth, textheight = d.textsize(text, font)
    x = width / 2 - textwidth / 2
    y = height - textheight - 300

    # Applying Text
    d.text((x, y), f"{text}", fill=(255, 255, 255, 75), font=font)

    # Combining Original Image with Text and Saving
    watermarked = Image.alpha_composite(img, txt)
    new_name = new_file_entry.get()

    wm_pic = watermarked.save(rf'{new_name}.png')
    photo = PhotoImage(file=rf'{new_name}.png')

    canvas = Canvas(width=200, height=200, highlightthickness=0)
    lock_img = PhotoImage(file=photo)
    canvas.create_image(100, 100, image=lock_img)
    canvas = Canvas(width=200, height=200)
    canvas.grid(column=0, row=3, columnspan=2)

# Position image


adhar = Label(
    ws,
    text='Upload a JPG to watermark:'
)
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    ws,
    text='Choose File',
    command=lambda: open_file()
)
adharbtn.grid(row=0, column=1)


watermark_text_label = Label(text="Watermark Input Text")
watermark_text_label.grid(column=0, row=1, sticky="EW")

watermark_text_entry = Entry(width=35)
print(watermark_text_entry.get())
watermark_text_entry.grid(column=1, row=1, columnspan=1, sticky="EW")
watermark_text_entry.focus()


new_file_label = Label(text="Name of New file")
new_file_label.grid(column=0, row=2, sticky="EW")


new_file_entry = Entry(width=35)
print(new_file_entry.get())
new_file_entry.grid(column=1, row=2, columnspan=1, sticky="EW")
new_file_entry.focus()


# #add button
# add_button = Button(text="Add", width= 33)
# add_button.grid(column=1, row=4, columnspan = 2, sticky="EW")


upld = Button(ws,text='Watermark Files',command=lambda: [watermark_file()])
upld.grid(row=3, columnspan=3, pady=10)


ws.mainloop()