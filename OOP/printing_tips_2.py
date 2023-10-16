def animals_status(self):
    # info = {"Lion": [], "Tiger": [], "Cheetah": []}
    # first way:
    # [info[x.__class__.__name__].append(str(x)) for x in self.animals]
    # second way:
    # for animal in self.animals:
    #     info[animal.__class__.__name__].append(str(animal))
    # third way:
    lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
    tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
    cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

    result = [
        f"You have {len(self.animals)} animals",
        f"----- {len(lions)} Lions:"
    ]
    result.extend(lions)

    result.append(f"----- {len(tigers)} Tigers:")
    result.extend(tigers)

    result.append(f"----- {len(cheetahs)} Cheetahs:")
    result.extend(cheetahs)

    return "\n".join(str(r) for r in result)

# More info in project_04 => folder wild_cat_zoo
