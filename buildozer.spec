
# 应用基础信息
title = beep_4
package.name = beep4
package.domain = org.example
version = 1.0

# 源代码配置
source.dir = ./src # 关键修正点：指定当前目录为源码目录
source.include_exts = py,png,jpg,kv,ttf
requirements = python3==3.9.13,kivy==2.1.0,requests==2.28.1 # 添加网络依赖

# 安卓专属配置
android.api = 30 
android.minapi = 21 
android.ndk = 23b 
android.permissions = INTERNET 
android.allow_backup = False 


# 构建优化
log_level = 2
warn_on_root = 1
