import pandas as pd
from statsmodels.formula.api import MNLogit, Logit
import argparse

parser = argparse.ArgumentParser(description='pie analysis')
parser.add_argument('--data', '-d', help='Data file path')
args = parser.parse_args()

hie = pd.read_csv(args.data, na_values='nd')
outcome_labels = {'0': 'healthy', '1': 'moderate', '2e': 'severe', '3': 'death'}
hie['outcome'] = hie['outcome'].map(outcome_labels, na_action='ignore')
binarized_labels = {'healthy': 1, 'moderate': 1, 'severe': 0, 'death': 0}
hie['positive_outcome'] = hie['outcome'].map(binarized_labels, na_action='ignore')
print(hie.info())

hie_imp = hie.copy()
hie_imp_median = hie_imp.fillna(hie_imp.median())
hie_imp_mode = hie_imp.fillna(hie_imp.mode())
hie_imp_mean = hie_imp.fillna(hie_imp.mean())

hie['copeptin_6h_pmol_l_zscored'] = (hie['copeptin_6h_pmol_l'] - hie['copeptin_6h_pmol_l'].mean()) / hie[
    'copeptin_6h_pmol_l'].std()
hie['copeptin_12h_pmol_l_zscored'] = (hie['copeptin_12h_pmol_l'] - hie['copeptin_12h_pmol_l'].mean()) / hie[
    'copeptin_12h_pmol_l'].std()
hie['copeptin_24h_pmol_l_zscored'] = (hie['copeptin_24h_pmol_l'] - hie['copeptin_24h_pmol_l'].mean()) / hie[
    'copeptin_24h_pmol_l'].std()
hie['copeptin_48h_pmol_l_zscored'] = (hie['copeptin_48h_pmol_l'] - hie['copeptin_48h_pmol_l'].mean()) / hie[
    'copeptin_48h_pmol_l'].std()
hie['copeptin_72h_pmol_l_zscored'] = (hie['copeptin_72h_pmol_l'] - hie['copeptin_72h_pmol_l'].mean()) / hie[
    'copeptin_72h_pmol_l'].std()
hie['copeptin_168h_pmol_l_zscored'] = (hie['copeptin_168h_pmol_l'] - hie['copeptin_168h_pmol_l'].mean()) / hie[
    'copeptin_168h_pmol_l'].std()
hie['copeptin_avg'] = (hie['copeptin_6h_pmol_l_zscored'] + hie['copeptin_12h_pmol_l_zscored'] + hie[
    'copeptin_24h_pmol_l_zscored']) / 3

hie['NSE_6h_ng_ml_zscored'] = (hie['NSE_6h_ng_ml'] - hie['NSE_6h_ng_ml'].mean()) / hie['NSE_6h_ng_ml'].std()
hie['NSE_12h_ng_ml_zscored'] = (hie['NSE_12h_ng_ml'] - hie['NSE_12h_ng_ml'].mean()) / hie['NSE_12h_ng_ml'].std()
hie['NSE_24h_ng_ml_zscored'] = (hie['NSE_24h_ng_ml'] - hie['NSE_24h_ng_ml'].mean()) / hie['NSE_24h_ng_ml'].std()
hie['NSE_48h_ng_ml_zscored'] = (hie['NSE_48h_ng_ml'] - hie['NSE_48h_ng_ml'].mean()) / hie['NSE_48h_ng_ml'].std()
hie['NSE_72h_ng_ml_zscored'] = (hie['NSE_72h_ng_ml'] - hie['NSE_72h_ng_ml'].mean()) / hie['NSE_72h_ng_ml'].std()
hie['NSE_168h_ng_ml_zscored'] = (hie['NSE_168h_ng_ml'] - hie['NSE_168h_ng_ml'].mean()) / hie['NSE_168h_ng_ml'].std()
hie['NSE_avg'] = (hie['NSE_6h_ng_ml_zscored'] + hie['NSE_12h_ng_ml_zscored'] + hie['NSE_24h_ng_ml_zscored']) / 3

# model1 = MNLogit.from_formula('outcome ~ copeptin_6h_pmol_l + NSE_6h_ng_ml', hie, missing='drop').fit()
# print(model1.summary())

model2 = Logit.from_formula('positive_outcome ~ copeptin_6h_pmol_l + NSE_6h_ng_ml', hie, missing='drop').fit()
print(model2.summary())
# model2_1 = Logit.from_formula('positive_outcome ~ copeptin_6h_pmol_l + NSE_6h_ng_ml', hie_imp_median, missing='drop').fit()
# print(model2_1.summary())
# model2_2 = Logit.from_formula('positive_outcome ~ copeptin_6h_pmol_l + NSE_6h_ng_ml', hie_imp_mode, missing='drop').fit()
# print(model2_2.summary())
model2_3 = Logit.from_formula('positive_outcome ~ copeptin_avg + NSE_avg', hie, missing='drop').fit()
print(model2_3.summary())

model3 = Logit.from_formula('positive_outcome ~ copeptin_12h_pmol_l + NSE_12h_ng_ml', hie, missing='drop').fit()
print(model3.summary())
model3_1 = Logit.from_formula('positive_outcome ~ copeptin_12h_pmol_l + NSE_12h_ng_ml', hie_imp_median,
                              missing='drop').fit()
print(model3_1.summary())

# model4 = Logit.from_formula('positive_outcome ~ copeptin_24h_pmol_l + NSE_24h_ng_ml', hie, missing='drop').fit()
# print(model4.summary())

