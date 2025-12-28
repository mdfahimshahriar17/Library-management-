from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Member, BorrowRecord
from .forms import BookForm, MemberForm, BorrowRecordForm
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def home(request):

    return render(request, 'base.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'library/login.html')




@login_required
def logout_view(request):
    logout(request)

    return redirect('home')





def book_list(request):

    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query)|
            Q(author__icontains=query)|
            Q(isbn__icontains=query)
        )
    else:
        books = Book.objects.all()

    context = {
        'books': books,
        'query': query,  #Ager query gulo dekhanor jonno
    }

    return render(request, 'library/book_list.html', context)


@login_required
def add_new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES) #request.FILES for image recive
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'library/add_new_book.html', {'form': form})

@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    
    else:
        form = BookForm(instance=book)
    
    return render(request, 'library/book_edit.html', {'form': form})

@login_required
def add_member(request):

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('member_list')
        
    else:
        form = MemberForm()

    return render(request, 'library/add_member.html', {'form': form})


@login_required
def member_list(request):
    query = request.GET.get('q','')
    if query:
        members = Member.objects.filter(
            Q(name__icontains=query)|
            Q(email__icontains=query)|
            Q(phone__icontains=query)
        )

        #Q diye ekadhik onk field search kora jay
        #icontains mane field er moddhe query ache kina eita dekhe case-insensitive capital/choto hater likhlei hobe
    else:
        members = Member.objects.all()

    return render(request, 'library/member_list.html', {'members': members, 'query': query})


@login_required
def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member) #instance=member mane Django bujhe nibe eta kono notun data na eta purono data update kora hoche
        if form.is_valid():
            form.save()
            return redirect('member_list')
        
    else:
        form = MemberForm(instance=member)
        #jodi edit e dhukle django instance er maddhome purono data dekhay

    return render(request, 'library/edit_member.html', {'form': form})


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()


    return redirect('book_list')
    
@login_required
def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()


    return redirect('member_list')




@login_required
def give_borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    #quantity check
    if book.quantity <= 0:
        
        return redirect('book_list') 
    
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            borrow_record = form.save(commit=False) #amra ekhono database e save korinai commit=False rakhsi

            #book quantity decrease kortesi
            borrow_record.book.quantity -= 1
            borrow_record.book.save() #ei khane book -1 kore save korsi

            borrow_record.save() # ekhon database e save korlam
            return redirect('borrwed_book_list')
        

    else:
        form = BorrowRecordForm(initial={'book': book})

    return render(request, 'library/give_borrow_book.html', {'form': form})

@login_required
def borrwed_book_list(request):
    query = request.GET.get('q', '')
    today = timezone.now().date()

    if query:
        borrwed_books = BorrowRecord.objects.filter(
            Q(member__name__icontains=query)|
            Q(member__email__icontains=query)|
            Q(book__title__icontains=query)|
            Q(book__isbn__icontains=query)
        ).select_related('member', 'book')

    else:
        borrwed_books  = BorrowRecord.objects.all().select_related('member', 'book')


    return render(request, 'library/borrow_book_list.html', {'borrwed_books': borrwed_books, 'query': query, 'today': today})

@login_required
def return_receive(request, pk):
    borrow_record = get_object_or_404(BorrowRecord, pk=pk)

    if not borrow_record.is_returned:
        borrow_record.is_returned = True
        borrow_record.return_date = timezone.now().date()

        borrow_record.book.quantity +=1
        borrow_record.book.save()

        borrow_record.save()

    return redirect('borrwed_book_list')


