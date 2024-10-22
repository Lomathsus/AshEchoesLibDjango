import os
import django


# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AshEchoesLibDjango.settings")

# 初始化 Django
django.setup()


import json
from apps.skill.models import EngravingSkill

directory = "/Users/teorema_mac/Documents/Work/Develop/Personal/Python/AshEchoesScraper/data/skills"  # 指定JSON文件目录


def load_all_skills():
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            load_one_skill(filename)


def load_one_skill(filename):
    file_path = os.path.join(directory, filename)
    with open(file_path, "r") as file:
        print(f"{filename} loading...")
        data = json.load(file)
        load_engraving_skill(data)
    print(f"{filename} loaded!")


def load_engraving_skill(data):
    rarity_dict = {
        "r": 4,
        "sr": 5,
        "ssr": 6,
    }
    rarity = data["rarity"].lower()
    if rarity == "ssr":
        if "激励" in data["skill_tags"]:
            skill_type = "inspire"
        else:
            skill_type = "core"
    else:
        skill_type = "regular"

    skill, created = EngravingSkill.objects.update_or_create(
        name=data["name"],
        defaults={
            "rarity": rarity_dict[rarity],
            "professions": data["professions"],
            "type": skill_type,
            "profession_types": data["profession_types"],
            "tags": data["skill_tags"],
            "description": data["skill_description"],
            "icon": data["skill_icon"],
            "source": data["source"],
            "point_requirement": data["point_requirement"],
            "elements": data["elements"],
            "skill_stats": data["skill_stats"],
            "enemy_types": data["enemy_types"],
            "activation_modes": data["activation_modes"],
            "damage_increases": data["damage_increases"],
            "damage_reduction": data["damage_reduction"],
            "target_debuffs": data["target_debuffs"],
            "stats_increases": data["stats_increases"],
            "special_mechanism": data["special_mechanism"],
        },
    )
    print(f"{'Created' if created else 'Updated'} EngravingSkill - {skill.name}")


# load_one_skill("一线生机.json")
load_all_skills()
