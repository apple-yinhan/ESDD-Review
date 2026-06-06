from data_utils import genSpoof_list, ADD_Dataset, eval_to_score_file
import json

print('====== Evaluation ======')
dir_path = './data/track_2_label.json'
eval_output = './data/track_2_b02.txt'

print('test data path: ', dir_path)
with open(dir_path, 'r') as f:
        data = json.load(f)
print('no. of test trials',len(data))
eer = eval_to_score_file(eval_output, dir_path)