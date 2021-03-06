'''新增功能：
     完善子弹类

'''

import pygame,time,random
SCREEN_WIDTH = 700
SCREEN_HIGHT = 500
BG_COLOR = pygame.Color('black')
TEXT_COLOR = pygame.Color('red')

class MainGame():
    window = None
    my_tank = None
    #创建存储地方坦克的列表
    enemyTanklist = []
    #定义地方坦克的数量
    enemyTankcount = 5
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
        #初始化地方坦克并将敌方坦克添加到列表中
        self.createEnemyTank()
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
            MainGame.window.blit(self.getTextSurface('敌方坦克剩余数量%d'%len(MainGame.enemyTanklist)),(10,10))
            #调用坦克显示的方法
            MainGame.my_tank.displayTank()
            #循环遍历地方坦克列表，展示地方坦克
            self.blitEnemyTank()
            #调用移动方法
            #如果坦克的开关是开启，才可以移动
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            pygame.display.update()

    # 初始化地方坦克并将敌方坦克添加到列表中
    def createEnemyTank(self):
        top = 100
        #循环形成地方坦克
        for i in range(MainGame.enemyTankcount):
            left = random.randint(0,600)
            speed = random.randint(1,4)
            enemy = enemyTank(left,top,speed)
            MainGame.enemyTanklist.append(enemy)

    def blitEnemyTank(self):
    # 循环遍历地方坦克列表，展示地方坦克
        for enemyTank in MainGame.enemyTanklist:
            enemyTank.displayTank()
            enemyTank.randMove()


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
    def __init__(self):
        pass

#敌方坦克
class enemyTank(Tank):
    def __init__(self,left,top,speed):
        #加载图片集
        self.images = {
            'U':pygame.image.load('image/enemy1U.gif'),
            'D': pygame.image.load('image/enemy1D.gif'),
            'L': pygame.image.load('image/enemy1L.gif'),
            'R': pygame.image.load('image/enemy1R.gif')
        }
        #方向,随机生成敌方坦克的方向
        self.direction = self.randDirection()
        # 根据方向获取图片
        self.image = self.images[self.direction]
        #区域
        self.rect = self.image.get_rect()
        #对left和top进行赋值
        self.rect.left = left
        self.rect.top = top
        # 速度
        self.speed = speed
        # 移动开关
        self.stop = True
        #新增步数变量
        self.step = 80

    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    # 地方坦克随机移动的方法
    def randMove(self):
        if self.step<=0:
            self.direction = self.randDirection()
            #让步数复位
            self.step = 80
        else:
            self.move()
            # 步数递减
            self.step -= 1


#子弹类
class Bullet():
    def __init__(self,tank):
        #加载图片
        self.image = pygame.image.load('image\enemymissile.gif')
        #坦克的方向决定子弹的方向
        self.direction = tank.direction
        #获取区域
        self.rect = self.image.get_rect()
        #子弹的left与top与方向有关位置
        if self.direction == 'u':
            self.rect.left = tank.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        #子弹的速度
        self.speed = 5

    #移动
    def move(self):
        pass

    #显示子弹
    def displayBullet(self):
        #  将图片surface加载到窗口
        MainGame.window.blit(self.image,self.rect)

#墙壁
class Wall():
    def __init__(self):
        pass

    def diaplayWall(self):
        pass


class Explode:
    def __init__(self):
        pass
    #展示爆炸的效果
    def displayExplode(self):
        pass

#音效类
class music():
    def __init__(self):
        pass
    #播放音乐的方法
    def play(self):
        pass


if __name__ == '__main__':
    MainGame().startgame()


