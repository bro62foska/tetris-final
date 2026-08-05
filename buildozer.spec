[app]
title = Tetris Geopolitics
package.name = tetrisgeo
package.domain = org.tetris
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Зависимости без привязки версий (чтобы избежать конфликтов Python)
requirements = python3,kivy

orientation = portrait
android.api = 33
android.minapi = 21

# Стабильный NDK
android.ndk = 26b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
