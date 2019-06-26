# coding:utf-8
import random
import threading
import uuid
import event
import object


class TheWorld:
    # todo:完善新对象的生存周期的相关操作，例如对象生成/移动/销毁等
    def __init__(self, handle, size=(100, 100, 100)):
        super(TheWorld, self).__init__()
        # self.time = None 想了想似乎不需要？
        self.tick = 0  # 类似于回合
        self.handle = handle
        self.flag_finish = True
        self.users = {}
        self.i = 0  # 对象id
        self.event_i = 0  # 事件id
        self.event_map = {}
        self.objects = {}
        self.world_size = size
        self.__create_world(size[0], size[1], size[2])
        self.detector = object.Detector()

    def __check_alive_user(self):
        # 判断存活玩家
        alive = 0
        for i in self.users:
            if i["alive"] is True:
                alive += 1
        if alive == 1:
            self.flag_finish = True
        return alive

    def __tick_iteration(self):
        # 游戏回合迭代
        print(self.event_map)
        print(self.world, self.tick)
        # if self.event_map[self.tick]:
        #     self.event_map.pop(self.tick)  # GC，虽然我觉得python内部的计数器会帮我GC但是我还是忍不住自己GC一下
        self.tick += 1
        for i in self.event_map:
            self.event_map[i].callback()

        # debug segment

        if self.tick == 2:
            self.flag_finish = True
            return
        # debug end
        # todo:解决最大下潜深度的问题
        self.__tick_iteration()

    def __create_world(self, x, y, z):
        # 地图创建
        self.world = [[[0] * x for i in range(y)] * 1 for i in range(z)]  # 构建3D世界
        # todo: 生成随机星球资源

    def __id_generate(self):
        return self.i + 1

    def __event_id_generate(self):
        return self.event_i + 1

    def __create_object(self, type_id, user_hash, direction_x_y_z):
        x, y, z = direction_x_y_z
        self.users[user_hash]["objects"] += 1
        obj = self.detector.get(type_id)
        if obj:
            # todo:替换成detector来创建
            i = self.__id_generate()
            obj_ = obj(self, user_hash, i, direction_x_y_z)
            self.objects[i] = obj_
            self.world[x][y][z] = i
            return i

    def __event_distributor(self, occurrence_direction, event):
        # 事件下发器
        x, y, z = 0, 0, 0
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
        x = random.randint(0, self.world_size[0] - 1)
        y = random.randint(0, self.world_size[1] - 1)
        z = random.randint(0, self.world_size[2] - 1)
        return x, y, z

    def control_start_game(self):
        if self.flag_finish:
            self.flag_finish = False
            # threading.Thread(self.__tick_iteration()).start()
            self.__tick_iteration()
            return True
        else:
            return False

    def control_add_user(self):
        dre = self.__random_coordinate_generate()
        user_hash = str(uuid.uuid4())

        self.users[user_hash] = {
            "objects": 0,  # 还或者多少单位
            "alive": True,
            "base": dre,  # 基地车位置
            "magic_CD": 0  # 某些查询的功能的冷却事件，是按照回合计算的
        }  # 创建用户信息
        o_id = self.__create_object(1, user_hash, dre)
        return user_hash, o_id

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

    def api_get_tick(self):
        return self.tick

    def inline_maps_move(self, obj_id, direction_x_y_z):
        # 内部函数，返回真实移动的位置
        x = direction_x_y_z[0]
        y = direction_x_y_z[1]
        z = direction_x_y_z[2]
        if self.world[x][y][z] == 0:
            rx, ry, rz = self.objects[obj_id].get_coordinate()
            self.world[rx][ry][rz] = 0
            self.world[x][y][z] = obj_id
            return x, y, z
        else:
            # todo: 想个办法解决了如果移动目的地有东西在的问题
            pass

    def api_action(self, user_hash, obj_id, direction_x_y_z, action_type):
        # 参数二不代表对象位置，而是对象事件的参数
        # todo:完善事件ID和事件对应的参数表,第三个参数direction修改为已当前位置为0坐标而不是直接坐标
        if self.objects[obj_id].attributes()["belong"] == user_hash:
            # todo:action处理,和object绑定
            if action_type == event.EVENT_ACTION_MOVE:
                n = event.Event(self.__event_id_generate(), self.objects[obj_id], self.tick, action_type,
                                direction_x_y_z)
                if self.objects[obj_id].get_event() is not None and self.objects[obj_id].get_event() in self.event_map:
                    del (self.event_map[self.objects[obj_id].get_event()])
                self.event_map[self.__event_id_generate()] = n
        else:
            return
