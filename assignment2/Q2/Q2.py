import csv
'''
australia.py

A program that simulates the relocation of Australian animals across states.

Each animal has a known threat to avoid. The goal is to relocate as many
animals as possible while ensuring that no animal ends up near its threat —
and no two animals share the same state.

This program involves reading animal data from a file, building objects to
represent each animal, and implementing relocation logic to ensure animals
are placed safely.
'''

ADJACENT_STATES = {
    "NSW" : ["VIC","SA","QLD"],
    "QLD" : ["NT","SA","NSW"],
    "VIC" : ["SA","NSW"],
    "TAS" : [],
    "SA" : ["WA","NT","QLD","NSW","VIC"],
    "NT" : ["WA","SA","QLD"],
    "WA" : ["SA","NT"]
}  # fill in with adjacent states for each state!


class FictionalAnimal:
    '''
    Represents a fictional Australian animal used in the relocation simulation.

    Each animal has a name, habitat, threat, and current state.
    '''

    def __init__(self, name: str, habitat: str, threat: str, state = "ACT"):
        '''
        Initialises a new FictionalAnimal with the given name, habitat, and threat.
        Sets the starting state to 'ACT' by default.

        Parameters:
            name (str): The name of the animal.
            habitat (str): The animal's preferred habitat.
            threat (str): The name of another animal that poses a threat.
        '''
        self.name = name
        self.habitat = habitat
        self.threat = threat
        self.state = state
        pass

    def get_state(self) -> str:
        '''Returns the current state where this animal is located.'''
        return self.state
        pass

    def set_state(self, state: str):
        '''
        Updates the animal's state if the new state is valid.

        A valid state is one that exists in the list of defined states.
        If the state is not valid, the location does not change.

        Parameters:
            state (str): The new state to assign to the animal.
        '''
        if state not in ADJACENT_STATES.keys():
            return None
        else:
            self.state = state
        pass

    def __str__(self) -> str:
        '''
        Returns a formatted string representing the animal's details.
        Format:
        <name>
           Habitat : <habitat>
           Threat  : <threat>
           State   : <state>
        '''
        return f"{self.name}\n   Habitat : {self.habitat}\n   Threat  : {self.threat}\n   State   : {self.state}"
        pass

    def load_dataset() -> list['FictionalAnimal']:
        '''
        Loads animal data from animals.csv and returns a list of FictionalAnimal
        objects.

        Lines must follow the format: <name>,<habitat>,<threat>

        Lines with missing or extra fields are skipped.
        If the file does not exist, returns an empty list.

        Returns:
            list[FictionalAnimal]: A list of valid animal objects.
        '''
        list_fictional_animals = []
        try:
            with open("animals.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                # 一行一行输出
                for row in reader:
                    if len(row) != 3:
                        continue
                    fa = FictionalAnimal(row[0], row[1], row[2])
                    list_fictional_animals.append(fa)
            return list_fictional_animals
        except FileNotFoundError:
            return list_fictional_animals
        pass


def relocate_animals(animals: list[FictionalAnimal]):
    '''
    Simulates the relocation of Australian animals.

    No two animals can share the same state, and no animal can be next to its
    threat.

    The relocation respects the following fixed state order:
    NSW → QLD → VIC → TAS → SA → NT → WA

    Animals are considered for relocation one by one, in the order they appear
    in the list. If an animal cannot be placed in a state, its state remains
    as 'ACT'.

    Parameters:
        animals (list[FictionalAnimal]): A list of FictionalAnimal objects.
    '''
    temp = {
        "NSW": None,
        "QLD": None,
        "VIC": None,
        "TAS": None,
        "SA": None,
        "NT": None,
        "WA": None
    }
    count = 0
    temp_locate = ["NSW", "QLD", "VIC", "TAS", "SA", "NT", "WA"]
    temp_summary = []
    for i in animals:
        b = True
        for j in temp_locate:
            bol = True
            if temp[j] is None:
                for k in ADJACENT_STATES[j]:
                    if temp[k] is not None:
                        sp = temp[k].split("|")
                        if i.name == sp[1] or i.threat == sp[0]:
                            bol = False
                            break
                if bol:
                    i.set_state(j)
                    temp[j] = i.name + "|" + i.threat
                    temp_summary.append(f"{i.name}: {i.state}")
                    count += 1
                    b = False
                    break
        if b:
            temp_summary.append(f"{i.name}: {i.state}")
    return count, temp_summary


def main():
    '''
    Runs the full relocation simulation from start to finish.

    This function should:
    - Load the fictional animal data from animals.txt
    - Print each animal's details before relocation
    - Relocate the animals using relocate_animals()
    - Print each animal's updated details after relocation
    '''
    print(">> READING IN ANIMALS.")
    fa = FictionalAnimal.load_dataset()
    print(f"Loaded {len(fa)} animals from animals.csv.")
    print()
    print(">> BEFORE RELOCATION.")
    for i in fa:
        print(i.__str__())
        print()
    count, summary = relocate_animals(fa)
    print(">> RELOCATING ANIMALS.")
    print(f"Animals relocated: {count}/{len(fa)}")
    print()
    print(">> SUMMARY.")
    for i in summary:
        print(i)
    pass


# Do not modify this!
if __name__ == '__main__':
    main()