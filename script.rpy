# Файл script.rpy - Основной сценарий игры

# --- Определение изображений фонов ---
image bg hall = "hall.png"
image bg extracurricular = "extracurricular.png"
image bg black = "black"
image bg logo = "college.png"
image bg priemnya = "priemnya.png"
image bg god = "god.png"

# --- Определение изображений персонажей (имена на латинице) ---
image principal smile = "AV_radost.png"
image principal sad = "AV_pechal.png"
image principal thoughtful = "AV_zadumchivost.png"
image principal interested = "AV_zainteresovannost.png"

image student smile = "EU_radost.png"
image student sad = "EU_pechal.png"
image student thoughtful = "EU_zadumchivost.png"
image student interested = "EU_zainteresovannost.png"

# --- ИЗОБРАЖЕНИЯ ПЕРСОНАЖА-АБИТУРИЕНТА (РАЗНЫЕ ЭМОЦИИ) ---
image player male = "male_student.png"
image player female = "female_student.png"
image player male rasteran = "male_student_rasteran.png"
image player female rasteran = "female_student_rasteran.png"
image player male smile = "male_student.png"
image player female smile = "female_student.png"

# --- ДОБАВЛЕНО: показ логотипа на чёрном фоне ---
image logo_display = "college.png"

# --- Определение изображений для внеучебной деятельности (ГАЛЕРЕИ) ---
# VIAR ASU (5 изображений)
image viar_0 = "viar.jpg"
image viar_1 = "viar1.jpg"
image viar_2 = "viar2.jpg"
image viar_3 = "viar3.jpg"
image viar_4 = "viar4.jpg"

# Театр (5 изображений)
image teatr_0 = "teatr.jpg"
image teatr_1 = "teatr1.jpg"
image teatr_2 = "teatr2.jpg"
image teatr_3 = "teatr3.jpg"
image teatr_4 = "teatr4.jpg"

# Волонтеры (6 изображений)
image volonter_0 = "volonter.jpg"
image volonter_1 = "volonter1.jpg"
image volonter_2 = "volonter2.jpg"
image volonter_3 = "volonter3.jpg"
image volonter_4 = "volonter4.jpg"
image volonter_5 = "volonter5.jpg"

# Спорт (4 изображения)
image sport_0 = "sport.jpg"
image sport_1 = "sport1.jpg"
image sport_2 = "sport2.jpg"
image sport_3 = "sport3.jpg"

# --- Определение музыки ---
define audio.gimn = "gimn.mp3"

# --- Определение персонажей ---
define dir = Character('Анна Валерьевна', who_color="#c8ffc8", who_outlines=[(2, "#0099cc")], image="principal")
define stud = Character('Евгения Юрьевна', who_color="#ffcc66", image="student")
define nv = Character(None, kind=nvl)

# --- ДОБАВЛЕНО: персонаж для ответов абитуриента ---
define player_char = Character('[player_name]', who_color="#ffffff")

# --- Переменные ---
default player_name = ""
default player_gender = "male"
default study_form = "fulltime"
default selected_specialty_code = ""
default selected_specialty_name = ""
default selected_specialty_duration = ""
default selected_specialty_budget = ""
default selected_specialty_paid = ""
default selected_specialty_profile = ""

# --- ПЕРЕМЕННЫЕ ДЛЯ ОПРОСА ПРЕДПОЧТЕНИЙ ---
default pref_subjects = ""
default pref_activity = ""
default pref_workplace = ""
default recommended_profile = ""
default current_edu_level = "grade9"

# --- Переходы и функции ---
init python:
    # Настройка громкости музыки (15% от максимума)
    renpy.music.set_volume(0.15, channel='music')
    
    def gender_ending():
        if player_gender == "female":
            return "а"
        return ""

    def get_form_name():
        if study_form == "fulltime":
            return "очной"
        return "заочной"
    
    def calculate_recommended_profile(subj, act, work):
        combo = subj + act + work
        
        if combo in ["AAA", "AAB", "ABA", "AGA"]:
            return "it"
        elif combo in ["BBB", "BBG", "BGB"]:
            return "economics"
        elif combo in ["VVV", "VVA", "VGV"]:
            return "science"
        elif combo in ["GVG", "GBG"]:
            return "design"
        elif combo in ["DGG"]:
            return "tourism"
        elif subj == "G":
            return "all"
        else:
            return "all"

