import numpy as np
import codecs, json 

a = np.arange(10).reshape(2,5)           # 2 by 5 array
b = a.tolist()                          # nested lists with same data, indices
file_path = "01_blocks_loops/array_jsonify.json"                ## your path variable

### this saves the array in .json format
json.dump(b, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) 

#  In order to "unjsonify" the array use:
obj_text = codecs.open(file_path, 'r', encoding='utf-8').read()
b_new = json.loads(obj_text)
a_new = np.array(b_new)