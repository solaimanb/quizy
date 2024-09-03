from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QuestionWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.question_label = Label(text='Question goes here')
        self.add_widget(self.question_label)
        
        for i in range(4):
            btn = Button(text=f'Answer {i+1}')
            btn.bind(on_press=self.on_answer_selected)
            self.add_widget(btn)
            
    def on_answer_selected(self, instance):
        # Logic to check if the answer is correct
        print(f'Answer selected: {instance.text}')