import os
import io
import pygame
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
        tabControl.configure(width=305, height=200)

        self.translate_tab = ttk.Frame(tabControl)
        tabControl.add(self.translate_tab, text="Translate")
        tabControl.grid()
        self.about_tab = ttk.Frame(tabControl)
        tabControl.add(self.about_tab, text="About")
        tabControl.grid()

        self.speak_it = BooleanVar()
        self.language = StringVar()
        self.languages = [
            'en',
            'ar',
            'bg',
            'bs',
            'cs',
            'da',
            'de',
            'el',
            'en',
            'es',
            'ga',
            'ru',
        ]
        self.translate_page()
        self.about_page()

    def translate_page(self):
        self.top_label = Label(self.translate_tab, text="Enter Word You Wish To Translate:")
        self.top_label.grid(column=0, row=0)

        self.word_entry = Entry(self.translate_tab, width=48)
        self.word_entry.grid(column=0, row=1, columnspan=3, padx=5, pady=5)

        self.language_label = Label(self.translate_tab, text="Language: ")
        self.language_label.grid(column=0, row=2, pady=5)
        self.language_menu = OptionMenu(self.translate_tab, self.language, *self.languages)
        self.language_menu.grid(column=1, row=2)
        
        self.translate_button = Button(self.translate_tab, text="Translate!", command=self.translate_func,bg='blue')
        self.translate_button.grid(column=0, row=3, pady=15)

        self.speek_check = Checkbutton(self.translate_tab, text="Say It!", variable=self.speak_it,bg='red')
        self.speek_check.grid(column=1, row=3)

        self.result = Label(self.translate_tab, text="")
        self.result.grid(column=0, row=4)
        
    def about_page(self):
        pass

    def translate_func(self):
        word = self.word_entry.get()
        language = self.language.get()
        translator = Translator(service_urls=["translate.google.com"])
        translation = translator.translate(word, dest=language)
        self.result.configure(text=translation.text)
        if self.speak_it.get():
            self.speak(translation.text, language)

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
    root.title("Translator GUI app")
    root.geometry("317x235")
    Translator_App(root)
    root.mainloop()
