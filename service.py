from data import configs

#GET configs by name
def get_configs(name):
  return [config for config in configs if config['name'] == name]

#GET all the configs
def get_all_configs():
  return configs

#POST a config
def add_config(name, monitored, limits):
  config = {
    'name': name,
    'metadata': {
      'monitoring': {
        'enabled': monitored
      },
      'limits': {
        'cpu': {
          'enabled': limits
        }
      }
    }
  }
  configs.append(config)
  return config

#DELETE a specific config
def remove_config(name):
  deleted_config = [config for config in configs if config['name'] == name]
  if len(deleted_config) == 0:
    return False
  else:
    configs.remove(deleted_config[0])
    return True

#PUT/UPDATE specific config
def update_config_by_name(name, updated_config):
  to_update_config= [config for config in configs if config['name'] == name]
  configs.remove(to_update_config[0])
  configs.append(updated_config)
  return updated_config

#SEARCH/QUERY specific config
def search_by_query(query, value):
  return [config for config in configs if check(config, query.split(".")) == value]

#method to get the QUERY value
def check(json, query):
  for i in range(len(query)):
    json=json.get(query[i])
  return str(json).lower() if type(json) is bool else json
