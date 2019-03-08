# -*- coding: utf-8 -*-

import re

import oyaml as yaml

from openfisca_core.parameters import Parameter, ParameterNode, ParameterAtInstant


def serialize_param_at_instant(param_at_instant):
  result = {'value': param_at_instant.value}
  if param_at_instant.metadata:
    result['metadata'] = param_at_instant.metadata
  return result

def serialize_parameter(param):
  serialized = {
  'description': param.description,
  'values': {
    pai.instant_str: serialize_param_at_instant(pai)
    for pai in param.values_list
    }
  }

  if (param.metadata):
    serialized['metadata'] = param.metadata

  if (param.documentation):
    serialized['documentation'] = param.documentation

  return serialized

def serialize_parameter_node(node):
  result = {'description': node.description}
  for child_name, child in node.children.items():
    if isinstance(child, ParameterNode):
      result[child_name] = serialize_parameter_node(child)
    elif isinstance(child, Parameter):
      result[child_name] = serialize_parameter(child)

  if (node.metadata):
    result['metadata'] = node.metadata

  if (node.documentation):
    result['documentation'] = node.documentation

  return result

def Parameter_representer(dumper, param):
  return dumper.represent_dict(serialize_parameter(param).items())

def ParameterNode_representer(dumper, node):
  return dumper.represent_dict(serialize_parameter_node(node).items())

def represent_str(dumper, data):
  if data.count('\n') >= 1:  # check for multiline string
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style = '|')
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(Parameter, Parameter_representer)
yaml.add_representer(ParameterNode, ParameterNode_representer)
yaml.add_representer(str, represent_str)

def to_yaml(param):
  result = yaml.dump(param, default_flow_style = False, allow_unicode = True)
  result = re.sub(
    r"'(\d{4}-\d{2}-\d{2})'",
    r"\1",
    result
    )

  return result
