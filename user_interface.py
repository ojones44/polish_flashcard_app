# UI MODULE #

from tkinter import *


class UI:
    """Class to set up and manage the user interface"""

    def __init__(self, app):
        """Initialize attributes"""

        self.settings = app.settings
        self.app = app
        self.set_window()
        self.create_images()
        self.set_canvas()
        self.set_buttons()

    def set_window(self):
        """Set up the window"""

        self.window = Tk()
        self.window.title(self.settings.app_title)
        self.window.config(padx=30, pady=30, bg=self.settings.GREEN)

    def create_images(self):
        """Assign images to class"""

        self.flashcard_back = PhotoImage(file=self.settings.card_back)
        self.flashcard_front = PhotoImage(file=self.settings.card_front)
        self.tick = PhotoImage(file=self.settings.tick_image)
        self.cross = PhotoImage(file=self.settings.cross_image)
        self.start_image = PhotoImage(file=self.settings.start_image)
        self.flip_image = PhotoImage(file=self.settings.flip_image)

    def set_canvas(self):
        """Set up any canvas classes"""

        self.canvas = Canvas(width=self.settings.canvas_width,
                             height=self.settings.canvas_height,
                             highlightthickness=0,
                             bg=self.settings.GREEN
                             )

        self.card = self.canvas.create_image(self.settings.canvas_width/2,
                                             self.settings.canvas_height/2,
                                             image=self.flashcard_back)

        self.language = self.canvas.create_text(400, 150,
                                                text=self.settings.lan_welcome,
                                                font=('Arial', 30),
                                                fill='white',
                                                )

        self.word = self.canvas.create_text(400, 300,
                                            text=self.settings.welcome,
                                            font=('Arial', 30),
                                            fill='white',
                                            )

        self.canvas.grid(column=1, row=1, columnspan=3)

    def set_buttons(self):
        """Set up any button classes"""

        self.tick_button = Button(image=self.tick,
                                  border=0,
                                  highlightthickness=0,
                                  bg=self.settings.GREEN,
                                  command=self.app.store_info
                                  )

        self.cross_button = Button(image=self.cross,
                                   border=0,
                                   highlightthickness=0,
                                   bg=self.settings.GREEN,
                                   command=self.app.get_word,
                                   )

        self.centre_button = Button(image=self.start_image,
                                    border=0,
                                    highlightthickness=0,
                                    bg=self.settings.GREEN,
                                    command=self.app.start_cards
                                    )

        self.tick_button.grid(column=1, row=2)
        self.centre_button.grid(column=2, row=2)
        self.cross_button.grid(column=3, row=2)

    def flip_card_front(self):
        """Flip the flash card to English"""

        self.canvas.itemconfig(self.language,
                               text='English',
                               fill='black',
                               font=('Arial', 30, 'italic'),
                               )

        self.canvas.itemconfig(self.word,
                               text=self.app.word_data.translation,
                               fill='black',
                               font=('Arial', 45, 'bold'),
                               )

        self.canvas.itemconfig(self.card,
                               image=self.flashcard_front)

    def flip_card_back(self):
        """Flip the flash card to Polish"""

        self.canvas.itemconfig(self.language,
                               text='Polish',
                               fill='white',
                               font=('Arial', 30, 'italic'),
                               )

        self.canvas.itemconfig(self.word,
                               text=self.app.word_data.new_word,
                               fill='white',
                               font=('Arial', 45, 'bold'),
                               )

        self.canvas.itemconfig(self.card,
                               image=self.flashcard_back)

    def change_centre_button(self):
        """Change centre button each time it is pressed"""

        self.centre_button.config(image=self.flip_image,
                                  command=self.app.switch_card,
                                  )
