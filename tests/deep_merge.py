from openfisca_core.parameters import Parameter

from param_tools.deep_merge import deep_merge, merge_dict
from param_tools.p2y import to_yaml

param_1 = Parameter('rate', data = {
  'description': 'Income tax rate applied on salaries',
  'values': {
      "2014-01-01": {'value': 520, 'metadata': {'reference': 'http://taxes.gov/income_tax/2014'}},
      "2015-01-01": {'value': 550, 'metadata': {'reference': 'http://taxes.gov/income_tax/2015'}},
      "2016-01-01": {'value': 600, 'metadata': {'reference': 'http://taxes.gov/income_tax/2016'}}
      },
  })

param_2 = Parameter('rate', data = {
  'values': {
      "2015-01-01": {'value': 550},
      "2016-01-01": {'value': 600},
      "2018-01-01": {'value': 620},
      }
  })


def test_merge_dict():
  x = {1: 10}
  y = {2: 20}
  assert(merge_dict(x,y) == {1:10, 2:20})

def test_deep_merge_dict():
  x = {1: {3: 30}}
  y = {1: {4: 40}}
  assert(merge_dict(x,y) == {1:{3:30, 4:40}})

def test_merge_leafs():
  merged_param = deep_merge(param_1, param_2)
  print(to_yaml(merged_param))
  from nose.tools import set_trace; set_trace(); import ipdb; ipdb.set_trace()
