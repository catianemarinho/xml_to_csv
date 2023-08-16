import os
from conversion import get_datas, create_table

values = []

if __name__ == "__main__":
    for xml in os.listdir("xml"):
        get_datas(xml, values)
    
    create_table(values)
