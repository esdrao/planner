from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

class CustomTextInput(TextInput):
    pass

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        with self.canvas.before:
            Color(1, 0.6, 0.6, 1)  # Rosa
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])

    def update_canvas(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class PlannerApp(App):
    def build(self):
        try:
            # Define o tamanho da janela e a cor de fundo para pessego
            Window.size = (400, 550)
            Window.clearcolor = (1, 0.8, 0.6, 1)  # Cor pessego com valor alpha

            layout = FloatLayout()

            # Adiciona a imagem de perfil
            image_source = '/Users/Administrador/Downloads/myplaces.jpeg'
            image_width = Window.width * 0.3
            image_height = image_width * (3 / 4)
            img_widget = Image(source=image_source, size_hint=(None, None), size=(image_width, image_height))
            img_widget.pos_hint = {'center_x': 0.5, 'center_y': 0.7}
            layout.add_widget(img_widget)

            # Adiciona o campo de e-mail personalizado
            email_input = CustomTextInput(hint_text="Digite seu e-mail", size_hint=(None, None), size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.43})
            email_input.background_normal = ''
            email_input.background_active = ''
            email_input.background_color = (1, 0.7, 0.3, 1)  # Cor de fundo da caixa de entrada (laranja mais claro)
            email_input.cursor_color = (0, 0, 0, 1)  # Cor do cursor preta
            layout.add_widget(email_input)

            # Adiciona um texto explicativo para o código enviado por e-mail
            code_label = Label(text="Digite o código enviado para o e-mail", size_hint=(None, None), size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.37}, color=(0, 0, 0, 1))
            layout.add_widget(code_label)

            # Adiciona o campo do código enviado por e-mail
            code_input = CustomTextInput(hint_text="Código enviado por e-mail", size_hint=(None, None), size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.32})
            code_input.background_normal = ''
            code_input.background_active = ''
            code_input.background_color = (1, 0.7, 0.3, 1)  # Cor de fundo da caixa de entrada (laranja mais claro)
            code_input.cursor_color = (0, 0, 0, 1)  # Cor do cursor preta
            layout.add_widget(code_input)

            # Adiciona um botão de continuar com bordas arredondadas
            confirm_button = RoundedButton(text="Continuar", size_hint=(None, None), size=(300, 40), pos_hint={'center_x': 0.5, 'center_y': 0.25})
            layout.add_widget(confirm_button)

            return layout
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == '__main__':
    PlannerApp().run()
