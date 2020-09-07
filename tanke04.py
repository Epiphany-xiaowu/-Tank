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

# 新增功能：
    # 加载主窗口  www。pygame。org
    # 添加事件 ，
    #       点击关闭窗口
    #       对上下左右键做处理
import pygame
SCREEN_WIDTH = 700
SCREEN_HIGHT = 500
BG_COLOR = pygame.Color(0,0,0)

class MainGame():
    window = None
    def __int__(self):
        pass

    # 开始游戏
    def startgame(self):
        pygame.display.init()       #初始化窗口
        #设置窗口的大小及显示
        MainGame.window=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HIGHT])
        #设置标题
        pygame.display.set_caption('坦克大战1.03')
        while True:
            #给窗口设置填充字
            MainGame.window.fill(BG_COLOR)
            #获取事件
            self.getEvent()
            pygame.display.update()


    #结束游戏
    def endgame(self):
        print('谢谢使用，欢迎再次使用')
        exit()


    #获取事件
    def getEvent(self):
        eventlist = pygame.event.get()
        #遍历事件
        for event in eventlist:
            #判断按下的键是关闭还是键盘
            if event.type ==pygame.QUIT:
                self.endgame()
            if event.type == pygame.KEYDOWN:
                #判断的是上、下、左、右
                if event.key == pygame.K_LEFT:
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_RIGHT:
                    print('按下右键，坦克向右移动')
                elif event.key == pygame.K_DOWN:
                    print('按下下键，坦克向下移动')
                elif event.key == pygame.K_UP:
                    print('按下上键，坦克向上移动')

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


if __name__ == '__main__':
    MainGame().startgame()


