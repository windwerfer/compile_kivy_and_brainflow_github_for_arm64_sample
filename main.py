import kivy.uix.boxlayout
import kivy.uix.textinput
import kivy.uix.label
import kivy.uix.button
# from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
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
        self.textInput = kivy.uix.textinput.TextInput(text=merged_string)
        # kver = kivy.__version__
        # bver = BoardShim.get_version()
        self.label = kivy.uix.label.Label(text=f"Your Message.")
        self.button = kivy.uix.button.Button(text="Click Me.")
        self.button.bind(on_press=self.displayMessage)
        self.boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.boxLayout.add_widget(self.textInput)
        self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.button)
        return self.boxLayout
    def displayMessage(self, btn):
        self.label.text = self.textInput.text

if __name__ == "__main__":
    simpleApp = SimpleApp()

simpleApp.run()
