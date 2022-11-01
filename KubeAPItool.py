from kubernetes import client, config ,watch
# To Load the cluster config, by default it will load ~/.kube/config
# For a task it is ok to load default config, but in live environemnts we should provide associated configs.
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

print("*******************************************************")

print("Listing Deployments with default Namespace")
print("Name of Deployment\t\t\tNamespace- Default\tTimeStamp")
rete = v1.list_namespaced_pod(namespace="default", watch=False)


for i in rete.items:
    print("%s\t%s\t\t\t%s" % (i.metadata.name,i.metadata.namespace,i.metadata.creation_timestamp ))
