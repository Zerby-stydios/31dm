init:
    $ mods["z1miky"]=u"Неделя с Мику" #Название мода

label z1miky:
    jump z1m_test

label z1m_test:
    mi "Как же табя зовут?"
    th "Кажется, это мой шанс начать всё с нуля..."
    extend "Начну пожалуй со смены имени."
    
    $ player_name = renpy.input("Как меня будут звать?").strip() #Получение имени
    if player_name == "": #Проверка имени на пустоту
        $ player_name = "Артём"

    player_name "Меня зовут [player_name]!"
    extend " А как тебя?"
    mi "Меня зовут Мику! Приятно познакомиться:)"

label z1m_day1:
    $ sunset_time()
    play music music_list["no_tresspassing"]
    scene bg int_bus