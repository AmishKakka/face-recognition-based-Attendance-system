from dependencies import tk, comaptible_image_format
from database import record_exists, delete_record

delete_window = tk.Tk()
delete_window.title('Delecte records')
win_width, win_height = 800, 500
delete_window.geometry(str(win_width)+'x'+str(win_height))


# Display background image
bg = comaptible_image_format(r'SE_project\dome.jpeg', (win_width,win_height))
canvas = tk.Canvas(delete_window, width=win_width, height=win_height)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')

# Variables to get inputs from entry fields
name_var = tk.StringVar()
id_var = tk.StringVar()


def submit():
    name = name_var.get()
    id = id_var.get()
    print("Name: ", name)
    print("Id: ", id)

    delete_record(name, id)
        


# Making a details section for new user.
details_label = tk.Label(canvas,
                        text='Enter details',
                        font=('Helvetica 20 bold'),
                        foreground='blue')
details_label.place(x=int((win_width/2)-100), y=100)
name_field = tk.Label(canvas, text='Name', 
            font=('Helvetica 17'), 
            foreground='black', 
            background='white')
name_field.place(x=int((win_width/2))-150, y=200)
id_field = tk.Label(canvas, text='Id no.', 
            font=('Helvetica 17'), 
            foreground='black', 
            background='white')
id_field.place(x=int((win_width/2))-150, y=250)
input_name = tk.Entry(canvas, textvariable=name_var, width=20)
input_name.place(x=int((win_width/2))-50, y=205)
input_id = tk.Entry(canvas, textvariable=id_var, width=20)
input_id.place(x=int((win_width/2))-50, y=255)

submit_button = tk.Button(canvas,
                        text='Submit',
                        font=('Helvetica 18 bold'),
                        command=submit)
submit_button.place(x=int((win_width/2))-80, y=350)

delete_window.mainloop()