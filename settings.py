from utils.config_to_json import load_json_file_to_dict

config = load_json_file_to_dict()

URL = config["URL"]
PROCESSED_VIDEOS = config["PROCESSED_VIDEOS"]
