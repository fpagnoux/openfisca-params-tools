# -*- coding: utf-8 -*-

from openfisca_core.parameters import Parameter, ParameterAtInstant


def merge_object(obj1, obj2, path = ''):
  if obj2 is None:
    return obj1
  if obj1 is None:
    return obj2

  if isinstance(obj1, dict) and isinstance(obj2, dict):
    return merge_dict(obj1, obj2, path)
  if isinstance(obj1, ParameterAtInstant) and isinstance(obj2, ParameterAtInstant):
    return merge_parameter_at_instant(obj1, obj2, path)

  if obj1 != obj2:
    raise ValueError(f"The 2 params conflict in property {path}. Fix the conflict before merging.")

  return obj1


def merge_dict(d1, d2, path = ''):
  new_dict = {}
  all_keys = list(dict.fromkeys(list(d1.keys()) + list(d2.keys())))
  for key in all_keys:
    new_dict[key] = merge_object(d1.get(key), d2.get(key), f'{path}/{key}')
  return new_dict


def merge_parameter_at_instant(p1, p2, path = ''):
  new_p = ParameterAtInstant('', p1.instant_str)
  new_p.metadata = merge_object(p1.metadata, p2.metadata, f'{path}/metadata')
  new_p.value = merge_object(p1.value, p2.value, f'{path}/value')
  return new_p


def merge_values_list(param_1, param_2):
  value_by_period_1 = {
    param_at_instant.instant_str: param_at_instant
    for param_at_instant in param_1.values_list
  }
  value_by_period_2 = {
    param_at_instant.instant_str: param_at_instant
    for param_at_instant in param_2.values_list
  }
  all_periods = set().union(value_by_period_1.keys(), value_by_period_2.keys())
  all_periods = sorted(list(all_periods), reverse = True)

  result = [
    merge_object(value_by_period_1.get(period), value_by_period_2.get(period), period)
    for period in all_periods
    ]
  return result


def merge_parameters(param_1, param_2):
  new_param = Parameter(param_1.name, {})
  new_param.description = merge_object(param_1.description, param_2.description, 'description')
  new_param.documentation = merge_object(param_1.documentation, param_2.documentation, 'documentation')
  new_param.values_list = merge_values_list(param_1, param_2)
  new_param.metadata = merge_object(param_1.metadata, param_2.metadata, 'metadata')

  return new_param
