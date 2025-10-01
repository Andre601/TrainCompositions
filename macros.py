import posixpath
import json

def define_env(env):
    @env.macro
    def load_json(file_path: str):
        path = posixpath.sep.join([env.project_dir, file_path])
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    @env.macro
    def set_title(character: str):
        match character:
            case 'l':
                return 'Locomotive'
            case '1':
                return '1st Class'
            case '2':
                return '2nd Class'
            case '1/2':
                return '1st and 2nd class'
            case 'r':
                return 'Restaurant'
            case _:
                return 'Unknown'