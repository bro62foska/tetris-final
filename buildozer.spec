[app]
title = Tetris Geopolitics
package.name = tetrisgeo
package.domain = org.tetris
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
orientation = portrait

# Фиксируем стабильные версии API, чтобы он не пытался качать сырые беты
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.ndk = 25.2.9519653
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

