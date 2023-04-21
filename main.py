import kivy.uix.boxlayout
import kivy.uix.textinput
from kivy.uix.scrollview import ScrollView
import kivy.uix.label
import kivy.uix.button
#from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from kivy.app import App
from kivy.uix.button import Button


import sys
import pkg_resources


class SimpleApp(kivy.app.App):
    def build(self):
        li = []
        # Get a list of all installed packages
        # packages = pkg_resources.working_set
        packages = sorted(pkg_resources.working_set, key=lambda p: p.project_name.lower())

        for package in packages:
            li.append(f"{package.project_name} == {package.version}")
            # print(package.key, package.version)
        merged_string = 'python version ' + str(sys.version_info)+ '\n' + '\n'.join(li)
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
