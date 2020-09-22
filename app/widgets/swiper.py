from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.clock import Clock

from math import atan2, degrees


class Card(Scatter):
    symm_boundary = NumericProperty(120)
    angle = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        touch.ud['direction'] = 0
        touch.ud['origCenter'] = self.center
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if not(self.collide_point(*touch.pos) and 'origCenter' in touch.ud):
            return False

        '''
        diff_x_tp = touch.x - touch.ud['origCenter'][0]
        if 'angle' in touch.profile:
            touch.ud['angle'] = touch.a
            print('The touch angle is', touch.a)
        else:
            # replace initial_y and initial_x with the some sort of baseline(y) center(x) (=origin) around which we want to rotate
            def updates_spin(*args):
                if diff_x_tp > 0:
                    self.angle = -abs(touch.x - touch.ud['origCenter'][0])/10
                elif diff_x_tp < 0:
                    self.angle = abs(touch.x - touch.ud['origCenter'][0])/10
                else:
                    pass  # do nothing
                #self.angle = degrees(atan2(touch.y - touch.ud['origCenter'][1], touch.x - touch.ud['origCenter'][0]))
                print('The touch angle is', self.angle)
            Clock.schedule_once(updates_spin, 0.01)
        '''

        touch.ud['direction'] = (self.center_x - touch.ud['origCenter'][0])
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if not(self.collide_point(*touch.pos) and 'direction' in touch.ud):
            return False

        if touch.ud['direction'] >= self.symm_boundary:
            print('Released right ---', touch)
        elif touch.ud['direction'] <= -self.symm_boundary:
            print('Released left ---', touch)
        else:
            self.center = touch.ud['origCenter']
            def updates_spin(*args):
                self.angle = 0
            Clock.schedule_once(updates_spin, 0.01)
            print('Reseting position and angle')

        super().on_touch_up(touch)

    def on_transform_with_touch(self, touch):
        '''
        Called when a touch event has transformed the scatter widget.
        By default this does nothing, but can be overriden by derived
        classes that need to react to transformations caused by user
        input.

        :Parameters:
            `touch`:
                The touch object which triggered the transformation.

        .. versionadded:: 1.8.0
        '''
        print('Moving', touch.ud['direction'])

    def build(self):
        return self


class Swiper(FloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        '''
        card_config = {
            #'size_hint': (None, None),
            #'size': (300,700),
            #'pos_hint': {'center_y': .5, 'center_x': .5},
            'do_rotation': True,
            'do_scale': False,
            'do_translation': True,
            'do_collide_after_children': False
        }
        '''

        return self
