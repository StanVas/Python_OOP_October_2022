from project_05.hotel_rooms.project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = self.find_room(room_number)
        result = room.take_room(people)

        if result:
            return result

        self.guests += people

    def free_room(self, room_number: int):
        room = self.find_room(room_number)
        guests = room.guests
        result = room.free_room()

        if result:
            return result

        self.guests -= guests

    def find_room(self, room_number):
        return [r for r in self.rooms if r.number == room_number][0]

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        result = [f"Hotel {self.name} has {self.guests} total guests",
                  f"Free rooms: {', '.join(free_rooms)}",
                  f"Taken rooms: {', '.join(taken_rooms)}"
                  ]

        return '\n'.join(result)
