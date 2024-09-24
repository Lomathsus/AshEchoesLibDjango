RARITY_CHOICES = [(4, "R"), (5, "SR"), (6, "SSR")]

PROFESSION_CHOICES = [
    ("bulwark", "铁御"),
    ("vanguard", "轻卫"),
    ("striker", "尖锋"),
    ("ranger", "筑术师"),
    ("support", "护佑者"),
    ("tactician", "战术家"),
    ("skirmisher", "游徒"),
]

PROFESSION_CATEGORY_CHOICES = [
    ("square", "方块"),
    ("triangle", "三角"),
    ("diamond", "菱形"),
]

STAT_CHOICES = [
    ("vitality", "体质"),
    ("defence", "防御"),
    ("attack", "攻击"),
    ("mastery", "专精"),
    ("terminal", "终端"),
]

ELEMENT_CHOICES = [
    ("fire", "炎"),
    ("water", "水"),
    ("lighting", "雷"),
    ("ice", "霜"),
    ("wind", "风"),
    ("corrosion", "蚀"),
    ("physical", "物理"),
]

ENEMY_CHOICES = [
    ("common", "一般单位"),
    ("elite", "精英单位"),
    ("boss", "首领单位"),
    ("ground", "地面单位"),
    ("air", "空中单位"),
    ("native", "原生单位"),
    ("alien", "异种单位"),
    ("humanoid", "人形单位"),
    ("mechanical", "机械单位"),
    ("shield", "屏障保护"),
]


TRAINING_CHOICES = STAT_CHOICES + [
    ("attack_speed", "攻击速度"),
    ("healing", "治愈力"),
    ("block", "格挡强度"),
    ("basic_damage_reduction", "减伤"),
]

SKILL_TYPE = [("awaking", "唤醒"), ("nexus", "漫巡")]
