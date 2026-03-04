from data_utils import genSpoof_list, ADD_Dataset, eval_to_score_file
import json

print('====== Evaluation ======')
dir_path = '/home/han/projects/EnvSDD-main/eval_output/track_2_label.json'
eval_output = '/home/han/projects/EnvSDD-main/eval_output/track_2_b02.txt'
# target_generators = ['audiolcm', 'tangoflux', 'audioldm2'] 
target_generators = ['foleycrafter', 'diff_foley']

print('test data path: ', dir_path)
with open(dir_path, 'r') as f:
        data = json.load(f)
print('no. of test trials',len(data))
eer = eval_to_score_file(eval_output, dir_path)

for target_generator in target_generators:
    print(f'Filter data with target audio generator: {target_generator}')
    filtered_data = []
    for item in data:
        if item['generative_model'] == target_generator or item['generative_model'] == 'none':
            filtered_data.append(item)

    output_path = dir_path.replace('.json', f'_{target_generator}.json')
    print('no. of test trials',len(filtered_data))
    with open(output_path, 'w') as f:
        json.dump(filtered_data, f, indent=4)
    
    eer = eval_to_score_file(eval_output, output_path)