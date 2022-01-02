from ursina import *
from itertools import product
from ursina.prefabs.first_person_controller import FirstPersonController
from PIL import ImageTk,Image

def eltern_kind_beziehung(achse,schicht):
    for w in wurfel:
        w.position, w.rotation = round(w.world_position,1), w.world_rotation
        w.parent = scene

    zentrum.rotation = 0

    for w in wurfel:
        if eval(f'w.position.{achse}') == schicht:
            w.parent = zentrum


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def input(key):
    if key not in rot_dict:return
    achse, schicht, winkel = rot_dict[key]
    eltern_kind_beziehung(achse,schicht)
    shift = held_keys['shift']
    eval(f'zentrum.animate_rotation_{achse} ({-winkel if shift else winkel},duration=0.5)')

app = Ursina()
window.borderless = False
window.size = (800,500)
window.position = (200,200)
window.color = rgb(238,233,233)
window.title = "RUBIK CUBE"
window.icon="logo"

EditorCamera()

zentrum = Entity()

rot_dict = ({'u': ['y',1,90],'e':['y',0,-90], 'd':['y',-1,-90],
             'l':['x',-1,-90],'m':['x',0,-90],'r':['x',1,90],
             'f':['z',-1,90],'s':['z',0,90],'b':['z',1,-90]})

wurfel = []
for pos in product((-1,0,1),repeat=3):
    wurfel.append(Entity(model="Teil_46_model.obj",texture="i125.png",position=(1,-1,-1),scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i25.png", position=(1,-1,0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i235.png", position=(1, -1, 1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i12.png", position=(1, 0, -1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i2.png", position=(1, 0, 0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i23.png", position=(1, 0, 1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i126.png", position=(1, 1,-1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i26.png", position=(1, 1, 0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i236.png", position=(1, 1, 1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i15.png", position=(0,-1,-1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i5.png", position=(0, -1, 0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i35.png", position=(0, -1, 1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i1.png", position=(0, 0, -1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i1.png", position=(0, 0, 0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i3.png", position=(0, 0, 1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i16.png", position=(0, 1, -1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i6.png", position=(0, 1, 0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i36.png", position=(0, 1, 1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i145.png", position=(-1, -1, -1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i45.png", position=(-1, -1, 0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i345.png", position=(-1, -1, 1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i14.png", position=(-1, 0, -1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i4.png", position=(-1, 0, 0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i34.png", position=(-1, 0, 1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i146.png", position=(-1, 1, -1), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i46.png", position=(-1, 1, 0), scale=0.5))
    wurfel.append(Entity(model="Teil_46_model.obj", texture="i346.png", position=(-1, 1, 1), scale=0.5))


txt2 = Text(text='LOCKTON:', color=color.black,bold=True,scale =3,x=-.45,y=.4)
txt1 = Text(text='RETO DEL CUBO', color=rgb(51,161,201),bold=True,scale =3,x=-.05,y=.4)
txt3 = Text(text="¡COMENCEMOS", color=rgb(51,161,201),scale =1.3,x=-0.65,y=0.22)
txt4 = Text(text="A JUGAR!", color=rgb(51,161,201),scale =1.3,x=-0.65,y=0.18)
txt5 = Text(text="Muévete por el cubo", color=color.black,scale =1,x=-0.7,y=0.10)
txt6 = Text(text="con el click derecho de", color=color.black,scale =1,x=-0.7,y=0.07)
txt7 = Text(text="tu mouse sin soltarlo.", color=color.black,scale =1,x=-0.7,y=0.04)
txt8 = Text(text="Recuerda con el Scroll", color=color.black,scale =1,x=-0.7,y=-0.04)
txt9 = Text(text="del mouse puedes usar", color=color.black,scale =1,x=-0.7,y=-0.07)
txt10 = Text(text="el Zoom y leer la", color=color.black,scale =1,x=-0.7,y=-0.10)
txt11 = Text(text="información.", color=color.black,scale =1,x=-0.7,y=-0.13)
txt12 = Text(text="¡DEMUESTRA TUS HABILIDADES!",color=rgb(34,139,34),scale =2,x=-.35,y=-0.4)
txt13 = Text(text="Los Comandos de juego son:", color=color.black,scale =1,x=0.35,y=0.25)
txt14 = Text(text="U", color=rgb(255,105,180),scale =1,x=0.35,y=0.20)
txt14_1 = Text(text="para girar la parte superior", color=color.black,scale =1,x=0.39,y=0.2)
txt15 = Text(text="E", color=rgb(255,105,180),scale =1,x=0.35,y=0.15)
txt15_1 = Text(text="para el sector medio", color=color.black,scale =1,x=0.39,y=0.15)
txt15_2 = Text(text="horizontal", color=color.black,scale =1,x=0.39,y=0.10)
txt16 = Text(text="D", color=rgb(255,105,180),scale =1,x=0.35,y=0.05)
txt16_1 = Text(text="para la parte inferior",color=color.black,scale =1,x=0.39,y=0.05)
txt17 = Text(text="L", color=rgb(255,105,180),scale =1,x=0.35,y=0)
txt17_1 = Text(text="para el lado izquierdo", color=color.black,scale =1,x=0.39,y=0)
txt18 = Text(text="M", color=rgb(255,105,180),scale =1,x=0.35,y=-0.05)
txt18_1 = Text(text="para el sector medio",color=color.black,scale =1,x=0.39,y=-0.05)
txt18_2 = Text(text="vertical", color=color.black,scale =1,x=0.39,y=-0.10)
txt19 = Text(text="R", color=rgb(255,105,180),scale =1,x=0.35,y=-0.15)
txt19_1 = Text(text="para el lado derecho", color=color.black,scale =1,x=0.39,y=-0.15)
txt20 = Text(text="F", color=rgb(255,105,180),scale =1,x=0.35,y=-0.20)
txt20_1 = Text(text="para el área frontal", color=color.black,scale =1,x=0.39,y=-0.20)
txt21 = Text(text="S", color=rgb(255,105,180),scale =1,x=0.35,y=-0.25)
txt21_1 = Text(text="para el lado medio lateral", color=color.black,scale =1,x=0.39,y=-0.25)
txt22 = Text(text="B", color=rgb(255,105,180),scale =1,x=0.35,y=-0.30)
txt22_1 = Text(text="para el lado posterior", color=color.black,scale =1,x=0.39,y=-0.30)
b1= Button(icon="logoem",scale=0.1,color=rgb(238,233,233),x=-0.55,y=0.37)
b2= Button(icon="f2",scale=0.1,color=rgb(238,233,233),x=-0.7,y=0.2)


app.run()