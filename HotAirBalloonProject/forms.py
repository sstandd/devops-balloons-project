from django import forms
from .models import Flight


class FlightsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FlightsForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Flight
        exclude = ("user",)
