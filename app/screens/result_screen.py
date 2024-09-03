from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.result_label = Label(text='Your result is: 0/0', font_size=30)
        self.layout.add_widget(self.result_label)
        
        self.restart_button = Button(text='Restart Quiz', font_size=20)
        self.restart_button.bind(on_release=self.restart_quiz)
        self.layout.add_widget(self.restart_button)
        
        self.add_widget(self.layout)
        
    def set_score(self, score, total):
        self.result_label.text = f'Your result is: {score}/{total}'
        
    def restart_quiz(self, instance):
        self.manager.current = "welcome!"