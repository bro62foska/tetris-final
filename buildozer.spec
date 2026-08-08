[app]

# (str) Title of your application
title = TetrisGeo

# (str) Package name
package.name = tetrisgeo

# (str) Package domain (needed for android packaging)
package.domain = org.tetrisgeo

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Зафиксированы Kivy 2.3.0 и Cython 0.29.33 для исключения ошибок компиляции GIL
requirements = python3,kivy==2.3.0,cython==0.29.33

# (str) Presumed orientation (portrait, landscape, sensor-landscape, etc.)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (bool) Автоматическое принятие лицензий Android SDK
android.accept_sdk_license = True

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Фиксация рабочей версии Build-Tools (устраняет ошибку Aidl)
android.build_tools_version = 33.0.2

# (list) List of Android architectures to build for
android.archs = arm64-v8a

# (bool) Enable Android auto backup feature
android.allow_backup = True

# (str) A branch to checkout of python-for-android
# Ветка develop предотвращает затягивание экспериментального Python 3.14
p4a.branch = develop

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
