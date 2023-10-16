def vowel_filter(func_ref):
    vowels = "aoeiu"

    def wrapper():
        func_res = func_ref()
        return [x for x in func_res if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
