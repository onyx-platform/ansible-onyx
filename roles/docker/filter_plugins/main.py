def natural_index_of (coll, x):
  ''' Returns the index of x in coll, plus 1.
      This is useful for ZooKeeper or Kafka style host IDs.
  '''
  return coll.index(x) + 1

class FilterModule(object):
    ''' Ansible Jinja2 filters '''

    def filters(self):
      return {
        'natural_index_of': natural_index_of,
      }
