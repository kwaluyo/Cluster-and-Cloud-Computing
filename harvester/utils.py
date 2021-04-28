import os
import json

def load_config():
    configs = [i for i in os.listdir("./") if 'config' in i]
    cfg = []

    if len(configs) == 0 :
        print("No config file found.")
        exit(1)

    for cf in configs:
        with open(cf, "r") as f:
            try:
                config = json.load(f)
            except:
                print('File', cf, ': Incorrect JSON format.')
                exit(1)

            if not 'TWITTER' in config:
                print('File', cf, ': Twitter account not found.')
                exit(1)

            if not 'KEYWORDS' in config:
                print('File', cf, ': Search keywords not found.')
                exit(1)

            if not 'LOCATION' in config:
                print('File', cf, ': Search location not found.')

            cfg.append(config)

    print(len(cfg), "config files found.")
    return cfg