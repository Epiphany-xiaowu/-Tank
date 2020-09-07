'''新增功能

    1.完善音效类
    2.添加开场音效
    3.我方坦克发射子弹音效

'''

import pygame, time, random

SCREEN_WIDTH = 700
SCREEN_HIGHT = 500
BG_COLOR = pygame.Color('black')
TEXT_COLOR = pygame.Color('red')


# 定义一个基类
class Baseitem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class MainGame():
    window = None
    my_tank = None
    # 创建存储地方坦克的列表
    enemyTanklist = []
    # 定义地方坦克的数量
    enemyTankcount = 5
    # 存储我方子弹的列表
    mybulletlist = []
    #存储敌方子弹的列表
    enemybulletlist = []
    #存储爆炸效果的列表
    explodeList=[]
    #创建墙壁裂变
    walllist = []


    def __int__(self):
        pass

    # 开始游戏
    def startgame(self):
        pygame.display.init()  # 初始化窗口
        # 设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HIGHT])
        # 设置标题
        # 初始化我方坦克
        self.createmytank()
        # 初始化地方坦克并将敌方坦克添加到列表中
        self.createEnemyTank()
        #初始化墙壁
        self.createwall()
        # 设置窗口的标题
        pygame.display.set_caption('坦克大战1.03')

        while True:
            # 坦克移动速度慢一点
            time.sleep(0.02)
            # 给窗口设置填充字
            MainGame.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            # 绘制文字
            MainGame.window.blit(self.getTextSurface('敌方坦克剩余数量%d' % len(MainGame.enemyTanklist)), (10, 10))
            # 调用坦克显示的方法
            #判断我方坦克是否存活
            if MainGame.my_tank and MainGame.my_tank.live:
                MainGame.my_tank.displayTank()
            else:
                #删除我方坦克
                del MainGame.my_tank
                MainGame.my_tank = None

            # 循环遍历地方坦克列表，展示敌方坦克
            self.blitEnemyTank()
            # 循环遍历显示我方坦克的子弹
            # 循环遍历敌方坦克子弹列表,展示敌方子弹
            self.blitEnemybullet()
            self.blitMybullt()
            #循环遍历爆炸列表，展示爆炸效果
            self.blitExplode()
            #循环遍历墙壁列表，展示墙壁
            self.blitwall()
            # 调用移动方法
            # 如果坦克的开关是开启，才可以移动
            if MainGame.my_tank and MainGame.my_tank.live:
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
                    #检测我方坦克是否与墙壁发生碰撞
                    MainGame.my_tank.hitwall()
                    #检测我方坦克是否与敌方坦克发生碰撞
                    MainGame.my_tank.mytank_hit_enemytank()



            pygame.display.update()

    #循环遍历墙壁列表，展示墙壁
    def blitwall(self):
        for wall in MainGame.walllist:
            #判断墙壁是否存活
            if wall.live :
                #展示墙壁
                wall.diaplayWall()
            else:
                #从墙壁列表移除
                MainGame.walllist.remove(wall)

    #初始化墙壁
    def createwall(self):
        #初始化墙壁
        for i in range(6):
            wall = Wall(i*150,220)
            #将墙壁添加到列表中
            MainGame.walllist.append(wall)

    #创建我方坦克
    def createmytank(self):
        MainGame.my_tank = myTank(350, 300)
        #创建我的music对象
        music = Music('image/start.wav')
        #播放音乐
        music.play()
    # 初始化地方坦克并将敌方坦克添加到列表中
    def createEnemyTank(self):
        top = 100
        # 循环形成敌方坦克
        for i in range(MainGame.enemyTankcount):
            left = random.randint(0, 600)
            speed = random.randint(1, 4)
            enemy = enemyTank(left, top, speed)
            MainGame.enemyTanklist.append(enemy)



    #循环展示爆炸效果
    def blitExplode(self):
        for explode in MainGame.explodeList:
            #判断是否活着
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.explodeList.remove(explode)


    def blitEnemyTank(self):
        # 循环遍历地方坦克列表，展示地方坦克
        # 判断当前敌方坦克是否活着
        for enemytank in MainGame.enemyTanklist:
            if enemytank.live:
                enemytank.displayTank()
                enemytank.randMove()
                #调用检测是否与墙壁碰撞
                enemytank.hitwall()
                #检测地方坦克是否与我方坦克发生碰撞
                if MainGame.my_tank and MainGame.my_tank.live:
                    enemytank.enemytank_hit_mytank()
                # 发射子弹
                enemybullt = enemytank.shot()
                # 敌方子弹是否为None,如果不为None则添加到敌方子弹列表中
                if enemybullt:
                    # 将敌方子弹存储到敌方子弹列表
                    MainGame.enemybulletlist.append(enemybullt)
            else:
                MainGame.enemyTanklist.remove(enemytank)

    ## 循环遍历显示我方坦克的子弹
    def blitMybullt(self):
        for mybullt in MainGame.mybulletlist:
            # 判断当前子弹是否活着状态，如果是，则显示及移动，否则在列表中删除
            if mybullt.live:
                mybullt.displayBullet()
                # 调用子弹的移动方法
                mybullt.move()
                #调用检测我方子弹是否与敌方坦克发生碰撞
                mybullt.mybullet_hit_enemytank()
                # 检测地方子弹是否与墙壁碰撞
                mybullt.hitwall()
            else:
                MainGame.mybulletlist.remove(mybullt)

    def blitEnemybullet(self):
        for enemybullet in MainGame.enemybulletlist:
            if enemybullet.live:  # 判断敌方子弹是否存活
                enemybullet.displayBullet()
                enemybullet.move()
                #调用敌方子弹与我方坦克碰撞的方法
                enemybullet.enemybullet_hit_mytank()
                #检测地方子弹是否与墙壁碰撞
                enemybullet.hitwall()
            else:
                MainGame.enemybulletlist.remove(enemybullet)

    # 结束游戏
    def endgame(self):
        print('谢谢使用，欢迎再次使用')
        exit()

    # 左上角文字的绘制
    def getTextSurface(self, text):
        pygame.font.init()
        # 查看所有的字体名称
        # print(pygame.font.get_fonts())
        # 获取字体Font对象
        font = pygame.font.SysFont('kaiti', 18)
        # 绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface

    # 获取事件
    def getEvent(self):
        eventlist = pygame.event.get()
        # 遍历事件
        for event in eventlist:
            # 判断按下的键是关闭还是键盘
            if event.type == pygame.QUIT:
                self.endgame()
            if event.type == pygame.KEYDOWN:
                #当坦克死亡，按下ESC复活
                if not MainGame.my_tank:
                    if event.key == pygame.K_ESCAPE:
                        self.createmytank()     #我方坦克重生
                # 判断的是上、下、左、右
                if MainGame.my_tank and MainGame.my_tank.live:
                    if event.key == pygame.K_LEFT:
                        # 切换方向
                        MainGame.my_tank.direction = 'L'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('按下左键，坦克向左移动')
                    elif event.key == pygame.K_RIGHT:
                        MainGame.my_tank.direction = 'R'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('按下右键，坦克向右移动')
                    elif event.key == pygame.K_DOWN:
                        MainGame.my_tank.direction = 'D'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('按下下键，坦克向下移动')
                    elif event.key == pygame.K_UP:
                        MainGame.my_tank.direction = 'U'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('按下上键，坦克向上移动')
                    elif event.key == pygame.K_SPACE:
                        # 创建我方坦克子弹
                        # 如果当前我方子弹列表长度小于等于3，才可以创建
                        if len(MainGame.mybulletlist) <= 3:
                            mybullet = Bullet(MainGame.my_tank)
                            MainGame.mybulletlist.append(mybullet)
                            #添加发射子弹音效
                            music = Music('image/hit.wav')
                            music.play()
                        print('发射子弹')
            # 松开方向键停止，修改坦克移动的开关
            if event.type == pygame.KEYUP:
                # 判断释放的键是上下左右时候才停止坦克移动
                if MainGame.my_tank and MainGame.my_tank.live:
                    if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                        MainGame.my_tank.stop = True


