## 阴阳师自动化脚本

前言：如果你是个小白，请先看该文件[ROOKIE.txt](ROOKIE.txt)

### 说明

`特别声明：该脚本仅限个人自行使用。`  
 脚本设计初衷是解决【阴阳师】这款游戏中肝度高，替代重复性动作等因素所设计，顺便还能提升开发者我的项目能力；  
 其中包含御魂、绘卷等高强度肝度活动，后续常驻活动的相关脚本也会积极去开发完善；  
 为保证账号安全性，该项目也考虑区域随机点击，时间间隔停顿等模拟正常玩家操作行为。  
 项目主要使用图片识别的公开库`“airtest”`，通过图片匹配进行场景判断和行为动作的执行，由于图片识别的技术影响，游戏在部分设备上可能存在无法识别，脚本执行异常，造成无法正常工作的情况。届时需要开发者自行调试处理，当然本人也会积极完善，增强项目本身的健硕性。

### 目录

- config 设置
- Dungeon 业务脚本
- images 图片
- utils 工具文件
- logs 日志

### 终端 cmd 启动

window 下执行 win.py 文件查看窗口句柄，手机设备请自行查找连接电脑的方式。AirtestIDE 中也有连接设备的功能。
```
python D:\Develop\GameScript-yys\index.py
```

### iOS环境命令

```
cd /Users/Desktop/GameScript-yys ; /usr/bin/env /usr/local/bin/python3.12 -- /Users/Desktop/GameScript-yys/index.py
```

### iOS IP 映射

```
iproxy 8100 8100
sudo lsof -i :8100 端口
kill -9 端口映射地址（PID）
```
