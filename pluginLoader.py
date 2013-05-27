import imp
import os

'''
Credits for pluginsystem
http://lkubuntu.wordpress.com/2012/10/02/writing-a-python-plugin-api/
'''

PluginDir="/plugins"
MainModule = "__init__"
MainPath=os.path.dirname(os.path.realpath(__file__))
PluginPath=MainPath+PluginDir

def getPlugins():
    plugins = []
    possibleplugins = os.listdir(PluginPath)
    for i in possibleplugins:
        location = os.path.join(PluginPath, i)
        if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
            continue
        info = imp.find_module(MainModule, [location])
        plugins.append({"name": i, "info": info})
    return plugins
    
def loadPlugin(plugin):
    return imp.load_module(MainModule, *plugin["info"])
