"""Do gym."""


class Trainers:
    """Create and pull info of trainer objects."""

    def __init__(self, stamina: int, color: str):
        """Constructor, add stamina and color to obj."""
        self.stamina = stamina
        self.color = color

    def __repr__(self):
        """Print output."""
        return f"Trainers: [{self.stamina}, {self.color}]"


class Member:
    """Class for member object creating and info pulling."""

    def __init__(self, name: str, age: int, trainers: Trainers):
        """Create with name, age and Trainer class object as variables. Also gyms where member belongs to."""
        self.name = name
        self.age = age
        self.trainers = trainers
        self.gyms = []

    def get_all_gyms(self) -> list:
        """Return list of all gyms member is part of."""
        return self.gyms

    def get_gyms(self) -> list:
        """Return list of all gyms member is part of."""
        return self.gyms

    def __repr__(self):
        """Print output for the class."""
        return f"{self.name}, {self.age}: {self.trainers}"


class Gym:
    """Gym class for creating and managing gyms and by extension also members."""

    def __init__(self, name: str, max_members_number: int):
        """Create with name, max members and list of member variables."""
        self.name = name
        self.max_members = max_members_number
        self.members = []

    def add_member(self, member: Member) -> Member or None:
        """Add a member to gym. If full, remove member(s) with lowest trainer staminas. Also add gym to member."""
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
            return member
        return None

    def can_add_member(self, member: Member) -> bool:
        """Check if member can join. Has to be Member, have trainer color and pos stamina and not in this gym."""
        if type(
                member) is Member and member.trainers.color and member.trainers.stamina >= 0 and member not in self.members:
            return True
        return False

    def remove_member(self, member: Member):
        """Remove member from gym and also gym from member's gym list."""
        if member in self.members:
            self.members.remove(member)
            member.gyms.remove(self)

    def get_total_stamina(self) -> int:
        """Return gym's members' stamina sum."""
        stamina_sum = 0
        for member in self.members:
            stamina_sum += member.trainers.stamina
        return stamina_sum

    def get_members_number(self) -> int:
        """Return the number on members in gym."""
        return len(self.members)

    def get_all_members(self) -> list:
        """Return list of all gym members."""
        return self.members

    def get_average_age(self) -> float:
        """Return average gym member age, rounded to 2 decimals."""
        age_sum = 0
        for member in self.members:
            age_sum += member.age
        return round(age_sum / len(self.members), 2)

    def get_trainer_color_count(self, color: str):
        """Return number of members with specified trainer color."""
        count = 0
        for member in self.members:
            if member.trainers.color == color:
                count += 1
        return count

    def get_name_count(self, name: str):
        """Return number of members with specified name."""
        count = 0
        for member in self.members:
            if member.name == name:
                count += 1
        return count

    def __repr__(self):
        """Print output for the class."""
        return f"Gym {self.name} : {len(self.members)} member(s)"


class City:
    """City class for creating and destroying gyms and pulling some data."""

    def __init__(self, max_gym_number: int):
        """Create max gym count variable and list of gyms in city."""
        self.max_gyms = max_gym_number
        self.gyms = []

    def build_gym(self, gym: Gym) -> Gym or None:
        """Create gym if can build one."""
        if self.can_build_gym():
            self.gyms.append(gym)
            return gym
        return None

    def can_build_gym(self) -> bool:
        """Return true if building a gym wouldn't go above allowed gym count in city."""
        if self.max_gyms > len(self.gyms):
            return True
        return False

    def destroy_gym(self):
        """Destroy gym(s) with lowest member count from city, remove gym members first."""
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
        """Return list of gym(s) with max member count."""
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
        """Return list of gym(s) with max total stamina."""
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
        """Return list of gym(s) with highest average member age."""
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
        """Return list of gym(s) with lowest average member age."""
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
        """Return list of gym(s) with members of specified trainers color, sorted from highest to lowest count."""
        gyms_with_color = []
        for gym in self.gyms:
            count = gym.get_trainer_color_count(color)
            if count:
                gyms_with_color.append(gym)
        return sorted(gyms_with_color, key=lambda x: x.get_trainer_color_count(color), reverse=True)

    def get_gyms_by_name(self, name: str) -> list:
        """Return list of gym(s) with members of specified name, sorted from highest to lowest count."""
        gyms_with_this_name = []
        for gym in self.gyms:
            count = gym.get_name_count(name)
            if count:
                gyms_with_this_name.append(gym)
        return sorted(gyms_with_this_name, key=lambda x: x.get_name_count(name), reverse=True)

    def get_all_gyms(self) -> list:
        """Return list of all gyms in the city."""
        return self.gyms
