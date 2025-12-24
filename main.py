import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

checkdata = config['paths']['audio']['hit_sound_path']
sprites = config['paths']['explosion_sprites']

for sprite in sprites:
    print(sprite)

    
    