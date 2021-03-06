from django import forms
from ..models import Pedido, Cliente


class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    class Meta:
        model = Pedido
        fields = ['cliente', 'data_pedido', 'valor', 'status', 'observacao']