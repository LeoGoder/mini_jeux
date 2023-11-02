from ursina import *
import worldgen

class mainMenu(Entity):
     def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)
        self.main_menu = Entity(parent=self, enabled=True)
        self.options_menu = Entity(parent=self, enabled=False)
        self.help_menu = Entity(parent=self, enabled=False)
        self.choose = Entity(parent=self, enabled=False)
        self.gameslist = Entity(parent=self, enabled=False)
        self.minecraft = Entity(parent=self, enabled=False)
        self.background = Sprite('shore', color=color.dark_gray, z=1)

        Text("MAIN MENU", parent=self.main_menu, y=0.4, x=0, origin=(0,0))

        def switch(menu1, menu2):
            menu1.enable()
            menu2.disable()

        # 1st button of main menu
        ButtonList(button_dict={
            # 
            "Start": Func(lambda: switch(self.choose, self.main_menu)),
            "Options": Func(lambda: switch(self.options_menu, self.main_menu)),
            "Help": Func(lambda: switch(self.help_menu, self.main_menu)),
            "Exit": Func(lambda: application.quit())
        },y=0,parent=self.main_menu)
        #when press show a choosing menu 
        Text ("Start Menu", parent=self.choose, y=0.4, x=0, origin=(0, 0))

        #list of button of Start menu
        ButtonList (button_dict={
            "Games": Func(lambda: switch(self.gameslist, self.choose)),
            "Server": Func(print_on_screen,"You clicked on server button!", position=(0,.1), origin=(0,0)),
            "Create games": Func(print_on_screen,"You clicked on create games button!", position=(0,.1), origin=(0,0)),
        }, y=0, parent=self.choose)

        Button("Back",parent=self.choose,y=-0.3,scale=(0.1,0.05),color=rgb(50,50,50),
               on_click=lambda: switch(self.main_menu, self.choose))
        
        #when games is press show this 
        Text ("Games list", parent=self.gameslist, y=0.4, x=0, origin=(0, 0))

                #list of games
        ButtonList (button_dict={
            "Minecraft": Func(lambda: switch(self.minecraft, self.main_menu)),
            "Counter-Strike": Func(print_on_screen,"You clicked on counter strike button!", position=(0,.1), origin=(0,0)),
            "idk for now": Func(print_on_screen,"You clicked on create games button!", position=(0,.1), origin=(0,0)),
        }, y=0, parent=self.gameslist)

        Button("Back",parent=self.gameslist,y=-0.3,scale=(0.1,0.05),color=rgb(50,50,50),
        on_click=lambda: switch(self.choose, self.gameslist))
        #when press  show menu to change option 
        Text ("OPTIONS MENU", parent=self.options_menu, y=0.4, x=0, origin=(0, 0))

        Button("Back",parent=self.options_menu,y=-0.3,scale=(0.1,0.05),color=rgb(50,50,50),
               on_click=lambda: switch(self.main_menu, self.options_menu))
        
        #when press show a help menu about the games, how to set servers...
        Text ("HELP MENU", parent=self.help_menu, y=0.4, x=0, origin=(0, 0))

        # menu list
        ButtonList (button_dict={
            "Gameplay": Func(print_on_screen,"You clicked on Gameplay help button!", position=(0,.1), origin=(0,0)),
            "Battle": Func(print_on_screen,"You clicked on Battle help button!", position=(0,.1), origin=(0,0)),
            "Control": Func(print_on_screen,"You clicked on Control help button!", position=(0,.1), origin=(0,0)),
            "Back": Func (lambda: switch(self.main_menu, self.help_menu))
        }, y=0, parent=self.help_menu)
        # [HELP MENU] WINDOW END

        # Here we can change attributes of this class when call this class
        for key, value in kwargs.items ():
            setattr (self, key, value)

    # Input function that check if key pressed on keyboard
        def input(self, key):
        # And if you want use same keys on different windows
        # Like [Escape] or [Enter] or [Arrows]
        # Just write like that:

            # If our main menu enabled and we press [Escape]
            if self.main_menu.enabled and key == "escape":
                    application.quit()
            elif self.options_menu.enabled and key == "escape":
                self.main_menu.enable()
                self.options_menu.disable()
            elif self.help_menu.enabled and key == "escape":
                self.main_menu.enable()
                self.help_menu.disable()

        # Update function that check something every frame
        # You can use it similar to input with checking
        # what menu is currently enabled
        def update(self):
            pass