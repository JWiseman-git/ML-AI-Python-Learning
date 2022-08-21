import requests
import pandas as pd
import numpy as np
import json

fpl_url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(fpl_url)
hits = r.json()
print(hits.keys())
print(type(hits))
#json_list = json.loads(hits) # --> Json into Dict
# print(type(json_list))
# elements_df = pd.DataFrame(json['elements'])
# print(json_list)

# #json_formatted_str = json.dumps(json_list, indent=2)
# #print(json_formatted_str)


# #print(hits.keys())

# print(len(json_list))

# for rows in json_list:
#     print(rows)
