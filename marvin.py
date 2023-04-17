
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

# Define the Kivy Builder string for the app layout
disp_text = 'hi'
kv = """
BoxLayout:
    orientation: 'vertical'
    TabbedPanel:
        do_default_tab: False
        TabbedPanelItem:
            text: 'Tab 1'
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Text Input:'
                    size_hint_y: None
                    height: '30dp'
                ScrollView:
                    id: scrlv
                    size_hint_y: 1  # Set fixed height for the ScrollView
                    TextInput:
                        id: my_text_input
                        text: 'disp_text'
                        size_hint: 1, None
                        height: max( (len(self._lines)+1) * self.line_height, scrlv.height)
                Button:
                    text: 'Show First 59 Chars'
                    on_release: root.show_first_59_chars()
                Label:
                    id: my_label
                    text: ''
                    size_hint_y: None
                    height: '30dp'
        TabbedPanelItem:
            text: 'Tab 2'
        TabbedPanelItem:
            text: 'Tab 3'
        TabbedPanelItem:
            text: 'Tab 4'
        TabbedPanelItem:
            text: 'Tab 5'
        TabbedPanelItem:
            text: 'Tab 6'
        TabbedPanelItem:
            text: 'Tab 7'
"""

class MyTabbedApp(App):
    def build(self):
        return Builder.load_string(kv)

    def show_first_59_chars(self):
        text_input = self.root.ids.my_text_input
        label = self.root.ids.my_label
        label.text = text_input.text[:59]

if __name__ == '__main__':
    MyTabbedApp().run()
