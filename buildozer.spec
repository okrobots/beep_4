 # (1) Application configuration
[app]

# (2) General app settings
title = My Kivy App
package.name = mykivyapp
package.domain = org.example
source.dir = .
source.exclude_dirs = bin, .idea, .buildozer, __pycache__
version = 0.1
requirements = python3, kivy==2.3.0
# Add other Python dependencies here, e.g.,
# requirements = python3, kivy==2.3.0, requests, pillow

# Uncomment and modify if you have a specific icon file
# icon.filename = %(source.dir)s/data/icon.png

# Uncomment and modify if you have a specific splash screen
# splash.filename = %(source.dir)s/data/splash.png
# splash.color = #FFFFFF
# splash.orientation = portrait # or landscape, or all

# (3) Android specific settings (THESE ARE STILL PART OF THE SAME [app] SECTION)
android.minsdk = 21
android.targetsdk = 33
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, WAKELOCK, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION
android.debug = True

# Keystore information for signing your APK (for release builds)
# To create a keystore:
# keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
# android.release = True
# android.keystore = /path/to/your/my-release-key.keystore
# android.keystore.alias = alias_name
# android.keystore.password = your_keystore_password
# android.key_alias.password = your_alias_password

# (4) iOS specific settings (THESE ARE STILL PART OF THE SAME [app] SECTION)
# Set to true if you are building for iOS
# ios = False
# ios.min_deployment_target = 13.0
# ios.frameworks = Foundation, UIKit, CoreGraphics

# (5) Buildozer internal settings
# This section defines how buildozer interacts with the tools
[buildozer]

# Path to the .buildozer directory (where temporary files and builds are stored)
buildozer.dir = .buildozer

# Log level for buildozer output (0=silent, 1=error, 2=warning, 3=info, 4=debug)
log_level = 2

# Whether to install system dependencies (apt-get, pacman, etc.)
# If you're on a clean system, set to True. If you manage dependencies manually, False.
warn_on_metadeps = 1

# If you have specific patches for recipes
# patches = recipes/kivy/fix_some_bug.patch

# Enable or disable AAB (Android App Bundle) generation
# AAB is recommended for Google Play uploads. Set to True for release.
android.enable_aab = False

# Enable or disable the use of `pip install --user` for dependencies
# Set to `True` if you encounter permission issues when installing dependencies
# android.force_system_pip = False

