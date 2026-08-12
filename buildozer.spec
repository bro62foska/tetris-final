[app]

# Название и уникальный идентификатор приложения
title = Tetris Geo
package.name = tetrisgeo
package.domain = org.tetris

# Исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# КРИТИЧНО: Явно фиксируем целевую версию Python (3.11.5) для Android
requirements = python3==3.11.5,kivy==2.3.0

# Ориентация экрана
orientation = portrait
fullscreen = 0

# Разрешения Android
android.permissions = INTERNET

# Настройки SDK/NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
