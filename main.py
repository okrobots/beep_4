from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

class Beep4Notepad(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.textbox = TextInput(
            text=self.load_notes(),
            font_size='18sp',
            background_color=[1,1,1,1]
        )
        
        btn = Button(
            text='保存内容',
            size_hint_y=0.1
        )
        btn.bind(on_press=self.save_notes)
        
        layout.add_widget(self.textbox)
        layout.add_widget(btn)
        return layout
    
    def load_notes(self):
        if os.path.exists('shared_notes.txt'):
            with open('shared_notes.txt', 'r', encoding='utf-8') as f:
                return f.read()
        return "开始输入共享内容..."
    
    def save_notes(self, instance):
        with open('shared_notes.txt', 'w', encoding='utf-8') as f:
            f.write(self.textbox.text)

if __name__ == '__main__':
    Beep4Notepad().run()
