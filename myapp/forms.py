from django import forms
select_item = (
    ('cap','cap'),
    ('shirt','shirt'),
    ('tshirt','tshirt'),
    ('jeans','jeans'),
    ('scarf','scarf'),
    ('skirt','skirt'),
    ('shorts','shorts'),
    ('jacket','jacket'),
)

class items(forms.Form):
    Item = forms.ChoiceField(choices=select_item, label="Select item")
    Quantity = forms.IntegerField()
