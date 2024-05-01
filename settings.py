class Settings:
    """A class to store all settings for Alien invasion"""

    def __init__(self):
        """Initialise the game's static settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (60, 60, 60)

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_colour = (0, 0, 0)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_directon of 1 represents right; -1 represents left
        self.fleet_direction = 1 

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.differculty_level = ()

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game"""
        if self.differculty_level == 'easy':
            self.ship_limit = 5
            self.bullets_allowed = 10
            self.ship_speed = 0.75
            self.bullet_speed = 1.5
            self.alien_speed = 0.5
        elif self.differculty_level == 'medium':
            self.ship_limit = 3
            self.bullets_allowed = 3
            self.ship_speed = 1.5
            self.bullet_speed = 3
            self.alien_speed = 1.0
        elif self.differculty_level == 'hard': 
            self.ship_limit = 1
            self.bullets_allowed = 3
            self.ship_speed = 3.0
            self.bullet_speed = 6
            self.alien_speed = 2.0

        #Scoring settings
            self.alien_points = 50

        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        

    def set_differculty(self, diff_settings):
        if diff_settings == 'easy':
            print('easy')
        elif diff_settings == 'medium':
            pass
        elif diff_settings == 'hard':
            pass
