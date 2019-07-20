# python-crud-operation

The aim of test is to create a simple HTTP service that stores and returns configurations that satisfy certain conditions. the service should be automatically deployed to kubernetes.

Your application MUST confirm to the following endpoint structure and return the HTTP status codes appropriate to each operation.

Following are the endpoints that should be implemented:
Name 	Method 	URL
List 	GET 	/configs
Create 	POST 	/configs
Get 	GET 	/configs/{name}
Update 	PUT/PATCH 	/configs/{name}
Delete 	DELETE 	/configs/{name}
Query 	GET 	/search?metadata.key=value
Query

The query endpoint MUST return all configs that satisfy the query argument.
curl http://config-service/search?metadata.monitoring.enabled=true
Query example-1:configs = [
  {
    "name": "datacenter-1",
    "metadata": {
      "monitoring": {
        "enabled": True
      },
      "limits": {
        "cpu": {
          "enabled": False
        }
      }
    }
  },
  {
    "name": "datacenter-2",
    "metadata": {
      "monitoring": {
        "enabled": True
      },
      "limits": {
        "cpu": {
          "enabled": True
        }
      }
    }
  }
]




