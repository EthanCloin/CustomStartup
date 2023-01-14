"""
this module is responsible for providing the interface for a user
to interact with their StartupProfile. Provides functions which:

create a new StartupRoutine
edit an existing StartupRoutine
delete an existing StartupRoutine
execute a StartupRoutine
"""

from tkinter import Tk, ttk
from openers.startup import StartupRoutine, WORK_BASICS


def main():
    root = Tk()
    root.title("Self Starter")
    root.geometry("1200x800")
    ProfileFrame(root).pack(expand=True, fill="both")

    root.mainloop()


class ProfileFrame(ttk.Frame):
    def __init__(self, master: Tk, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        main_window_label_text = "Your Startup Routines"

        child_width = int(master.winfo_width() // (4 / 10))
        child_height = int(master.winfo_height() // (8 / 10))
        # print(f"{child_width}x{child_height}")

        # frame for available routines list
        RoutinesListView(self, width=500, height=child_height).pack(
            side="left", expand=True, fill="x"
        )
        RoutinesListView(self, width=child_width, height=child_height).pack(
            side="left", expand=True, fill="y"
        )
        # RoutinesListView(self, width=600, height=400).pack(
        #     side="left", expand=True, fill="both"
        # )

        # frame for detail view of selected routine


class RoutinesListView(ttk.Frame):

    routines_list = ["Routine 1", "routine 2", "routine three"]

    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        for routine in self.routines_list:
            ttk.Button(self, text=routine).pack(side="top", expand=True, fill="both")


if __name__ == "__main__":
    main()

# from tkinter import Tk
# from tkinter import ttk

# from openers.startup import StartupRoutine, WORK_BASICS


# class ProfileWindow(ttk.Frame):
#     window_title = "Self Starter"
#     content_title = "Your Startup Routine"

#     listed_routines: ttk.Frame
#     selected_routine_detail: ttk.Frame

#     # geometry
#     min_width, min_height = 600, 400

#     def __init__(self, master, *args, **kwargs):
#         super().__init__(master=master, *args, **kwargs)
#         self.listed_routines = RoutinesListView(master=self).pack(
#             side="left", expand=True
#         )
#         self.selected_routine_detail = RoutineDetailView(master=self).pack()


# class RoutinesListView(ttk.LabelFrame):
#     routines_list = ["Routine 1", "routine 2", "routine three"]

#     def __init__(self, master):
#         super().__init__(master=master)
#         for idx, routine in enumerate(self.routines_list):
#             routine_label = ttk.Label(self, text=routine)
#             routine_label.pack(side="top")


# # styler = ttk.Style()
# # styler.configure("RedFrame.TFrame", background="red")


# class RoutineDetailView(ttk.Frame):
#     details = WORK_BASICS

#     def __init__(self, master):
#         super().__init__(master=master)
#         name_group = ttk.Frame(self, style="RedFrame.TFrame").grid()
#         name_label = ttk.Label(name_group, text="Name: ").grid(row=0, column=0)
#         name_value = ttk.Entry(
#             name_group, text=self.details.name, state="DISABLED"
#         ).grid(row=0, column=1)

#         # info_group
#         # info_label = ttk.Label(self, text="Info: ").pack(side="top")
#         # apps_value = ttk.Label(
#         #     self, text=f"Apps: {len(self.details.applications)}"
#         # ).pack(side="right")
#         # sites_value = ttk.Label(self, text=f"Sites: {len(self.details.websites)}").pack(
#         #     side="right"
#         # )


# def testing():
#     import tkinter as tk

#     # Create Tkinter Object
#     root = Tk()

#     # Set Geometry
#     root.geometry("400x400")

#     # Frame 1
#     frame1 = tk.Frame(root, bg="black", width=500, height=300)
#     frame1.pack()

#     # Frame 2
#     frame2 = tk.Frame(frame1, bg="white", width=100, height=100)
#     frame2.pack(pady=20, padx=20)

#     # Execute Tkinter
#     root.mainloop()


# def main():
#     root = Tk()
#     root.geometry("600x400")

#     # make instance of profile window and call the pack method to layout within root
#     ProfileWindow(root).pack()
#     root.mainloop()


# if __name__ == "__main__":
#     main()
