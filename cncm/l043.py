# 4.3 The Harmonic Exercise in Python with Loops

# Listing 4.3 Python and our spring

# 没有官方文档是什么鬼
import pylab as pyl

dt = 0.05 # delta-t
p = -0.5 # constant P
sp = 5.0 # what???????????

acc = [p * sp] # acceleration
vel = [0.0] # velocity
s = [sp]
t = [0.0]

for i in range(1,100):
    acc.append(s[-1] * p)
    vel.append(vel[-1] + acc[-1] * dt)
    s.append(s[-1] + vel[-1] * dt)
    t.append(dt * i)

# pylab.plot(x,y): 目测是以x和y列表的数值为自变量和因变量绘制平滑曲线
dp = pyl.plot(t,s)
pyl.show()

### DIY时间

x = [0.0]
y = [0.0]

for i in range(1,50):
    x.append(i)
    y.append(x[i]*x[i])

test = pyl.plot(x,y)
pyl.show()