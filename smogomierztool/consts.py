import sys

from .qtvariant import QtCore


# Firmware update repository
#UPDATE_REPOSITORY = 'https://raw.githubusercontent.com/hackerspace-silesia/Smogomierz/blob/dev/firmware/'
#UPDATE_REPOSITORY = 'http://smogomierz.hs-silesia.pl/firmware/'
UPDATE_REPOSITORY = 'https://smogomierz.hs-silesia.pl/firmware/'


# URI prefixes (protocol parts, essentially) to be downloaded using requests
ALLOWED_PROTO = ('http://', 'https://')

# vid/pid pairs of known NodeMCU/ESP8266 development boards
PREFERED_PORTS = [
    # CH341
    (0x1A86, 0x7523),

    # CP2102
    (0x10c4, 0xea60),
]

ROLE_DEVICE = QtCore.Qt.UserRole + 1

if sys.platform.startswith('darwin'):
    DRIVERS_URL = 'https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver'
elif sys.platform.startswith(('cygwin', 'win32')):
    DRIVERS_URL = 'http://www.wch.cn/downloads/CH341SER_ZIP.html'
else:
    DRIVERS_URL = None
