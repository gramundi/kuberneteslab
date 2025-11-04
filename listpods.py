from kubernetes import client, config
from kubernetes.client.rest import ApiException

def list_pods_in_namespace_in_cluster(namespace):
    """
    Lists all pods in a given namespace using in-cluster configuration.
    """
    try:
        # 1. Load configuration from the service account mounted in the Pod
        config.load_incluster_config()
    except config.ConfigException as e:
        print(f"Error loading in-cluster config: {e}")
        print("This code should only be run inside a Kubernetes Pod.")
        return

    # Rest of the logic remains the same
    v1 = client.CoreV1Api()
    # ... (API call and printing logic)
    try:
        pod_list = v1.list_namespaced_pod(namespace=namespace)
        print(f"Listing pods in namespace: **{namespace}**")
        print("-" * 30)
        for pod in pod_list.items:
            print(f"Name: {pod.metadata.name}\tStatus: {pod.status.phase}")
            
    except ApiException as e:
        print(f"Exception when calling CoreV1Api->list_namespaced_pod: {e}")

# Example usage
TARGET_NAMESPACE = "default" 
list_pods_in_namespace_in_cluster(TARGET_NAMESPACE)