from django.forms import (
    Form,
    CharField,
    DateTimeField,
)


class VisitForm(Form):
    visitor = CharField()
    date_time = DateTimeField()
    reason = CharField()


class VisitorNameForm(Form):
    visitor_name = CharField()


class GradesForm(Form):
    name = CharField()
    grades = CharField()