# --- БАЗА ДАННЫХ СПЕЦИАЛЬНОСТЕЙ ---
init python:
    specialties_data = {
        "grade9": {
            "it": [
                {"code": "09.02.08", "name": "Интеллектуальные интегрированные системы", "duration": "2 года 10 месяцев", "budget": "25", "paid": "25", "qualification": "Техник по интеллектуальным интегрированным системам", "profile": "it",
                 "description": "Умный дом, интернет вещей, автоматизированные системы управления — это твоя среда.",
                 "skills": ["Проектировать архитектуру интеллектуальных систем", "Разрабатывать приложения для взаимодействия с ними", "Обслуживать и сопровождать интеллектуальные системы"]},
                {"code": "09.02.09", "name": "Веб-разработка", "duration": "2 года 10 месяцев", "budget": "25", "paid": "25", "qualification": "Разработчик веб-приложений", "profile": "it",
                 "description": "Фронтенд и бэкенд, клиентская и серверная части — ты освоишь всё.",
                 "skills": ["Проектировать и разрабатывать веб-ресурсы", "Администрировать и сопровождать информационные системы", "Работать с клиентской и серверной частями приложений"]},
                {"code": "09.02.11", "name": "Разработка и управление программным обеспечением", "duration": "3 года 10 месяцев", "budget": "30", "paid": "30", "qualification": "Разработчик программного обеспечения", "profile": "it",
                 "description": "Серьёзная, фундаментальная программа для тех, кто хочет управлять процессом разработки.",
                 "skills": ["Разрабатывать программное обеспечение разного уровня сложности", "Управлять процессом разработки", "Тестировать и сопровождать ПО"]},
                {"code": "09.02.12", "name": "Техническая эксплуатация и сопровождение информационных систем", "duration": "2 года 10 месяцев", "budget": "20", "paid": "30", "qualification": "Специалист по информационным системам", "profile": "it",
                 "description": "Ты будешь тем, кто обеспечивает стабильную работу IT-инфраструктуры.",
                 "skills": ["Эксплуатировать и сопровождать информационные системы", "Выявлять и устранять неисправности", "Обеспечивать бесперебойную работу IT-сервисов"]}
            ],
            "economics": [
                {"code": "38.02.03", "name": "Операционная деятельность в логистике", "duration": "2 года 10 месяцев", "budget": "30", "paid": "30", "qualification": "Логист", "profile": "economics",
                 "description": "Как товары попадают с завода на полку магазина? Логист.",
                 "skills": ["Организовывать перевозки и складскую работу", "Управлять запасами и закупками", "Оптимизировать логистические процессы"]},
                {"code": "38.02.06", "name": "Финансы", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Финансист", "profile": "economics",
                 "description": "Деньги — это ресурс, и ты научишься им управлять.",
                 "skills": ["Планировать финансы организаций и бюджетов", "Проводить финансовый анализ и оценку рисков", "Работать с налогами и бюджетами РФ"]},
                {"code": "40.02.04", "name": "Юриспруденция", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Юрист", "profile": "economics",
                 "description": "Широкая юридическая подготовка.",
                 "skills": ["Осуществлять правоприменительную деятельность", "Оказывать юридическую помощь", "Обеспечивать правовую поддержку организаций"]}
            ],
            "science": [
                {"code": "18.02.12", "name": "Технология аналитического контроля химических соединений", "duration": "3 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Техник-химик", "profile": "science",
                 "description": "Лаборатории, анализы, контроль качества.",
                 "skills": ["Проводить качественные и количественные анализы", "Работать с химическим оборудованием", "Контролировать качество продукции"]},
                {"code": "25.02.08", "name": "Эксплуатация беспилотных авиационных систем", "duration": "3 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по БПЛА", "profile": "science",
                 "description": "Дроны — это не игрушки, а серьёзная техника.",
                 "skills": ["Пилотировать беспилотники разных типов", "Обслуживать и ремонтировать БПЛА", "Работать с полезной нагрузкой и обработкой данных"]}
            ]
        },
        "grade11": {
            "it": [
                {"code": "09.02.09", "name": "Веб-разработка", "duration": "1 год 10 месяцев", "budget": "25", "paid": "25", "qualification": "Разработчик веб-приложений", "profile": "it",
                 "description": "Максимально быстрый вход в IT.",
                 "skills": ["Создавать веб-приложения «под ключ»", "Администрировать и поддерживать сайты", "Работать с базами данных"]}
            ],
            "economics": [
                {"code": "38.02.03", "name": "Операционная деятельность в логистике", "duration": "1 год 10 месяцев", "budget": "25", "paid": "25", "qualification": "Логист", "profile": "economics",
                 "description": "Ускоренный курс по управлению цепочками поставок.",
                 "skills": ["Организовывать перевозки и складирование", "Управлять закупками и запасами", "Оптимизировать логистику"]},
                {"code": "40.02.04", "name": "Юриспруденция", "duration": "1 год 10 месяцев", "budget": "75", "paid": "75", "qualification": "Юрист", "profile": "economics",
                 "description": "Самая быстрая юридическая программа.",
                 "skills": ["Применять право на практике", "Оказывать юридическую помощь", "Работать с документами и законодательством"]}
            ]
        },
        "extramural": [
            {"code": "09.02.08", "name": "Интеллектуальные интегрированные системы", "duration": "2 года 6 месяцев (заочная)", "budget": "25", "paid": "25", "qualification": "Техник по интеллектуальным интегрированным системам", "profile": "it",
             "description": "Заочная форма для тех, кто хочет освоить профессию в сфере умных систем.",
             "skills": ["Проектировать архитектуру интеллектуальных систем", "Обслуживать и сопровождать интеллектуальные системы"]},
            {"code": "40.02.04", "name": "Юриспруденция", "duration": "2 года 6 месяцев (заочная)", "budget": "25", "paid": "25", "qualification": "Юрист", "profile": "economics",
             "description": "Заочное юридическое образование.",
             "skills": ["Применять право на практике", "Оказывать юридическую помощь", "Работать с документами и законодательством"]}
        ]
    }

# --- Позиции ---
transform left:
    xalign 0.15 yalign 1.0

transform right:
    xalign 0.85 yalign 1.0

transform center:
    xalign 0.5 yalign 1.0

