from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from pymongo import MongoClient

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]
        self.background_color = [1, 1, 1, 1]  # Define o fundo como branco
        self.spacing = 20  # Espaçamento entre widgets

        # Adicione a imagem do logotipo "VI BANK" (ajuste o tamanho conforme necessário)
        self.logo_image = Image(
            source='image-removebg-preview.png',  # Substitua pelo caminho da sua imagem
            size_hint=(None, None),
            size=(300, 300),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}  # Centralize a imagem
        )
        self.add_widget(self.logo_image)

        self.cpf_input = MDTextField(
            hint_text="CPF",
            input_type="number",
            size_hint=(None, None),
            size=(300, 48)  # Ajuste o tamanho da caixa de entrada de CPF
        )
        self.add_widget(self.cpf_input)

        self.password_input = MDTextField(
            hint_text="Senha",
            password=True,
            size_hint=(None, None),
            size=(300, 48)  # Ajuste o tamanho da caixa de entrada de senha
        )
        self.add_widget(self.password_input)

        self.login_button = Button(
            text="Entrar",
            size_hint=(None, None),
            size=(150, 48),  # Ajuste o tamanho do botão
            on_release=self.login
        )
        self.add_widget(self.login_button)

        self.signup_label = Label(
            text="[ref=Cadastro][color=0000FF]Cadastrar-se[/color][/ref]",
            markup=True,
            halign="left",  # Alinhe o texto à esquerda
            on_ref_press=self.show_signup_popup
        )
        self.add_widget(self.signup_label)

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
            popup = Popup(title='Falha',
                          content=Label(text='Senha ou usuário incorreto!'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

        self.cpf_input.text = ""
        self.password_input.text = ""

    def show_signup_popup(self, instance, value):
        # Implemente a lógica para exibir o popup de cadastro aqui
        pass

class MyApp(MDApp):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
