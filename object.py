#coding:utf-8
# todo:完善基本对象接口需求


class ObjectNotFound:
    pass


class BaseObject(object):
    pass


class T(object):
    def __init__(self):
        self.maps = {}

    def get(self, id):
        if id in self.maps:
            return self.maps[id]
        else:
            raise ObjectNotFound


class Me(object):
    # todo:加入神经网络，模拟变异
    def __init__(self, world, belong, id, coordinate, atk, gar, spd, car, sex, fld, is_base=False):
        self.is_base = is_base
        self.coordinate = coordinate
        self.user_hash = belong
        self.world = world  # 处于哪个世界
        self.type_id = 1
        self.id = id
        self.event = None
        self.ATK = atk  # 攻击力
        self.bag = {}
        self.GAR = gar  # 防御力
        self.SPD = spd  # 速度
        self.CAR = car  # 运载力
        self.SEX = sex  # 性别
        self.FLD = fld  # 视野

    def set_coordinate(self,coordinate):
        self.coordinate = coordinate

    def get_coordinate(self):
        return self.coordinate

    def get_type(self):
        return self.type_id

    def get_event(self):
        return self.event

    def __calc_extra_attributes(self):
        # 计算背包中装备对数值的加成
        atk = self.ATK
        gar = self.GAR
        spd = self.SPD
        car = self.CAR
        sex = self.SEX
        fld = self.FLD
        if self.bag:
            # calculate the equipment
            pass

        return {
            "atk": atk,
            "gar": gar,
            "spd": spd,
            "car": car,
            "sex": sex,
            "fld": fld
        }

    def attributes(self):
        return {
            "id": self.id,
            "type": self.type_id,
            "belong": self.user_hash,
            "attribute": self.__calc_extra_attributes()
        }

    def stimulate(self, occurrence_direction, event):
        # 外部接收到刺激
        pass

    def action(self, event=None):
        # 记录事件
        if event is None:
            return self.event
        else:
            if self.event is not None:
                old_event = self.event
                self.event = event
                return old_event
            else:
                self.event = event
                return None


class Planet(object):
    def __init__(self, id):
        self.type_id = 2
        self.id = id
        self.store = 10000
        self.water = 10000

    def get_type(self):
        return self.type_id

    def action(self):
        pass
