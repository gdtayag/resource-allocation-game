r"""
Evennia settings file.

The available options are found in the default settings file found
here:

c:\users\mtaya\onedrive\umd\spring 2020\inst 490\evennia\evennia\evennia\settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "inst490-game"

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")

# open to the internet: 4000, 4001, 4002
# closed to the internet (internal use): 4005, 4006
TELNET_PORTS = [4000]
WEBSOCKET_CLIENT_PORT = 4002
WEBSERVER_PORTS = [(80, 4005)]
AMP_PORT = 4006

# Optional - security measures limiting interface access
# (don't set these before you know things work without them)
WEBSERVER_INTERFACES = ['0.0.0.0']
TELNET_INTERFACES = ['0.0.0.0']
WEBSOCKET_CLIENT_INTERFACE = '0.0.0.0'
WEBSOCKET_CLIENT_URL = ""
ALLOWED_HOSTS = ["*"]

# uncomment if you want to lock the server down for maintenance.
# LOCKDOWN_MODE = True


try:
    # Created by the `evennia connections` wizard
    from .connection_settings import *
except ImportError:
    pass
