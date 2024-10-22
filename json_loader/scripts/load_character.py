import os
import django
from django.core.management import execute_from_command_line


# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AshEchoesLibDjango.settings")

# 初始化 Django
django.setup()

import json
from apps.character.models import (
    Character,
    Combat,
    BasicStat,
    Collection,
    Document,
    DomSkill,
    EngravingStat,
    Equipment,
    Report,
    Seed,
    Training,
    TrainingProgram,
    SeedStableCompatibility,
    Trait,
    TraitLevel,
)
from utils.date_parse import parse_chinese_date
from utils.extract_number import extract_number

directory = "/Users/teorema_mac/Documents/Work/Develop/Personal/Python/AshEchoesScraper/data/characters"  # 指定JSON文件目录


def load_all_character():
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            load_one_character(filename)


def load_one_character(filename):
    file_path = os.path.join(directory, filename)
    with open(file_path, "r") as file:
        print(f"{filename}.json loading...")
        data = json.load(file)
        character = load_info(data)
        load_combat(character, data)
        load_basic_stat(character, data)
        load_collection(character, data)
        load_document(character, data)
        # load_dom_skill(character, data)
        load_engraving_stat(character, data)
        load_equipment(character, data)
        load_report(character, data)
        load_seed_report(character, data)
        load_training(character, data)
        load_trait(character, data)
    print(f"{filename}.json loaded!")


def load_info(data):
    character, created = Character.objects.get_or_create(
        name=data["name"],
        defaults={
            "en_name": data["en_name"],
            "jp_name": data["jp_name"],
            "cn_cv": data["cn_cv"],
            "jp_cv": data["jp_cv"],
            "profession": data["profession"],
            "element": data["element"],
            "rarity": data["rarity"],
            "tags": data["tags"],
            "prototype": data["prototype"],
            "implemented_at": parse_chinese_date(data["implemented_at"]),
            "acquisitions": data["acquisitions"],
            "expressions": data["expressions"],
        },
    )
    if created:
        print(f"Created new character: {character.id} - {character.name}")
    else:
        print(f"Found existing character: {character.id} - {character.name}")
    return character


def load_combat(character, data):
    assert (
        character.id is not None
    ), "Character instance must be saved before associating with Combat"

    combat_data = data["combat_stats"]
    mastery_bonus = data["mastery_bonus"]

    combat, created = Combat.objects.update_or_create(
        character=character,
        defaults={
            "attack_tags": combat_data["attack_tags"],
            "attack_range": combat_data["attack_range"],
            "attack_range_value": combat_data["range_value"],
            "attack_speed": combat_data["attack_speed"],
            "attack_description": combat_data["attack_description"],
            "critical_rate": combat_data["critical_rate"],
            "basic_damage_reduction": combat_data["basic_damage_reduction"],
            "reposition_distance": combat_data["reposition_distance"],
            "reposition_cooldown": combat_data["reposition_cooldown"],
            "mastery_on_healing": mastery_bonus["healing"],
            "mastery_on_damage_bonus": mastery_bonus["damage_bonus"],
            "mastery_on_block": mastery_bonus["block"],
            "character_enhancement": data["character_enhancement"],
        },
    )
    print(
        f"Saved Combat for Character {character.id} - {character.name}: {'Created' if created else 'Updated'}"
    )


def load_basic_stat(character, data):
    for level, stats in data["basic_stats"].items():
        basic_stat, created = BasicStat.objects.update_or_create(
            character=character,
            level=extract_number(level),
            defaults={
                "vitality": stats["vitality"],
                "attack": stats["attack"],
                "mastery": stats["mastery"],
            },
        )

        print(
            f"{"Created" if created else "Updated"} BasicStat for level {level} of character {character.name}."
        )


def load_collection(character, data):
    for index, (key, description) in enumerate(data["collection"].items()):
        collection, created = Collection.objects.update_or_create(
            character=character,
            sort_number=index + 1,
            defaults={
                "description": description,
            },
        )

        print(
            f"{"Created" if created else "Updated"} collection - {index} of character {character.name}."
        )


def load_document(character, data):
    for index, item in enumerate(data["documents"]):
        document, created = Document.objects.update_or_create(
            character=character,
            name=item["title"],
            defaults={"content": item["content"]},
        )
        print(
            f"{"Created" if created else "Updated"} document - {document.name} of character {character.name}."
        )


