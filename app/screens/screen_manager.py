from kivy.uix.screenmanager import ScreenManager, Screen
from app.screens.welcome_screen import WelcomeScreen
from app.screens.quiz_screen import QuizScreen
from app.screens.result_screen import ResultScreen

def create_screen_manager():
    sm = ScreenManager()
    sm.add_widget(WelcomeScreen(name='welcome'))
    sm.add_widget(QuizScreen(name='quiz'))
    sm.add_widget(ResultScreen(name='result'))
    return sm