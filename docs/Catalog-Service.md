#ConsumerClient

##getAllResources

Return all resources that are available to the current user.

Parameters:
* show[string] = This determines what is returned. Use json to return a json object or
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

##getResource

Get a vRA resource by Id

Parameters:
* id[string] = id of the vRA resource

This function will return a json object. You can interact with this object in the same way
that you would with any object.

```
resourceId='171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'
resource = client.getResource(id=resourceId)
print resource['id']
print resource['name']
```
If you want to return raw json, you will need to use json.dumps().

```
resourceId='171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'
resource = client.getResource(id=resourceId)
resourceRaw = json.dumps(resource)
print resourcesRaw
```

##getResourceNetworking

Return networking information for a given resource.

Parameters:
* id[string] = Id of the vRA Resource

This function will return a json object. You can interact with this object in the same way
that you would with any object.

```
resourceId='171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'
networking = client.getResourceNetworking(id=resourceId)

for i in networking:
  print i['key']
  print i['value']['value']
```

If you want to return raw json, you will need to use json.dumps().

```
resourceId='171d8ab9-1b5b-44e8-ac20-b559da4c1ef3'
networking = client.getResourceNetworking(id=resourceId)
networkingRaw = json.dumps(networking)
print networkingRaw
```

##getEntitledCatalogItems

Return all entitled catalog items for the current user.

Parameters:
* show[string] = This determines what is returned. Use json to return a json object or
                    table to return a table. This parameter is not mandatory.

By default this function will return a table containing the id and name of the
resource. This can be changed by adding the show parameter as follows:

```
entitledCatalogItems = client.getEntitledCatalogItems(show='json')
```

show='json' will return an object. You can interact with this object in the same way
that you would with any object.

```
entitledCatalogItems = client.getEntitledCatalogItems(show='json')

for i in entitledCatalogItems:

  print i['catalogItem']['id']
  print i['catalogItem']['name']
```

If you want to return raw json, you will need to use json.dumps().

```
entitledCatalogItems = client.getEntitledCatalogItems(show='json')
entitledCatalogItemsRaw = json.dumps(entitledCatalogItems)
print entitledCatalogItemsRaw
```

##getResourceIdByRequestId

Search for a resource with a matching request id

parameters:
* id[string] = Request id of the vRA resource

When you deploy a machine with requestResource() it will return the request id. Use this function
to get the ID of the resource you have just deployed. Once you have the resource id, you can go on
to query things like networking.

##requestResource


##getRequest
