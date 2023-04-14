from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.terminal import Terminal

Builder.load_string("""
<TerminalTab>:
    terminal: terminal
    Terminal:
        id: terminal
        font_size: '12sp'
        background_color: (0, 0, 0, 1)
        foreground_color: (1, 1, 1, 1)
        show_cursor: True
        multiline: False
        on_command: app.handle_terminal_command(self.text)
""")

class TerminalTab(TabbedPanelItem):
    pass

class StaticTab(TabbedPanelItem):
    pass

class MyTabbedApp(TabbedPanel):
    def handle_terminal_command(self, command):
        # Handle terminal command here
        print("Terminal command:", command)

class MyApp(App):
    def build(self):
        return MyTabbedApp()


if __name__ == '__main__':
    MyApp().run()
