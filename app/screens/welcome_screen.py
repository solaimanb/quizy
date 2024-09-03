from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text='Welcome to Quizy!', font_size=30)
        self.layout.add_widget(self.label)
        
        self.start_button = Button(text='Start Quiz')
        self.start_button.bind(on_release=self.start_quiz)
        self.layout.add_widget(self.start_button)
        print("WelcomeScreen initialized")
        
    def start_quiz(self, instance):
        self.manager.current = 'quiz'