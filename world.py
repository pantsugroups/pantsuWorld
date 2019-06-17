# coding:utf-8s
class TheWorld(object):

    def __init__(self, user=0, size=(100, 100, 100)):
        super(TheWorld, self).__init__()
        # self.time = None 想了想似乎不需要？
        self.round = 0
        self.flag_finish = False
        self.alive_user = user
        self.event_list = []

    def __check_alive_user(self):
        # 判断存活玩家
        if self.alive_user == 1:
            self.flag_finish = True
            # 游戏结束
            return

    def __tick_iteration(self):
        # 游戏回合迭代
        pass

    def __create_world(self):
        # 地图创建
        pass

    def api_move(self, user_hash, obj_id, direction_x_y_z):
        # 控制某个目标移动
        pass

    def api_action(self, user_hash, obj_id, direction_x_y_z, action_type):
        pass
