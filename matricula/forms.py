from django import forms
from matricula.models import Aluno


class Matricula(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'data_nascimento', 'n_bi',
                  'n_contato', 'n_contato_alternativo', 'nome_pai', 'nome_mae',
                  'residencia', 'naturalidade', 'provincia', 'escola', 'ano_lectivo', 'nacionalidade']
        labels = {'escola': 'Nome da Escola',
                  'ano_lectivo': 'Ano lectivo',
                  'nome': 'Nome do Aluno',
                  'sobrenome': 'Sobrenome do Aluno',
                  'data_nascimento': 'Data de Nascimento',
                  'n_bi': 'Numero BI/Passaporte',
                  'nome_pai': 'Nome do Pai',
                  'nome_mae': 'Nome da Mae',
                  'nacionalidade': 'Nacionalidade',
                  'naturalidade': 'Naturalidade',
                  'provincia': 'Provincia',
                  'n_contato': 'Numero telefone',
                  'n_contato_alternativo': 'Numero telefone alternativo',
                  'residencia': 'Residencia'}
