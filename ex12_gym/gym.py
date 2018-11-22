"""Do gym."""


class Trainers:
    """Trainer class for trainer stuff."""

    def __init__(self, stamina: int, color: str):
        self.stamina = stamina
        self.color = color

    def __repr__(self):
        return f"Trainers: [{self.stamina}, {self.color}]"


class Member:
    """Member class for member stuff."""

    def __init__(self, name: str, age: int, trainers: Trainers):
        self.name = name
        self.age = age
        self.trainers = trainers
        self.gyms = []

    def get_all_gyms(self) -> list:
        return self.gyms

    def get_gyms(self) -> list:
        return self.gyms

    def __repr__(self):
        return f"{self.name}, {self.age}: {self.trainers}"


class Gym:
    """Gym class for gym stuff."""

    def __init__(self, name: str, max_members_number: int):
        self.name = name
        self.max_members = max_members_number
        self.members = []

    def add_member(self, member: Member) -> Member:
        if self.can_add_member(member):
            if len(self.members) >= self.max_members:
                min_stamina = float("inf")
                min_members = []
                for any_member in self.members:
                    if any_member.trainers.stamina < min_stamina:
                        min_stamina = any_member.trainers.stamina
                        min_members = [any_member]
                    elif any_member.trainers.stamina == min_stamina:
                        min_members.append(any_member)
                for min_member in min_members:
                    self.remove_member(min_member)
            self.members.append(member)
            member.gyms.append(self)
            return Member
        return None

    def can_add_member(self, member: Member) -> bool:
        if type(member) is Member and member.trainers.color and member.trainers.stamina >= 0 and member not in self.members:
            return True
        return False

    def remove_member(self, member: Member):
        if member in self.members:
            self.members.remove(member)
            member.gyms.remove(self)

    def get_total_stamina(self) -> int:
        stamina_sum = 0
        for member in self.members:
            stamina_sum += member.trainers.stamina
        return stamina_sum

    def get_members_number(self) -> int:
        return len(self.members)

    def get_all_members(self) -> list:
        return self.members

    def get_average_age(self) -> float:
        age_sum = 0
        for member in self.members:
            age_sum += member.age
        return round(age_sum / len(self.members), 2)

    def get_trainer_color_count(self, color: str):
        count = 0
        for member in self.members:
            if member.trainers.color == color:
                count += 1
        return count

    def get_name_count(self, name: str):
        count = 0
        for member in self.members:
            if member.name == name:
                count += 1
        return count

    def __repr__(self):
        return f"Gym {self.name} : {len(self.members)} member(s)"


class City:

    def __init__(self, max_gym_number: int):
        self.max_gyms = max_gym_number
        self.gyms = []

    def build_gym(self, gym: Gym) -> Gym or None:
        if self.can_build_gym():
            self.gyms.append(gym)
            return gym
        return None

    def can_build_gym(self) -> bool:
        if self.max_gyms > len(self.gyms):
            return True
        return False

    def destroy_gym(self):
        min_membercount = float("inf")
        min_membercount_gyms = []
        for gym in self.gyms:
            if len(gym.members) < min_membercount:
                min_membercount = len(gym.members)
                min_membercount_gyms = [gym]
            elif len(gym.members) == min_membercount:
                min_membercount_gyms.append(gym)
        for gym in min_membercount_gyms:
            for member in gym.members:
                gym.remove_member(member)
            self.gyms.remove(gym)

    def get_max_members_gym(self) -> list:
        max_membercount = 0
        max_membercount_gyms = []
        for gym in self.gyms:
            if len(gym.members) > max_membercount:
                max_membercount = len(gym.members)
                max_membercount_gyms = [gym]
            elif len(gym.members) == max_membercount:
                max_membercount_gyms.append(gym)
        return max_membercount_gyms

    def get_max_stamina_gyms(self) -> list:
        max_stamina = 0
        max_stamina_gyms = []
        for gym in self.gyms:
            if gym.get_total_stamina() > max_stamina:
                max_stamina = gym.get_total_stamina()
                max_stamina_gyms = [gym]
            elif gym.get_total_stamina() == max_stamina:
                max_stamina_gyms.append(gym)
        return max_stamina_gyms

    def get_max_average_ages(self) -> list:
        max_avgage = 0
        max_avgage_gyms = []
        for gym in self.gyms:
            if gym.get_average_age() > max_avgage:
                max_avgage = gym.get_average_age()
                max_avgage_gyms = [gym]
            elif gym.get_average_age() == max_avgage:
                max_avgage_gyms.append(gym)
        return max_avgage_gyms

    def get_min_average_ages(self) -> list:
        min_avgage = float("inf")
        min_avgage_gyms = []
        for gym in self.gyms:
            if gym.get_average_age() < min_avgage:
                min_avgage = gym.get_average_age()
                min_avgage_gyms = [gym]
            elif gym.get_average_age() == min_avgage:
                min_avgage_gyms.append(gym)
        return min_avgage_gyms

    def get_gyms_by_trainers_color(self, color: str) -> list:
        gyms_with_color = []
        for gym in self.gyms:
            count = gym.get_trainer_color_count(color)
            if count:
                gyms_with_color.append(gym)
        return sorted(gyms_with_color, key=lambda x: x.get_trainer_color_count(color), reverse=True)

    def get_gyms_by_name(self, name: str) -> list:
        gyms_with_this_name = []
        for gym in self.gyms:
            count = gym.get_name_count(name)
            if count:
                gyms_with_this_name.append(gym)
        return sorted(gyms_with_this_name, key=lambda x: x.get_name_count(name), reverse=True)

    def get_all_gyms(self) -> list:
        return self.gyms