# --- КРАСИВЫЕ АНИМИРОВАННЫЕ ТРАНСФОРМЫ ДЛЯ ОКНА АНАЛИЗА ---
transform analysis_window:
    xalign 0.5 yalign 0.5
    zoom 0.0
    alpha 0.0
    linear 0.3 zoom 1.0 alpha 1.0
    
transform analysis_window_exit:
    linear 0.3 zoom 0.0 alpha 0.0

transform loading_spinner:
    rotate 0
    linear 1.0 rotate 360
    repeat

# --- ДОБАВЛЕНО: позиция для логотипа по центру ---
transform logo_center:
    xalign 0.5 yalign 0.4
    zoom 0.6

# --- ПОЗИЦИЯ ДЛЯ ИЗОБРАЖЕНИЙ МЕЖДУ ПЕРСОНАЖАМИ ---
transform between_characters:
    xalign 0.5 yalign 0.35
    zoom 0.6

# --- ЭКРАН С ЛОГОТИПОМ (ПО КЛИКУ) ---
screen logo_screen():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xpadding 0 ypadding 0
        background None
        add "logo_display" at logo_center
        text "Нажмите, чтобы продолжить..." size 16 color "#aaaaaa" xalign 0.5 yalign 0.95
    key "K_SPACE" action Return()
    key "K_RETURN" action Return()
    key "K_KP_ENTER" action Return()
    key "mouseup_1" action Return()

# --- КРАСИВОЕ ОКНО ДЛЯ ТЕКСТА "ДОБРО ПОЖАЛОВАТЬ" (ПО КЛИКУ) ---
screen welcome_message():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xpadding 40 ypadding 30
        background Frame("gui/frame.png", gui.frame_borders)
        at analysis_window
        vbox:
            spacing 20
            xalign 0.5
            text "Добро пожаловать в колледж!" size 36 color "#c8ffc8" bold True xalign 0.5
    key "K_SPACE" action Return()
    key "K_RETURN" action Return()
    key "K_KP_ENTER" action Return()
    key "mouseup_1" action Return()

# --- КРАСИВОЕ ОКНО ДЛЯ АНАЛИЗА ПРЕДПОЧТЕНИЙ (ПО КЛИКУ) ---
screen analysis_screen():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xsize 500 ysize 220
        background Frame("gui/frame.png", gui.frame_borders)
        at analysis_window
        vbox:
            spacing 20
            xalign 0.5 yalign 0.5
            text "Анализ предпочтений" size 28 color "#ffcc66" bold True xalign 0.5
            hbox:
                xalign 0.5
                spacing 10
                text "●" size 40 color "#c8ffc8" at loading_spinner
                text "●" size 40 color "#ffcc66" at loading_spinner
                text "●" size 40 color "#c8ffc8" at loading_spinner
            text "Обработка ответов..." size 18 color "#ffffff" xalign 0.5
            text "Нажмите, чтобы продолжить..." size 14 color "#aaaaaa" xalign 0.5
    key "K_SPACE" action Return()
    key "K_RETURN" action Return()
    key "K_KP_ENTER" action Return()
    key "mouseup_1" action Return()

# --- ЭКРАН КРАСИВОГО РЕЗУЛЬТАТА РЕКОМЕНДАЦИИ (ПО КЛИКУ) ---
screen recommendation_result(profile_name, message):
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xsize 750
        background Frame("gui/frame.png", gui.frame_borders)
        at analysis_window
        vbox:
            spacing 20
            xfill True
            text "✨ Рекомендованный профиль ✨" size 24 color "#c8ffc8" xalign 0.5
            text profile_name size 34 color "#ffcc66" bold True xalign 0.5
            text message size 20 color "#ffffff" xalign 0.5 text_align 0.5
            text "Нажмите, чтобы продолжить..." size 14 color "#aaaaaa" xalign 0.5
    key "K_SPACE" action Return()
    key "K_RETURN" action Return()
    key "K_KP_ENTER" action Return()
    key "mouseup_1" action Return()

# --- ЭКРАН ВЫБОРА СПЕЦИАЛЬНОСТИ С РЕКОМЕНДАЦИЕЙ (КРАСИВЫЙ) ---
screen specialty_chooser_with_recommendation():
    modal True
    
    add "gui/overlay/confirm.png"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 550
        ysize 400
        background Frame("gui/frame.png", gui.frame_borders)
        padding (30, 30)
        
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            
            if recommended_profile != "all":
                frame:
                    background Frame("gui/frame.png", gui.frame_borders)
                    xfill True
                    padding (25, 20)
                    vbox:
                        spacing 8
                        text "✨ РЕКОМЕНДОВАННЫЙ ПРОФИЛЬ ✨" size 18 color "#c8ffc8" bold True xalign 0.5
                        text "«[recommended_profile]»" size 26 color "#ffcc66" bold True xalign 0.5
                
                text "Что скажешь?" size 22 color "#ffffff" xalign 0.5
            
            vbox:
                spacing 12
                xalign 0.5
                xsize 380
                
                if recommended_profile != "all":
                    textbutton "🎯 Показать рекомендованный профиль":
                        action [Hide("specialty_chooser_with_recommendation"), ShowMenu("specialty_chooser_filtered", profile=recommended_profile)]
                        style "recommend_button"
                        xfill True
                
                textbutton "📋 Показать все специальности":
                    action [Hide("specialty_chooser_with_recommendation"), ShowMenu("specialty_chooser")]
                    style "recommend_button"
                    xfill True
                
                textbutton "🤔 Я ещё не определился":
                    action [Hide("specialty_chooser_with_recommendation"), ShowMenu("specialty_chooser")]
                    style "recommend_button"
                    xfill True

