init:
    $ mods["z1miky"]=u"Неделя с Мику"
    
label z1miky:
    $ sunset_time()
    play music music_list["no_tresspassing"]
    scene bg int_bus
    "В глаза ударил яркий солнечный свет."
    "Я находился в автобусе.."
    th "Но как я сюда попал?!"
    "Я вышел из автобуса"
    scene bg ext_bus
    "На улице было жарко."
    extend " Росла высокая зелёная трава."
    extend " Пели птицы."
    th "Подождите!"
    extend " Но ведь вчера была зима!"
    "Я обернулся."
    scene bg ext_camp_entrance_day
    extend " Передо мной стояли большие стальные ворота с надписью \"Совёнок\""
    th "Что так может называться?"
    extend " Школа?"
    extend " Детский сад?"
    extend " Музей?"
    "Собравшись с духом, я хотел сделать пару шагов в сторону ворот, но передо мной выросла высокая девушка."
    show mi smile pioneer at center with dissolve
    "Заметив меня, её лицо сменилось удивлением."
    show mi shocked pioneer at center with dissolve
    mi "П-п-привет!"
    menu:
        "Уебать её с ноги":
            "Ей это явно не понравилось"
        "Послать нахуй":
            "Ей это явно не понравилось"
    show mi cry pioneer at center with dissolve
    mi "Я-я ж-же просто хотел-ла познакомьтся..." 