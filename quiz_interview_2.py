nodes = {'A': 1,
        'B': 2,
        'C': 7
       }

paths = {'A': ['B', 'C'],
        'B': ['C'],
        'C': []
        }

def find_max_path(_nodes, _paths, start_node, path=[], _vv=0):
  _v = _nodes[start_node]
  _p = _paths[start_node]

  path = path + [start_node]
  _vv = _v + _vv
  
  if len(_p) == 0:
    return [path], _vv

  ps = []
  values = []

  for _t1 in _p:
    if _t1 not in path:
      newpaths, value = find_max_path(_nodes, _paths, _t1, path, _vv)
      for newpath in newpaths:
        ps.append(newpath)
      
      values.extend(value) if isinstance(value, list) else values.append(value)
      
  return ps, values

if __name__ == '__main__':
  print("result=", find_max_path(nodes, paths, 'A'))
