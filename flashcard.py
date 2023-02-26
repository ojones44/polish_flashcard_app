# TKINTER FLASHCARD APP #


from settings import Settings
from user_interface import UI
from word_data import WordData


class FlashcardApp:
    """Class to manage language learning flashcard app"""

    def __init__(self):
        """Initialize attributes"""

        self.settings = Settings()
        self.word_data = WordData(self)
        self.UI = UI(self)
        self.pulse_code = 1

    def run_app(self):
        """Method to contain the running of the app"""

        self.UI.window.mainloop()

    def start_cards(self):
        """Start flashcard app after user hits start"""

        self.UI.change_centre_button()
        self.get_word()

    def get_word(self):
        """Show user the next word"""

        self.word_data.get_next_word()
        self.UI.flip_card_back()

        if self.pulse_code == -1:
            self.reset_pulse_code()

    def switch_card(self):
        """Alternate the card switch for middle button"""

        if self.pulse_code == 1:
            self.UI.flip_card_front()
        elif self.pulse_code == -1:
            self.UI.flip_card_back()

        self.pulse_code *= -1

    def reset_pulse_code(self):
        """Set pulse code back to 1 if buttons are pressed while card is
        flipped on translated side"""

        self.pulse_code = 1

    def store_info(self):
        """Remove word from dictionary if tick button pressed"""

        self.word_data.store_data()
        self.get_word()


if __name__ == '__main__':
    fc = FlashcardApp()
    fc.run_app()