if __name__ == "__main__":
    city1 = City(100)
    gym = Gym("TTÜ Sport", 50)
    city1.build_gym(gym)

    trainers1 = Trainers(50, "blue")
    trainers2 = Trainers(50, "grey")

    member = Member("Ago Luberg", 35, trainers1)
    member2 = Member("Ahti Lohk", 35, trainers2)

    gym.add_member(member)
    gym.add_member(member2)

    print(gym.get_members_number())  # 2

    print(gym.get_all_members())  # [Ago Luberg, 35: Trainers: [50, blue], Ahti Lohk, 35: Trainers: [50, grey]]

    gym.add_member(member)  # Trying to add Ago again
    print(gym.get_members_number())  # 2 //We can't...

    for i in range(48):
        gym.add_member(Member("Tudeng Tudeng", 20, Trainers(49, "blue")))

    print(gym.get_members_number())  # 50

    trainers3 = Trainers(60, "blue")
    member_new = Member("Megane", 19, trainers3)
    gym.add_member(member_new)

    print(
        gym.get_members_number())  # 3 -> Ago, Ahti and Megan, all others were removed because of the lowest trainers' stamina

    city2 = City(10)
    city2.build_gym(Gym("MyFitness", 100))
    city2.destroy_gym()

    for i in range(10):
        city2.build_gym(Gym("Super Gym", 10))

    print(city2.can_build_gym())  # False -> Cannot build gym, city is full of them

    #######################################################################################

    city3 = City(100)

    gym4 = Gym("Sparta", 50)
    gym5 = Gym("People Fitness", 30)
    gym6 = Gym("Gym Eesti", 100)

    city3.build_gym(gym4)
    city3.build_gym(gym5)
    city3.build_gym(gym6)

    gym4.add_member(Member("Bob", 18, Trainers(50, "black")))
    gym4.add_member(Member("Emma", 20, Trainers(70, "red")))
    gym4.add_member(Member("Ken", 25, Trainers(40, "grey")))

    gym5.add_member(Member("Merili", 18, Trainers(100, "pink")))
    gym5.add_member(Member("Richard", 20, Trainers(70, "green")))

    gym6.add_member(Member("Bella", 40, Trainers(15, "green")))
    gym6.add_member(Member("Bob", 50, Trainers(70, "green")))
    gym6.add_member(Member("Sandra", 25, Trainers(30, "pink")))
    gym6.add_member(Member("Bob", 35, Trainers(50, "black")))

    print(city3.get_max_members_gym())  # [Gym Gym Eesti : 4 member(s)]
    print(city3.get_max_stamina_gyms())  # [Gym People Fitness : 2 member(s)]
    print(city3.get_max_average_ages())  # [Gym Gym Eesti : 4 member(s)] => average age 37,5
    print(city3.get_min_average_ages())  # [Gym People Fitness : 2 member(s)] => average age 19
    print(city3.get_gyms_by_trainers_color(
        "green"))  # [Gym Gym Eesti : 4 member(s), Gym People Fitness : 2 member(s)] => Gym Eesti has 2 members with green trainers, People Fitness has 1.
    print(city3.get_gyms_by_name(
        "Bob"))  # [Gym Gym Eesti : 4 member(s), Gym Sparta : 2 member(s)] => Gym Eesti has 2 members with name Bob, Sparta has 1.