class Tank():
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {
            'U': pygame.image.load('image/p1tankU.gif'),
            'D': pygame.image.load('image/p1tankD.gif'),
            'L': pygame.image.load('image/p1tankL.gif'),
            'R': pygame.image.load('image/p1tankR.gif')
        }
        # 方向
        self.direction = 'U'
        # 根据当前图片的方向获取图片
        self.image = self.images[self.direction]
        # 根据图片获取区域
        self.rect = self.image.get_rect()
        # 设置区域的left和top
        self.rect.left = left
        self.rect.top = top
        # 坦克移动速度
        self.speed = 5
        # 坦克移动的开关
        self.stop = True
        # 是否活着
        self.live = True
        # 新增属性原来的坐标
        self.oldleft = self.rect.left
        self.oldtop = self.rect.top

    # 移动
    def move(self):
        #移动后的坐标再次赋值
        self.oldleft = self.rect.left
        self.oldtop = self.rect.top
        # 判断坦克的方向进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.width < 500:
                self.rect.top += self.speed
        else:
            if self.rect.left + self.rect.height < 700:
                self.rect.left += self.speed

    # 射击
    def shot(self):
        return Bullet(self)

    def stay(self):
        self.rect.left = self.oldleft
        self.rect.top = self.oldtop



    #检测坦克是否与墙壁碰撞
    def hitwall(self):
        for wall in MainGame.walllist:
            if pygame.sprite.collide_rect(self,wall):
                #将坐标设置为移动之前的坐标
                self.stay()

    # 展示坦克
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法
        MainGame.window.blit(self.image, self.rect)


# 我方坦克
class myTank(Tank):
    def __init__(self,left,top):
        super(myTank,self).__init__(left,top)

    #检测我方坦克与敌方坦克发生碰撞
    def mytank_hit_enemytank(self):
        #循环遍历敌方坦克列表
        for enemytank in MainGame.enemyTanklist:
            if pygame.sprite.collide_rect(self,enemytank):
                self.stay()

