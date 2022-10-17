from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.animation import Animation
time_sicund = 15
timer = 45

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        
        TI = TextInput(
            text = '',
            size_hint = (.35,.049),
            pos = (330,175))
        
        TI2 = TextInput(
            text = '',
            size_hint = (.35,.049),
            pos = (330,135))

        btn = Button(
            text="Начать",
            font_size = 25,#размерр текста
            size_hint = (.30,.13),#размер кнопки
            pos = (210,20))
        
        
        txt = Label(
            text = 'Это такое тест руфье но хотя оно не точное\n ну крч регестрируйся',
            size_hint = (.3,.5),
            font_size = 25,
            pos = (170,360,))
        
        txt2 = Label(
            text = 'Введите имя:',
            size_hint = (.3,.5),
            font_size = 24,
            pos = (100,45,))
        
        txt3 = Label(
            text = 'Введите возраст:',
            size_hint = (.3,.5),
            font_size = 24,
            pos = (100,5,))

        btn.on_press = self.next
        
        self.add_widget(btn)#оно показывает на окно этот написанный виджет
        self.add_widget(txt)
        self.add_widget(txt2)
        self.add_widget(txt3)
        self.add_widget(TI)
        self.add_widget(TI2)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'#переключения экранов 

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        
        TI = TextInput(
            text = '',
            size_hint = (.30,.1),
            pos = (270,145),
            disabled = True)

        txt2 = Label(
            text = 'напеши сюда сколько вышло ',
            size_hint = (.4,.5),
            font_size = 25,
            pos = (240,100,))

        txt = Label(
            text = 'напеши свои пульс сердца в тичение 15 секунд',
            size_hint = (.4,.5),
            font_size = 25,
            pos = (240,210,))
        
        btn = (Button(
            text="Нажми что бы измерить пульс",
            size_hint = (.30,.13),
            font_size = 16,
            pos = (270,50)))

        btn.on_press = self.on_enter
        btn.on_press = self.on_ente
        
        self.add_widget(txt2)
        self.add_widget(txt)#оно показывает на окно этот написанный виджет
        self.add_widget(btn)#оно показывает на окно этот написанный виджет
        self.add_widget(TI)#оно показывает на окно этот написанный виджет
    
    def on_enter(self):
        Clock.schedule_once(self.wads, time_sicund)
    
    def on_ente(self):
        
        btn2 = (Button(
            text="",
            size_hint = (.30,.13),
            font_size = 25,
            pos = (270,50),
            disabled = True))
            #background_color = (0, 0, 0)))
        self.add_widget(btn2)
        TI2 = TextInput(
            text = 'измеряй',
            size_hint = (.30,.1),
            pos = (270,145),
            disabled = True)
        self.add_widget(TI2)
    
    def wads(self,on_ente):
        
        
        btn2 = (Button(
            text="НАПЕШИ",
            size_hint = (.30,.13),
            font_size = 25,
            pos = (270,50)))
            #background_color = (0, 0, 0)))
        self.add_widget(btn2)
        TI2 = TextInput(
            text = '',
            size_hint = (.30,.1),
            pos = (270,145))
        self.add_widget(TI2)
        
        btn2.on_press = self.next
    def next(self):
        self.manager.current = 'thirt'
    
    
