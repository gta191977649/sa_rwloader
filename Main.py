import os
from DFF import *
lua = ""
def readDFF(filename,file):
    global lua
    lua += "\t[\"{}\"] = {{\n".format(file.lower())

    DFF = dff()
    DFF.load_file(filename)
    for g in DFF.geometry_list:
        print("n of materials {}".format(len(g.materials)))
        for i,m in enumerate(g.materials):
            for txd in m.textures:
                #print("{}:{}".format(i,txd.name))
                lua += "\t\t{{ index={}, name=\"{}\" }},\n".format(i,txd.name.lower())
    lua += "\t},\n"


if __name__ == '__main__':
    dffPath = "D:/dev/sa_gta3.img"
    # Generate Lua Var Head
    lua += "SAMP_IMG = {\n"
    for root, dirs, files in os.walk(dffPath):
        for name in files:
            if name.endswith((".dff")):
                filename = "{}/{}".format(root, name)
                print(filename)
                readDFF(filename,name)
                print(lua)
    lua += "}\n"

    f = open("SA_MAT.lua", "a")
    f.write(lua)
    f.close()
    print("File Write.")