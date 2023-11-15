# 配置文件说明

## 文件目录
  - index.json  
  脚本存储信息的文件，存储状态以及与其他设备通讯，脚本会写入，请勿在启动期间修改。
  - switch.json  
  外部控制脚本的方式，脚本只读，会监听该文件内容变更。


### 文件参数详情
  - index.json  
    - equipment[] 设备地址
    - equipmentState[] 设备状态
      - link 是否连接中
    - task 任务配置
      - loopTaskNum 任务循环次数，-1为无限循环
      - scene[] 任务内容
    - yuhunGroup 御魂组队
      - equipmentInfo[] 组队信息
        - isLead 是否为队长
        - loc 相对于队长，队员所在好友位坐标，补充：第一位为栏目位，第二位为顺序位
      - passTime 通关时间，秒 

  - switch.json  
    - close 结束脚本，当前任务完成后会自动退出
    - stopTask 任务暂停，当前行为结束后会暂停
    - tupoLoseMaxNum 突破失败退出次数
