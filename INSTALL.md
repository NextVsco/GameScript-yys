## 安装：

- vscode 安装

  - 安装扩展插件：`Python` 插件安装，`Pip Manager` 插件安装

- [python 安装地址](https://www.python.org/downloads/release/python-3114/)

  - python 环境变量配置： path 新增“C:\Users\Administrator\AppData\Local\Programs\Python\Python311”

  - pip 环境变量配置 path 新增“C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Scripts”

- [Airtest IDE 安装地址（可选装）](http://airtest.netease.com/download.html?download=win64/AirtestIDE-win-1.2.15.zip&&site=io)

- 安装 airtest 外部库命令
  ```cmd
  pip install airtest
  ```
  注：`python 3.12中移除了distutils，需要安装以下包`
  ```
  pip install setuptools
  pip install packaging
  ```

## 补充

安装完成后，使用终端启动 `index.py` 文件，注意：苹果设备需要`Xcode`安装相关程序才可 🔗 手机

## 库文件修改：

### Windows

- [控制台关闭 airtest 模块 log 输出（windos 下）](Lib\logging__init__.py)
  ```py
  # 在104行附近，将DEBUG = 10改为DEBUG = 0
  WARNING = 30
  WARN = WARNING
  INFO = 20
  # DEBUG = 10
  DEBUG = 0
  NOTSET = 0
  ```

### iOS

- [swipe 方法在 iOS 下异常](/Python/Python312/Lib/site-packages/airtest/core/ios/ios.py)

  ```py
  # 在459行附近，注释原本对fpos、tpos的换算方法
  def swipe(self, fpos, tpos, duration=0, delay=None, *args, **kwargs):
        """
        Args:
            fpos: start point
            tpos: end point
            duration (float): start coordinate press duration (seconds), default is None
            delay (float): start coordinate to end coordinate duration (seconds)

        Returns:
            None

        Examples:
            >>> swipe((1050, 1900), (150, 1900))
            >>> swipe((0.2, 0.5), (0.8, 0.5))

        """
        # if not (fx < 1 and fy < 1):
        #     fx, fy = int(fx * self.touch_factor), int(fy * self.touch_factor)
        # if not (tx < 1 and ty < 1):
        #     tx, ty = int(tx * self.touch_factor), int(ty * self.touch_factor)
        fx, fy = self._transform_xy(fpos)
        tx, ty = self._transform_xy(tpos)
  ```
