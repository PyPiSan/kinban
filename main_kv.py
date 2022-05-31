KV_FILE = """
#:import get_color_from_hex kivy.utils.get_color_from_hex


MDScreen:
    md_bg_color: get_color_from_hex("#d4fad2")
    MDToolbar:
        id: toolbar
        title: "Kinban"
        elevation: 18
        pos_hint: {"top":1}
        md_bg_color: get_color_from_hex("#a4d9f5")
        specific_text_color: get_color_from_hex("#4a4939")
        left_action_items:[['menu', lambda x: nav_drawer.set_state("open")]]


    MDNavigationLayout:
        ScreenManager:
            id : screen_manager
            # Home:
            MainScreen:
                screen_manager: screen_manager
            HindiWordEdit:
            About:


        MDNavigationDrawer:
            id: nav_drawer
            md_bg_color: get_color_from_hex("#a6f5a2")
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

<HindiWordEdit>:
    name: "hindi"



<About>:
    name: "about"
    MDBoxLayout:
        orientation : "vertical"
        padding: dp(34)
        center_y: 0.2
        MDLabel:
            text:"About"
            bold : True
            font_style: "H6"
            size_hint_y: None
            height : self.texture_size[1] + dp(10)
        
        MDSeparator:

        MDLabel:
            text:"This app is currently in devlopment..."
            bold : True
            font_style: "Subtitle1"
            size_hint_y: None
            height : self.texture_size[1] + dp(10)
        MDLabel:
            text:"Please contribute for getting it bigger...."
            bold : True
            font_style: "Subtitle1"
            size_hint_y: None
            height : self.texture_size[1] + dp(10)
        MDLabel:
            text:"Contact me: sanjeev.mishra96@gmail.com"
            bold : True
            font_style: "Subtitle1"
            size_hint_y: None
            height : self.texture_size[1] + dp(10)
        ScrollView:

<MainScreen>:
    name: "main"
    md_bg_color: get_color_from_hex("#d4fad2")   
    MDCard:
        id: card
        orientation: "vertical"
        padding: dp(20)
        size_hint: None, None
        size: root.width*0.8, root.height*0.5
        pos_hint: {"center_x": .5, "center_y": 0.6}
        md_bg_color: get_color_from_hex("#a4d9f5")
        MDLabel:
            id: word
            text: root.japanese
            halign: "center"
            font_style: "H5"
            bold: True
            font_name: "images/meiryo.ttc"
        MDLabel:
            id: kana_word
            text: f'({root.curr["Kana"]})'
            font_style: "H6"
            font_name: "images/meiryo.ttc" 
        MDLabel:
            id: type
            text: f'word type: {root.curr["type"]}'
    MDBoxLayout:
        orientation: "vertical"
        spacing : dp(20)
        padding : dp(20)
        MDFillRoundFlatButton:
            text: "Show Answer"
            size_hint_x: 0.85
            pos_hint: {"center_x": .5}
            on_press: root.do()

        MDFillRoundFlatButton:
            text: "Next Card"
            size_hint_x: 0.85
            pos_hint: {"center_x": .5}
            on_press: root.next()
        
    # MDFloatingActionButton:
    #     id: edit
    #     icon : "pencil"
    #     pos_hint: {"center_x": 0.91, "center_y": 0.28}
    #     md_bg_color: 0, 1, 0.5, 1
    #     on_press : root.screen_manager.current = "hindi"    


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "5dp"
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "70dp", "70dp"
            source: "images/kinban.png"

    MDLabel:
        text: "Kinban"
        font_style: "Body1"
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        text: "sanjeev.mishra@gmail.com"
        font_style: "Body2"
        size_hint_y: None
        height: self.texture_size[1]

    MDSeparator:

    ScrollView:
        MDList:

            OneLineIconListItem:
                text: "Home"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "main"
                IconLeftWidget:
                    icon: "home"

            OneLineIconListItem:
                text: "Add Hindi Words"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "hindi"   
                IconLeftWidget:
                    icon: "pencil"
            
            OneLineIconListItem:
                text: "About"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "about" 
                IconLeftWidget:
                    icon: "information"
            OneLineIconListItem:
                text: "Exit"
                on_press:app.stop()                    
                IconLeftWidget:
                    icon: "exit-to-app"
<Home>
    name: "home"
    MDBoxLayout:
        MDLabel:
            text: "Welcome To Our Word"
            halign: "center"
<Content>:
    orientation: "vertical"
    spacing : dp(18)
    size_hint_y : None
    height : dp(200)
    # width: dp(80)
    MDRoundFlatButton:
        text: "BEGINNEER"
        size_hint_x: 0.85
        pos_hint: {"center_x": .5}
        on_press: root.begin()
    MDRoundFlatButton:
        text: "   EASY   "
        size_hint_x: 0.85
        pos_hint: {"center_x": .5}
        on_press: app.easy()
    MDRoundFlatButton:
        text: "MODERATE  "
        size_hint_x: 0.85
        pos_hint: {"center_x": .5}
        on_press: app.moderate()
    MDRoundFlatButton:
        text: " ADVANCE  "
        size_hint_x: 0.85
        pos_hint: {"center_x": .5}
        on_press: app.advance()
"""
