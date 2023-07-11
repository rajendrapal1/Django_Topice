from django.shortcuts import render

def student(request):

    data={
        'name':'python',
        'fee':1000,
        'numb':[1,2,3,4,5,6,7,8,9]
    }
    return render(request,'temp.html',data)