#!/usr/bin/env python3

import argparse
import json, os, random, sys, requests
import shutil

#image_url = "https://picsum.photos/1920/1080"
image_url = "https://picsum.photos/3840/2160"

home_dir = os.path.expanduser("~")
config_dir = os.path.join(home_dir, '.config/hypaper')
json_file = os.path.join(config_dir,'data.json')
save_images_path = os.path.join(home_dir, '.cache/hypaper')

default_data = {
    "wallpapers_path": "~/Pictures/Wallpapers/",
    "actual_wallpaper": ""
}
#### setup ####

if os.path.exists(config_dir):
    if os.path.exists(json_file):
        pass
    else:
        with open(json_file, 'w') as file:
            json.dump(default_data, file, indent=4)
else:
    os.mkdir(config_dir)
    with open(json_file, 'w') as file:
        json.dump(default_data, file, indent=4)

with open(json_file, 'r') as file:
    data = json.load(file)
    path = data["wallpapers_path"]
    path = os.path.expanduser(path)
    if not os.path.exists(path) or not os.path.isdir(path):
        try:
            print("Your wallpaper folder do not existing, creating this folder ...")
            os.mkdir(path)
        except:
            print("There was error od creating dir in your wallpaper directory, change your directory and make sure that util has pesmission to this path.")

#~/Pictures/Wallpapers/

##### comands #####
def set_wallpaper_path(args):
    with open(json_file, 'r') as file:
        data = json.load(file)
    if args.path[-1] != "/":
        args.path = args.path + "/"
    data["wallpapers_path"] = args.path
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Setting wallpaper path to: {args.path}")

def get_wallpaper_path(args):
    with open(json_file, 'r') as file:
        data = json.load(file)
        #data = json.loads(data)
    print(f'Getting current wallpaper path: {data['wallpapers_path']}')

def list_wallpapers(args):
    with open(json_file, 'r') as file:
        data = json.load(file)
        active_wallpaper = data["actual_wallpaper"]
        path = data["wallpapers_path"]
    path = os.path.expanduser(path)
    if os.path.exists(path):
        if os.path.isdir(path):
            wallpapers = ""
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            for file in files:
                wallpapers = wallpapers + file + " "
            print(wallpapers)
        else:
            print("That path is not a dir")
    else:
        print("That folder do not exist. Set valid wallpapers folder with set_path")

def set_random_local(args):
    if args.source == "online":
        os.makedirs(save_images_path, exist_ok=True)
        online_file_path = os.path.join(save_images_path, "online_image.jpg")
        response = requests.get(image_url)

        if response.status_code == 200:
            with open(online_file_path, 'wb') as f:
                f.write(response.content)
                f.close()

            stream = os.popen(f'swww img {online_file_path}')
            output = stream.read()

            with open(json_file, 'r') as file:
                data = json.load(file)
                file.close()
            data["actual_wallpaper"] = ""
            with open(json_file, 'w') as file:
                json.dump(data, file, indent=4)
                file.close()
        else:
            print("Failed to download the image")
    elif args.source == "local":
        with open(json_file, 'r') as file:
            data = json.load(file)
            active_wallpaper = data["actual_wallpaper"]
            path = data["wallpapers_path"]
        path = os.path.expanduser(path)
        print(path)
        if os.path.exists(path):
            if os.path.isdir(path):
                files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
                if active_wallpaper in files:
                    files.remove(active_wallpaper)
                wallpaper = random.choice(files)
                stream = os.popen(f'swww img {path + wallpaper}')
                output = stream.read()
                print(output)
                print("done")
                with open(json_file, 'r') as file:
                    data = json.load(file)
                data["actual_wallpaper"] = wallpaper
                with open(json_file, 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                print("That path is not a dir")
        else:
            print("That folder do not exist. Set valid wallpapers folder with set_path")
    else:
        print("invalid option chosen")

def next_wallpaper(args):
        with open(json_file, 'r') as file:
            data = json.load(file)
            active_wallpaper = data["actual_wallpaper"]
            path = data["wallpapers_path"]
        path = os.path.expanduser(path)
        if os.path.exists(path):
            if os.path.isdir(path):
                files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
                #print("Files using os module:", files)
                if active_wallpaper == "":
                    wallpaper_index = 0
                else:
                    wallpaper_index = files.index(active_wallpaper) + 1
                    if wallpaper_index > len(files)-1:
                        wallpaper_index = 0
                wallpaper = files[wallpaper_index]
                stream = os.popen(f'swww img {path + wallpaper}')
                output = stream.read()
                print(output)
                print("done")
                with open(json_file, 'r') as file:
                    data = json.load(file)
                data["actual_wallpaper"] = wallpaper
                with open(json_file, 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                print("That path is not a dir")
        else:
            print("That folder do not exist. Set valid wallpapers folder with set_path")

def save_online_photo(args):
    with open(json_file, 'r') as file:
        data = json.load(file)
        path = data["wallpapers_path"]
    path = os.path.expanduser(path)
    if os.path.exists(path):
        if os.path.isdir(path):
            dst = os.path.join(path + "online_photo_1.jpg")
            base_filename = "online_photo"
            extension = ".jpg"
            index = 1
            while True:
                filename = f"{base_filename}_{index}{extension}"
                dst = os.path.join(path, filename)
                if not os.path.exists(dst):
                    break
                index += 1
            source_dir = os.path.join(home_dir, ".cache/hypaper/online_image.jpg")
            if os.path.exists(source_dir):
                shutil.copy(source_dir, dst)
            else:
                print("There is no wallpaper to save.")
        else:
            print("That path is not a dir")
    else:
        print("That folder do not exist. Set valid wallpapers folder with set_path")

def main():

    parser = argparse.ArgumentParser(prog="hypaper", description="Simple hyprland wallpapers util (hypaper)")
    subparsers = parser.add_subparsers(dest="command",  help="")

    set_patch_command = subparsers.add_parser('set_path', help='Set the wallpaper path.')
    set_patch_command.add_argument('path', type=str, help='Path to the wallpaper.')
    set_patch_command.set_defaults(func=set_wallpaper_path)

    get_path_command = subparsers.add_parser('get_path', help='Get the current wallpaper path.')
    get_path_command.set_defaults(func=get_wallpaper_path)

    list_command = subparsers.add_parser('list', help='List all local wallpapers.')
    list_command.set_defaults(func=list_wallpapers)

    next_command = subparsers.add_parser('next_wallpaper', help='Change current wallpaper to next in wallpapers dir')
    next_command.set_defaults(func=next_wallpaper)

    save_command = subparsers.add_parser('save', help='Save current online wallpaper to your wallpapers folder')
    save_command.set_defaults(func=save_online_photo)

    random_local_command = subparsers.add_parser('set_random', help='Set random wallpaper from your wallpapers folder (local) or internet (online)')
    random_local_command.add_argument('source', choices=['online', 'local'], default="local", nargs="?",
                                      help='Source of the random wallpaper (online or local)')
    random_local_command.set_defaults(func=set_random_local)

    args = parser.parse_args()
    if 'func' in args:
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()