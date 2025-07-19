[app]
# 应用基础信息
title = beep_4
package.name = beep4
package.domain = org.example
version = 1.0

# 源代码配置
source.dir = .  # 关键修正点：指定当前目录为源码目录
source.include_exts = py,png,jpg,kv,ttf
requirements = python3,kivy,requests  # 添加网络依赖

# 安卓专属配置
android.permissions = INTERNET  # 启用网络权限
android.api = 33  # 指定Android API级别
p4a.branch = develop  # 使用开发版工具链

# 构建优化
log_level = 2
warn_on_root = 1
