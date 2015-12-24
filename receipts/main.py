import kivy
kivy.require('1.0.6') # check

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import AsyncImage, Image

from kivy.properties import *
from kivy.input.shape import ShapeRect
from kivy.graphics import Color, Rectangle

Builder.load_string('''
<CustomLayout>
    canvas.before:
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 10, 10, 10, 10
            texture: self.background_image.texture
            pos: self.pos
            size: self.size

<RootWidget>
    CustomLayout:
        size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1
        Label:
            text: "I don't suffer from insanity, I enjoy every minute of it"
            text_size: self.width-20, self.height-20
            valign: 'top'
        Label:
            text: "When I was born I was so surprised; I didn't speak for a year and a half."
            text_size: self.width-20, self.height-20
            valign: 'middle'
            halign: 'center'
        Label:
            text: "A consultant is someone who takes a subject you understand and makes it sound confusing"
            text_size: self.width-20, self.height-20
            valign: 'bottom'
            halign: 'justify'
''')


class CustomLayout(GridLayout):

    background_image = ObjectProperty(
        Image(
            source='../examples/widgets/sequenced_images/data/images/button_white_animated.zip',
            anim_delay=.1))


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
    	super(RootWidget, self).__init__(**kwargs)
    	with self.canvas:
    		self.rect = Rectangle(pos=self.pos, size=self.size)

    	self.bind(pos=self.update_rect)
    	self.bind(size=self.update_rect)

    def update_rect(self, *args):
    	self.rect.pos = self.pos;
    	self.rect.size = self.size


class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()


class LoginScreen(GridLayout):
	"""docstring for LoginScreen"""
	def __init__(self, **kwargs):
		super(LoginScreen,self).__init__(**kwargs)
		self.cols = 1
		self.add_widget(Label(text='User Name'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)
