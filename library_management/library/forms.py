from django import forms
from .models import Book, Member, BorrowRecord


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'quantity', 'cover_image']




class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'member_image']




class BorrowRecordForm(forms.ModelForm):

    class Meta:
        model = BorrowRecord
        fields = ['member', 'book', 'return_date']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'})
        }

