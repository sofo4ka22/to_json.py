import json
from tovar import nounlist2
from price import nounlist2

def converToJSON():
    with open("D:\Student\ICS_18.09.2020\I_C_S-18.09.2020\price_json.json",'w') as write_file:
        json.dump(nounlist1, write_file)
def converToJSON():
    with open("D:\Student\ICS_18.09.2020\I_C_S-18.09.2020\tovar_json.json",'w') as write_file:
        json.dump(nounlist2, write_file)
