# buildozer.spec for Betting Hub v6.0

[app]

# (str) Title of your application
title = Betting Hub

# (str) Package name
package.name = BettingHub

# (str) Package domain (reverse DNS style)
package.domain = org.maganyule.bettinghub

# (list) Source file extensions to include (separated by commas)
source.include_exts = py,kv,json,png,jpg

# (str) Application requirements
requirements = python3,kivy,requests

# (list) Permissions
android.permissions = INTERNET

# (int) Target API level (optional)
# android.api = 33

# (int) Minimum API your app will support (optional)
# android.minapi = 21

# (int) Android SDK version to use (optional)
# android.sdk = 24

# (str) Presplash image path (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (bool) If True, use --private data storage (optional)
# android.private_storage = True

# (bool) If True, copy all assets inside APK (optional)
# android.copy_libs = 1

# (str) Android entry point, default is org.kivy.android.PythonActivity (optional)
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'import android' (optional)
# android.theme = '@android:style/Theme.NoTitleBar'

# (list) Permissions (additional) if any
# android.permissions = INTERNET, ACCESS_FINE_LOCATION

[buildozer]

# (str) Log level (optional)
log_level = 2

# (int) Number of build processes (optional)
# max_parallel_builds = 1
