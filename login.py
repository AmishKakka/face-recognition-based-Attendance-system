from dependencies import tk 
from dependencies import Image, ImageTk
from dependencies import comaptible_image_format

mainWin = tk.Tk()
s_height, s_width = mainWin.winfo_screenheight(), mainWin.winfo_screenwidth()
mainWin.geometry(str(s_width)+"x"+str(s_height))
mainWin.title('Attendance system')

# Getting the background image.
photo = comaptible_image_format(r'SE_project\dome.jpeg', (s_width, s_height))

# Displaying the background image.
canvas = tk.Canvas(mainWin, width=s_width, height=s_height)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=photo, anchor='nw')


# Functions to call respective files.
def RegisterPage():
    mainWin.destroy()
    import Registration_window

def AttendancePage():
    mainWin.destroy()
    import Attendance_window

def DeleteRecord():
    mainWin.destroy()
    import Delete_record


# Creating registration and attendance buttons.
new_user_icon = comaptible_image_format(r'SE_project\NewUser.jpeg', (50,50))
register_page = tk.Button(mainWin, 
                        text='New Registration',
                        font=('Helvetica 20 bold'),
                        image=new_user_icon,
                        compound='left',
                        relief='raised',
                    
                        command=RegisterPage)
register_page.place(x=70, y=400)

attendance_icon = comaptible_image_format(r'SE_project\take_attendance.jpeg', (50,50))
attendance_page = tk.Button(mainWin, 
                        text='Take Attendance',
                        font=('Helvetica 20 bold'),
                        image=attendance_icon,
                        compound='left',
                        relief='raised',
                        command=AttendancePage)
attendance_page.place(x=900, y=400)

delete_icon = comaptible_image_format(r'SE_project\delete_record.jpeg', (50,50))
delete_record = tk.Button(mainWin, 
                        text='Delete Record',
                        font=('Helvetica 20 bold'),
                        image=delete_icon,
                        compound='left',
                        relief='raised',
                        command=DeleteRecord)
delete_record.place(x=475, y=400)

mainWin.mainloop()    
