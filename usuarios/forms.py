from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        ),
    )

    senha = forms.CharField(
        label = 'Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
            'class':'form-control',
            'placeholder':'Digite sua Senha'
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome Completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.: João Silva'
            }
        ),
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.:joaosilva@xpto.com'
            }
        ),
    )

    senha = forms.CharField(
        label = 'Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
            'class':'form-control',
            'placeholder':'Digite sua Senha'
            }
        ),
    )    

    confirmar_senha = forms.CharField(
        label = 'Confirmação de Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
            'class':'form-control',
            'placeholder':'Digite sua Senha mais uma vez'
            }
        ),
    )  
    
    
