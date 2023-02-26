# MODULE FOR IMPORTING WORD DATA #

import pandas
import random
import tkinter.messagebox


class WordData:
    """Class for importing and managing the word data"""

    def __init__(self, app):
        """Initialize data"""

        self.settings = app.settings
        self.index = 0
        self.new_word = None
        self.translation = None
        self.import_words()

    def import_words(self):
        """Use Pandas module to bring in word data"""

        try:
            self.pl_en = pandas.read_csv(self.settings.words_to_learn)
        except FileNotFoundError:
            self.pl_en = pandas.read_csv(self.settings.filename)
        finally:
            self.words = self.pl_en.to_dict(orient='records')
            self.shuffle_word_list()

    def get_next_word(self):
        """Show the user a polish word"""

        if self.list_has_words():
            if self.index >= len(self.words):
                self.index = 0
                self.shuffle_word_list()

            self.new_word = self.words[self.index]['polish']
            self.translation = self.words[self.index]['english']
            self.index += 1
        else:
            tkinter.messagebox.showwarning('Flashcard App',
                                           'No more words to show')

    def list_has_words(self):
        """Check to see if the list contains words still"""

        if len(self.words) == 0:
            tkinter.messagebox.showinfo('Flashcard App',
                                        'You\'ve ran out of words!')
            return False
        else:
            return True

    def shuffle_word_list(self):
        """Shuffle the list of words"""

        random.shuffle(self.words)

    def store_data(self):
        """Create CSV of learned words on window close"""

        learnt = {
            'polish': [self.new_word],
            'english': [self.translation],
        }

        learnt_data = pandas.DataFrame(learnt)
        self.words.remove(self.words[self.index-1])

        try:
            pandas.read_csv(self.settings.learned_words)
        except FileNotFoundError:
            learnt_data.to_csv(self.settings.learned_words, index=False)
        else:
            learnt_data.to_csv(self.settings.learned_words,
                               mode='a',
                               index=False,
                               header=False)

        to_learn = {
            'polish': [word['polish'] for word in self.words],
            'english': [word['english'] for word in self.words]
        }

        to_learn_data = pandas.DataFrame(to_learn)
        to_learn_data.to_csv(self.settings.words_to_learn, index=False)
