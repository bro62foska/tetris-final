[app]

# Название и идентификаторы приложения
title = Tetris Geo
package.name = tetrisgeo
package.domain = org.tetris

# Исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Требования к сборке
requirements = python3,kivy==2.3.0

# Настройки экрана
orientation = portrait
fullscreen = 0

# Разрешения Android
android.permissions = INTERNET

# Настройки SDK / NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

# КРИТИЧНО: Запрещаем подгрузку нестабильной ветки master с Python 3.14.
# Фиксируем проверенный релиз python-for-android
p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
