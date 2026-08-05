[app]

# (str) Title of your application
title = Tetris Geopolitics

# (str) Package name
package.name = tetrisgeo

# (str) Package domain (needed for android/ios packaging)
package.domain = org.tetris

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# ВАЖНО: Убран фиксированный 'python3==3.11' для предотвращения конфликтов с hostpython3
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 26b

# (bool) If True, then automatically accept SDK license agreements.
android.accept_sdk_license = True

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (list) Gradle dependencies to add
android.gradle_dependencies = 'com.android.tools.build:gradle:8.0.2'

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with output of which commands run))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
