from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from pymongo import MongoClient
import pymongo

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]

        # Adicione a imagem do logotipo "VI BANK" (ajuste o tamanho conforme necessário)
        self.logo_image = Image(
            source='image-removebg-preview.png',  # Substitua pelo caminho da sua imagem
            size_hint=(None, None),
            size=(300, 300),  
            pos_hint={'center_x': 0.5, 'center_y': 0.7}  # Centralize a imagem
        )
        self.add_widget(self.logo_image)

        self.cpf_input = TextInput(
            hint_text="CPF",
            input_type="number",
        )
        self.add_widget(self.cpf_input)

        self.password_input = TextInput(
            hint_text="Senha",
            password=True,
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

        # Conexão com o MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['ProjetoFinal']  # Substitua pelo nome do seu banco de dados
        collection = db['clientes']  # Substitua pelo nome da sua coleção

        # Verifique se o usuário e a senha estão corretos
        user = collection.find_one({'cpf': cpf, 'senha': password})
        if user:
            popup = Popup(title='Sucesso',
                          content=Label(text='Login bem-sucedido!'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            popup = Popup(title='falha',
                          content=Label(text='senha ou usuario incorreto!'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

        self.cpf_input.text = ""
        self.password_input.text = ""

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()