from django.db import models

# Импортируется функция-валидатор.
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))

    class Meta:
        verbose_name = 'именинник'
        verbose_name_plural = 'Именинники'

    def __str__(self):
        return self.last_name
