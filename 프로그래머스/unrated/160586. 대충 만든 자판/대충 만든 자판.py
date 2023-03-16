def solution(keymap, targets):
    keytable = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i + 1
            else:
                keytable[key] = min(keytable[key], i + 1)
                # "keytable"이라는 딕셔너리에서 "key" 값이 이미 존재하면 그 값을 그대로 유지하면서, "i+1" 값이 더 작을 경우에만 해당 값을 업데이트

    result = []
    for target in targets:
        clicked = 0
        for key in target:
            if key not in keytable:
                clicked = -1
                break
            clicked += keytable[key]
        result.append(clicked)

    return result