# coding:utf-8s
import random
import threading
import uuid

import object


class TheWorld(object):
    # todo:完善新对象的生存周期的相关操作，例如对象生成/移动/销毁等
    def __init__(self, event_object, size=(100, 100, 100)):
        super(TheWorld, self).__init__()
        # self.time = None 想了想似乎不需要？
        self.round = 0
        self.event = event_object
        self.flag_finish = True
        self.users = {}
        self.i = 0
        self.objects = {}
        self.world_size = size
        self.__create_world(size[0], size[1], size[2])
        self.table = object.T()

    def __check_alive_user(self):
        # 判断存活玩家
        alive = 0
        for i in self.users:
            if i["alive"] is True:
                alive += 1
        if alive == 1:
            self.flag_finish = True

    def __tick_iteration(self):
        # 游戏回合迭代
        pass

    def __create_world(self, x, y, z):
        # 地图创建
        self.world = [[[0] * x for i in range(y)] * 1 for i in range(z)]  # 构建3D世界
        # todo: 生成随机星球资源

    def __id_generate(self):
        return self.i + 1

    def __create_object(self, type_id, direction_x_y_z):
        obj = self.table.get(type_id)
        if obj:
            obj_ = obj(self.__id_generate(), direction_x_y_z)
            self.objects[self.i] = obj_

    def __event_distributor(self, occurrence_direction, event):
        # 事件下发器
        x,y,z = 0, 0, 0
        maps = self.api_sight(10, occurrence_direction)
        for i in maps:
            x += 1
            y = 0
            for j in i:
                y += 1
                z = 0
                for k in j:
                    z += 1
                    if k != 0:
                        # x_ = x-1
                        # y_ = y-1
                        # z_ = z-1
                        # 因为是从1开始计算，-1后才是真实数组下标
                        k.stimulate(occurrence_direction, event)  # 事件发送给对象

    def __random_coordinate_generate(self):
        x = random.randint(0, self.world_size[0])
        y = random.randint(0, self.world_size[1])
        z = random.randint(0, self.world_size[2])
        return x, y, z

    def control_start_game(self):
        if self.flag_finish and not self.alive_user:
            self.flag_finish = False
            threading.Thread(self.__tick_iteration()).start()
            return True
        else:
            return False

    def control_add_user(self):
        dre = self.__random_coordinate_generate()
        user_hash = uuid.uuid4()
        self.__create_object(self.__id_generate(), dre)
        self.users[user_hash] = {
            "objects": 0,  # 还或者多少单位
            "alive": True,
            "base": dre,  # 基地车位置
            "magic_CD": 0  # 某些查询的功能的冷却事件，是按照回合计算的
        }  # 创建用户信息
        return user_hash

    def callback(self):
        pass

    def api_sight(self, field, object_direction_x_y_z):
        # 获取单位周围的地图信息
        # field可以为object的fld
        x = object_direction_x_y_z[0]
        y = object_direction_x_y_z[1]
        z = object_direction_x_y_z[2]
        # todo:解决field越界问题
        return self.world[x - field / 2:x + field / 2][y - field / 2:y + field / 2][z - field / 2:z + field / 2]

    def api_move(self, user_hash, obj_id, direction_x_y_z):
        # 控制某个目标移动。参数三输入个tuple：(x,y,z) ，xyz是以对象当前坐标为基准
        pass

    def api_action(self, user_hash, obj_id, direction_x_y_z, action_type):
        # todo:完善事件ID和事件对应的参数表
        pass
