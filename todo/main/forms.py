from .models import Todo
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateInput


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'date_to_complete']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите, что вам нужно сделать'
            }),
            # "date_created": DateTimeInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Создано'
            # }), ЕСЛИ ПОНАДОБИТСЯ ВВОДИТЬ ВРУНУЮ - ДОБАВИТЬ DATE_CREATED В ФИЛДС И РАСКОММЕНТИРОВАТЬ
            "date_to_complete": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Срок'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите задание поподробнее'
            }),
        }
