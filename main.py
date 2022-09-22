import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import Calendar, DateEntry
# 
window_width = 400
window_height = 550
class_list = ('Select Class', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10', )
blood_group_list = ('Select Blood Group', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
sex_list = ('Select Gender', 'Male', 'Female', 'Others')
# 
root = tk.Tk()

root.title("Student Registration Form")

root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Register form Frame
register_frame = tk.Frame(root)
register_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
register_frame.columnconfigure(0, weight=1)
register_frame.columnconfigure(1, weight=3)
# Register Weiged
name_label = ttk.Label(register_frame, text="Student Name:")
father_name_label = ttk.Label(register_frame, text="Father's Name:")
mother_name_label = ttk.Label(register_frame, text="Mother's Name:")
phone_label = ttk.Label(register_frame, text="Phone Number:")
father_phone_label = ttk.Label(register_frame, text="Father's Phone Number:")
email_label = ttk.Label(register_frame, text="Email:")
gender_label = ttk.Label(register_frame, text="Gender:")
birth_date_label = ttk.Label(register_frame, text="Date of Birth:")
address_label = ttk.Label(register_frame, text="Address:")
blood_group_label = ttk.Label(register_frame, text="Blood Group:")
class_label = ttk.Label(register_frame, text="Class:")
photo_label = ttk.Label(register_frame, text="Photo:")
password_label = ttk.Label(register_frame, text="Password:")
# 
# all label grid
name_label.grid(row=0, column=0, sticky=tk.W)
father_name_label.grid(row=1, column=0, sticky=tk.W)
mother_name_label.grid(row=2, column=0, sticky=tk.W)
phone_label.grid(row=3, column=0, sticky=tk.W)
father_phone_label.grid(row=4, column=0, sticky=tk.W)
email_label.grid(row=5, column=0, sticky=tk.W)
gender_label.grid(row=6, column=0, sticky=tk.W)
birth_date_label.grid(row=7, column=0, sticky=tk.W)
address_label.grid(row=8, column=0, sticky=tk.W)
blood_group_label.grid(row=9, column=0, sticky=tk.W)
class_label.grid(row=10, column=0, sticky=tk.W)
photo_label.grid(row=11, column=0, sticky=tk.W)
password_label.grid(row=12, column=0, sticky=tk.W)
# 

name_input = ttk.Entry(register_frame)
father_name_input = ttk.Entry(register_frame)
mother_name_input = ttk.Entry(register_frame)
phone_input = ttk.Entry(register_frame)
father_phone_input = ttk.Entry(register_frame)
email_input = ttk.Entry(register_frame)

gender_input = ttk.Combobox(register_frame, state="readonly", values=sex_list)
gender_input.current(0)

birth_date_input = DateEntry(register_frame, width= 16, foreground= "white", bd=2, date_pattern='dd-mm-y')

address_input = ttk.Entry(register_frame)

blood_group_input = ttk.Combobox(register_frame, state="readonly", values=blood_group_list)
blood_group_input.current(0)

class_input = ttk.Combobox(register_frame, state="readonly", values=class_list)
class_input.current(0)

photo_input = ttk.Entry(register_frame)
password_input = ttk.Entry(register_frame, show="*")
# 
name_input.grid(row=0, column=1, padx=10, pady=5, ipady=2, sticky="we")
father_name_input.grid(row=1, column=1, padx=10, pady=5, ipady=2, sticky="we")
mother_name_input.grid(row=2, column=1, padx=10, pady=5, ipady=2, sticky="we")
phone_input.grid(row=3, column=1, padx=10, pady=5, ipady=2, sticky="we")
father_phone_input.grid(row=4, column=1, padx=10, pady=5, ipady=2, sticky="we")
email_input.grid(row=5, column=1, padx=10, pady=5, ipady=2, sticky="we")
gender_input.grid(row=6, column=1, padx=10, pady=5, ipady=2, sticky="we")
birth_date_input.grid(row=7, column=1, padx=10, pady=5, ipady=2, sticky="we")
address_input.grid(row=8, column=1, padx=10, pady=5, ipady=2, sticky="we")
blood_group_input.grid(row=9, column=1, padx=10, pady=5, ipady=2, sticky="we")
class_input.grid(row=10, column=1, padx=10, pady=5, ipady=2, sticky="we")
photo_input.grid(row=11, column=1, padx=10, pady=5, ipady=2, sticky="we")

password_input.grid(row=12, column=1, padx=10, pady=5, ipady=2, sticky="we")
# 
buttons_frame = tk.Frame(register_frame)
buttons_frame.grid(row=13, column=1, sticky="we")
buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=3)
# 
reset_btn = ttk.Button(buttons_frame, text="Reset")
register_btn = ttk.Button(buttons_frame, text="Register")
# 
reset_btn.grid(row=0, column=0, sticky="e", padx=0, pady=5)
register_btn.grid(row=0, column=1, sticky="e", padx=8, pady=5)

if __name__ == '__main__':
    root.mainloop()
