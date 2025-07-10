[app]
# (str) Title of your application
title = Betting Hub

# (str) Package name
package.name = BettingHub

# (str) Package domain (reverse DNS style)
package.domain = org.maganyule.bettinghub

# (str) Source code directory
source.dir = .

# (list) Source file extensions to include (comma separated)
source.include_exts = py,kv,json,png,jpg

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests

# (list) Permissions
android.permissions = INTERNET

# (str) Icon of the app (optional)
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Supported Android SDK API level
# android.api = 33

# (str) Minimum Android SDK API your APK will support
# android.minapi = 21

# (str) Android SDK version to use
# android.sdk = 33

# (str) Android NDK version to use
# android.ndk = 25b

# (bool) Use --private data storage (True recommended)
# android.private_storage = True

[buildozer]
# (int) Log level (0=error, 1=info, 2=debug)
log_level = 2

# (int) Number of build processes to run in parallel (default 1)
# max_parallel_builds = 1

# (str) Path to build directory (optional)
# build_dir = ./build

# (str) Path to cache directory (optional)
# cache_dir = ~/.buildozer