# Стили для кнопок
style recommend_button:
    background Frame("gui/button/choice_idle_background.png", 10, 10)
    hover_background Frame("gui/button/choice_hover_background.png", 10, 10)
    xsize 380
    ysize 55
    xpadding 15
    ypadding 10

style recommend_button_text:
    color "#ffffff"
    hover_color "#ffcc66"
    size 18
    textalign 0.5

# --- ЭКРАН СПЕЦИАЛЬНОСТЕЙ С ФИЛЬТРАЦИЕЙ ПО ПРОФИЛЮ ---
screen specialty_chooser_filtered(profile):
    tag menu
    use game_menu("Выберите специальность - " + profile, scroll="viewport"):
        vbox:
            spacing 15
            
            if profile == "it":
                label "Информационные технологии" style "game_menu_label_text"
                for spec in specialties_data[current_edu_level]["it"]:
                    textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)
            elif profile == "economics":
                label "Экономика, право, управление и логистика" style "game_menu_label_text"
                for spec in specialties_data[current_edu_level]["economics"]:
                    textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)
            elif profile == "science":
                label "Технические и естественные науки" style "game_menu_label_text"
                for spec in specialties_data[current_edu_level]["science"]:
                    textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)
            else:
                label "Все специальности" style "game_menu_label_text"
                use specialties_all
            
            textbutton "Посмотреть другие профили" action ShowMenu("specialty_chooser") style "navigation_button" xalign 0.5

# --- ЭКРАН ВСЕХ СПЕЦИАЛЬНОСТЕЙ ---
screen specialties_all():
    vbox:
        spacing 10
        label "Информационные технологии" style "pref_label_text"
        for spec in specialties_data[current_edu_level]["it"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)
        
        label "Экономика, право, управление и логистика" style "pref_label_text"
        for spec in specialties_data[current_edu_level]["economics"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)
        
        if current_edu_level == "grade9":
            if "science" in specialties_data[current_edu_level]:
                label "Технические и естественные науки" style "pref_label_text"
                for spec in specialties_data[current_edu_level]["science"]:
                    textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

# --- ЭКРАН ВЫБОРА СПЕЦИАЛЬНОСТИ (ОСНОВНОЙ) ---
screen specialty_chooser():
    tag menu
    use game_menu("Выберите специальность", scroll="viewport"):
        vbox:
            spacing 15
            label "Уровень образования" style "game_menu_label_text"
            hbox:
                spacing 10
                textbutton "После 9 класса":
                    action SetVariable("current_edu_level", "grade9")
                    style "navigation_button"
                textbutton "После 11 класса":
                    action SetVariable("current_edu_level", "grade11")
                    style "navigation_button"
                if study_form == "extramural":
                    textbutton "Заочная (11 классов)":
                        action SetVariable("current_edu_level", "extramural")
                        style "navigation_button"
            
            if current_edu_level == "grade9":
                use specialties_grade9
            elif current_edu_level == "grade11":
                use specialties_grade11
            elif current_edu_level == "extramural":
                use specialties_extramural

