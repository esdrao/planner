from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window

class PeachApp(App):
    def build(self):
        try:
            # Define a cor de fundo para pessego
            Window.clearcolor = (1, 0.8, 0.6, 1)  # Cor pessego com valor alpha
            
            # Obtém as dimensões da tela do dispositivo
            width, height = Window.size

            layout = FloatLayout(size=(width, height))

            # Adicionando a imagem de perfil
            profile_image = Image(source="profile_image.png", size_hint=(None, None), size=(150, 150), pos_hint={'x': 0, 'top': 1})
            layout.add_widget(profile_image)

            # Label para "E-mail"
            email_label = Label(text="E-mail:", size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.1, 'top': 0.8})
            layout.add_widget(email_label)

            # Caixa de texto para inserir o e-mail
            email_input = TextInput(hint_text="Digite seu e-mail", size_hint=(None, None), size=(300, 40), pos_hint={'x': 0.3, 'top': 0.8})
            layout.add_widget(email_input)

            # Label para "Senha"
            password_label = Label(text="Senha:", size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.1, 'top': 0.7})
            layout.add_widget(password_label)

            # Caixa de texto para inserir a senha
            password_input = TextInput(hint_text="Digite sua senha", password=True, size_hint=(None, None), size=(300, 40), pos_hint={'x': 0.3, 'top': 0.7})
            layout.add_widget(password_input)

            # Botão de login
            login_button = Button(text="Login", size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.5, 'top': 0.5})
            layout.add_widget(login_button)

            return layout
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == '__main__':
    PeachApp().run()
