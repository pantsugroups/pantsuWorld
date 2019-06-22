EVENT_ACTION_MOVE = 0
EVENT_ACTION_STOP = 1
EVENT_ACTION_ATTACK = 2


class Event(object):
    def __init__(self, start_tick, end_tick, action):
        self.s_tick = start_tick
        self.e_tick = end_tick
        self.action = action

    def interface(self, user_hash):
        # 用来接收事件对象
        pass

    def control(self):
        # 作为事件上报到世界中
        pass