# --- ЭКРАНЫ СПЕЦИАЛЬНОСТЕЙ ДЛЯ РАЗНЫХ УРОВНЕЙ ---
screen specialties_grade9():
    vbox:
        spacing 10
        label "Информационные технологии" style "pref_label_text"
        for spec in specialties_data["grade9"]["it"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)
        
        label "Экономика, право, управление и логистика" style "pref_label_text"
        for spec in specialties_data["grade9"]["economics"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)
        
        label "Технические и естественные науки" style "pref_label_text"
        for spec in specialties_data["grade9"]["science"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

screen specialties_grade11():
    vbox:
        spacing 10
        label "Информационные технологии" style "pref_label_text"
        for spec in specialties_data["grade11"]["it"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)
        
        label "Экономика, право, управление и логистика" style "pref_label_text"
        for spec in specialties_data["grade11"]["economics"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

screen specialties_extramural():
    vbox:
        spacing 10
        for spec in specialties_data["extramural"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

# --- ЭКРАН ДЕТАЛЬНОГО ОПИСАНИЯ СПЕЦИАЛЬНОСТИ ---
screen specialty_detail(spec):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background Frame("gui/frame.png", gui.frame_borders)
        viewport:
            scrollbars "vertical"
            mousewheel True
            vbox:
                spacing 15
                label spec['name'] style "game_menu_label_text"
                text "Код: [spec['code']]" size 24
                text "Срок обучения: [spec['duration']]"
                text "Бюджетных мест: [spec['budget']]"
                text "Платных мест: [spec['paid']]"
                text "Квалификация: [spec['qualification']]" bold True
                text spec['description']
                text "Чему научишься:" bold True
                for skill in spec['skills']:
                    text "• [skill]" size 24
                hbox:
                    spacing 20
                    xalign 0.5
                    textbutton "Выбрать":
                        action [SetVariable("selected_specialty_code", spec['code']),
                                SetVariable("selected_specialty_name", spec['name']),
                                SetVariable("selected_specialty_duration", spec['duration']),
                                SetVariable("selected_specialty_budget", spec['budget']),
                                SetVariable("selected_specialty_paid", spec['paid']),
                                SetVariable("selected_specialty_profile", spec['profile']),
                                Return()]
                    textbutton "Назад" action Hide("specialty_detail")
    
    textbutton "X" action Hide("specialty_detail") xalign 1.0 yalign 0.0

# --- Игра ---
label start:
    # Включаем фоновую музыку (гимн колледжа) на громкости 15%
    play music gimn volume 0.15 loop
    
    # --- КРАСИВЫЙ ПОКАЗ ЛОГОТИПА НА ЧЁРНОМ ФОНЕ (ПО КЛИКУ) ---
    scene bg black
    with dissolve
    
    call screen logo_screen
    hide screen logo_screen
    with dissolve
    
    pause 0.5

    # --- КРАСИВОЕ ПРИВЕТСТВИЕ В ОКНЕ (ПО КЛИКУ) ---
    scene bg black
    call screen welcome_message
    hide screen welcome_message
    with dissolve

    scene bg hall
    call screen choose_gender
    hide screen choose_gender

    scene bg hall with fade
    show principal smile at left
    
    # Показываем выбранного персонажа
    if player_gender == "female":
        show player female at right
    else:
        show player male at right

    dir "Здравствуйте! Вы, судя по взволнованному взгляду, к нам впервые? Я — Прасолова Анна Валерьевна, директор этого колледжа. Давайте знакомиться. Как вас зовут?"

    python:
        player_name = renpy.input("Введите ваше имя:", length=32)
        if not player_name:
            player_name = "Абитуриент"

    dir "Очень приятно, [player_name]! Скажите, а вы уже окончили школу или ещё учитесь? От этого зависит, какие двери перед вами откроются."

    menu:
        "Хочу полностью погрузиться в студенческую жизнь. Пары каждый день, общение с одногруппниками, практика в современных лабораториях, участие в мероприятиях.":
            $ study_form = "fulltime"
            dir "Отличный выбор! Очное отделение — это максимальное погружение. Это классическое студенчество — яркое, насыщенное и незабываемое."
        "Мне нужно совмещать учёбу с работой или другими делами. Хочу учиться в своём темпе.":
            $ study_form = "extramural"
            dir "Разумный подход! Заочная форма даёт гибкость. Ты самостоятельно изучаешь материал, а несколько раз в год приезжаешь на установочные и экзаменационные сессии."

    # --- НОВЫЙ БЛОК: ОПРОС ПРЕДПОЧТЕНИЙ АБИТУРИЕНТА ---
    call preferences_survey from _call_preferences_survey
    
    # --- ПЕРЕХОД К ВЫБОРУ СПЕЦИАЛЬНОСТИ С УЧЁТОМ РЕКОМЕНДАЦИИ ---
    call screen specialty_chooser_with_recommendation

    # --- После выбора специальности ---
    call final_congratulation from _call_final_congratulation
    jump extracurricular

    return

# --- ФИНАЛЬНОЕ ПОЗДРАВЛЕНИЕ ---
label final_congratulation:
    scene bg hall with fade
    show principal smile at left
    if player_gender == "female":
        show player female at right
    else:
        show player male at right

    if selected_specialty_profile == "it":
        dir "[player_name], поздравляю! Ты выбрал[gender_ending()] «[selected_specialty_name]» — одну из самых перспективных сфер современности. Мир держится на коде, алгоритмах и цифровых решениях. [selected_specialty_duration] в [get_form_name()] форме — и ты будешь готов[gender_ending()] создавать технологии будущего."
    elif selected_specialty_profile == "economics":
        dir "[player_name], с выбором! «[selected_specialty_name]» — это надёжный фундамент для карьеры. Финансы, логистика, юриспруденция — сферы, где ценят профессионалов. За [selected_specialty_duration] [get_form_name()] формы ты получишь не просто диплом, а реальные навыки, которые помогут тебе зарабатывать и помогать людям."
    elif selected_specialty_profile == "science":
        dir "[player_name], отличный выбор! «[selected_specialty_name]» — для тех, кто хочет менять мир вокруг себя. [selected_specialty_duration] [get_form_name()] формы пролетят незаметно, а навыки останутся на всю жизнь."
    else:
        dir "[player_name], решение принято! «[selected_specialty_name]», форма обучения — [get_form_name()], срок — [selected_specialty_duration]. Теперь ты знаешь, куда идти. Впереди — годы учёбы, дружбы, открытий и побед. Добро пожаловать в колледж!"

    dir "Ты выбрал[gender_ending()] «[selected_specialty_name]». Срок обучения — [selected_specialty_duration], и у нас есть [selected_specialty_budget] бюджетных мест и [selected_specialty_paid] платных. Ты сделал[gender_ending()] первый шаг к своей профессии. Но запомни: в колледже жизнь не ограничивается парами. Оглянись!"

    return

# --- БЛОК ОПРОСА ПРЕДПОЧТЕНИЙ ---
label preferences_survey:
    scene bg hall with fade
    show principal thoughtful at left
    if player_gender == "female":
        show player female at right
    else:
        show player male at right
    
    dir "[player_name], прежде чем мы перейдём к специальностям, давай я немного узнаю о твоих интересах и способностях. Это поможет нам подобрать тебе специальность"
    
    dir "Какие школьные предметы тебе нравятся больше всего? Что тебе легче даётся?"
    
    menu:
        "Математика, информатика, физика":
            $ pref_subjects = "A"
            player_char "Обожаю решать задачи, разбираться в алгоритмах, программировать. Логика и точные науки — моё!"
        "Русский язык, литература, история, обществознание":
            $ pref_subjects = "B"
            player_char "Мне нравится работать с текстами, анализировать, разбираться в законах, истории и обществе."
        "Химия, биология, география":
            $ pref_subjects = "V"
            player_char "Меня привлекает природа, эксперименты, изучение живых организмов и окружающего мира."
        "Иностранный язык, искусство":
            $ pref_subjects = "G"
            player_char "Творчество, языки, дизайн, создание чего-то нового и красивого — вот что меня вдохновляет."
        "Физкультура, труд, ОБЖ":
            $ pref_subjects = "D"
            player_char "Больше практики, меньше теории. Люблю работать руками или быть в движении."
    
    dir "Понятно-понятно. А теперь ещё один вопрос: каким делом ты хотел[gender_ending()] бы заниматься в будущем? Куда тянется душа?"
    
    menu:
        "Создавать новые технологии, писать программы, разрабатывать сайты и приложения":
            $ pref_activity = "A"
            player_char "Хочу быть в IT, создавать цифровые продукты, возможно, заниматься кибербезопасностью."
        "Работать с людьми, помогать им, консультировать, организовывать процессы":
            $ pref_activity = "B"
            player_char "Люблю общение, хочу быть юристом, логистом, работать в туризме или финансах."
        "Работать в лаборатории, исследовать, проводить анализы, следить за экологией":
            $ pref_activity = "V"
            player_char "Хочу работать с химией, биологией, экологией, возможно, управлять дронами или заниматься дизайном."
        "Пока не определился(ась), но хочу попробовать разное и понять":
            $ pref_activity = "G"
            player_char "Интересы меняются, хочу посмотреть все варианты и выбрать то, что откликнется."
    
    dir "И последний вопрос, [player_name]: как ты видишь своё идеальное рабочее место?"
    
    menu:
        "За компьютером в современном офисе или удалённо":
            $ pref_workplace = "A"
            player_char "Люблю работать с техникой, могу часами сидеть за кодом или дизайном."
        "В коллективе, где нужно общаться, обсуждать, решать задачи вместе":
            $ pref_workplace = "B"
            player_char "Одиночество — не моё, хочу работать в команде и с людьми."
        "В лаборатории, на производстве, в поле, с техникой и приборами":
            $ pref_workplace = "V"
            player_char "Хочу практическую работу с оборудованием, материалами, возможно, выезды на объекты."
        "В творческой студии, в движении, на событиях, в путешествиях":
            $ pref_workplace = "G"
            player_char "Не люблю сидеть на месте, хочу создавать что-то красивое или быть в эпицентре событий."
    # Анализ и рекомендация
    dir "Спасибо за откровенность, [player_name]. Я услышал[gender_ending()] тебя. Давай посмотрим, что у нас получилось..."
    
    # --- КРАСИВОЕ ОКНО АНАЛИЗА ПРЕДПОЧТЕНИЙ (ПО КЛИКУ) ---
    call screen analysis_screen
    hide screen analysis_screen
    with dissolve
    
    $ recommended_profile = calculate_recommended_profile(pref_subjects, pref_activity, pref_workplace)
    
    # --- КРАСИВО ОФОРМЛЕННЫЙ РЕЗУЛЬТАТ В РАМКЕ (ПО КЛИКУ) ---
    if recommended_profile == "it":
        call screen recommendation_result("Информационные технологии", "Ты любишь логику, хочешь создавать цифровые продукты и готов работать за компьютером. Это твоё!")
        hide screen recommendation_result
    elif recommended_profile == "economics":
        call screen recommendation_result("Экономика, право, управление и логистика", "Ты любишь работать с людьми, анализировать и организовывать процессы.")
        hide screen recommendation_result
    elif recommended_profile == "science":
        call screen recommendation_result("Технические и естественные науки", "Ты любишь исследования, эксперименты и практическую работу.")
        hide screen recommendation_result
    elif recommended_profile == "design":
        call screen recommendation_result("Дизайн, туризм, реклама", "Ты любишь создавать что-то новое и красивое.")
        hide screen recommendation_result
    elif recommended_profile == "tourism":
        call screen recommendation_result("Туризм, спорт, события", "Ты любишь движение, практику и работу с людьми.")
        hide screen recommendation_result
    else:
        call screen recommendation_result("Широкий спектр направлений", "Твои интересы довольно широкие. У тебя есть время попробовать разное! Обрати внимание на направления, которые тебе откликнутся.")
        hide screen recommendation_result
    
    

# --- ВНЕУЧЕБНАЯ ДЕЯТЕЛЬНОСТЬ (ГАЛЕРЕИ) ---
label extracurricular:
    scene bg hall with fade
    show principal interested at left
    if player_gender == "female":
        show player female at right
    else:
        show player male at right

    dir "А теперь Евгения Юрьевна расскажет тебе про документы и поступление."

    # --- ВЫЗОВ НОВОГО ДИАЛОГА НА ПРИЁМНОЙ КОМИССИИ ---
    call priem_dialog from _call_priem_dialog

    # --- ВОЗВРАЩАЕМСЯ К ВНЕУЧЕБНОЙ ДЕЯТЕЛЬНОСТИ (КРУЖКИ) ---
    scene bg hall with fade
    show principal interested at left
    if player_gender == "female":
        show player female at right
    else:
        show player male at right

    dir "Оглянись! У нас кипит внеучебная жизнь."

    hide principal with moveoutleft
    show student smile at left

    stud "У нас все ребята талантливые, и для каждого найдется свой кружок!"

    scene bg extracurricular with fade
    show student smile at left
    if player_gender == "female":
        show player female at right
    else:
        show player male at right
    
    # --- VIAR ASU (галерея) ---
    show student thoughtful at left
    with dissolve
    stud "Обьединение VIAR ASU - это ребята, которые воплощают в жизнь самые крутые идеи в мире IT."
    
    call screen gallery_viar
    
    # --- Творческое сердце (театр) ---
    show student thoughtful at left
    with dissolve
    stud "А здесь творческое сердце. Музыка, театр, танцы."
    
    call screen gallery_teatr
    
    # --- Волонтерский отряд ---
    show student thoughtful at left
    with dissolve
    stud 'А это Волонтерский отряд "Бумеранг". Помощь приютам, экологические акции.'
    
    call screen gallery_volonter
    
    # --- Спортивный клуб ---
    show student thoughtful at left
    with dissolve
    stud "Вот Спортивный клуб. Баскетбол, волейбол — для тех, кто хочет держать себя в форме."
    
    call screen gallery_sport

    show student smile at left
    with dissolve
    stud "Ну как? Глаза разбегаются? Это только малая часть!"

    stud "Лови момент, [player_name]! Именно здесь ты найдешь друзей и дело по душе."
    
    # --- ФИНАЛ: только фото god.png, без персонажей и реплик ---
    scene bg god with fade
    
    show screen final_message with dissolve
    pause 3.0
    hide screen final_message with dissolve
    
    # --- ВОЗВРАТ К ВЫБОРУ СПЕЦИАЛЬНОСТЕЙ ---
    jump return_to_specialties

# --- ВОЗВРАТ К ВЫБОРУ СПЕЦИАЛЬНОСТЕЙ ---
label return_to_specialties:
    scene bg hall with fade
    show principal interested at left
    if player_gender == "female":
        show player female at right
    else:
        show player male at right
    
    dir "[player_name], хочешь ещё раз посмотреть специальности или, может быть, выбрать другую?"
    
    menu:
        "Да, хочу посмотреть специальности ещё раз":
            call screen specialty_chooser_with_recommendation
            call final_congratulation from _call_final_congratulation_1
            jump return_to_specialties
        
        "Нет, я уже определился(ась), спасибо!":
            dir "Отлично! Тогда ждём тебя с документами. Удачи!"
            
            show screen final_message with dissolve
            pause 3.0
            hide screen final_message with dissolve
            


# --- НОВЫЙ ДИАЛОГ С ЕВГЕНИЕЙ ЮРЬЕВНОЙ НА ПРИЁМНОЙ КОМИССИИ (КОРОТКИЙ ОСНОВНОЙ ДИАЛОГ) ---
# --- НОВЫЙ ДИАЛОГ С ЕВГЕНИЕЙ ЮРЬЕВНОЙ НА ПРИЁМНОЙ КОМИССИИ (КОРОТКИЙ ОСНОВНОЙ ДИАЛОГ) ---
label priem_dialog:
    scene bg priemnya with fade
    show student smile at left
    
    # Показываем растерянного персонажа
    if player_gender == "female":
        show player female rasteran at right
    else:
        show player male rasteran at right
    
    stud "Привет! Я вижу, ты изучаешь наш стенд. Давай знакомиться — Евгения Юрьевна, ответственный секретарь приемной комиссии."
    
    # --- КОРОТКИЙ ОСНОВНОЙ ДИАЛОГ ---
    stud "Для поступления в наш колледж нужны: паспорт, аттестат, СНИЛС (если есть) и 4 фото 3×4. Подать документы можно лично в приёмной комиссии, онлайн через сайт или Госуслуги, а также почтой."
    stud "Приём документов на очную форму — до 10-15 августа, на заочную — до 23 сентября. Оригинал аттестата нужно принести до 15-18 августа (для очников) или до 23 сентября (для заочников)."
    stud "Вступительные испытания нужны только на три специальности: Дизайн, Правоохранительная деятельность и Реклама. На остальные — зачисление по среднему баллу аттестата."
    stud "Общежитие предоставляется студентам с 18 лет. Адреса: Полярная, 34 и Червонная, 5."
    
    # --- ДОПОЛНИТЕЛЬНЫЕ ВОПРОСЫ (ЭКРАН С КНОПКАМИ) ---
    stud "У меня ещё есть несколько минут. Может, у тебя остались какие-то вопросы? Смотри, вот список того, о чём часто спрашивают абитуриенты."
    
    jump priem_questions_loop

# --- ЦИКЛ ДОПОЛНИТЕЛЬНЫХ ВОПРОСОВ ---
label priem_questions_loop:
    call screen priem_questions
    $ selected_question = _return
    
    # Если выбран пропуск
    if selected_question == "skip":
        stud "Ну что ж, тогда пойдём дальше!"
        jump priem_dialog_end
    
    # Если выбран режим "все вопросы подряд"
    if selected_question == "all":
        call priem_extra_lgoty from _call_priem_extra_lgoty
        call priem_extra_documents from _call_priem_extra_documents
        call priem_extra_submit from _call_priem_extra_submit
        call priem_extra_deadlines from _call_priem_extra_deadlines
        call priem_extra_exams from _call_priem_extra_exams
        call priem_extra_dorm from _call_priem_extra_dorm
        call priem_extra_schedule from _call_priem_extra_schedule
        # После всех вопросов спрашиваем, хочет ли продолжить
        menu:
            stud "Это были все вопросы. Хочешь задать ещё что-то или пойдём дальше?"
            "Задать ещё вопрос":
                jump priem_questions_loop
            "Пойдём дальше":
                jump priem_dialog_end
    else:
        # Отвечаем на выбранный вопрос
        if selected_question == "lgoty":
            call priem_extra_lgoty from _call_priem_extra_lgoty_1
        elif selected_question == "documents":
            call priem_extra_documents from _call_priem_extra_documents_1
        elif selected_question == "submit":
            call priem_extra_submit from _call_priem_extra_submit_1
        elif selected_question == "deadlines":
            call priem_extra_deadlines from _call_priem_extra_deadlines_1
        elif selected_question == "exams":
            call priem_extra_exams from _call_priem_extra_exams_1
        elif selected_question == "dorm":
            call priem_extra_dorm from _call_priem_extra_dorm_1
        elif selected_question == "schedule":
            call priem_extra_schedule from _call_priem_extra_schedule_1
        
        # После ответа на вопрос спрашиваем, хочет ли абитуриент задать ещё вопрос
        menu:
            stud "Хочешь задать ещё вопрос?"
            "Да, задать ещё вопрос":
                jump priem_questions_loop
            "Нет, пойдём дальше":
                jump priem_dialog_end
    
    label priem_dialog_end:
        stud "Так, а теперь пошли, покажу тебе наших!"
        return

# --- ДОПОЛНИТЕЛЬНЫЕ ОТВЕТЫ НА ВОПРОСЫ (ПОДРОБНЫЕ) ---

label priem_extra_lgoty:
    player_char "Кто имеет право на первоочередное зачисление?"
    stud "Право на первоочередное зачисление имеют:"
    stud "• Герои Российской Федерации и награждённые тремя орденами Мужества."
    stud "• Участники СВО (военнослужащие, добровольцы, сотрудники правоохранительных органов)."
    stud "• Мобилизованные граждане и заключившие контракт о добровольном содействии."
    stud "• Ветераны боевых действий ДНР и ЛНР с 2014 года."
    stud "• Дети всех перечисленных выше категорий."
    stud "• Дети военнослужащих, участвовавших в боевых действиях за границей."
    stud "• Дети медицинских работников, погибших от COVID-19 (только для медицинских специальностей)."
    stud "Подтверждающие документы: справка из воинской части или военкомата, удостоверение Героя РФ или удостоверение к ордену Мужества."
    return

label priem_extra_documents:
    player_char "Какие документы нужны для поступления?"
    stud "Базовый пакет: паспорт, аттестат, СНИЛС (если есть), 4 фото 3×4. Если есть льгота — документ на неё. Если вы иностранец — перевод аттестата на русский язык, заверенный нотариально. Если есть грамоты и дипломы — берите, это индивидуальные достижения."
    return

label priem_extra_submit:
    player_char "Как и где подать документы?"
    stud "Три способа:"
    stud "1. Лично — по адресам: Барнаул (пр. Ленина, 61), Бийск (ул. Социалистическая, 23/1), Рубцовск (пр. Ленина, 200Б), Славгород (ул. Р. Люксембург, 75)."
    stud "2. Онлайн — через личный кабинет на сайте АГУ или Госуслуги."
    stud "3. Почтой — заказным письмом по адресу: 656049, Барнаул, пр. Ленина, 61."
    stud "Бланки заявления и согласия на обработку персональных данных есть на сайте."
    return

label priem_extra_deadlines:
    player_char "До какого числа можно подать документы?"
    stud "Очная форма: последний день приёма документов — 10 августа (с вступительными) или 15 августа (без вступительных). Оригинал аттестата — до 15-18 августа. Приказы — с 17 августа."
    stud "Очно-заочная и заочная форма: приём документов до 23 сентября, оригинал аттестата до 23 сентября, приказы 28 сентября."
    stud "На платное отделение — договор нужно заключить в те же сроки."
    return

label priem_extra_exams:
    player_char "Нужно ли сдавать вступительные экзамены?"
    stud "На большинство специальностей — нет, зачисление по среднему баллу аттестата."
    stud "Вступительные испытания нужны только на три специальности:"
    stud "• 54.02.01 Дизайн — творческое испытание (рисунок, композиция)."
    stud "• 40.02.02 Правоохранительная деятельность — психологическое тестирование."
    stud "• 42.02.01 Реклама — творческое испытание."
    stud "Результаты — зачёт/незачёт. Если не пройдёте, можно выбрать другую специальность."
    return

label priem_extra_dorm:
    player_char "Дают ли общежитие?"
    stud "Да, общежитие предоставляется студентам с 18 лет. Адреса: Полярная, 34 (общежитие №1) и Червонная, 5 (общежитие №5)."
    stud "Подавайте заявление на заселение сразу после зачисления — места разбирают быстро."
    return

label priem_extra_schedule:
    player_char "Когда работает приёмная комиссия?"
    stud "Понедельник — четверг: с 8:00 до 17:00."
    stud "Пятница: с 8:00 до 16:00."
    stud "Обед: с 12:00 до 12:48."
    stud "Приходите в любое время, кроме обеда и пятницы после 16:00."
    return