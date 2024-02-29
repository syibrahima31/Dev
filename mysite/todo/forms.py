from django import forms 
from .models import Todo


class UpdateTodoForm(forms.ModelForm):
    """Form definition for UpdateTodo."""

    class Meta:
        """Meta definition for UpdateTodoform."""

        model = Todo
        fields = ('name', 'completed')


class AddTodoForm(forms.ModelForm):
    """Form definition for AddTodo."""

    class Meta:
        """Meta definition for AddTodoform."""

        model = Todo
        fields = ('name','completed')

