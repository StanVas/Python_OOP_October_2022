class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cos: int):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cos

        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        output = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        [output.append(f"==={s} - {m}") for s, m in self.skills.items()]
        # for key, value in self.skills.items():   # the same like top
        #     output.append(f"==={key} - {value}")
        return "\n".join(output)
        # return f"Name: {self.name}\n" \
        #        f"Guild: {self.guild}\n" \
        #        f"HP: {self.hp}\n" \
        #        f"MP: {self.mp}\n" + \
        #     '\n'.join([f"==={s} - {m}" for s, m in self.skills.items()])
