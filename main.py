import my_secrets 
from cursepy import CurseClient
from cursepy import MinecraftWrapper
from cursepy.classes.search import SearchParam
from cursepy.classes.base import CurseAddon
import parse_mods
import json

# Initialize CurseClient
client = CurseClient(my_secrets.C_API_KEY)
# game = client.game(my_secrets.GAME_ID)
# modpack = client.(my_secrets.MODPACK_ID)

search_param = SearchParam(searchFilter="Ornon")

mclient = MinecraftWrapper(my_secrets.C_API_KEY)
modpack: CurseAddon
modpack = mclient.search_modpacks(search_param)


# def callback(data):
#     print(data)
# client.bind_callback(callback)

# ======================== #

# Compare curseforge mods with local mods
# local_mods = parse_mods.parse_mods("PATH_TO_MODS_DIR")
# parse_mods.compare_mods(local_mods, modpack.mods)

# Update local mods

# Output
modpack = modpack[0]
print(type(modpack))

for attr, value in vars(modpack).items():
    print(f"{attr}: {value}\n")

# print(json.dumps(modpack.mods, indent=4))
