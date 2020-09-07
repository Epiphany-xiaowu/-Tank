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
    # 按下方向键 坦克一直移动

import pygame,time
SCREEN_WIDTH = 700
SCREEN_HIGHT = 500
BG_COLOR = pygame.Color('black')
TEXT_COLOR = pygame.Color('red')

class MainGame():
    window = None
    my_tank = None
    def __int__(self):
        pass

    # 开始游戏
    def startgame(self):
        pygame.display.init()       #初始化窗口
        #设置窗口的大小及显示
        MainGame.window=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HIGHT])
        #设置标题
        #初始化我方坦克
        MainGame.my_tank = Tank(350,250)
        #设置窗口的标题
        pygame.display.set_caption('坦克大战1.03')
        while True:
            #坦克移动速度慢一点
            time.sleep(0.02)
            #给窗口设置填充字
            MainGame.window.fill(BG_COLOR)
            #获取事件
            self.getEvent()
            #绘制文字
            MainGame.window.blit(self.getTextSurface('敌方坦克剩余数量%d'%6),(10,10))
            #调用坦克显示的方法
            MainGame.my_tank.displayTank()
            #调用移动方法
            #如果坦克的开关是开启，才可以移动
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            pygame.display.update()


    #结束游戏
    def endgame(self):
        print('谢谢使用，欢迎再次使用')
        exit()

    # 左上角文字的绘制
    def getTextSurface(self,text):
        pygame.font.init()
        # 查看所有的字体名称
        # print(pygame.font.get_fonts())
        # 获取字体Font对象
        font = pygame.font.SysFont('kaiti',18)
        #绘制文字信息
        textSurface=font.render(text,True,TEXT_COLOR)
        return textSurface


    #获取事件
    def getEvent(self):
        eventlist = pygame.event.get()
        #遍历事件
        for event in eventlist:
            #判断按下的键是关闭还是键盘
            if event.type ==pygame.QUIT:
                self.endgame()
            if event.type == pygame.KEYDOWN :
                #判断的是上、下、左、右
                if event.key == pygame.K_LEFT:
                    # 切换方向
                    MainGame.my_tank.direction = 'L'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_RIGHT:
                    MainGame.my_tank.direction = 'R'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print('按下右键，坦克向右移动')
                elif event.key == pygame.K_DOWN:
                    MainGame.my_tank.direction = 'D'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print('按下下键，坦克向下移动')
                elif event.key == pygame.K_UP:
                    MainGame.my_tank.direction = 'U'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print('按下上键，坦克向上移动')
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')
            #松开方向键停止，修改坦克移动的开关
            if event.type == pygame.KEYUP:
                #判断释放的键是上下左右时候才停止坦克移动
                if event.key==pygame.K_UP or event.key==pygame.K_LEFT or event.key==pygame.K_DOWN or event.key==pygame.K_RIGHT:
                    MainGame.my_tank.stop = True

class Tank():
    def __init__(self,left,top):
        #保存加载的图片
        self.images = {
                        'U':pygame.image.load('image/p1tankU.gif'),
                       'D':pygame.image.load('image/p1tankD.gif'),
                       'L': pygame.image.load('image/p1tankL.gif'),
                       'R': pygame.image.load('image/p1tankR.gif')
                       }
        #方向
        self.direction = 'U'
        #根据当前图片的方向获取图片
        self.image = self.images[self.direction]
        #根据图片获取区域
        self.rect = self.image.get_rect()
        #设置区域的left和top
        self.rect.left = left
        self.rect.top = top
        #坦克移动速度
        self.speed = 1
        #坦克移动的开关
        self.stop = True


    #移动
    def move(self):
        #判断坦克的方向进行移动
        if self.direction == 'L':
            if self.rect.left>0:
                self.rect.left -=self.speed
        elif self.direction == 'U':
            if self.rect.top>0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.width<500:
                self.rect.top += self.speed
        else:
            if self.rect.left + self.rect.height < 700:
                self.rect.left += self.speed

    #射击
    def shot(self):
        pass

    #展示坦克
    def displayTank(self):
        #获取展示的对象
        self.image = self.images[self.direction]
        #调用blit方法
        MainGame.window.blit(self.image,self.rect)

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