# def load_dom_skill(character, data):
#     for index, item in enumerate(data["dome_skill"]):
#         if ("name" in item and item["name"]) or (
#             "description" in item and item["description"]
#         ):
#             dom_skill, created = DomSkill.objects.update_or_create(
#                 character=character,
#                 name=item["name"],
#                 defaults={"description": item["description"]},
#             )
#             print(
#                 f"{"Created" if created else "Updated"} document - {dom_skill.name} of character {character.name}."
#             )


def load_engraving_stat(character, data):
    for level, stats in data["engraving_stats"].items():
        basic_stat, created = EngravingStat.objects.update_or_create(
            character=character,
            level=extract_number(level),
            defaults={
                "vitality": stats["vitality"],
                "attack": stats["attack"],
                "mastery": stats["mastery"],
                "defence": stats["defence"],
                "terminal": stats["terminal"],
            },
        )

        print(
            f"{"Created" if created else "Updated"} EngravingStats for level {level} of character {character.name}."
        )


def load_equipment(character, data):
    equipment_data = data["equipment"]
    if equipment_data["name"] and (not equipment_data["name"] == "无"):
        equipment, created = Equipment.objects.update_or_create(
            character=character,
            name=equipment_data["name"],
            defaults={
                "description": equipment_data["description"],
                "detail": equipment_data["detail"],
            },
        )
        print(
            f"{"Created" if created else "Updated"} equipment {equipment.name} of character {character.name}."
        )


def load_report(character, data):
    report_data = data["report"]
    report, created = Report.objects.update_or_create(
        character=character,
        defaults={
            "gender": report_data["gender"],
            "height": report_data["height"],
            "birthday": report_data["birthday"],
            "document_name": report_data["document_name"],
            "birth_world": report_data["birth_world"],
            "alias_name": report_data["alias_name"],
            "faction": report_data["faction"],
            "teleported_from": report_data["teleported_from"],
            "birthplace": report_data["birthplace"],
            "address": report_data["address"],
            "brief_report": report_data["brief_report"],
        },
    )
    print(
        f"{"Created" if created else "Updated"} report of character {character.name}."
    )


def load_seed_report(character, data):
    seed_report_data = data["seed_report"]
    seed_report, seed_report_created = Seed.objects.update_or_create(
        character=character,
        name=seed_report_data["name"],
        defaults={
            "init_compatibility": seed_report_data["init_compatibility"],
            "cell_synchronisation_rate": seed_report_data["cell_synchronisation_rate"],
            "inspection_agency": seed_report_data["inspection_agency"],
            "comment": seed_report_data["comment"],
        },
    )
    print(
        f"{"Created" if seed_report_created else "Updated"} seed report {seed_report.name} of character {character.name}."
    )

    stable_compatibility_args = {
        k: v
        for k, v in seed_report_data.items()
        if k.startswith("stable_compatibility_")
    }
    for key, value in stable_compatibility_args.items():
        if value:
            num = extract_number(key)
            stable_compatibility, stable_compatibility_created = (
                SeedStableCompatibility.objects.update_or_create(
                    seed=seed_report,
                    compatibility_number=num,
                    defaults={"detail": value},
                )
            )
            print(
                f"{"Created" if stable_compatibility_created else "Updated"} seed stable_compatibility {stable_compatibility.compatibility_number} of character {character.name}."
            )


def load_training(character, data):
    training_data = data["training"]
    for phase_name, values in training_data.items():
        phase_number = extract_number(phase_name)
        phase, phase_created = Training.objects.update_or_create(
            character=character,
            phase=phase_number,
        )
        print(
            f"{"Created" if phase_created else "Updated"} training {phase_name}  of character {character.name}."
        )

        for index, (key, value) in enumerate(values.items()):
            program, program_created = TrainingProgram.objects.update_or_create(
                training=phase,
                sort_number=index + 1,
                defaults={"name": key, "value": extract_number(value)},
            )
            print(
                f"{"Created" if program_created else "Updated"} training {program.name}  of character {character.name}."
            )


def load_trait(character, data):
    trait_data = data["trait"]
    trait, trait_created = Trait.objects.update_or_create(
        character=character,
        name=trait_data["name"],
    )
    print(
        f"{"Created" if trait_created else "Updated"} trait {trait.name} of character {character.name}."
    )
    for key, value in trait_data["description"].items():
        level = extract_number(key)
        trait_level, trait_level_created = TraitLevel.objects.update_or_create(
            trait=trait,
            level=level,
            defaults={"description": value},
        )
        print(
            f"{"Created" if trait_level_created else "Updated"} trait level {level} of character {character.name}."
        )


# load_one_character("乐无异.json")
load_all_character()
