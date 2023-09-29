"""
This module converts yaml to jsons
"""


import yaml
import json
import os


def yaml_to_json(read_folder_yaml: str):
    """
    Iterate through all files of a specific folder and transfers the yaml files into
    jsons.
    For that, a json folder will be created in each folder that contains a yaml file
    and the converted jsons will be dumped there under the same name as
    the yaml but with a .json extension

    :param read_folder_yaml: String, Input folder through which will be iterated.
    Absolute path will be extracted in the function

    :return: None, the files will be created
    """

    # get absolute path for directory
    input_dir = os.path.abspath(read_folder_yaml)

    for subdir, dirs, files in os.walk(input_dir):
        for file in files:

            if file.endswith("yaml"):
                # create a json folder in the  respective folder if it does not exist yet
                json_dir = os.path.join(subdir, "json")

                if not os.path.exists(json_dir):
                    os.makedirs(json_dir)
                path_yaml = os.path.join(subdir, file)

                # get name of file but with json extension
                json_file_name = os.path.splitext(file)[0] + ".json"
                path_json = os.path.join(json_dir, json_file_name)

                with open(path_yaml, 'r') as yaml_in, open(path_json, "w") as json_out:
                    yaml_object = yaml.safe_load(yaml_in)  # yaml_object will be a list or a dict
                    json.dump(yaml_object, json_out, indent=2)


# Read all files
# Comment in if you want to execute this

# input_folder = "."
# yaml_to_json(input_folder)