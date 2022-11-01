from kubernetes import client, config ,watch

# Load the connection config, default behaviour is to load ~/.kube/config
# For development this is fine, when moving into production another way
# of providing the config is required
config.load_kube_config()


v1 = client.CoreV1Api()
apis_api = client.AppsV1Api()

imagetest=client.V1ContainerImage()
print("Listing Deployments with their names")
print("Name of Deployment\t\t\tImages of Each deployment\t\tTimeStamp")
ret = v1.list_pod_for_all_namespaces(watch=False)

#print(ret)
for i in ret.items:
    print("%s\t\t\t\t%s\t\t\t\t%s" % (i.metadata.name,i.metadata.namespace,i.metadata.creation_timestamp ))


print("-----------------------------------------------")

print("Listing Deployments with default Namespace")
print("Name of Deployment\t\t\tNamespace- Default\tTimeStamp")
rete = v1.list_namespaced_pod(namespace="default", watch=False)


for i in rete.items:
    print("%s\t%s\t\t\t%s" % (i.metadata.name,i.metadata.namespace,i.metadata.creation_timestamp ))

