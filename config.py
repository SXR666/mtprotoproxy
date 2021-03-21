PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "012334sxr666456789fanqiang666def",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.cloudflare.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "284d05e57156ec0900537153378f1a46"
