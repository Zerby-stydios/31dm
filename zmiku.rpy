init:
    $ mods["zmiku"]=u"Микушная сказка"
    $ config.developer = True
    
    define school_ul = Character('Ульяна', color="#FFC618")
    
    image bg bridge_morning = "mods/zmiku/gfx/bg/bridge_morning.jpg"
    image bg bedroom = "mods/zmiku/gfx/bg/bedroom.jpg"
    image bg c_white = "mods/zmiku/gfx/bg/white.jpg"
    
    image cg mi_beach = "mods/zmiku/gfx/cg/mi_beach_p.png"
    
    image un zmb = "mods/zmiku/gfx/sp/un_zmb.png"
    image school_ul smule = "mods/zmiku/gfx/sp/school_ul_smule.png"
    image school_ul smule2 = "mods/zmiku/gfx/sp/school_ul_smule2.png"
    image school_ul angry = "mods/zmiku/gfx/sp/school_ul_angry.png"
    image school_ul tlen = "mods/zmiku/gfx/sp/school_ul_tlen.png"
    image school_ul wow = "mods/zmiku/gfx/sp/school_ul_wow.png"

label zmiku:
    $ prolog_time()
    $ persistent.sprite_time = "night"
    play music music_list["a_promise_from_distant_days"] fadein 4
    scene ext_camp_entrance_night with dissolve
    
    "Мне опять снился сон."
    "Этот сон…"
    "Каждую ночь одно и то же."
    "На утро, как обычно, всё забудется."
    "Может, быть, оно и к лучшему…"
    "Останутся только туманные воспоминания о приоткрытых, словно приглашающх куда-то воротах, рядом с которыми в камне застыли два пионера."
    "И вновь Мику…"
    "Которая постоянно спрашивает…"
    show mi shy pioneer with dissolve
    mi "Не хочешь прогуляться?"
    
    menu:
        "Конечно!":
            my "Конечно хочу!"
            my "Куда мы пойдем на этот раз?"
            show mi dontlike pioneer with dissolve
            mi "Пойдём на пляж?"
            my "Пойдем!"
            show ext_beach_night with dissolve
            scene cg mi_beach with dissolve
            mi "Красиво..."
            my "Да...{w}Мику.."
            mi "Что?"
            my "Всегда хотел спросить...где ты живешь?"
            mi "Ахаха{w} Хм..{w}Я живу.....{w}..{w}..{w}..{w}Я не скажу где я живу."
            my "Ну Мику!"
            mi "Неужели тебе это так важно?"
            my "Да не то, чтобы прямо важно..."
            mi "Ну вот, давай не будем тогда об этом. {w}Важно то, что сейчас мы вместе!"
            my "Да..."
            mi "Что-то холодно..{w} Пойдем обратно?"
            my "Пошли"
            show ext_beach_night with dissolve
            pause(0.3)
        "В другой раз":
            my "Прости, у меня сегодня много дел.{w}Давай в другой раз?"
            show mi sad pioneer with dissolve
            mi "Эх..."
            show mi grin pioneer with dissolve
            mi "Хорошо, в другой раз - так в другой раз!"
    
    show ext_no_bus_night with dissolve
    show mi normal pioneer with dissolve
    my "Увидимся!"
    mi "До встречи!"
    hide mi with dissolve
    
    "Она ушла."
    "Вoт так, каждый раз приходится решать."
    "Но на что влияют мои выборы? {w}Это мне, видимо, не узнать."
    "Как и не узнать то место, где я сейчас нахожусь."
    th "Я же сплю, так зачем мне все эти размышления? {w}Я же могу просто наслаждаться красотами этой непонятной мне локации..."
    th "Почему бы мне просто не пойти прямо, по дороге? {w}Хорошая идея..."
    
    scene ext_road_night2 with dissolve
    "На улице дул прохладный небольшой ветерок."
    "Мир только просылпался, поэтому встретить какое-либо живой существо было практически невозможно. {w}Да и в любом случае, это же просто сон..."
    "Спустя полчаса я пришел к мосту."
    
    scene bg bridge_morning with dissolve
    th "Какая же всё таки Мику милашка...{w} Жаль, что это просто сон...а я так бы хотел, чтобы она была настоящей..."
    th "Интересно, что это за речка?"
    stop music fadeout 4
    play sound sfx_punch_washstand
    show bg bridge_morning with flash_red
    play music music_list["doomed_to_be_defeated"] fadein 4
    "Я обернулся. {w}От увиденного меня скова ужас."
    show un zmb at center with dissolve
    "Передо мной стояло...{w}{b}ЧТО ЭТО ВООБЩЕ ТАКОЕ?!{/b}"
    "Это существо медленно двигало ртом, словно пытаясь что-то сказать"
    dreamgirl "Вста..."
    "Страх охватил меня, и я на автомате выкрикнул."
    my "{b}ПОШЛА НАХУЙ!{/b}"
    
    show un zmb at center:
        linear 0.1 zoom 2
    play sound sfx_punch_washstand
    show bg bridge_morning with flash_red
    show un zmb at center:
        linear 0.3 zoom 1
    
    "Мне стало ломить всё тело."
    "Существо всё еще пыталось что-то сказать."
    dreamgirl "Артём..."
    my "{b}ДА ХУЛИ ТЕБЕ ОТ МЕНЯ НАДО?{/b}"
    
    show un zmb at center:
        linear 0.1 zoom 2
    play sound sfx_punch_washstand
    scene bg c_white with flash_red
    pause(1)
    scene bg bedroom with dissolve
    $ persistent.sprite_time = "day"
    
    school_ul "ВСТАВАЙ Я СКАЗАЛА!"
    stop music fadeout 4
    show school_ul angry at center with dissolve:
        zoom 2
    my "Ульяна?"
    show school_ul tlen at center:
        linear 0.3 zoom 1
    play music music_list["i_want_to_play"] fadein 4
    school_ul "Нет, Блин, Таня"
    my "Какая Таня?"
    show school_ul smule2 at center with dissolve
    school_ul "Вечером увидишь. {w}Какого хера ты спать улёгся?"
    my "А что будет вечером?"
    show school_ul tlen at center with dissolve
    school_ul "Бля, я тебе походу память отшибла. {w}В школе у нас вечеринка.{w} Начинаем уже через час!"
    my "Что..."
    show school_ul angry at center:
        linear 0.1 zoom 2
    play sound sfx_punch_washstand
    school_ul "Я СКАЗАЛА ПОДЪЕМ!"
    my "Ладно, ладно, встаю..."
    show school_ul smule at center with dissolve
    school_ul "Мы тебя уже ждем, одевайся и подходи."
    my "Хорошо, через час подойду."
    show school_ul smule2 at center:
        linear 0.3 zoom 1
    school_ul "Ага."
    hide school_ul with dissolve
    "Даже не знаю, что меня волновало больше: то, что я накричал на Ульяну, или то, что она зашла в закрытый дом."
    
    
    
    