# 敌方坦克
class enemyTank(Tank):
    def __init__(self, left, top, speed):
        #调用父类的初始化方法
        super(enemyTank, self).__init__(left,top)
        # 加载图片集
        self.images = {
            'U': pygame.image.load('image/enemy1U.gif'),
            'D': pygame.image.load('image/enemy1D.gif'),
            'L': pygame.image.load('image/enemy1L.gif'),
            'R': pygame.image.load('image/enemy1R.gif')
        }
        # 方向,随机生成敌方坦克的方向
        self.direction = self.randDirection()
        # 根据方向获取图片
        self.image = self.images[self.direction]
        # 区域
        self.rect = self.image.get_rect()
        # 对left和top进行赋值
        self.rect.left = left
        self.rect.top = top
        # 速度
        self.speed = speed
        # 移动开关
        self.stop = True
        # 新增步数变量
        self.step = 80

    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    #敌方坦克与我方坦克坦克是否发生碰撞
    def enemytank_hit_mytank(self):
        if pygame.sprite.collide_rect(self,MainGame.my_tank):
            self.stay()

    # 地方坦克随机移动的方法
    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            # 让步数复位
            self.step = 80
        else:
            self.move()
            # 步数递减
            self.step -= 1

    def shot(self):
        # 随机生成100以内的数
        num = random.randint(1, 500)
        if num < 10:
            return Bullet(self)


# 子弹类
class Bullet():
    def __init__(self, tank):
        # 加载图片
        self.image = pygame.image.load('image\enemymissile.gif')
        # 坦克的方向决定子弹的方向
        self.direction = tank.direction
        # 获取区域
        self.rect = self.image.get_rect()
        # 子弹的left与top与方向有关位置
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        # 子弹的速度
        self.speed = 5
        # 子弹的状态，是否碰到墙壁,如果碰到墙壁，修改此状态
        self.live = True

    #子弹是否碰撞墙壁
    def hitwall(self):
        #墙壁列表和子弹
        for wall in MainGame.walllist:
            if pygame.sprite.collide_rect(self,wall):
                #让子弹消失
                self.live = False
                wall.hp -=1
                if wall.hp <= 0 :
                    #修改墙壁的状态
                    wall.live = False

    # 移动
    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 修改子弹状态
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < 700:
                self.rect.left += self.speed
            else:
                # 修改子弹状态
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < 500:
                self.rect.top += self.speed
            else:
                # 修改子弹状态
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                # 修改子弹状态
                self.live = False

    # 显示子弹
    def displayBullet(self):
        #  将图片surface加载到窗口
        MainGame.window.blit(self.image, self.rect)

    # 我方子弹与地方坦克的碰撞
    def mybullet_hit_enemytank(self):
        # 遍历敌方坦克列表,判断是否发生碰撞
        for enemyTank in MainGame.enemyTanklist:
            if pygame.sprite.collide_rect(enemyTank,self):
                # 修改地方坦克和我方子弹的状态
                enemyTank.live = False
                self.live = False
                #创建爆炸对象
                explode = Explode(enemyTank)
                #将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)

    #敌方子弹与我方坦克的碰撞
    def enemybullet_hit_mytank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                # 产生爆炸对象
                explode = Explode(MainGame.my_tank)
                # 将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)
                # 修改敌方子弹与我方坦克的状态
                self.live = False
                MainGame.my_tank.live = False


# 墙壁
class Wall():
    def __init__(self,left,top):
        #加载图片
        self.image = pygame.image.load('image/steels.gif')
        #获取墙壁的区域
        self.rect = self.image.get_rect()
        #设置位置left，top
        self.rect.left = left
        self.rect.top = top
        #是否活着
        self.live = True
        #设置生命值
        self.hp = 3

    def diaplayWall(self):
        MainGame.window.blit(self.image,self.rect)



class Explode:
    def __init__(self,tank):
        #爆炸的位置由当前子弹打中的坦克位置决定
        self.rect = tank.rect
        self.images=[
            pygame.image.load('image/blast0.gif'),
            pygame.image.load('image/blast1.gif'),
            pygame.image.load('image/blast2.gif'),
            pygame.image.load('image/blast3.gif'),
            pygame.image.load('image/blast4.gif')
        ]
        self.step =0
        self.image = self.images[self.step]
        #是否活着
        self.live = True

    # 展示爆炸的效果
    def displayExplode(self):
        if self.step < len(self.images):
            # 根据索引获取爆炸对象
            self.image = self.images[self.step]
            self.step += 1
            # 添加到主窗口
            MainGame.window.blit(self.image, self.rect)
        else:
            # 修改活着的状态
            self.live = False
            self.step = 0


# 音效类
class Music():
    def __init__(self,filename):
        self.filename = filename
        #初始化混合器
        pygame.mixer.init()
        #加载音乐
        pygame.mixer.music.load(self.filename)

    #播放音乐
    def play(self):
            pygame.mixer.music.play()




if __name__ == '__main__':
    MainGame().startgame()
