from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Aluno(models.Model):
    PROVINCIAS = (('Bengo', 'Bengo'), ('Benguela', 'Benguela'), ('Bie', 'Bie'), ('Cabinda', 'Cabinda'), ('Cuando Cubango', 'Cuando Cubango'),
                  ('Cuanza Norte', 'Cuanza Norte'), ('Cuanza Sul', 'Cuanza Sul'), ('Cunene', 'Cunene'), ('Huambo', 'Huambo'), ('Huila', 'Huila'),
                  ('Luanda', 'Luanda'), ('Lunda Norte', 'Lunda Norte'), ('Lunda Sul', 'Lunda Sul'), ('Malanje', 'Malanje'), ('Moxico', 'Moxico'),
                  ('Namibe', 'Namibe'), ('Uige', 'Uige'), ('Zaire', 'Zaire'), ('Outra', 'Outra (Estrangeira)'))

    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=30)
    n_bi = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(auto_now=timezone.now)
    n_contato = models.CharField(max_length=13)
    n_contato_alternativo = models.CharField(max_length=13)
    nome_pai = models.CharField(max_length=50)
    nome_mae = models.CharField(max_length=50)
    residencia = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=20)
    naturalidade = models.CharField(max_length=30)
    provincia = models.CharField(max_length=20, choices=PROVINCIAS, default='Luanda')

    escola = models.CharField(max_length=30, help_text='O nome da escola que deseja ingressar.')
    ano_lectivo = models.CharField(max_length=4, default=2022, help_text='O ano lectivo que deseja iniciar.')

    def __str__(self):
        return f"ID-Aluno: {self.id}\n" \
               f"Nome: {self.nome} {self.sobrenome}\n" \
               f"Data Nascimento: {self.data_nascimento}\n" \
               f"Filho de: {self.nome_pai} e de: {self.nome_mae}\n" \
               f"BI/Passaporte: {self.n_bi}\n" \
               f"Nacionalidade: {self.nacionalidade}" \
               f"Naturalidade: {self.naturalidade}-{self.provincia}"
