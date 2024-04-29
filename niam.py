from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import Image
import pymongo
from pymongo import collection
from pymongo import database

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]

        # Adicione a imagem do logotipo "VI BANK" (ajuste o tamanho conforme necessário)
        self.logo_image = Image(
            source='image-removebg-preview.png',  # Substitua pelo caminho da sua imagem
            size_hint=(None, None),
            size=(300, 300),  # Ajuste o tamanho da imagem
            pos_hint={'center_x': 0.5, 'center_y': 0.7}  # Centralize a imagem
        )
        self.add_widget(self.logo_image)

        self.cpf_input = MDTextField(
            hint_text="CPF",
            helper_text="Digite seu CPF (somente números)",
            helper_text_mode="on_focus",
            input_type="number",
            max_text_length = 11
        )
        self.add_widget(self.cpf_input)

        self.password_input = MDTextField(
            hint_text="Senha",
            helper_text="Digite sua senha(Somente números)",
            helper_text_mode="on_focus",
            password=True,
            max_text_length = 6
        )
        self.add_widget(self.password_input)

        self.login_button = Button(
            text="Entrar",
            size_hint=(None, None),
            size=(150, 48),  # Ajuste o tamanho do botão
            on_release=self.login
        )
        self.add_widget(self.login_button)

    def login(self, instance):
        cpf = self.cpf_input.text
        password = self.password_input.text
#Aqui você pode adicionar a lógica de autenticação com o CPF e senha fornecidos
#Por enquanto, apenas exibirei uma mensagem de sucesso.
        print(f"CPF: {cpf}, Senha: {password}")
        self.cpf_input.text = ""
        self.password_input.text = ""

class MyApp(MDApp):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()