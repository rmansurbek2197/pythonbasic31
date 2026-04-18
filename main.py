def eng_kichik_son(sonlar):
    if not sonlar:
        return None
    return min(sonlar)

sonlar = [12, 45, 7, 23, 56, 89, 34]
print(eng_kichik_son(sonlar))