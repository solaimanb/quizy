from kivy.uix.screenmanager import Screen
from app.widgets.question_widget import QuestionWidget
from app.services.score_manager import ScoreManager

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.question_widget = QuestionWidget()
        self.add_widget(self.question_widget)
        self.score_manager = ScoreManager()
        
    def on_enter(self):
        # Load the first question
        # self.question_widget.load_question()
        pass