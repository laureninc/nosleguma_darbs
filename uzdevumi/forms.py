from django.forms import (
    Form,
    CharField,
    DateTimeField,
)


class VisitForm(Form):

    visitor = CharField()
    date_time = DateTimeField()
    reason = CharField()
