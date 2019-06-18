# coding:utf-8s
import random,uuid
import object

class TheWorld(object):
    # todo:完善新对象的生存周期的相关操作，例如对象生成/移动/销毁等
    def __init__(self, size=(100, 100, 100)):
        super(TheWorld, self).__init__()
        # self.time = None 想了想似乎不需要？
        self.round = 0
        self.flag_finish = False
        self.alive_user = 0
        self.i = 0
        self.objects = {}
        self.world_size = size
        self.__create_world(size[0], size[1], size[2])
        self.table = object.T()

    def __check_alive_user(self):
        # 判断存活玩家
        if self.alive_user == 1:
            self.flag_finish = True
            # 游戏结束
            return

    def __tick_iteration(self):
        # 游戏回合迭代
        pass

    def __create_world(self, x, y, z):
        # 地图创建
        self.world = [[[0] * x for i in range(y)] * x for i in range(z)]  # 构建3D世界

    def __create_object(self, id, direction_x_y_z):
        obj = self.table.get(id)
        if obj:
            self.i = self.i + 1
            obj_ = obj(self.i, direction_x_y_z)
            self.objects[self.i] = obj_

    def __user_generate(self):
        x = random.randint(0, self.world_size[0])
        y = random.randint(0, self.world_size[1])
        z = random.randint(0, self.world_size[2])
        user_hash = uuid.uuid4()
        return user_hash

    def control_add_user(self):
        user_hash = self.__user_generate()
        return user_hash

    def api_move(self, user_hash, obj_id, direction_x_y_z):
        # 控制某个目标移动
        pass

    def api_action(self, user_hash, obj_id, direction_x_y_z, action_type):
        # todo:完善事件ID和事件对应的参数表
        pass
