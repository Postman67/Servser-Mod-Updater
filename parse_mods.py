import os

def parse_mods(mods_dir):
    local_mods = [f for f in os.listdir(mods_dir) if f.endswith(".jar")]
    
    print("Local Mods:")
    for mod in local_mods:
        print(mod)
    return local_mods

def compare_mods(local_mods, modpack_mods):
    print("Comparing mods...")

    mod_name = os.path.basename(local_mods)
    if mod_name in modpack_mods:
        print(f"{mod_name} is up to date.")
    else:
        print(f"{mod_name} is missing or outdated.")