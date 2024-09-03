from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

from app.app import QuizyApp

if __name__ == '__main__':
    QuizyApp().run()