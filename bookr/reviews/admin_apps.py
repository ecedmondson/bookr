from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

# This file was renamed from apps.py
# to admin_apps.py
# https://github.com/PacktPublishing/Web-Development-with-Django/issues/5
# There was some sort of inheritance/filtering/other? error.


class ReviewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reviews"


class ReviewsAdminConfig(AdminConfig):
    default_site = "admin.BookrAdminSite"
