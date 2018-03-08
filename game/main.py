import imp
import importlib


classname='bjkuai3'




fp, pathname, description = imp.find_module("work",[classname])
print('fp : '+str(fp))
print('pathname : '+str(pathname))
print('description : '+str(description))
try:
    m = imp.load_module("bjkuai3_work", fp, pathname, description)
    m.handler(74086)   # 这样就可以直接执行了，详细信息看官方文档。
finally:
    if fp:
        fp.close()
