# SETTING MODULE #


class Settings:
    """Class to manage password settings"""

    def __init__(self):
        """Initialize attributes"""

        # ----- UI SETTINGS ----- #

            # -- TEXT -- #

        self.app_title = 'Flashcard App'
        self.lan_welcome = 'Cześć!'
        self.welcome = "Hello! You're learning Polish!"

            # -- IMAGES -- #

        self.tick_image = 'Images\\tick.png'
        self.cross_image = 'Images\\cross.png'
        self.card_back = 'Images\\card_back.png'
        self.card_front = 'Images\\card_front.png'
        self.start_image = 'Images\\start.png'
        self.flip_image = 'Images\\flip.png'

            # -- SIZES -- #

        self.canvas_width = 800
        self.canvas_height = 526

        # ----- FONT SETTINGS ----- #

        self.font = 'Arial'
        self.font_size = 30

        # ----- TXT FILE SETTINGS ----- #

        self.filename = 'Words/polish-english.csv'
        self.learned_words = 'Words\\learnedwords.csv'
        self.words_to_learn = 'Words\\wordstolearn.csv'

        # ----- COLOURS ----- #

        self.GREEN = "#B1DDC6"
