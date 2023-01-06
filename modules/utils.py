import appdirs


def get_chrome_profile_path(profile_name):
    app_name = "Chrome"
    org_name = "Google"

    return appdirs.user_data_dir(app_name, org_name, roaming=False) + rf'\User Data\{profile_name}'
