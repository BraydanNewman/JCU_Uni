HEX_NAME_VALUES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc",
    "antiquewhite3": "#cdc0b0",
    "antiquewhite4": "#8b8378",
    "aquamarine1": "#7fffd4",
    "aquamarine2": "#76eec6",
    "aquamarine4": "#458b74",
    "azure1": "#f0ffff",
    "azure2": "#e0eeee"
}

colour_name = input("Name: ").lower()
while colour_name != "":
    if colour_name in HEX_NAME_VALUES:
        print(HEX_NAME_VALUES[colour_name])
    else:
        print("Name does not exist")
    colour_name = input("Name: ").upper()
