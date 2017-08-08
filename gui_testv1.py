from guizero import App, Text, TextBox
app = App(title="Hello world")
welcome_message = Text(app, text="Welcome to my app", size=26, font="Helvetica", color="red")
my_name = TextBox(app, width=20)
app.display()
