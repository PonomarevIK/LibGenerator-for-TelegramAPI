def to_json(obj):
    if hasattr(obj, "json"):
        return obj.json
    return obj
