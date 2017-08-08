from guizero import App, Combo, Text
app = App(title="My second GUI app", width=300, height=200, layout="grid")
film_description = Text(app, text="Which film?", grid=[0,0], align="left")
film_choice = Combo(app, options=["Star Wars", "Indiana Jones", "Batman"], grid=[0,1], align="left")
app.display()