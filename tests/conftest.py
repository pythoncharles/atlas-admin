import os

os.environ.setdefault("DJANGO_SECRET_KEY", "test-secret-key-with-at-least-32-bytes")
os.environ.setdefault("DJANGO_DEBUG", "true")
os.environ.setdefault("MYSQL_DATABASE", ":memory:")
