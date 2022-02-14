#!pip install chembl_webresource_client
#!pip install 

import pandas as pd
from chembl_webresource_client.new_client import new_client
#import matplotlib.pyplot as plt
#import numpy as np

def main():
  keys = ['molecule_chembl_id', 'canonical_smiles', 
          'standard_type', 'standard_units', 'standard_relation', 
          'standard_value', 'assay_description']
  
  def get_chembl_targs(endpoint="hERG",act="IC50"):
    """inhibition,ki,ec50"""
    activity = new_client.activity
    
    herg = new_client.target.filter(pref_name__iexact=endpoint).only('target_chembl_id')[0]
    
    herg_act = activity.filter(target_chembl_id=herg['target_chembl_id']).filter(standard_type=act)
    return herg_act

  def dct_sorter(dct_list,keys_to_look_for=keys): 
      """Maps entry function"""
      a={}
      #print(dct_list)
      for key in keys_to_look_for:
        a[key]=dct_list[key]
      return a

  full=list(map(dct_sorter,get_chembl_targs("hERG","IC50")))
  
  print(full)
  
  df=pd.DataFrame(full)
  
  df.to_csv("test.csv")

if __name__ == '__main__':
  main()