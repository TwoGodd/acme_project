from django.shortcuts import render

# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm


def birthday(request):
    print(request.GET)  # Напечатаем.
    form = BirthdayForm()
    context = {'form': form}
    return render(request, 'birthday/birthday.html', context)
