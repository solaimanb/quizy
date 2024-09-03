from kivy.app import App
from app.screens.screen_manager import create_screen_manager

class QuizyApp(App):
    def build(self):
        self.title = 'Quizy'
        screen_manager = create_screen_manager()
        return screen_manager
    
    def on_start(self):
        print('QuizyApp started!')
        
    def on_stop(self):
        print('QuizyApp stopped!')