def player_info(self):
    output = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
    [output.append(f"==={s} - {m}") for s, m in self.skills.items()]
    # for key, value in self.skills.items():   # the same like top
    #     output.append(f"==={key} - {value}")
    return "\n".join(output)

# another way
    # return f"Name: {self.name}\n" \
    #        f"Guild: {self.guild}\n" \
    #        f"HP: {self.hp}\n" \
    #        f"MP: {self.mp}\n" + \
    #     '\n'.join([f"==={s} - {m}" for s, m in self.skills.items()])
