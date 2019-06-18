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
    def __init__(self, id):
        self.type_id = 1
        self.id = id
        self.ATK = 0
        self.bag = {}
        self.DEF = 0

    def get_type(self):
        return self.type_id

    def attributes(self):
        pass

    def action(self):
        pass


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

