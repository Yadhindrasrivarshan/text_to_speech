import os
import io
import pygame
import threading
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from gtts import gTTS
from googletrans import Translator


class Translator_App(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=395, height=200)

        self.translate_tab = ttk.Frame(tabControl)
        tabControl.add(self.translate_tab, text="Translate")
        tabControl.grid()
        self.translate_tab.grid_propagate(0)

        self.about_tab = ttk.Frame(tabControl)
        tabControl.add(self.about_tab, text="About")
        tabControl.grid()

        self.speak_it = BooleanVar()
        self.language = StringVar()
        self.languages = {
            'Arabic': 'ar', 'Belarusian': 'be',
            'Bulgarian': 'bg', 'Bosnian': 'bs',
            'Czech': 'cs', 'Danish': 'da',
            'German': 'de', 'Greek': 'el',
            'English': 'en', 'Spanish': 'es',
            'Persian': 'fa', 'Finnish': 'fi',
            'French': 'fr', 'Irish': 'ga',
            'Hebrew': 'he', 'Hindi': 'hi',
            'Hungarian': 'hu', 'Armenian': 'hy',
            'Indonesian': 'id', 'Italian': 'it',
            'Japanese': 'ja', 'Korean': 'ko',
            'Kurdish': 'ku', 'Latin': 'la',
            'Lithuanian': 'lt', 'Latvian': 'lv',
            'Dutch': 'nl', 'Norwegian': 'no',
            'Polish': 'pl', 'Portuguese': 'pt',
            'Romanian': 'ro', 'Russian': 'ru',
            'Somalia': 'so', 'Albanian': 'sq',
            'Serbian': 'sr', 'Swedish': 'sv',
            'Swahili': 'sw', 'Turkish': 'tr',
            'Vietnamese': 'vi'}
        self.translate_page()
        self.about_page()

    def translate_page(self):
        self.top_label = Label(self.translate_tab, text="Enter Sentence To Translate:")
        self.top_label.grid(column=0, row=0)

        self.word_entry = Entry(self.translate_tab, width=48)
        self.word_entry.grid(column=0, row=1, columnspan=3, padx=5, pady=5)

        self.language_label = Label(self.translate_tab, text="Language: ")
        self.language_label.grid(column=0, row=2, pady=5)

        self.language_menu = ttk.Combobox(self.translate_tab, values=[*self.languages.keys()])
        self.language_menu.grid(column=1, row=2)
        self.language_menu.current(0)

        self.translate_button = Button(self.translate_tab, text="Translate!", command=self.translate_func)
        self.translate_button.grid(column=0, row=3, pady=15)

        self.speak_check = Checkbutton(self.translate_tab, text="Say It!", variable=self.speak_it)
        self.speak_check.grid(column=1, row=3)

        self.result = Label(self.translate_tab, text="")
        self.result.grid(column=0, row=4, columnspan=3)

    def about_page(self):
        pass

    def translate_func(self):
        word = self.word_entry.get()
        language = self.languages.get(self.language_menu.get())
        translator = Translator(service_urls=["translate.google.com"])
        translation = translator.translate(word, dest=language)
        speak_thread = threading.Thread(target=self.speak, args=(translation.text, language))
        self.result.configure(text=translation.text)
        if self.speak_it.get():
            speak_thread.start()

    def speak(self, text, language):
        with io.BytesIO() as file:
            gTTS(text=text, lang=language).write_to_fp(file)
            file.seek(0)
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue


if __name__ == '__main__':
    root = Tk()
    root.title("Translator")
    root.geometry("400x235")
    Translator_App(root)
    root.mainloop()
