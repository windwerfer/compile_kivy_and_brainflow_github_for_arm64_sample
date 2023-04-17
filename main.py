import kivy.uix.boxlayout
import kivy.uix.textinput
from kivy.uix.scrollview import ScrollView
import kivy.uix.label
import kivy.uix.button
#from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from kivy.app import App
from kivy.uix.button import Button

import pkg_resources


class SimpleApp(kivy.app.App):
    def build(self):
        installed_packages = pkg_resources.working_set
        installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
             for i in installed_packages])
        # print(installed_packages_list)
        merged_string = '\n'.join([' '.join(pair) for pair in installed_packages_list])

        scrlv = ScrollView(do_scroll_x=False)
        self.textInput = kivy.uix.textinput.TextInput(text=merged_string, size_hint=(1, None), height=max(self.minimum_height, scrlv.height))

        # Wrap the TextInput object in a ScrollView
        # scroll_view = ScrollView(do_scroll_x=False, size_hint=(1, None), height=300, bar_width=10, scroll_type=['bars'])
        scrlv.add_widget(self.textInput)
        
        # kver = kivy.__version__
        # bver = BoardShim.get_version()
        self.label = kivy.uix.label.Label(text=f"Your Message.")
        self.button = kivy.uix.button.Button(text="Click Me.")
        self.button.bind(on_press=self.displayMessage)
        self.boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.boxLayout.add_widget(scroll_view)
        self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.button)
        return self.boxLayout
    def displayMessage(self, btn):
        self.label.text = self.textInput.text

if __name__ == "__main__":
    simpleApp = SimpleApp()

simpleApp.run()
