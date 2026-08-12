[app]

# Название приложения
title = Tetris Geo
# Имя пакета (должно быть уникальным)
package.name = tetrisgeo
# Домен (вместе с именем пакета формирует уникальный ID)
package.domain = org.tetris
# Исходный код (точка означает текущую папку)
source.dir = .
# Расширения файлов для упаковки
source.include_exts = py,png,jpg,kv,atlas

# Версия
version = 0.1

# Требования (библиотеки)
requirements = python3,kivy==2.3.0

# Настройки экрана
orientation = portrait
fullscreen = 0

# Разрешения Android
android.permissions = INTERNET

# Настройки Android SDK/NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]

# Уровень логов (2 — подробный)
log_level = 2
warn_on_root = 1
