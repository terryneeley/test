from guizero import App, Text, TextBox, PushButton
def say_my_name():
    welcome_message.set( my_name.get() )
app = App(title="Hello world")
welcome_message = Text(app, text="Welcome to my app", size=26, font="Helvetica", color="red")
update_text = PushButton(app, command=say_my_name, text="Display my name")
my_name = TextBox(app, width=20)
app.display()
