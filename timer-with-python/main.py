import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class UpdateTimer:
    def __init__(self, parent, int_timer, label):
        self.parent = parent
        self.int_timer = int_timer
        self.label = label
        self.label['text'] = str(int_timer)



    def update(self):
        self.label['text'] = str(self.int_timer)
        self.i = self.int_timer
        self.timer()



    def run_timer(self):
        if self.i > 0:
            self.i -= 1



    def timer(self):
        self.run_timer()
        if self.i > 0:
            self.label.after(1000, self.timer)
            self.label['text'] = str(self.i)
        else:
            self.label['text'] = f'Time up!'



    def cmd_start(self):
        self.update()
        pass


    def cmd_stop(self):
        self.i = 0



    def cmd_set(self):
        answer = simpledialog.askinteger("Input", "Set initial timer (seconds) ", parent=self.parent, minvalue=0, maxvalue=100)

        if answer:
            self.int_timer = int(answer)
            self.label['text'] = str(self.int_timer)
        else:
            messagebox.showerror("Error", "Please enter a value between 1 and 100.")



def main():
    int_timer = 0

    window = tk.Tk()
    window.title("Countdown Timer")

    window.rowconfigure([0, 1], minsize=70, weight =1)
    window.columnconfigure([0, 1, 2] , minsize=100, weight= 1)


    lbl_value = tk.Label(master=window, text="0", font=("Arial", 30))
    lbl_value.grid(row=0, column=0, columnspan=3)


    ut = UpdateTimer(window, int_timer, lbl_value)

    btn_start = tk.Button(master=window, text="Start", command=ut.cmd_start, font=("Arial", 14))
    btn_start.grid(row =1 , column = 0, sticky="nsew")

    btn_stop = tk.Button(master=window, text="Stop",
    command=ut.cmd_stop, font=("Arial", 14))
    btn_stop.grid(row =1 , column = 2, sticky="nsew")



    btn_set = tk.Button(master=window, text="Set",
    command=ut.cmd_set, font=("Arial", 14))
    btn_set.grid(row=1, column=2, sticky="nsew")


    window.mainloop()




if __name__ == "__main__":
    main()

