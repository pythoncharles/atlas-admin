# atlas-admin 架构

## 职责边界

`atlas-admin` 是 Atlas 的企业管理后台，负责展示和操作 `atlas-server` 创建的业务数据。

它不负责：

- 创建业务表
- 修改业务表结构
- 管理 Alembic 迁移
- 调用 Qwen 生成业务内容
- 对外提供小程序 API

业务表结构唯一来源是 `atlas-server` 的 SQLAlchemy model 和 Alembic migration。

## 目录结构

```text
atlas_admin/
├── settings.py          # Django 配置和 .env 读取
├── urls.py
├── asgi.py
└── wsgi.py

apps/
├── users/               # 用户和用户资料
├── assessments/         # 问卷题目、回答、体检记录
├── reports/             # AI 报告
├── goals/               # 目标和任务
├── daily/               # 每日建议
├── weekly/              # 周报复盘
├── payments/            # 订单和会员
├── ai/                  # Prompt 与 AI 调用日志
├── shares/              # 分享记录
└── files/               # 文件记录

common/
├── business_admin.py    # 统一业务后台基类
└── permissions.py       # 权限预留

tests/
```

## 数据访问模型

每个业务 app 都定义 Django model，但这些 model 只映射已有表：

```python
class Meta:
    managed = False
    db_table = "server_table_name"
```

Django 可以用这些 model 做后台增删改查，但不会生成或执行业务表迁移。

## 后台模块

- 用户：`users`, `user_profiles`
- 问卷：`assessment_questions`, `assessment_answers`, `life_assessments`
- 报告：`life_reports`
- 目标：`goals`, `goal_tasks`
- 每日建议：`daily_suggestions`
- 周报：`weekly_reviews`
- 支付会员：`orders`, `subscriptions`
- AI：`prompt_templates`, `ai_call_logs`
- 分享：`share_records`
- 文件：`files`

## 配置

配置通过 `.env` 注入，由 `atlas_admin/settings.py` 读取。

关键配置：

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `MYSQL_HOST`
- `MYSQL_PORT`
- `MYSQL_DATABASE`
- `MYSQL_USER`
- `MYSQL_PASSWORD`

后台数据库用户应具备业务需要的读写权限，但不应拥有随意变更表结构的权限。

## 迁移策略

业务 app 在 `settings.py` 中配置：

```python
MIGRATION_MODULES = {
    "users": None,
    "assessments": None,
    "reports": None,
    "goals": None,
    "daily": None,
    "weekly": None,
    "payments": None,
    "ai": None,
    "shares": None,
    "files": None,
}
```

新增业务表时：

1. 先在 `atlas-server` 添加 SQLAlchemy model 和 Alembic migration。
2. 迁移数据库。
3. 在 `atlas-admin` 添加 `managed=False` model。
4. 注册 Django Admin。
5. 更新业务 model 测试，确认表名覆盖。

## 测试策略

- `test_business_models.py` 确认所有业务 model 都是 `managed=False`，且表名与 server 保持一致。
- `test_admin_business_permissions.py` 确认后台保留默认操作权限。
- `test_django_setup.py` 确认 Django 配置可加载。

## 与其他项目关系

```text
atlas-server
  -> 创建和迁移 atlas_db 业务表

atlas-admin
  -> 连接 atlas_db
  -> Django Admin 操作业务数据

atlas-miniapp
  -> 不访问 admin
  -> 只访问 atlas-server API
```
