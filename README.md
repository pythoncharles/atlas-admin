# atlas-admin

企业级 AI 人生副驾驶运营后台，基于 Django Admin 和 django-unfold，为运营人员提供业务数据管理能力。

## 技术栈

- Python 3.13.1
- Django 6.0
- django-unfold
- Poetry
- MySQL
- pytest / pytest-django

## 项目文档

- [项目架构](docs/ARCHITECTURE.md)

## 本地开发

```bash
poetry install
cp .env.example .env
poetry run python manage.py check
poetry run python manage.py runserver 0.0.0.0:9999
```

后台地址：

```text
http://127.0.0.1:9999/admin/
```

## 测试与质量检查

```bash
poetry run pytest
poetry run ruff check .
poetry run black --check .
poetry run python manage.py check
```

## 业务表规则

- `atlas-server` 使用 Alembic 管理所有业务表结构。
- `atlas-admin` 可以通过 Django Admin 操作业务数据。
- 所有业务 model 必须设置 `managed = False`。
- 禁止为业务 app 创建或执行 Django migrations。
- 新增业务表后，需要在后台同步 `managed=False` model、admin 注册和测试覆盖。

## Docker Compose

```bash
cp .env.example .env
docker compose up --build
```

`atlas-admin` 需要连接已经由 `atlas-server` 初始化和迁移完成的 `atlas_db`。

## 初始化管理员

```bash
poetry run python manage.py createsuperuser
```

也可以使用 `.env.example` 中预留的超级管理员变量自行编写初始化脚本。
