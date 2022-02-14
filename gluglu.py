!pip install chembl_webresource_client
!pip install 

import pandas as pd
from chembl_webresource_client.new_client import new_client
import matplotlib.pyplot as plt
import numpy as np

target = new_client.target
activity = new_client.activity
herg = target.filter(pref_name__iexact='hERG').only('target_chembl_id')[0]
herg_ic50 = activity.filter(target_chembl_id=herg['target_chembl_id']).filter(standard_type="IC50")
herg_inhibition = activity.filter(target_chembl_id=herg['target_chembl_id']).filter(standard_type="Inhibition")
herg_ki = activity.filter(target_chembl_id=herg['target_chembl_id']).filter(standard_type="Ki")
herg_ec50 = activity.filter(target_chembl_id=herg['target_chembl_id']).filter(standard_type="EC50")

keys = ['molecule_chembl_id', 'canonical_smiles', 
        'standard_type', 'standard_units', 'standard_relation', 
        'standard_value', 'assay_description']
        

fulllist = []
for item in range (len(herg_ic50)+1):
  a = [herg_ic50[item].get(key) for key in keys]
  fulllist.append(a)
  
pd.DataFrame(fulllist)