# label wefsfvgv:
    # #interfaces
    # $ prolog_time()
    # $ day_time()
    # $ sunset_time()
    # $ night_time()
    
    # #sprites
    # $ persistent.sprite_time = "day"
    # $ persistent.sprite_time = "sunset"
    # $ persistent.sprite_time = "night"
    
    # #avd mode
    # $ set_mode_adv()
    # window hide
    # window show
    
    # #nvl mode
    # $ set_mode_nvl()
    # nvl show dissolve
    # nvl hide dissolve 
    
    # #texts
    # "{alpha=0.1}Этот текст едва читаем!{/alpha}"
    # "Пример {b}текста, выделенного жирным шрифтом{/b}."
    # "{color=#f00}Красный{/color}, {color=#00ff00}Зелёный{/color}, {color=#0000ffff}Синий{/color}"
    # "Добро пожаловать в {i}СОЛ «Совёнок»!{/i}."
    # "Я очень надеюсь, что {s}тебе понравилось{/s}."
    # "Рада видеть {u}тебя{/u}!"
    # "Я{w} очень{w=1.0} рада!"
    
    # #scenes and sprites
    # scene bg ext_square_day with dissolve
    # show bg ext_square_night with dissolve
    # show dv angry pioneer
    
    # #eyes
    # show blink
    # show unblink
    # show blinking
    
    # #images
    # image bridge_morning = "mods/zmiku/gfx/bg/bridge_morning.jpg"
    
    # #dissolve_fast
    # #dissolve
    # #dissolve2
    
    # #fleft
    # #left
    # #cleft
    # #center
    # #cright
    # #right
    # #fright
    
    # #close
    # #far
    
    
    
