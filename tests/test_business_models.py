from django.apps import apps

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


def test_all_business_models_are_unmanaged() -> None:
    business_models = [model for model in apps.get_models() if model._meta.app_label in BUSINESS_APP_LABELS]

    assert business_models
    assert all(model._meta.managed is False for model in business_models)


def test_business_tables_keep_server_names() -> None:
    expected_tables = {
        "users",
        "user_profiles",
        "assessment_questions",
        "assessment_answers",
        "life_assessments",
        "life_reports",
        "goals",
        "goal_tasks",
        "daily_suggestions",
        "weekly_reviews",
        "orders",
        "subscriptions",
        "prompt_templates",
        "ai_call_logs",
        "share_records",
        "files",
    }
    actual_tables = {
        model._meta.db_table for model in apps.get_models() if model._meta.app_label in BUSINESS_APP_LABELS
    }

    assert expected_tables <= actual_tables
