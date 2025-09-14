# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False   # ✅ Set to False in production

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]  # update with your domain in production

# -----------------------
# Security Settings
# -----------------------

# Enforce HTTPS for all requests
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow browsers to preload HSTS policy

# Tell Django it’s behind a proxy that handles SSL
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Cookies sent only via HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Browser security headers
SECURE_BROWSER_XSS_FILTER = True   # Helps prevent reflected XSS attacks
SECURE_CONTENT_TYPE_NOSNIFF = True # Stops MIME type sniffing
X_FRAME_OPTIONS = "DENY"           # Prevents clickjacking
