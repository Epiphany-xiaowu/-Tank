'''坦克大战游戏的需求
1.项目有哪些类
2.每个类有哪些方法

1.坦克类（我方坦克、敌方坦克）继承
    射击
    移动类
    显示坦克的方法
2.子弹类（）
    移动
    显示子弹的方法
3.墙壁类
    属性：是否可以通过
4.爆炸效果
    展示爆炸效果
5.音效类
    播放音乐
6.主类
    开始游戏
    结束游戏
'''

class MainGame():
    def __int__(self):
        pass

    # 开始游戏
    def startgame(self):
        pass

    def endgame(self):
        pass


class Tank():
    def __int__(self):
        pass

    #移动
    def move(self):
        pass

    #射击
    def shot(self):
        pass

    #展示坦克
    def displayTank(self):
        pass

# 我方坦克
class myTank(Tank):
    def __int__(self):
        pass

#地方坦克
class enemyTank(Tank):
    def __int__(self):
        pass

#子弹类
class Bullet():
    def __int__(self):
        pass

    def move(self):
        pass

    def displayBullet(self):
        pass


#墙壁
class Wall():
    def __int__(self):
        pass

    def diaplayWall(self):
        pass


class Explode:
    def __int__(self):
        pass
    #展示爆炸的效果
    def displayExplode(self):
        pass

#音效类
class music():
    def __int__(self):
        pass
    #播放音乐的方法
    def play(self):
        pass
