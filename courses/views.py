from django.shortcuts import render


def my_first_view(request, who):
    return render(request, 'courses/hello.html', {
        'who': who,
    })
