from functools import reduce

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def get_from_id(parameter_tree, id_param):
  relative_id = remove_prefix(id_param, parameter_tree.name).strip('.')
  try:
    return reduce(lambda tree, name: tree.children[name], relative_id.split('.'), parameter_tree)
  except KeyError:
    import ipdb; ipdb.set_trace()
