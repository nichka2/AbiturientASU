################################################################################
## Инициализация
################################################################################

init offset = -1


################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Внутриигровые экраны
################################################################################


## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Если есть боковое изображение ("голова"), показывает её поверх текста.
    ## По стандарту не показывается на варианте для мобильных устройств — мало
    ## места.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Экран ввода #################################################################
##
## Этот экран используется, чтобы показывать renpy.input. Это параметр запроса,
## используемый для того, чтобы дать игроку ввести в него текст.
##
## Этот экран должен создать наложение ввода с id "input", чтобы принять
## различные вводимые параметры.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

screen quick_menu():

    ## Гарантирует, что оно появляется поверх других экранов.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Назад") action Rollback()
            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Б.Сохр") action QuickSave()
            textbutton _("Б.Загр") action QuickLoad()
            textbutton _("Опции") action ShowMenu('preferences')


## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Начать") action Start()

        else:

            textbutton _("История") action ShowMenu("history")

            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")

        textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Завершить повтор") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Главное меню") action MainMenu()

        textbutton _("Об игре") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Помощь не необходима и не относится к мобильным устройствам.
            textbutton _("Помощь") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Кнопка выхода блокирована в iOS и не нужна на Android и в веб-
            ## версии.
            textbutton _("Выход") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    tag menu

    add gui.main_menu_background

    ## Эта пустая рамка затеняет главное меню.
    frame:
        style "main_menu_frame"

    ## Оператор use включает отображение другого экрана в данном. Актуальное
    ## содержание главного меню находится на экране навигации.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None или один из "viewport" или "vpgrid". Этот
## экран предназначен для использования с одним или несколькими дочерними
## элементами, которые трансклюдируются (помещаются) внутрь него.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Вернуться"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

