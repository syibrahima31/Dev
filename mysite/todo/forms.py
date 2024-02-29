from django import forms 
from .models import Todo


class UpdateTodoForm(forms.ModelForm):
    """Form definition for UpdateTodo."""

    class Meta:
        """Meta definition for UpdateTodoform."""

        model = Todo
        fields = ('name', 'completed')
