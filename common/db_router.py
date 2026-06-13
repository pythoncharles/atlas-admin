BUSINESS_APP_LABELS = {
    "users",
    "assessments",
    "reports",
    "goals",
    "daily",
    "weekly",
    "payments",
    "ai",
    "shares",
    "files",
}


class BusinessDatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in BUSINESS_APP_LABELS:
            return "business"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in BUSINESS_APP_LABELS:
            return "business"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        app_labels = {obj1._meta.app_label, obj2._meta.app_label}
        if app_labels & BUSINESS_APP_LABELS:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in BUSINESS_APP_LABELS:
            return False
        return db == "default"
