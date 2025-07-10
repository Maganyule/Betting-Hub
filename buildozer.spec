[app]
title = Betting Hub
package.name = BettingHub
package.domain = org.maganyule.bettinghub

source.dir = .
source.include_exts = py,kv,json,png,jpg
version = 6.0

requirements = python3,kivy,requests
android.permissions = INTERNET

# ✅ Add this to fix zlib header issue in Termux
android.add_env = CFLAGS=-I/data/data/com.termux/files/usr/include,LDFLAGS=-L/data/data/com.termux/files/usr/lib

# Optional icon (if you have one)
# icon.filename = %(source.dir)s/icon.png

# Optional: include assets like fonts or sounds
# source.include_patterns = assets/*,fonts/*

[buildozer]
log_level = 2
warn_on_root = 1
