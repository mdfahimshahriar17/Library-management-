from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField(max_length=13, unique=True)
    quantity = models.IntegerField()
    cover_image = models.ImageField(upload_to='bookk_cover/', blank=True, null=True)

    def __str__(self):
        return self.title
    


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=15, null=True, blank=True)
    joined_date = models.DateField(auto_now_add=True)
    member_image = models.ImageField(upload_to='members_photo/', null=True, blank=True)

    def __str__(self):
        return self.email
    

class BorrowRecord(models.Model):
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):

        return f"{self.member.name} borrowed {self.book.title}"   
