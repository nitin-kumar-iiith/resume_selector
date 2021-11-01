from django import forms
# what ever you want to add/remove from form just add it here


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length=10)
    email = forms.EmailField(label="Enter Email")
    file = forms.FileField()  # for creating file input