screen about():

    tag menu

    ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    ## включён в порт просмотра внутри экрана игрового меню.
    use game_menu(_("Об игре"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Версия [config.version!t]\n")

            ## gui.about обычно установлено в options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen save():

    tag menu

    use file_slots(_("Сохранить"))


screen load():

    tag menu

    use file_slots(_("Загрузить"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        fixed:

            ## Это гарантирует, что ввод будет принимать enter перед остальными
            ## кнопками.
            order_reverse True

            ## Номер страницы, который может быть изменён посредством клика на
            ## кнопку.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Таблица слотов.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Кнопки для доступа к другим страницам.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}А") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Б") action FilePage("quick")

                    ## range(1, 10) задаёт диапазон значений от 1 до 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Загрузить Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Скачать Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Пропуск")
                    textbutton _("Всего текста") action Preference("skip", "toggle")
                    textbutton _("После выборов") action Preference("after choices", "toggle")
                    textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))

                ## Дополнительные vbox'ы типа "radio_pref" или "check_pref"
                ## могут быть добавлены сюда для добавления новых настроек.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость текста")

                    bar value Preference("text speed")

                    label _("Скорость авточтения")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Без звука"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Избегайте предсказывания этого экрана, так как он может быть очень
    ## массивным.
    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Это всё правильно уравняет, если history_height будет
                ## установлен на None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Берёт цвет из who параметра персонажа, если он
                        ## установлен.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")


## Это определяет, какие теги могут отображаться на экране истории.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Пробел")
        text _("Прохождение диалогов без возможности делать выбор.")

    hbox:
        label _("Стрелки")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Esc")
        text _("Вход в игровое меню.")

    hbox:
        label _("Ctrl")
        text _("Пропускает диалоги, пока зажат.")

    hbox:
        label _("Tab")
        text _("Включает режим пропуска.")

    hbox:
        label _("Page Up")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Page Down")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label "H"
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label "S"
        text _("Делает снимок экрана.")

    hbox:
        label "V"
        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")

    hbox:
        label "Shift+A"
        text _("Открывает меню специальных возможностей.")


screen mouse_help():

    hbox:
        label _("Левый клик")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Клик колёсиком")
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label _("Правый клик")
        text _("Вход в игровое меню.")

    hbox:
        label _("Колёсико вверх")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Колёсико вниз")
        text _("Откатывает предыдущее действие вперёд.")


screen gamepad_help():

    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Левый Триггер\nЛевый Бампер")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Правый бампер")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label _("Крестовина, Стики")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Старт, Гид, B/Правая кнопка")
        text _("Вход в игровое меню.")

    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс пользователя.")

    textbutton _("Калибровка") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Пропускаю")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Показывает меню, если есть. Меню может показываться некорректно, если
        ## config.narrator_menu установлено на True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Пузырьковый экран ###########################################################
##
## Экран пузырьков используется для отображения диалога игроку при использовании
## речевых пузырьков. Экран пузырьков принимает те же параметры, что и экран
## say, должен создать отображаемый объект с id "what", и может создавать
## отображаемые объекты с id "namebox", "who" и "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Мобильные варианты
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Раз мышь может не использоваться, мы заменили быстрое меню версией,
## использующей меньше кнопок, но больших по размеру, чтобы их было легче
## касаться.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Назад") action Rollback()
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Меню") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
    # Добавьте этот код в конец файла screens.rpy

# --- Экран выбора пола ---
# --- Экран выбора пола ---
screen choose_gender():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        background Frame("gui/frame.png", gui.frame_borders)
        vbox:
            spacing 20
            label "Выберите персонажа" xalign 0.5
            hbox:
                spacing 40
                imagebutton:
                    idle "gui/button/male_idle.png"
                    hover "gui/button/male_hover.png"
                    action [SetVariable("player_gender", "male"), Return()]
                imagebutton:
                    idle "gui/button/female_idle.png"
                    hover "gui/button/female_hover.png"
                    action [SetVariable("player_gender", "female"), Return()]

# --- Экран выбора специальности (основной) ---
screen specialty_chooser():
    tag menu
    use game_menu("Выберите специальность", scroll="viewport"):

        # Сначала выбор уровня образования
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

            # Отображение списка специальностей в зависимости от выбора
            if current_edu_level == "grade9":
                use specialties_grade9
            elif current_edu_level == "grade11":
                use specialties_grade11
            elif current_edu_level == "extramural":
                use specialties_extramural

            # Кнопка возврата, если всё просмотрено
            textbutton "Вернуться к выбору" action ShowMenu("specialty_chooser") style "navigation_button"

# --- Список специальностей для 9 классов ---
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

# --- Список специальностей для 11 классов ---
screen specialties_grade11():
    vbox:
        spacing 10
        label "Информационные технологии" style "pref_label_text"
        for spec in specialties_data["grade11"]["it"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

        label "Экономика, право, управление и логистика" style "pref_label_text"
        for spec in specialties_data["grade11"]["economics"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

# --- Список специальностей для заочной формы ---
screen specialties_extramural():
    vbox:
        spacing 10
        for spec in specialties_data["extramural"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

# --- Экран детального описания специальности ---
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
    # Кнопка закрытия
    textbutton "X" action Hide("specialty_detail") xalign 1.0 yalign 0.0

# --- База данных специальностей ---
init python:
    specialties_data = {
        "grade9": {
            "it": [
                {"code": "09.02.08", "name": "Интеллектуальные интегрированные системы", "duration": "2 года 10 месяцев", "budget": "25", "paid": "25", "qualification": "Техник по интеллектуальным интегрированным системам", "profile": "it",
"description": "Умный дом, интернет вещей, автоматизированные системы управления — это твоя среда. Ты научишься проектировать архитектуру интеллектуальных систем, разрабатывать приложения для их взаимодействия и обслуживать «умное» оборудование. Профессия, которая уже сейчас формирует будущее.",
"skills": ["Проектировать архитектуру интеллектуальных систем", "Разрабатывать приложения для взаимодействия с ними", "Обслуживать и сопровождать интеллектуальные системы"]},
                {"code": "09.02.09", "name": "Веб-разработка", "duration": "2 года 10 месяцев", "budget": "25", "paid": "25", "qualification": "Разработчик веб-приложений", "profile": "it",
"description": "Фронтенд и бэкенд, клиентская и серверная части — ты освоишь всё. Научишься создавать сайты, веб-приложения, администрировать их и поддерживать. Если хочешь быстро войти в IT и создавать то, чем пользуются миллионы, — это твой выбор.",
"skills": ["Проектировать и разрабатывать веб-ресурсы", "Администрировать и сопровождать информационные системы", "Работать с клиентской и серверной частями приложений"]},
                {"code": "09.02.11", "name": "Разработка и управление программным обеспечением", "duration": "3 года 10 месяцев", "budget": "30", "paid": "30", "qualification": "Разработчик программного обеспечения", "profile": "it",
"description": "Серьёзная, фундаментальная программа для тех, кто хочет не просто писать код, а управлять процессом разработки. Ты научишься создавать сложные программные продукты, руководить командами и доводить проекты до релиза. Это путь в senior-разработчики и тимлиды.",
"skills": ["Разрабатывать программное обеспечение разного уровня сложности", "Управлять процессом разработки", "Тестировать и сопровождать ПО"]},
                {"code": "09.02.12", "name": "Техническая эксплуатация и сопровождение информационных систем", "duration": "2 года 10 месяцев", "budget": "20", "paid": "30", "qualification": "Специалист по информационным системам", "profile": "it",
"description": "Ты будешь тем, кто обеспечивает стабильную работу IT-инфраструктуры в компаниях. Настройка, поддержка, модернизация и защита информационных систем — твоя задача. Надёжный специалист, без которого не обходится ни один серьёзный бизнес.",
"skills": ["Эксплуатировать и сопровождать информационные системы", "Выявлять и устранять неисправности", "Обеспечивать бесперебойную работу IT-сервисов"]},
                {"code": "10.02.05", "name": "Обеспечение информационной безопасности автоматизированных систем", "duration": "3 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по защите информации", "profile": "it",
"description": "Киберугрозы становятся сложнее, и компании нуждаются в защите. Ты научишься выявлять уязвимости, защищать данные и отражать атаки. Одна из самых востребованных и высокооплачиваемых профессий в IT.",
"skills": ["Защищать информацию программными и аппаратными средствами", "Эксплуатировать защищённые автоматизированные системы", "Выявлять угрозы и реагировать на инциденты"]}
            ],
            "economics": [
                {"code": "38.02.03", "name": "Операционная деятельность в логистике", "duration": "2 года 10 месяцев", "budget": "30", "paid": "30", "qualification": "Логист", "profile": "economics",
"description": "Как товары попадают с завода на полку магазина? Кто управляет складами, транспортом и поставками? Логист. Ты научишься строить эффективные цепочки поставок, экономить ресурсы и управлять процессами.",
"skills": ["Организовывать перевозки и складскую работу", "Управлять запасами и закупками", "Оптимизировать логистические процессы"]},
                {"code": "38.02.06", "name": "Финансы", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Финансист", "profile": "economics",
"description": "Деньги — это ресурс, и ты научишься им управлять. Бюджетирование, финансовый анализ, работа с налогами и бюджетами всех уровней. Востребовано в любой компании — от стартапа до госкорпорации.",
"skills": ["Планировать финансы организаций и бюджетов", "Проводить финансовый анализ и оценку рисков", "Работать с налогами и бюджетами РФ"]},
                {"code": "38.02.07", "name": "Банковское дело", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист банковского дела", "profile": "economics",
"description": "Кредиты, вклады, расчётные счета, пластиковые карты — банковская сфера ждёт тебя. Ты научишься работать с клиентами, оформлять кредиты, вести расчёты. Стабильность, карьерный рост и уважаемая профессия.",
"skills": ["Вести расчётные и кредитные операции", "Работать с банковскими продуктами", "Обслуживать физических и юридических лиц"]},
                {"code": "40.02.04", "name": "Правоохранительная деятельность", "duration": "3 года 6 месяцев", "budget": "150", "paid": "150", "qualification": "Юрист", "profile": "economics",
"description": "Служба закону и порядку. Ты будешь готов к работе в полиции, следствии, судах, службах безопасности. Оперативно-служебная, административная и управленческая деятельность. Серьёзная профессия для серьёзных людей.",
"skills": ["Осуществлять оперативно-служебную деятельность", "Работать в административной сфере", "Организовывать работу подразделений"]},
                {"code": "42.02.01", "name": "Юриспруденция", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Юрист", "profile": "economics",
"description": "Широкая юридическая подготовка. Ты сможешь работать в юридических отделах компаний, консультировать граждан, защищать права в судах. Универсальный юрист, который разбирается в разных отраслях права.",
"skills": ["Осуществлять правоприменительную деятельность", "Оказывать юридическую помощь", "Обеспечивать правовую поддержку организаций"]},
                {"code": "42.02.01", "name": "Реклама", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по рекламе", "profile": "economics",
"description": "Креатив, маркетинг, продвижение. Ты научишься создавать рекламные продукты, планировать кампании, продвигать бренды в интернете. Если хочешь влиять на умы и продажи — тебе сюда.",
"skills": ["Создавать рекламные продукты и креативы", "Планировать рекламные кампании", "Работать в digital-маркетинге"]},
                {"code": "43.02.16", "name": "Туризм и гостеприимство", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по туризму и гостеприимству", "profile": "economics",
"description": "Отели, туры, экскурсии, сервис. Ты будешь создавать впечатления и комфорт для людей. Работа в туристических агентствах, гостиницах, сфере событий.",
"skills": ["Организовывать работу служб туризма", "Предоставлять туроператорские и гостиничные услуги", "Управлять сервисом"]}
            ],
            "science": [
                {"code": "18.02.12", "name": "Технология аналитического контроля химических соединений", "duration": "3 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Техник-химик", "profile": "science",
"description": "Лаборатории, анализы, контроль качества. Ты будешь работать с химическими соединениями, проводить анализы сырья и готовой продукции. Востребовано на заводах, в научных центрах и экологических лабораториях.",
"skills": ["Проводить качественные и количественные анализы", "Работать с химическим оборудованием", "Контролировать качество продукции"]},
                {"code": "25.02.08", "name": "Эксплуатация беспилотных авиационных систем", "duration": "3 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по БПЛА", "profile": "science",
"description": "Дроны — это не игрушки, а серьёзная техника. Ты научишься пилотировать, обслуживать и применять беспилотники для съёмок, мониторинга, доставки и спецзадач. Профессия будущего, которая нужна уже сегодня.",
"skills": ["Пилотировать беспилотники разных типов", "Обслуживать и ремонтировать БПЛА", "Работать с полезной нагрузкой и обработкой данных"]},
                {"code": "54.02.01", "name": "Дизайн (по отраслям)", "duration": "3 года 10 месяцев", "budget": "15", "paid": "10", "qualification": "Дизайнер", "profile": "science",
"description": "Промышленный дизайн, предметно-пространственная среда. Ты будешь создавать проекты, которые потом воплотятся в реальные изделия. Рисунок, 3D-моделирование, макетирование, контроль производства.",
"skills": ["Разрабатывать дизайн-проекты", "Воплощать идеи в материале", "Контролировать качество изготовления"]}
            ]
        },
        "grade11": {
            "it": [
                {"code": "09.02.09", "name": "Веб-разработка", "duration": "1 год 10 месяцев", "budget": "25", "paid": "25", "qualification": "Разработчик веб-приложений", "profile": "it",
"description": "Максимально быстрый вход в IT. Всего за 1 год и 10 месяцев ты станешь востребованным веб-разработчиком. Научишься создавать сайты и приложения, работать с клиентской и серверной частями.",
"skills": ["Создавать веб-приложения «под ключ»", "Администрировать и поддерживать сайты", "Работать с базами данных"]},
                {"code": "09.02.12", "name": "Техническая эксплуатация и сопровождение информационных систем", "duration": "1 год 10 месяцев", "budget": "25", "paid": "25", "qualification": "Специалист по информационным системам", "profile": "it",
"description": "Ускоренная программа для тех, кто хочет быстро освоить профессию администратора и техподдержки IT-систем. Компаниям нужны надёжные специалисты, которые обеспечивают стабильную работу.",
"skills": ["Настраивать и сопровождать информационные системы", "Диагностировать и устранять сбои", "Обеспечивать бесперебойную работу"]}
            ],
            "economics": [
                {"code": "20.02.01", "name": "Экологическая безопасность природных комплексов", "duration": "1 год 10 месяцев", "budget": "15", "paid": "10", "qualification": "Специалист по охране окружающей среды", "profile": "science",
"description": "Экология, природоохранная деятельность, экологический контроль. Ты сможешь работать на предприятиях, в лабораториях и контролирующих органах.",
"skills": ["Проводить экологический мониторинг", "Осуществлять производственный экоконтроль", "Управлять отходами"]},
                {"code": "38.02.03", "name": "Операционная деятельность в логистике", "duration": "1 год 10 месяцев", "budget": "25", "paid": "25", "qualification": "Логист", "profile": "economics",
"description": "Ускоренный курс по управлению цепочками поставок, складами и транспортом. Профессия, которая нужна в любой компании, связанной с товарами.",
"skills": ["Организовывать перевозки и складирование", "Управлять закупками и запасами", "Оптимизировать логистику"]},
                {"code": "40.02.04", "name": "Правоохранительная деятельность", "duration": "2 года 6 месяцев", "budget": "125", "paid": "125", "qualification": "Юрист", "profile": "economics",
"description": "Ускоренная программа для тех, кто хочет служить в органах. Ты получишь знания и навыки для работы в полиции, следствии, судах, службах безопасности.",
"skills": ["Осуществлять оперативно-служебную деятельность", "Работать в административной сфере", "Управлять подразделениями"]},
                {"code": "40.02.04", "name": "Юриспруденция", "duration": "1 год 10 месяцев", "budget": "75", "paid": "75", "qualification": "Юрист", "profile": "economics",
"description": "Самая быстрая юридическая программа. Диплом юриста за 1 год 10 месяцев — и ты можешь работать в юридических отделах, консультировать, помогать людям.",
"skills": ["Применять право на практике", "Оказывать юридическую помощь", "Работать с документами и законодательством"]},
                {"code": "43.02.16", "name": "Туризм и гостеприимство", "duration": "1 год 10 месяцев", "budget": "50", "paid": "50", "qualification": "Специалист по туризму и гостеприимству", "profile": "economics",
"description": "Интенсивный курс для яркой профессии в сфере туризма, отелей и событий. Быстрый старт и работа с людьми.",
"skills": ["Организовывать туры и экскурсии", "Работать в гостиницах", "Управлять сервисом"]}
            ]
        },
        "extramural": [
            {"code": "09.02.08", "name": "Интеллектуальные интегрированные системы", "duration": "2 года 6 месяцев (заочная)", "budget": "25", "paid": "25", "qualification": "Техник по интеллектуальным интегрированным системам", "profile": "it",
"description": "Заочная форма для тех, кто хочет освоить профессию в сфере умных систем без отрыва от работы. Удобный график и качественное образование.",
"skills": ["Проектировать архитектуру интеллектуальных систем", "Разрабатывать приложения для взаимодействия с ними", "Обслуживать и сопровождать интеллектуальные системы"]},
            {"code": "40.02.04", "name": "Юриспруденция", "duration": "2 года 6 месяцев (заочная)", "budget": "25", "paid": "25", "qualification": "Юрист", "profile": "economics",
"description": "Заочное юридическое образование. Идеально для тех, кто уже работает в смежной сфере или хочет получить диплом юриста без отрыва от основной деятельности.",
"skills": ["Применять право на практике", "Оказывать юридическую помощь", "Работать с документами и законодательством"]}
        ]
    }

    # Текущий уровень образования для выбора специальностей
    current_edu_level = "grade9"
# Добавьте этот код в конец файла screens.rpy

# --- Экран выбора пола ---
screen choose_gender():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        background Frame("gui/frame.png", gui.frame_borders)
        vbox:
            spacing 20
            label "Выберите персонажа" xalign 0.5
            hbox:
                spacing 40
                imagebutton:
                    idle "gui/button/male_idle.png"
                    hover "gui/button/male_hover.png"
                    action [SetVariable("player_gender", "male"), Return()]
                imagebutton:
                    idle "gui/button/female_idle.png"
                    hover "gui/button/female_hover.png"
                    action [SetVariable("player_gender", "female"), Return()]

# --- Экран выбора специальности (основной) ---
screen specialty_chooser():
    tag menu
    use game_menu("Выберите специальность", scroll="viewport"):

        # Сначала выбор уровня образования
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

            # Отображение списка специальностей в зависимости от выбора
            if current_edu_level == "grade9":
                use specialties_grade9
            elif current_edu_level == "grade11":
                use specialties_grade11
            elif current_edu_level == "extramural":
                use specialties_extramural

            # Кнопка возврата, если всё просмотрено
            textbutton "Вернуться к выбору" action ShowMenu("specialty_chooser") style "navigation_button"

# --- Список специальностей для 9 классов ---
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

# --- Список специальностей для 11 классов ---
screen specialties_grade11():
    vbox:
        spacing 10
        label "Информационные технологии" style "pref_label_text"
        for spec in specialties_data["grade11"]["it"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

        label "Экономика, право, управление и логистика" style "pref_label_text"
        for spec in specialties_data["grade11"]["economics"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

# --- Список специальностей для заочной формы ---
screen specialties_extramural():
    vbox:
        spacing 10
        for spec in specialties_data["extramural"]:
            textbutton "[spec['name']] ([spec['duration']])" action ShowTransient("specialty_detail", spec=spec)

# --- Экран детального описания специальности ---
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
# Добавьте этот экран в конец файла screens.rpy или script.rpy
screen final_message():
    frame:
        xalign 0.5 yalign 0.5
        xsize 600
        ysize 200
        background Frame("gui/frame.png", gui.frame_borders)
        at final_message_anim
        vbox:
            spacing 15
            xalign 0.5 yalign 0.5
            text "✨ Спасибо за визит! ✨" size 32 color "#ffcc66" bold True xalign 0.5
            text "Ждём тебя в нашем колледже!" size 24 color "#c8ffc8" xalign 0.5
            text "❤️" size 30 color "#ff6666" xalign 0.5

transform final_message_anim:
    alpha 0.0
    zoom 0.5
    yoffset 50
    linear 0.3 alpha 1.0 zoom 1.0 yoffset 0
    pause 2.5
    linear 0.3 alpha 0.0 zoom 1.2 yoffset -20
    # Кнопка закрытия


# --- База данных специальностей ---
init python:
    specialties_data = {
        "grade9": {
            "it": [
                {"code": "09.02.08", "name": "Интеллектуальные интегрированные системы", "duration": "2 года 10 месяцев", "budget": "25", "paid": "25", "qualification": "Техник по интеллектуальным интегрированным системам", "profile": "it",
                 "description": "Умный дом, интернет вещей, автоматизированные системы управления — это твоя среда. Ты научишься проектировать архитектуру интеллектуальных систем, разрабатывать приложения для их взаимодействия и обслуживать «умное» оборудование. Профессия, которая уже сейчас формирует будущее.",
                 "skills": ["Проектировать архитектуру интеллектуальных систем", "Разрабатывать приложения для взаимодействия с ними", "Обслуживать и сопровождать интеллектуальные системы"]},
                {"code": "09.02.09", "name": "Веб-разработка", "duration": "2 года 10 месяцев", "budget": "25", "paid": "25", "qualification": "Разработчик веб-приложений", "profile": "it",
                 "description": "Фронтенд и бэкенд, клиентская и серверная части — ты освоишь всё. Научишься создавать сайты, веб-приложения, администрировать их и поддерживать. Если хочешь быстро войти в IT и создавать то, чем пользуются миллионы, — это твой выбор.",
                 "skills": ["Проектировать и разрабатывать веб-ресурсы", "Администрировать и сопровождать информационные системы", "Работать с клиентской и серверной частями приложений"]},
                {"code": "09.02.11", "name": "Разработка и управление программным обеспечением", "duration": "3 года 10 месяцев", "budget": "30", "paid": "30", "qualification": "Разработчик программного обеспечения", "profile": "it",
                 "description": "Серьёзная, фундаментальная программа для тех, кто хочет не просто писать код, а управлять процессом разработки. Ты научишься создавать сложные программные продукты, руководить командами и доводить проекты до релиза. Это путь в senior-разработчики и тимлиды.",
                 "skills": ["Разрабатывать программное обеспечение разного уровня сложности", "Управлять процессом разработки", "Тестировать и сопровождать ПО"]},
                {"code": "09.02.12", "name": "Техническая эксплуатация и сопровождение информационных систем", "duration": "2 года 10 месяцев", "budget": "20", "paid": "30", "qualification": "Специалист по информационным системам", "profile": "it",
                 "description": "Ты будешь тем, кто обеспечивает стабильную работу IT-инфраструктуры в компаниях. Настройка, поддержка, модернизация и защита информационных систем — твоя задача. Надёжный специалист, без которого не обходится ни один серьёзный бизнес.",
                 "skills": ["Эксплуатировать и сопровождать информационные системы", "Выявлять и устранять неисправности", "Обеспечивать бесперебойную работу IT-сервисов"]},
                {"code": "10.02.05", "name": "Обеспечение информационной безопасности автоматизированных систем", "duration": "3 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по защите информации", "profile": "it",
                 "description": "Киберугрозы становятся сложнее, и компании нуждаются в защите. Ты научишься выявлять уязвимости, защищать данные и отражать атаки. Одна из самых востребованных и высокооплачиваемых профессий в IT.",
                 "skills": ["Защищать информацию программными и аппаратными средствами", "Эксплуатировать защищённые автоматизированные системы", "Выявлять угрозы и реагировать на инциденты"]}
            ],
            "economics": [
                {"code": "38.02.03", "name": "Операционная деятельность в логистике", "duration": "2 года 10 месяцев", "budget": "30", "paid": "30", "qualification": "Логист", "profile": "economics",
                 "description": "Как товары попадают с завода на полку магазина? Кто управляет складами, транспортом и поставками? Логист. Ты научишься строить эффективные цепочки поставок, экономить ресурсы и управлять процессами.",
                 "skills": ["Организовывать перевозки и складскую работу", "Управлять запасами и закупками", "Оптимизировать логистические процессы"]},
                {"code": "38.02.06", "name": "Финансы", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Финансист", "profile": "economics",
                 "description": "Деньги — это ресурс, и ты научишься им управлять. Бюджетирование, финансовый анализ, работа с налогами и бюджетами всех уровней. Востребовано в любой компании — от стартапа до госкорпорации.",
                 "skills": ["Планировать финансы организаций и бюджетов", "Проводить финансовый анализ и оценку рисков", "Работать с налогами и бюджетами РФ"]},
                {"code": "38.02.07", "name": "Банковское дело", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист банковского дела", "profile": "economics",
                 "description": "Кредиты, вклады, расчётные счета, пластиковые карты — банковская сфера ждёт тебя. Ты научишься работать с клиентами, оформлять кредиты, вести расчёты. Стабильность, карьерный рост и уважаемая профессия.",
                 "skills": ["Вести расчётные и кредитные операции", "Работать с банковскими продуктами", "Обслуживать физических и юридических лиц"]},
                {"code": "40.02.04", "name": "Правоохранительная деятельность", "duration": "3 года 6 месяцев", "budget": "150", "paid": "150", "qualification": "Юрист", "profile": "economics",
                 "description": "Служба закону и порядку. Ты будешь готов к работе в полиции, следствии, судах, службах безопасности.",
                 "skills": ["Осуществлять оперативно-служебную деятельность", "Работать в административной сфере", "Организовывать работу подразделений"]},
                {"code": "42.02.01", "name": "Юриспруденция", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Юрист", "profile": "economics",
                 "description": "Широкая юридическая подготовка. Ты сможешь работать в юридических отделах компаний, консультировать граждан, защищать права в судах. Универсальный юрист, который разбирается в разных отраслях права.",
                 "skills": ["Осуществлять правоприменительную деятельность"]},
                {"code": "42.02.01", "name": "Реклама", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по рекламе", "profile": "economics",
                 "description": "Креатив, маркетинг, продвижение. Ты научишься создавать рекламные продукты, планировать кампании, продвигать бренды в интернете.",
                 "skills": ["Создавать рекламные продукты и креативы", "Планировать рекламные кампании"]},
                {"code": "43.02.16", "name": "Туризм и гостеприимство", "duration": "2 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по туризму и гостеприимству", "profile": "economics",
                 "description": "Отели, туры, экскурсии, сервис. Ты будешь создавать впечатления и комфорт для людей. Работа в туристических агентствах, гостиницах, сфере событий.",
                 "skills": ["Организовывать работу служб туризма", "Предоставлять туроператорские и гостиничные услуги", "Управлять сервисом"]}
            ],
            "science": [
                {"code": "18.02.12", "name": "Технология аналитического контроля химических соединений", "duration": "3 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Техник-химик", "profile": "science",
                 "description": "Лаборатории, анализы, контроль качества. Ты будешь работать с химическими соединениями, проводить анализы сырья и готовой продукции. Востребовано на заводах, в научных центрах и экологических лабораториях.",
                 "skills": ["Проводить качественные и количественные анализы", "Работать с химическим оборудованием", "Контролировать качество продукции"]},
                {"code": "25.02.08", "name": "Эксплуатация беспилотных авиационных систем", "duration": "3 года 10 месяцев", "budget": "15", "paid": "35", "qualification": "Специалист по БПЛА", "profile": "science",
                 "description": "Дроны — это серьёзная техника. Ты научишься пилотировать, обслуживать и применять беспилотники для съёмок, мониторинга, доставки и спецзадач. Профессия будущего, которая нужна уже сегодня.",
                 "skills": ["Пилотировать беспилотники разных типов", "Обслуживать и ремонтировать БПЛА", "Работать с полезной нагрузкой и обработкой данных"]},
                {"code": "54.02.01", "name": "Дизайн (по отраслям)", "duration": "3 года 10 месяцев", "budget": "15", "paid": "10", "qualification": "Дизайнер", "profile": "science",
                 "description": "Промышленный дизайн, предметно-пространственная среда. Рисунок, 3D-моделирование, макетирование, контроль производства.",
                 "skills": ["Разрабатывать дизайн-проекты", "Воплощать идеи в материале", "Контролировать качество изготовления"]}
            ]
        },
        "grade11": {
            "it": [
                {"code": "09.02.09", "name": "Веб-разработка", "duration": "1 год 10 месяцев", "budget": "25", "paid": "25", "qualification": "Разработчик веб-приложений", "profile": "it",
                 "description": "Максимально быстрый вход в IT. Всего за 1 год и 10 месяцев ты станешь востребованным веб-разработчиком. Научишься создавать сайты и приложения, работать с клиентской и серверной частями.",
                 "skills": ["Создавать веб-приложения «под ключ»", "Администрировать и поддерживать сайты", "Работать с базами данных"]},
                {"code": "09.02.12", "name": "Техническая эксплуатация и сопровождение информационных систем", "duration": "1 год 10 месяцев", "budget": "25", "paid": "25", "qualification": "Специалист по информационным системам", "profile": "it",
                 "description": "Ускоренная программа для тех, кто хочет быстро освоить профессию администратора и техподдержки IT-систем. Компаниям нужны надёжные специалисты, которые обеспечивают стабильную работу.",
                 "skills": ["Настраивать и сопровождать информационные системы", "Диагностировать и устранять сбои", "Обеспечивать бесперебойную работу"]}
            ],
            "economics": [
                {"code": "20.02.01", "name": "Экологическая безопасность природных комплексов", "duration": "1 год 10 месяцев", "budget": "15", "paid": "10", "qualification": "Специалист по охране окружающей среды", "profile": "science",
                 "description": "Экология, природоохранная деятельность, экологический контроль. Ты сможешь работать на предприятиях, в лабораториях и контролирующих органах.",
                 "skills": ["Проводить экологический мониторинг", "Осуществлять производственный экоконтроль", "Управлять отходами"]},
                {"code": "38.02.03", "name": "Операционная деятельность в логистике", "duration": "1 год 10 месяцев", "budget": "25", "paid": "25", "qualification": "Логист", "profile": "economics",
                 "description": "Ускоренный курс по управлению цепочками поставок, складами и транспортом. Профессия, которая нужна в любой компании, связанной с товарами.",
                 "skills": ["Организовывать перевозки и складирование", "Управлять закупками и запасами", "Оптимизировать логистику"]},
                {"code": "40.02.04", "name": "Правоохранительная деятельность", "duration": "2 года 6 месяцев", "budget": "125", "paid": "125", "qualification": "Юрист", "profile": "economics",
                 "description": "Ускоренная программа для тех, кто хочет служить в органах. Ты получишь знания и навыки для работы в полиции, следствии, судах, службах безопасности.",
                 "skills": ["Осуществлять оперативно-служебную деятельность", "Работать в административной сфере", "Управлять подразделениями"]},
                {"code": "40.02.04", "name": "Юриспруденция", "duration": "1 год 10 месяцев", "budget": "75", "paid": "75", "qualification": "Юрист", "profile": "economics",
                 "description": "Самая быстрая юридическая программа. Диплом юриста за 1 год 10 месяцев — и ты можешь работать в юридических отделах.",
                 "skills": ["Применять право на практике", "Оказывать юридическую помощь", "Работать с документами и законодательством"]},
                {"code": "43.02.16", "name": "Туризм и гостеприимство", "duration": "1 год 10 месяцев", "budget": "50", "paid": "50", "qualification": "Специалист по туризму и гостеприимству", "profile": "economics",
                 "description": "Интенсивный курс для яркой профессии в сфере туризма, отелей и событий. Быстрый старт и работа с людьми.",
                 "skills": ["Организовывать туры и экскурсии", "Работать в гостиницах", "Управлять сервисом"]}
            ]
        },
        "extramural": [
            {"code": "09.02.08", "name": "Интеллектуальные интегрированные системы", "duration": "2 года 6 месяцев (заочная)", "budget": "25", "paid": "25", "qualification": "Техник по интеллектуальным интегрированным системам", "profile": "it",
             "description": "Заочная форма для тех, кто хочет освоить профессию в сфере умных систем.",
             "skills": ["Проектировать архитектуру интеллектуальных систем", "Обслуживать и сопровождать интеллектуальные системы"]},
            {"code": "40.02.04", "name": "Юриспруденция", "duration": "2 года 6 месяцев (заочная)", "budget": "25", "paid": "25", "qualification": "Юрист", "profile": "economics",
             "description": "Заочное юридическое образование. Идеально для тех, кто уже работает в смежной сфере или хочет получить диплом юриста без отрыва от основной деятельности.",
             "skills": ["Применять право на практике", "Оказывать юридическую помощь", "Работать с документами и законодательством"]}
        ]
    }

    # Текущий уровень образования для выбора специальностей
    current_edu_level = "grade9"
screen choose_gender():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        background Frame("gui/frame.png", gui.frame_borders)
        vbox:
            spacing 30
            label "Выберите персонажа" xalign 0.5 text_size 45
            hbox:
                spacing 60
                # Кнопка для мужского пола (используем картинку абитуриента-парня)
                imagebutton:
                    idle "male_student.png"
                    hover Transform("male_student.png", matrixcolor=SaturationMatrix(1.2))
                    action [SetVariable("player_gender", "male"), Return()]
                # Кнопка для женского пола (используем картинку абитуриента-девушки)
                imagebutton:
                    idle "female_student.png"
                    hover Transform("female_student.png", matrixcolor=SaturationMatrix(1.2))
                    action [SetVariable("player_gender", "female"), Return()]
                    # --- ЭКРАН ФИНАЛЬНОГО СООБЩЕНИЯ (god.png) ---
screen final_message():
    frame:
        xalign 0.5 yalign 0.5
        xsize 600
        ysize 200
        background Frame("gui/frame.png", gui.frame_borders)
        at final_message_anim
        vbox:
            spacing 15
            xalign 0.5 yalign 0.5
            text "✨ Спасибо за визит! ✨" size 32 color "#ffcc66" bold True xalign 0.5
            text "Ждём тебя в нашем колледже!" size 24 color "#c8ffc8" xalign 0.5
            text "❤️" size 30 color "#ff6666" xalign 0.5

transform final_message_anim:
    alpha 0.0
    zoom 0.5
    yoffset 50
    linear 0.3 alpha 1.0 zoom 1.0 yoffset 0
    pause 2.5
    linear 0.3 alpha 0.0 zoom 1.2 yoffset -20
# --- ЭКРАН-ГАЛЕРЕЯ ДЛЯ VIAR (5 изображений) - переключение по клику ---
screen gallery_viar():
    default viar_idx = 0
    modal True
    
    add "bg black"
    
    # Изображение по центру
    if viar_idx == 0:
        add "viar_0" xalign 0.5 yalign 0.5
    elif viar_idx == 1:
        add "viar_1" xalign 0.5 yalign 0.5
    elif viar_idx == 2:
        add "viar_2" xalign 0.5 yalign 0.5
    elif viar_idx == 3:
        add "viar_3" xalign 0.5 yalign 0.5
    else:
        add "viar_4" xalign 0.5 yalign 0.5
    
    # Счётчик фото внизу
    text "Фото [viar_idx+1] из 5" size 24 color "#ffffff" xalign 0.5 yalign 0.95
    
    # Полупрозрачная рамка для счётчика
    frame:
        xalign 0.5 yalign 0.95
        xsize 160 ysize 45
        background Frame(Transform("gui/frame.png", alpha=0.7), 10, 10)
    
    # Клик по экрану - следующее фото или закрытие
    if viar_idx < 4:
        key "K_SPACE" action SetScreenVariable("viar_idx", viar_idx + 1)
        key "K_RETURN" action SetScreenVariable("viar_idx", viar_idx + 1)
        key "K_KP_ENTER" action SetScreenVariable("viar_idx", viar_idx + 1)
        key "mouseup_1" action SetScreenVariable("viar_idx", viar_idx + 1)
        text "Нажмите для следующего фото" size 18 color "#aaaaaa" xalign 0.5 yalign 0.98
    else:
        key "K_SPACE" action Return()
        key "K_RETURN" action Return()
        key "K_KP_ENTER" action Return()
        key "mouseup_1" action Return()
        text "Нажмите для выхода" size 18 color "#ffcc66" xalign 0.5 yalign 0.98

# --- ЭКРАН-ГАЛЕРЕЯ ДЛЯ ТЕАТРА (5 изображений) - переключение по клику ---
screen gallery_teatr():
    default teatr_idx = 0
    modal True
    
    add "bg black"
    
    if teatr_idx == 0:
        add "teatr_0" xalign 0.5 yalign 0.5
    elif teatr_idx == 1:
        add "teatr_1" xalign 0.5 yalign 0.5
    elif teatr_idx == 2:
        add "teatr_2" xalign 0.5 yalign 0.5
    elif teatr_idx == 3:
        add "teatr_3" xalign 0.5 yalign 0.5
    else:
        add "teatr_4" xalign 0.5 yalign 0.5
    
    text "Фото [teatr_idx+1] из 5" size 24 color "#ffffff" xalign 0.5 yalign 0.95
    
    frame:
        xalign 0.5 yalign 0.95
        xsize 160 ysize 45
        background Frame(Transform("gui/frame.png", alpha=0.7), 10, 10)
    
    if teatr_idx < 4:
        key "K_SPACE" action SetScreenVariable("teatr_idx", teatr_idx + 1)
        key "K_RETURN" action SetScreenVariable("teatr_idx", teatr_idx + 1)
        key "K_KP_ENTER" action SetScreenVariable("teatr_idx", teatr_idx + 1)
        key "mouseup_1" action SetScreenVariable("teatr_idx", teatr_idx + 1)
        text "Нажмите для следующего фото" size 18 color "#aaaaaa" xalign 0.5 yalign 0.98
    else:
        key "K_SPACE" action Return()
        key "K_RETURN" action Return()
        key "K_KP_ENTER" action Return()
        key "mouseup_1" action Return()
        text "Нажмите для выхода" size 18 color "#ffcc66" xalign 0.5 yalign 0.98

# --- ЭКРАН-ГАЛЕРЕЯ ДЛЯ ВОЛОНТЁРОВ (6 изображений) - переключение по клику ---
screen gallery_volonter():
    default volonter_idx = 0
    modal True
    
    add "bg black"
    
    if volonter_idx == 0:
        add "volonter_0" xalign 0.5 yalign 0.5
    elif volonter_idx == 1:
        add "volonter_1" xalign 0.5 yalign 0.5
    elif volonter_idx == 2:
        add "volonter_2" xalign 0.5 yalign 0.5
    elif volonter_idx == 3:
        add "volonter_3" xalign 0.5 yalign 0.5
    elif volonter_idx == 4:
        add "volonter_4" xalign 0.5 yalign 0.5
    else:
        add "volonter_5" xalign 0.5 yalign 0.5
    
    text "Фото [volonter_idx+1] из 6" size 24 color "#ffffff" xalign 0.5 yalign 0.95
    
    frame:
        xalign 0.5 yalign 0.95
        xsize 160 ysize 45
        background Frame(Transform("gui/frame.png", alpha=0.7), 10, 10)
    
    if volonter_idx < 5:
        key "K_SPACE" action SetScreenVariable("volonter_idx", volonter_idx + 1)
        key "K_RETURN" action SetScreenVariable("volonter_idx", volonter_idx + 1)
        key "K_KP_ENTER" action SetScreenVariable("volonter_idx", volonter_idx + 1)
        key "mouseup_1" action SetScreenVariable("volonter_idx", volonter_idx + 1)
        text "Нажмите для следующего фото" size 18 color "#aaaaaa" xalign 0.5 yalign 0.98
    else:
        key "K_SPACE" action Return()
        key "K_RETURN" action Return()
        key "K_KP_ENTER" action Return()
        key "mouseup_1" action Return()
        text "Нажмите для выхода" size 18 color "#ffcc66" xalign 0.5 yalign 0.98

# --- ЭКРАН-ГАЛЕРЕЯ ДЛЯ СПОРТА (4 изображения) - переключение по клику ---
screen gallery_sport():
    default sport_idx = 0
    modal True
    
    add "bg black"
    
    if sport_idx == 0:
        add "sport_0" xalign 0.5 yalign 0.5
    elif sport_idx == 1:
        add "sport_1" xalign 0.5 yalign 0.5
    elif sport_idx == 2:
        add "sport_2" xalign 0.5 yalign 0.5
    else:
        add "sport_3" xalign 0.5 yalign 0.5
    
    text "Фото [sport_idx+1] из 4" size 24 color "#ffffff" xalign 0.5 yalign 0.95
    
    frame:
        xalign 0.5 yalign 0.95
        xsize 160 ysize 45
        background Frame(Transform("gui/frame.png", alpha=0.7), 10, 10)
    
    if sport_idx < 3:
        key "K_SPACE" action SetScreenVariable("sport_idx", sport_idx + 1)
        key "K_RETURN" action SetScreenVariable("sport_idx", sport_idx + 1)
        key "K_KP_ENTER" action SetScreenVariable("sport_idx", sport_idx + 1)
        key "mouseup_1" action SetScreenVariable("sport_idx", sport_idx + 1)
        text "Нажмите для следующего фото" size 18 color "#aaaaaa" xalign 0.5 yalign 0.98
    else:
        key "K_SPACE" action Return()
        key "K_RETURN" action Return()
        key "K_KP_ENTER" action Return()
        key "mouseup_1" action Return()
        text "Нажмите для выхода" size 18 color "#ffcc66" xalign 0.5 yalign 0.98
        # --- ЭКРАН ВЫБОРА ВОПРОСОВ ДЛЯ ПРИЁМНОЙ КОМИССИИ ---
# --- ЭКРАН ВЫБОРА ВОПРОСОВ ДЛЯ ПРИЁМНОЙ КОМИССИИ ---
screen priem_questions():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        xsize 850
        ysize 600
        background Frame("gui/frame.png", gui.frame_borders)
        padding (30, 30)
        
        vbox:
            spacing 20
            xfill True
            
            text "О чём хочешь узнать?" size 28 color "#ffcc66" bold True xalign 0.5
            
            frame:
                xfill True
                background Frame("gui/frame.png", 10, 10)
                padding (20, 15)
                vbox:
                    spacing 12
                    textbutton "🏅 Кто имеет право на первоочередное зачисление?":
                        action Return("lgoty")
                        style "question_button"
                        xfill True
                    textbutton "📄 Какие документы нужны для поступления?":
                        action Return("documents")
                        style "question_button"
                        xfill True
                    textbutton "📍 Куда и как подавать документы?":
                        action Return("submit")
                        style "question_button"
                        xfill True
                    textbutton "📅 Сроки приёма и зачисления?":
                        action Return("deadlines")
                        style "question_button"
                        xfill True
                    textbutton "✏️ Нужно ли сдавать вступительные экзамены?":
                        action Return("exams")
                        style "question_button"
                        xfill True
                    textbutton "🏠 Дают ли общежитие?":
                        action Return("dorm")
                        style "question_button"
                        xfill True
                    textbutton "🕐 Режим работы приёмной комиссии?":
                        action Return("schedule")
                        style "question_button"
                        xfill True
            
            # Кнопки внизу - рядом друг с другом
            hbox:
                spacing 20
                xalign 0.5
                textbutton "❓ Задать все вопросы" action Return("all") style "question_button_small"
                textbutton "➡️ Пойти дальше" action Return("skip") style "question_button_small"

# Стиль для больших кнопок (вопросы)
style question_button:
    background Frame("gui/button/choice_idle_background.png", 10, 10)
    hover_background Frame("gui/button/choice_hover_background.png", 10, 10)
    xsize 650
    ysize 45
    xpadding 15
    ypadding 8

# Стиль для маленьких кнопок (внизу - рядом друг с другом)
style question_button_small:
    background Frame("gui/button/choice_idle_background.png", 10, 10)
    hover_background Frame("gui/button/choice_hover_background.png", 10, 10)
    xsize 280
    ysize 50
    xpadding 10
    ypadding 8

style question_button_text:
    color "#ffffff"
    hover_color "#ffcc66"
    size 18
    textalign 0.5

style question_button_small_text:
    color "#ffffff"
    hover_color "#ffcc66"
    size 17
    textalign 0.5