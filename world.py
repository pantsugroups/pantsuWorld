class TheWorkd(object):
    """
    生成游戏世界
        user<int>:用户数量
        size<tuple>:世界大小，3维
    return: 用户hash列表
    """
    def __init__(self,user=0, size=(100,100,100)):
        super(TheWorkd, self).__init__()
        users_hash =[]
        # self.time = None 想了想似乎不需要？
        self.round = 0
        self.event_list = []
        return users_hash
    def __roundIteration(self):
    """
        游戏回合迭代，回合制 or rts？ 
    """
        pass
    def __createWorld(self,):
        # 地图创建
        pass

    def Api_Move(self,user_hash,direction,l):
        pass 
        