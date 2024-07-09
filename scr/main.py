#!/usr/bin/env python3

import argparse
import json, os, random

home_dir = os.path.expanduser("~")
json_file = os.path.join(home_dir, '.config/hypaper/data.json')
#~/Pictures/Wallpapers/

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
        print("This function is not available right now")
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
                if active_wallpaper != "":
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
        print(path)
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

    random_local_command = subparsers.add_parser('set_random', help='Set random wallpaper from your wallpapers folder (local) or internet (online)')
    random_local_command.add_argument('source', choices=['online', 'local'],
                                      help='Source of the random wallpaper (online or local)')
    random_local_command.set_defaults(func=set_random_local)

    args = parser.parse_args()
    if 'func' in args:
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()