def mask_text(value: str | None, *, prefix: int = 4, suffix: int = 4) -> str:
    if not value:
        return ""
    if len(value) <= prefix + suffix:
        return "*" * len(value)
    return f"{value[:prefix]}****{value[-suffix:]}"
