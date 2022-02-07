init:
    $ mods["z1miky"]=u"Неделя с Мику"
	
label z1miky:
    jump z1m_day1

label z1m_day1:
    $ sunset_time()
    play music music_list["no_tresspassing"]
    scene bg int_bus
    
    

    