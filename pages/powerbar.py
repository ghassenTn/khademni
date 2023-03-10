import tkinter as tk

class PowerBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.value = 0
        self.bar = tk.Canvas(self, width=200, height=20, bg='WHITE')
        self.bar.pack(side=tk.LEFT, padx=5)
        self.slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL,
                               command=self.update_value)
        self.slider.pack(side=tk.LEFT, padx=5)
    
    def update_value(self, value):
        self.value = int(value)
        self.bar.delete("all")
        self.bar.create_rectangle(0, 0, self.value*2, 20, fill='green')
        if self.slider.from_>50 :
             self.bar.create_rectangle(0, 0, self.value*2, 20, fill='red')
        
# Example usage
root = tk.Tk()
power_bar = PowerBar(root)
power_bar.place(x=10,y=20)
root.mainloop()