class ThScr(Screen):
    def __init__(self, name='thirt'):
        super().__init__(name=name)
        
        #start_pos_hint = self.pos_hint
        #animate = animate + Animation(pos_hint={'top': 1.0}, background_color=(0, 1, 1, 1))
        #animate = animate + Animation(pos_hint={'top': 0.1}, background_color=(0, 0, 1, 1), duration=0.5)

       # def start_animation(self):
         #   self.animate.start(self)

        txt = Label(
            text = 'сделай присид 30 раз за 45 сек',
            size_hint = (.3,.5),
            font_size = 25,
            pos = (170,360,))

        TI = TextInput(
            text = '',
            size_hint = (.30,.1),
            pos = (240,145))

        btn = Button(
            text="Начать!",
            font_size = 25,
            size_hint = (.30,.13),
            pos = (240,50))
        
        rect = Button(
            size_hint = (.22,.1),
            pos = (500,455))

        btn.on_press = self.wwa
        
        self.add_widget(rect)
        self.add_widget(TI)
        self.add_widget(txt)
        self.add_widget(btn)#оно показывает на окно этот написанный виджет
    
    def on_enter(self):
        Clock.schedule_once(self.aaa, timer)

    def wwa(self):
        btn = Button(
            text="",
            font_size = 25,
            size_hint = (.30,.13),
            pos = (240,50),
            disabled = True)
        self.add_widget(btn)
        
        TI = TextInput(
            text = 'ДЕЛАЙ!!!',
            size_hint = (.30,.1),
            pos = (240,145),
            disabled = True)
        self.add_widget(TI)
    
    def aaa(self,dt):
        btn = Button(
            text="Следущие",
            font_size = 25,
            size_hint = (.30,.13),
            pos = (240,50))
        self.add_widget(btn)
        btn.on_press = self.next

        TI = TextInput(
            text = '',
            size_hint = (.30,.1),
            pos = (240,145))
        self.add_widget(TI)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'four'#переключения экранов 

class FrScr(Screen):
    def __init__(self, name='four'):
        super().__init__(name=name)
        txt = Label(
            text = 'в тичение минуты измерьте пульс 2 раза\nпрямо сейчас и \nпосле отдыха 15 сек',
            size_hint = (.3,.5),
            font_size = 22,
            pos = (200,360,))
        
        TI = TextInput(
            text = '',
            size_hint = (.35,.049),
            pos = (330,175),
            disabled = True)
        
        TI2 = TextInput(
            text = '',
            size_hint = (.35,.049),
            pos = (330,135),
            disabled = True)

        btn = Button(
            text="Начать",
            font_size = 25,
            size_hint = (.30,.13),
            pos = (240,50))
        btn.on_press = self.on_enter
        btn.on_press = self.wad
        
        txt2 = Label(
            text = 'Результат:',
            size_hint = (.3,.5),
            font_size = 24,
            pos = (100,45,))
        
        txt3 = Label(
            text = 'Результат после отдыха:',
            size_hint = (.3,.5),
            font_size = 24,
            pos = (34,5,))

        self.add_widget(TI2)
        self.add_widget(TI)
        self.add_widget(txt)
        self.add_widget(txt2)
        self.add_widget(txt3)
        self.add_widget(btn)#оно показывает на окно этот написанный виджет
    
    def on_enter(self):
        Clock.schedule_once(self.aaa, time_sicund)

    def wad(self):
        txt = Label(text='напеши свои пульс прямо сейчас')
        self.add_widget(txt)
        btn = Button(
            text="Начать",
            font_size = 25,
            size_hint = (.30,.13),
            pos = (240,50),
            disabled = True)
        self.add_widget(btn)
        TI = TextInput(
            text = '',
            size_hint = (.35,.049),
            pos = (330,175))
        self.add_widget(TI)
        TI2 = TextInput(
            text = 'сейчас измерь и одноврменно отдых ;)',
            size_hint = (.35,.049),
            pos = (330,135),
            disabled = True)
        self.add_widget(TI2)
    def aaa(self,dt):
        
        btn = Button(
            text="Завершить",
            font_size = 25,
            size_hint = (.30,.13),
            pos = (240,50))
        self.add_widget(btn)
        btn.on_press = self.next
        
        
        TI2 = TextInput(
            text = '',
            size_hint = (.35,.049),
            pos = (330,135))
        self.add_widget(TI2)


    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'five'#переключения экранов 

class FvScr(Screen):
    def __init__(self, name='five'):
        super().__init__(name=name)
        txt = Label(text="спорим ты ничего не делал")
        
        #ayout = BoxLayout(orientation='vertical')
        #layout.add_widget(txt)
        self.add_widget(txt)#оно показывает на окно этот написанный виджет
        
       

class MyApp(App):
    def build(self):
        
        sm = ScreenManager()
        
        sm.add_widget(SecondScr())
        sm.add_widget(FirstScr())
        sm.add_widget(ThScr())
        sm.add_widget(FrScr())
        sm.add_widget(FvScr())
        return sm
        
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
app = MyApp()
app.run()