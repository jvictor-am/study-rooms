from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Python for begginers'},
    {'id': 2, 'name': 'AWS & DevOps'},
    {'id': 3, 'name': 'React Expert'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'mainapp/home.html', context)

def room(request, pk):
    room = None
    for each_room in rooms:
        if each_room['id'] == int(pk):
            room = each_room
    context = {'room': room}

    return render(request, 'mainapp/room.html', context)
