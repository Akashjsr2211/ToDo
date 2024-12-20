from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class TodoApp(App):
    def build(self):
        self.title = "To-Do List"

        # Main layout
        self.main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Input box for new tasks
        input_box = BoxLayout(size_hint_y=None, height="50dp")
        self.task_input = TextInput(hint_text="Enter a new task", multiline=False)
        add_button = Button(text="Add", size_hint_x=None, width="80dp")
        add_button.bind(on_press=self.add_task)
        input_box.add_widget(self.task_input)
        input_box.add_widget(add_button)
        self.main_layout.add_widget(input_box)

        # Scrollable task list
        self.scroll_view = ScrollView()
        self.task_list = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        self.scroll_view.add_widget(self.task_list)
        self.main_layout.add_widget(self.scroll_view)

        return self.main_layout

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:  # Add only if text is not empty
            task_box = BoxLayout(size_hint_y=None, height="50dp", spacing=10)
            task_label = Label(text=task_text, size_hint_x=0.8, halign="left", valign="middle")
            task_label.bind(size=task_label.setter('text_size'))

            delete_button = Button(text="Delete", size_hint_x=0.2)
            delete_button.bind(on_press=lambda btn: self.delete_task(task_box))

            task_box.add_widget(task_label)
            task_box.add_widget(delete_button)

            self.task_list.add_widget(task_box)
            self.task_input.text = ""  # Clear the input box

    def delete_task(self, task_box):
        self.task_list.remove_widget(task_box)

if __name__ == "__main__":
    TodoApp().run()
