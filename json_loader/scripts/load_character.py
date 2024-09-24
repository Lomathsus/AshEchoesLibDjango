import json
import os

from apps.character.models import Character, Combat
from utils.date_parse import date_parse

directory = "/Users/teorema_mac/Documents/Work/Develop/Personal/Backend/Python/AshEchoesScraper/data/characters"  # 指定JSON文件目录


def load_character():
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                person = load_info(data)
                load_battle(person, data)
        return filename


def load_info(data):
    person = Character(
        name=data["name"],
        en_name=data["en_name"],
        jp_name=data["jp_name"],
        cn_cv=data["cn_cv"],
        jp_cv=data["jp_cv"],
        profession=data["profession"],
        element=data["element"],
        rarity=data["rarity"],
        tag=data["tag"],
        prototype=data["prototype"],
        implemented_at=date_parse(data["implemented_at"]),
        acquisition=data["acquisition"],
        music_name=data["music_name"],
        expression=data["expression"],
    )
    person.save()
    return person


def load_battle(character, data):
    person = Combat(
        character=character,
        attack_name=data["attack_name"],
        attack_tag=data["attack_tag"],
        attack_range=data["attack_range"],
        attack_range_value=data["attack_range_value"],
        attack_speed=data["attack_speed"],
        attack_description=data["attack_description"],
        critical=data["critical"],
        damage_reduction=data["damage_reduction"],
        movement_distance=data["movement_distance"],
        movement_cooldown=data["movement_cooldown"],
        mastery_on_heal=data["mastery_on_heal"],
        mastery_on_damage=data["mastery_on_damage"],
        mastery_on_block=data["mastery_on_block"],
        character_enhancement=data["character_enhancement"],
    )
    person.save()
