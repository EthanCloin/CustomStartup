"""
this module is responsible for providing the interface for a user
to interact with their StartupProfile. Provides functions which:

create a new StartupRoutine
edit an existing StartupRoutine
delete an existing StartupRoutine
execute a StartupRoutine
"""

import tkinter as tk
from openers.startup import WORK_BASICS

# Constants
BODY_FONT = ("Arial", 18)
TITLE_FONT = ("Arial", 32)


def main():
    root = tk.Tk()
    win_width = root.winfo_screenwidth() // 2
    win_height = root.winfo_screenheight() // 2

    root.geometry(f"{win_width}x{win_height}+{win_width // 2}+{win_height // 2}")
    # {win_width - 150}+{win_height}
    # print(
    #     WINDOW_SIZE
    #     + "+{}+{}".format(
    #         root.winfo_screenwidth() // 2 - 150, root.winfo_screenheight() // 2 - 75
    #     )
    # )

    frame1 = RoutineListView(root)
    frame1.pack(side="left")

    frame2 = RoutineDetailView(root)
    frame2.pack(side="right")

    root.mainloop()


class RoutineListView(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

        title = tk.Label(self, text="Your Routines", font=TITLE_FONT)
        title.pack()

        inner_frame = tk.Frame(self, bg="blue")
        inner_frame.pack(expand=True, fill="both")

        eg_routines = ["first routine", "second", "3rd routine"]

        for r in eg_routines:
            routine_btn = tk.Button(inner_frame, text=r, font=BODY_FONT)
            routine_btn.pack(side="top", anchor="nw", expand=True, fill="x")


class RoutineDetailView(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

        title = tk.Label(self, text="Routine Details", font=TITLE_FONT)
        title.pack()

        inner_frame = tk.Frame(self)
        inner_frame.pack()

        eg_routine = WORK_BASICS
        app_count = len(eg_routine.applications)
        site_count = len(eg_routine.websites)

        title_label = tk.Label(inner_frame, text=eg_routine.name, font=BODY_FONT)
        title_label.pack()

        app_label = tk.Label(inner_frame, text=f"Apps: {app_count}", font=BODY_FONT)
        app_label.pack(side="left")

        site_label = tk.Label(inner_frame, text=f"Sites: {site_count}", font=BODY_FONT)
        site_label.pack(side="right")


if __name__ == "__main__":
    main()
