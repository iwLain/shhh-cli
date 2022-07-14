import configparser

config_file = configparser.ConfigParser()

config_file.add_section("Settings")
config_file.set("Settings", "instanceUrl", "https://instance.tld/api")
config_file.set("Settings", "expire", "30m")
config_file.set("Settings", "tries", "3")
config_file.set("Settings", "hibp", "true")


with open(r"configuration.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

read_file = open("configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()