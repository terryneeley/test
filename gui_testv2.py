from guizero import App, Combo, Text, CheckBox
app = App(title="My second GUI app", width=300, height=200, layout="grid")
film_description = Text(app, text="Which film?", grid=[0,0], align="left")
film_choice = Combo(app, options=["Star Wars", "Indiana Jones", "Batman"], grid=[0,1], align="left")
vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")
seat_typ = Text(app, text="Seat Type", grid=[1,0], align="left")
app.display()