"""
Current working gui
"""
import tkinter
import tkinter.messagebox
import customtkinter
from inventory import *
import random

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 1080
    HEIGHT = 720
    TEXT = ("Roboto Medium", -16)

    def __init__(self):
        super().__init__()

        self.title("Car Application")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(6, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.title = customtkinter.CTkLabel(master=self.frame_left, text="Car Inventory", text_font=App.TEXT)
        self.title.grid(row=1, column=0, pady=10, padx=10)

        self.home_button = customtkinter.CTkButton(master=self.frame_left, text="App Info", text_font=App.TEXT, command=self.show_info_function)
        self.home_button.grid(row=2, column=0, pady=10, padx=20)
        
        self.add_car_button = customtkinter.CTkButton(master=self.frame_left, text="Add Car", text_font=App.TEXT, command=self.add_car_function)
        self.add_car_button.grid(row=3, column=0, pady=10, padx=20)

        self.search_button = customtkinter.CTkButton(master=self.frame_left, text="Search", text_font=App.TEXT, command=self.search_car_function)
        self.search_button.grid(row=4, column=0, pady=10, padx=20)

        self.color_mode_title = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:", text_font=App.TEXT)
        self.color_mode_title.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.color_mode_toggle = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        text_font=App.TEXT,
                                                        command=self.change_appearance_mode)
        self.color_mode_toggle.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============
        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_right ============
        # set default values
        self.color_mode_toggle.set("Dark")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


    def add_car_function(self):
        """ Creates frame for a form containing: Make, model, color, year."""
        def get_items():
            print(f'Car({ctk_items[1][0].get()}, {ctk_items[1][1].get()}, {ctk_items[1][2].get()}, {ctk_items[1][3].get()})')
            newCar = UsedCar(random.randint(1, 50), ctk_items[1][0].get(), ctk_items[1][1].get(), ctk_items[1][2].get(), ctk_items[1][3].get())
            newCar.save_to_file()
                
        ctk_items = [[],[]]
        items = ('Make', 'Model', 'Color', 'Year')
                
        self.add_car_frame = customtkinter.CTkFrame(master=self)                        # Embedded Frame == (master=self.frame_right) and column=0 
        self.add_car_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)       # Full Frame == (master=self) and column=1
            
        for element in range(4):
            ctk_items[0].append(customtkinter.CTkLabel(master=self.add_car_frame, text=f'{items[element]}:', text_font=App.TEXT))
            ctk_items[0][element].grid(row=element, column=0, padx=0, pady=15)
            
            ctk_items[1].append(customtkinter.CTkEntry(master=self.add_car_frame, text_font=App.TEXT))
            ctk_items[1][element].grid(row=element, column=1, padx=0, pady=15)  
                
        self.output_car_button = customtkinter.CTkButton(master=self.add_car_frame, text="Add Car", command=get_items)
        self.output_car_button.grid(row=4, column=1, pady=15, padx=0)

    def search_car_function(self):

        def find_car():
            newSearch = Inventory(ctk_items[1][0].get(), ctk_items[1][1].get())
            returnedSearch = newSearch.search()
            print(returnedSearch)
            # ctk_items[1][0].delete(0, customtkinter.END)
            ctk_items[1][1].delete(0, customtkinter.END)
            
        ctk_items = [[],[]]

        self.add_car_frame = customtkinter.CTkFrame(master=self)                        # Embedded Frame == (master=self.frame_right) and column=0 
        self.add_car_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)       # Full Frame == (master=self) and column=1

        ctk_items[1].append(customtkinter.CTkOptionMenu(master=self.add_car_frame, values=['make', 'model', 'color', 'year'], text_font=App.TEXT))
        ctk_items[1][0].grid(row=1, column=1, padx=0, pady=15)
            
        ctk_items[1].append(customtkinter.CTkEntry(master=self.add_car_frame, text_font=App.TEXT, placeholder_text="Value"))
        ctk_items[1][1].grid(row=2, column=1, padx=0, pady=15)  

        self.search_car_button = customtkinter.CTkButton(master=self.add_car_frame, text="Search Inventory", command=find_car)
        self.search_car_button.grid(row=4, column=1, pady=15, padx=0)

    def show_info_function(self):
        info = 'Welcome to our car inventory app!'

        ctk_items = [[],[]]

        self.add_info_frame = customtkinter.CTkFrame(master=self)                         
        self.add_info_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)       

        ctk_items[0].append(customtkinter.CTkLabel(master=self.add_info_frame, text=f'{info}', text_font=App.TEXT))
        ctk_items[0][0].grid(row=0, column=0, padx=0, pady=15)


if __name__ == "__main__":
    app = App()
    app.mainloop()