import pandas as pd
import requests
import json

calibration_results = pd.read_csv('data/calibration_results')

print(calibration_results['role_id'].value_counts())

def get_role_data(role_id):
    response = requests.get(f'https://www.paraform.com/api/roles/public?role_id={role_id}')
    return response.json()

def get_candidate_data(candidate_id):
    response = requests.get(f'https://www.paraform.com/api/candidate/find_candidate?candidate_id={candidate_id}')
    return response.json()

filtered_calibration = calibration_results[calibration_results['role_id'] == 'cm4u6sfjb006jjs0cakx7ds3h']
candidate_urls = []
for _, row in filtered_calibration.iterrows():
    candidate_data = get_candidate_data(row['candidate_id'])
    candidate_urls.append("https://linkedin.com/in/" + candidate_data['linkedin_user'])

data = {
    'role_id': filtered_calibration['role_id'].values,
    'candidate_id': filtered_calibration['candidate_id'].values,
    'calibration_result': filtered_calibration['calibration_result'].values,
    'linkedin_url': candidate_urls
}

joined_df = pd.DataFrame(data)
joined_df.to_csv('data/serval_calibration_results_with_urls.csv', index=False)
