class Settings():

        def __init__(self):
                self.screen_width = 800
                self.screen_height = 600
                self.bg_color = (230,230,230)
                self.black_color = (12,10,15)
                self.bullet_width = 3
                self.bullet_height = 15
                self.bullet_color = (246,174,19)
                self.bullets_allowed = 7
                self.fleet_drop_speed = 10
                self.ship_limit = 3
                self.speedup_scale = 1.2
                self.score_scale = 1.5
                self.initialize_dynamic_settings()
                self.ship_left = [('image//ship_left_2.bmp'),('image//ship_left.bmp')]
                self.ship_right = [('image//ship_right_2.bmp'),('image//ship_right.bmp')]
                self.ship_stop = [('image//ship.bmp', 0.001),('image//ship_2.bmp', 0.001),('image//ship_3.bmp', 0.001)]
                self.anim_delay = 0.01
                self.anim_bg = [('image//bg//1 (1).png', 0.1),
                                ('image//bg//1 (2).png', 0.1),
                                ('image//bg//1 (3).png', 0.1),
                                ('image//bg//1 (4).png', 0.1),
                                ('image//bg//1 (5).png', 0.1),
                                ('image//bg//1 (6).png', 0.1),
                                ('image//bg//1 (7).png', 0.1),
                                ('image//bg//1 (8).png', 0.1),
                                ('image//bg//1 (9).png', 0.1),
                                ('image//bg//1 (10).png', 0.1),
                                ('image//bg//1 (11).png', 0.1),
                                ('image//bg//1 (12).png', 0.1),
                                ('image//bg//1 (13).png', 0.1),
                                ('image//bg//1 (14).png', 0.1),
                                ('image//bg//1 (15).png', 0.1),
                                ('image//bg//1 (16).png', 0.1),
                                ('image//bg//1 (17).png', 0.1),
                                ('image//bg//1 (18).png', 0.1),
                                ('image//bg//1 (19).png', 0.1),
                                ('image//bg//1 (20).png', 0.1),
                                ('image//bg//1 (21).png', 0.1),
                                ('image//bg//1 (22).png', 0.1),
                                ('image//bg//1 (23).png', 0.1),
                                ('image//bg//1 (24).png', 0.1),
                                ('image//bg//1 (25).png', 0.1),
                                ('image//bg//1 (26).png', 0.1),
                                ('image//bg//1 (27).png', 0.1),
                                ('image//bg//1 (28).png', 0.1),
                                ('image//bg//1 (29).png', 0.1),
                                ('image//bg//1 (30).png', 0.1),
                                ('image//bg//1 (31).png', 0.1),
                                ('image//bg//1 (32).png', 0.1),
                                ('image//bg//1 (33).png', 0.1),
                                ('image//bg//1 (34).png', 0.1),
                                ('image//bg//1 (35).png', 0.1),
                                ('image//bg//1 (36).png', 0.1),
                                ('image//bg//1 (37).png', 0.1),
                                ('image//bg//1 (38).png', 0.1),
                                ('image//bg//1 (39).png', 0.1),
                                ('image//bg//1 (40).png', 0.1),]
                self.anim_boom = [('image//boom//boom0000.png', 0.1),
                                  ('image//boom//boom0001.png', 0.1),
                                  ('image//boom//boom0002.png', 0.1),
                                  ('image//boom//boom0003.png', 0.1),
                                  ('image//boom//boom0004.png', 0.1),
                                  ('image//boom//boom0005.png', 0.1),
                                  ('image//boom//boom0006.png', 0.1),
                                  ('image//boom//boom0007.png', 0.1),
                                  ('image//boom//boom0008.png', 0.1),
                                  ('image//boom//boom0009.png', 0.1),
                                  ('image//boom//boom0010.png', 0.1),
                                  ('image//boom//boom0011.png', 0.1),
                                  ('image//boom//boom0012.png', 0.1),
                                  ('image//boom//boom0013.png', 0.1),
                                  ('image//boom//boom0014.png', 0.1),
                                  ('image//boom//boom0015.png', 0.1),
                                  ('image//boom//boom0016.png', 0.1)]
                                                                   
                
        def initialize_dynamic_settings(self):
                self.ship_speed_factor = 2.0
                self.bullet_speed_factor = 2.5
                self.alien_speed_factor = 0.7
                self.fleet_direction = 1
                self.alien_points = 50
                
        def increase_speed(self):
                self.ship_speed_factor *= self.speedup_scale
                self.alien_speed_factor *= self.speedup_scale
                self.bullet_speed_factor *= self.speedup_scale
                self.alien_points = int(self.alien_points * self.score_scale)
