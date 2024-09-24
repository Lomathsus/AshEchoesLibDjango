import os
import django
from django.core.management import execute_from_command_line


# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AshEchoesLibDjango.settings")

# 初始化 Django
django.setup()

import json
from apps.character.models import Character, Combat, BasicStat
from utils.date_parse import date_parse
from utils.extract_numbers import extract_numbers

directory = "/Users/teorema_mac/Documents/Work/Develop/Personal/Backend/Python/AshEchoesScraper/data/characters"  # 指定JSON文件目录


def load_all_character():
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                character = load_info(data)
                load_combat(character, data)
        return filename


def load_one_character(filename):
    file_path = os.path.join(directory, filename + ".json")
    with open(file_path, "r") as file:
        print(f"{filename}.json loading...")
        data = json.load(file)
        character = load_info(data)
        load_combat(character, data)
        # load_basic_stat(character, data["basic_stats"])
    print(f"{filename}.json loaded!")


def load_info(data):
    character = Character(
        name=data["name"],
        en_name=data["en_name"],
        jp_name=data["jp_name"],
        cn_cv=data["cn_cv"],
        jp_cv=data["jp_cv"],
        profession=data["profession"],
        element=data["element"],
        rarity=data["rarity"],
        tags=data["tags"],
        prototype=data["prototype"],
        implemented_at=date_parse(data["implemented_at"]),
        acquisitions=data["acquisitions"],
        music_name=data["music_name"],
        expressions=data["expressions"],
    )
    existed_character = character.save()
    if existed_character:
        return existed_character
    else:
        return character


def load_combat(character, data):
    combat_data = data["combat_stats"]
    mastery_bonus = data["mastery_bonus"]

    combat = Combat(
        character=character,
        attack_tags=combat_data["attack_tags"],
        attack_range=combat_data["attack_range"],
        attack_range_value=combat_data["range_value"],
        attack_speed=combat_data["attack_speed"],
        attack_description=combat_data["attack_description"],
        critical_rate=combat_data["critical_rate"],
        basic_damage_reduction=combat_data["basic_damage_reduction"],
        reposition_distance=combat_data["reposition_distance"],
        reposition_cooldown=combat_data["reposition_cooldown"],
        mastery_on_healing=mastery_bonus["healing"],
        mastery_on_damage_bonus=mastery_bonus["damage_bonus"],
        mastery_on_block=mastery_bonus["block"],
        character_enhancement=data["character_enhancement"],
    )
    combat.save()


def load_basic_stat(character, data):
    print(data)
    # for level in data.basic_stats:
    # level_num = extract_numbers(level)
    # basic_stat = BasicStat(
    #     character=character,
    #     level=level_num,
    #     vitality=level.vatility
    # )


load_one_character("乐无异")
