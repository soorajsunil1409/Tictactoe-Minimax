from customtkinter import *
import customtkinter

class Board(CTk):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height

        self.geometry(f"{self.width}x{self.height}")
        customtkinter.set_appearance_mode("light")

        self.initialize_buttons()

    
    def initialize_buttons(self):
        self.button_frame = CTkFrame(self)
        self.button_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.buttons = [CTkButton(self.button_frame, width=self.width//3, height=self.height//3, text="X", text_color="black", bg_color="black", font=("Helvetica", 30)) for i in range(9)]

        for i, btn in enumerate(self.buttons):
            idx, idy = i // 3, i % 3
            btn.place(x=idx*self.width//3, y=idy*self.height//3)



if __name__ == "__main__":
    board = Board(600, 600)
    board.mainloop()