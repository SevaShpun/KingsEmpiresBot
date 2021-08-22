age_lvl = {
    "Каменный": 1,
    "Бронзовый": 2,
    "Средневековый": 3,
    "Инудстриальный": 4,
    "Информационный": 5,
    "Эра Марса": 6,
    "Эра Млечного Пути": 7

}

age_next = {
    "Каменный": "Бронзовый",
    "Бронзовый": "Средневековый",
    "Средневековый": "Индустриальный",
    "Индустриальный": 4,
    "Информационный": 5,
    "Эра Марса": 6,
    "Эра Млечного Пути": 7
}

age_buildings = {
    "Каменный": {
        "food": "🐑 Загон",
        "stock": "🏺 Гончарня",
        "energy": None,
        "graviton": None,
    },
    "Бронзовый": {
        "food": "🍷 Винодельня",
        "stock": "🪓 Лесопилка",
        "energy": None,
        "graviton": None,
    },
    "Средневековый": {
        "food": "👨‍🌾 Ферма",
        "stock": "⛏ Шахта",
        "energy": None,
        "graviton": None,
    },
    "Инудстриальный": {
        "food": "🛒 Магазин",
        "stock": "⚒ Мастерская",
        "energy": "🏭 Фабрика",
        "graviton": None,
    },
    "Информационный": {
        "food": "🛍 Гипермаркет",
        "stock": "🏢 Завод",
        "energy": "🔋 Электростанция",
        "graviton": None,
    },
    "Эра Марса": {
        "food": "🥕 Пищевой Принтер",
        "stock": "🖨 Сырьевой Принтер",
        "energy": "⚛ АЭС",
        "graviton": "🧬 Генератор Гравитона",
    },
    "Эра Млечного Пути": 7
}

age_resource_buff = {
    "Каменный": {
        "food": 200,
        "stock": 100,
        "energy": None,
        "graviton": None,
    },
    "Бронзовый": {
        "food": 400,
        "stock": 200,
        "energy": None,
        "graviton": None,
    },
    "Средневековый": {
        "food": 600,
        "stock": 300,
        "energy": None,
        "graviton": None,
    },
    "Инудстриальный": {
        "food": 1000,
        "stock": 500,
        "energy": None,
        "graviton": None,
    },
    "Информационный": {
        "food": 1500,
        "stock": 750,
        "energy": 200,
        "graviton": None,
    },
    "Эра Марса": {
        "food": 200,
        "stock": 2000,
        "energy": 500,
        "graviton": None,
    },
    "Эра Млечного Пути": 3000

}

age_stock_buff = {
    "Каменный": 100,
    "Бронзовый": 200,
    "Средневековый": 300,
    "Инудстриальный": 500,
    "Информационный": 750,
    "Эра Марса": 1000,
    "Эра Млечного Пути": 1500

}

resource_emoji = {
    "food": "🍇",
    "stock": "🌲",
    "energy": "⚡",
    "graviton": "🧬",
}

names_all_territories = [
    "Demondome", "Hellion", "Nero Coliseum",
    "Riddle Terrain", "The Scarlet Moon",
    "Nimbus Yonder", "The Foaming Lair", "Mellow Forest"
]

age_units = {
    "Каменный": {
        "unit_1": "🗡 Копейщик",
        "unit_2": "🏹 Лучник",
    },
    "Бронзовый": {
        "unit_1": "🛡 Легионер",
        "unit_2": "🐴 Всадник",
    },

}

units_create_timer = {
    "Каменный": {
        "unit_1": 70,
        "unit_2": 70,
    },
    "Бронзовый": {
        "unit_1": 80,
        "unit_2": 80,
    },

}

unit_weight_dict = {
    "Каменный": {
        "unit_1": 1.2,
        "unit_2": 1.8,
    },
    "Бронзовый": {
        "unit_1": 3.2,
        "unit_2": 5.5,
    },

}

unit_create_price = {
    "Каменный": {
        "unit_1": {
            "food": 25,
            "stock": 0,
            "energy": 0,
        },
        "unit_2": {
            "food": 20,
            "stock": 10,
            "energy": 0,
        },
    },
    "Бронзовый": {
        "unit_1": {
            "food": 65,
            "stock": 20,
            "energy": 0,
        },
        "unit_2": {
            "food": 80,
            "stock": 10,
            "energy": 0,
        },
    },

}

unit_upgrade_price = {
    "Каменный": {
        "unit_1": {
            "food": 2000,
            "stock": 1000,
            "energy": 0,
        },
        "unit_2": {
            "food": 20,
            "stock": 10,
            "energy": 0,
        },
    },
    "Бронзовый": {
        "unit_1": {
            "food": 2000,
            "stock": 0,
            "energy": 0,
        },
        "unit_2": {
            "food": 2000,
            "stock": 10,
            "energy": 0,
        },
    },

}


next_age_price = {
    "Каменный": {
        "food": 5000,
        "stock": 2500,
        "energy": 0
    },
    "Бронзовый": {
        "food": 10000,
        "stock": 5000,
        "energy": 0
    }
}

next_age_changes = {
    "Каменный": {
        "buildings": {
            "food": "🍷 Винодельня",
            "stock": "🪓 Лесопилка"
        },
        "units": {
            "unit_1": "🛡 Легионер",
            "unit_2": "🐴 Всадник"
        }
    }

}