
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.base import runTouchApp

# Create a TextInput object with default text 'hi'
text_input = TextInput(text='hi')

# Wrap the TextInput object in a ScrollView
scroll_view = ScrollView(do_scroll_x=False)
scroll_view.add_widget(text_input)

# Set the ScrollView as the root widget
Window.add_widget(scroll_view)

# Run the app
runTouchApp()
