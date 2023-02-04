from django.shortcuts import render
from .models import *
import random


def random_zag_sheeps():
    ran_zag = random.randint(0, 3)
    ran_sheeps = random.randint(1, 3)

    zagon = Zagons.objects.all()[ran_zag]
    sheeps_zag = Sheeps.objects.filter(zagon=zagon)
    last_sheeps = int(str(Sheeps.objects.all().last())[-2:])
    if len(sheeps_zag) != 1:
        for i in range(ran_sheeps):
            sheeps = Sheeps()
            sheeps.title = f'Овечка{last_sheeps + 1}'
            sheeps.zagon = Zagons.objects.all()[ran_zag]
            sheeps.save()
            last_sheeps += 1


# Create your views here.
def say_hello(request):
    random_zag_sheeps()
    zagon1 = Zagons.objects.all()[0]
    sheeps1 = Sheeps.objects.filter(zagon=zagon1)
    zagon2 = Zagons.objects.all()[1]
    sheeps2 = Sheeps.objects.filter(zagon=zagon2)
    zagon3 = Zagons.objects.all()[2]
    sheeps3 = Sheeps.objects.filter(zagon=zagon3)
    zagon4 = Zagons.objects.all()[3]
    sheeps4 = Sheeps.objects.filter(zagon=zagon4)
    return render(request, 'hello.html',
                  {
                      'zagon1': zagon1,
                      'sheeps1': sheeps1,
                      'zagon2': zagon2,
                      'sheeps2': sheeps2,
                      'zagon3': zagon3,
                      'sheeps3': sheeps3,
                      'zagon4': zagon4,
                      'sheeps4': sheeps4,
                  })


def command(request):
    print(request.POST['command'])
    if len(request.POST['command']) < 1:
        pass
    else:
        command_list = request.POST['command'].split()
        print(command_list)
        if 'переместить' == command_list[1]:
            sheep = Sheeps.objects.get(title=command_list[0])
            zagon = Zagons.objects.get(title=command_list[2])
            sheep.zagon = zagon
            sheep.save()
        elif 'Убить' == command_list[0]:
            sheep = Sheeps.objects.get(title=command_list[1])
            deleted_sheeps = Deleted_sheeps()
            deleted_sheeps.title = sheep.title
            deleted_sheeps.zagon = sheep.zagon
            deleted_sheeps.save()
            sheep.delete()

    zagon1 = Zagons.objects.all()[0]
    sheeps1 = Sheeps.objects.filter(zagon=zagon1)
    zagon2 = Zagons.objects.all()[1]
    sheeps2 = Sheeps.objects.filter(zagon=zagon2)
    zagon3 = Zagons.objects.all()[2]
    sheeps3 = Sheeps.objects.filter(zagon=zagon3)
    zagon4 = Zagons.objects.all()[3]
    sheeps4 = Sheeps.objects.filter(zagon=zagon4)
    return render(request, 'hello.html',
                  {
                      'zagon1': zagon1,
                      'sheeps1': sheeps1,
                      'zagon2': zagon2,
                      'sheeps2': sheeps2,
                      'zagon3': zagon3,
                      'sheeps3': sheeps3,
                      'zagon4': zagon4,
                      'sheeps4': sheeps4,
                  })
