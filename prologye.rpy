init:
    $ mods["z1miky"]=u"Неделя с Мику"

label z1miky:
    jump z1m_prologue

label z1m_prologue:
    th "Я раздумывал над тем, чтобы сменить моё имя."
    $ player_name = renpy.input("Как же мне тогда тебя звать?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Артём"

    th "[player_name], вроде звучит прикольно!"

label z1m_day1:
    $ sunset_time()
    play music music_list["no_tresspassing"]
    scene bg int_bus