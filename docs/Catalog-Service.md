#ConsumerClient

##getAllResources

Return all resources that are available to the current user.

Parameters:
    show[string] = This determines what is returned. Use json to return a json object or
                    table to return a table. This parameter is not mandetory.

By default this function will return a table containing the id and name of the
resource. This can be changed by adding the show parameter as folllows

```
resources = client.getAllResources(show='json')
```

show='json' will return an object. You can interact with this object in the same way
that you would with any object.

```
resources = client.getAllResources(show='json')

for resource in resources:

  print resource['id']
  print resource['name']
```

If you want to return raw json, you will need to use json.dumps().

```
resources = client.getAllResources(show='json')
resourcesRaw = json.dumps(resources)
print resourcesRaw
```
