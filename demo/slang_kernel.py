rules = [
    ("discount", "10", lambda s: s.get("total", 0) > 100),
    ("premium", "true", lambda s: s.get("discount") == "10"),
    ("offer", "unlocked", lambda s: s.get("premium") == "true"),
]

state = {
    "total": 150
}

changed = True

while changed:
    changed = False
    for key, value, cond in rules:
        if cond(state) and state.get(key) != value:
            state[key] = value
            changed = True

print(state)
