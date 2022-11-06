import os.path
import os
import sys
import tempfile
import shutil
import re

path_to_python_3x = os.path.dirname(sys.executable)
# print(path_to_python_3x)
# print(os.getcwd())

path_to_site_packages = path_to_python_3x + "\\Lib\\site-packages"
#print(path_to_site_packages)
path_to_site_ttp = path_to_site_packages +"\\ttp"
#print(path_to_site_ttp)

_MEI_regex = "_MEI.*"
_MEI_regex_a_list = []

while True:
    path_to_temp_file = tempfile.gettempdir()
    for temp_file in os.listdir(path_to_temp_file):
        if re.search(_MEI_regex, temp_file):
            path_to_temp_mei = path_to_temp_file +f"\\{temp_file}"
            _MEI_regex_a_list.append(path_to_temp_mei)
            path_to_temp_ttp = os.path.join(path_to_temp_mei, "ttp")
            try:
                if "ttp" not in os.listdir(path_to_temp_mei):
                    shutil.copytree(path_to_site_ttp, path_to_temp_ttp)
            except Exception as e:
                #print(e) 
                pass
