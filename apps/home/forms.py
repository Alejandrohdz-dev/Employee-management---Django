from django import forms
from .models import Test

class TestForm(forms.ModelForm):
    """Form definition for Test."""

    class Meta:
        """Meta definition for Testsform."""

        model = Test
        fields = (
            'title',
            'subtitle',
            'quantity',
        )

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Insert text here'
                }
            )
            
            # 'quantity': forms.
        }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 10:
            raise forms.ValidationError('Quantity must be more than 10')

        return quantity