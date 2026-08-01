
[app]
title = Tetris Geopolitics
package.name = tetrisgeo
package.domain = org.tetris
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Указываем конкретную стабильную версию Python (ЭТО ИСПРАВИТ ОШИБКУ!)
requirements = python3==3.11,kivy

orientation = portrait
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1



