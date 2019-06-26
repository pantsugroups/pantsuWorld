EVENT_ACTION_MOVE = 0
EVENT_ACTION_STOP = 1
EVENT_ACTION_ATTACK = 2
EVENT_ACTION_STEP = 2


class Event(object):
    def __init__(self, id, father_object, create_tick, action, direction_x_y_z):
        self.id = id
        self.father = father_object
        self.s_tick = create_tick
        # self.life = life_cycle
        self.action = action
        self.direction_x_y_z = direction_x_y_z

    def callback(self):
        if self.action == EVENT_ACTION_MOVE:
            # todo:距离修改，按照回合修改坐标达到移动效果
            # 这里先暂时只搞成瞬移
            t_dir = self.father.inline_maps_move(self.id, self.direction_x_y_z)
            self.father.set_coordinate(t_dir)



