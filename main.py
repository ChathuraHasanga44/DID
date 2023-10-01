from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class MyApp(App):
    def build(self):
        # Create the root widget as a BoxLayout with yellow background
        root = BoxLayout(orientation='vertical', spacing=10, padding=10,
                         size_hint=(None, None), size=(400, 400),
                         pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Set the background color for the entire BoxLayout
        with root.canvas.before:
            Color(1, 1, 0, 1)  # Yellow background (RGBA color values)
            rect = Rectangle(size=root.size, pos=root.pos)

        # Create a Button with a blue background
        button = Button(text='View Certificate', background_color=(0, 0, 1, 1))  # Blue background

        # Add the Button to the BoxLayout (on top of the yellow background)
        root.add_widget(button)

        return root

if __name__ == '__main__':
    MyApp().run()
