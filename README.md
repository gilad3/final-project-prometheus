# Kubernetes Monitoring Dashboard for Grafana

A comprehensive Grafana dashboard for monitoring Kubernetes clusters with detailed metrics on node performance, pod status, and resource utilization.
# 🚀 **Kubernetes Monitoring Dashboard with Prometheus & Grafana**

### 🌟 **Project Overview**
In this project, I've built a **Grafana dashboard** that monitors the health and performance of your Kubernetes cluster, powered by **Prometheus** as the data source. The dashboard provides detailed visualizations of key metrics across different levels (Node, Namespace, Pod, and Container) in your cluster. With this dashboard, you can track system resource usage, pod status, network traffic, and more!

### 🧐 **Monitoring Requirements**
The dashboard tracks these critical metrics:

#### 🖥️ **Node-Level Monitoring**:
- **Pods Running on Node**: Monitor how many pods are running on each node in your cluster.
- **CPU Usage by Cores**: Visualize the CPU usage for each core on the node.
- **CPU Usage Percentage**: See the percentage of CPU utilization on each node to spot potential bottlenecks.

#### 📦 **Namespace-Level Monitoring**:
- **Pods That Restarted**: Track the number of pods that have restarted within a specific namespace.
- **CPU Usage in Namespace**: Get an overview of the CPU usage across the entire namespace.
- **Pods Running in Namespace**: View the number of pods running in a given namespace.
- **Deployments Running in Namespace**: Monitor the number of deployments active in the namespace.
- **Network Traffic (Inbound & Outbound)**: Watch the network traffic, both receiving and transmitting, in the namespace.
- **Memory Usage in Namespace**: Track the memory consumption across all pods in the namespace.

#### 🔹 **Pod-Level Monitoring**:
- **Network Traffic (Receive & Transmit)**: Monitor the amount of data being sent and received by each pod.
- **Disk I/O (Read & Write)**: Keep track of disk read and write operations for pods.
- **CPU Usage by Percentage**: View CPU utilization as a percentage for each pod.
- **Pod Age**: Check how long each pod has been running.
- **Average Memory Usage**: Get the average memory usage of each pod over time.
- **CPU Usage**: Monitor the total CPU usage in cores for each pod.

#### 🟢 **Container-Level Monitoring**:
- **CPU Usage**: Track the CPU usage (in cores) for each container in a pod.
- **Memory Usage**: Watch the memory consumption (in MiB or GiB) for each container in the pod.

---

### ⚙️ **Setup Instructions**
Follow these steps to get the monitoring system up and running:

1. **Deploy Prometheus**:
   - Install **Prometheus** to scrape metrics from your Kubernetes cluster. 
   - You can either use Helm or a custom deployment to install Prometheus.

2. **Install Grafana**:
   - Deploy **Grafana** to visualize the metrics from Prometheus.

3. **Import the Dashboard**:
   - Import the **`finalproject.json`** file into Grafana to load the custom dashboard configuration.

4. **Configure Prometheus as the Data Source**:
   - In Grafana, set **Prometheus** as the data source for your dashboards.

5. **Customize Prometheus Queries**:
   - The dashboard queries use **PromQL** to fetch metrics from Prometheus. Ensure that variables are used in the queries for flexibility:
     - `node`: Represents a node in the Kubernetes cluster.
     - `namespace`: Represents a namespace where pods are deployed.
     - `pod`: Represents a specific pod.
     - `container`: Represents a container within the pod.

6. **Set Up Alerts** (Optional):
   - Set up **Grafana Alerts** to get notified if certain thresholds are exceeded (e.g., CPU usage > 80%).

---

### 📂 **Files in This Repository**
- **`finalproject.json`**: The Grafana dashboard configuration file that you can import to visualize the monitoring data.
- **`README.md`**: This file, providing project details and setup instructions.

---

### 🛠️ **Tools Used**
- **Prometheus**: For scraping and storing Kubernetes metrics.
- **Grafana**: For visualizing the metrics and creating dashboards.

---

### 💬 **Contribute**
Feel free to open an issue or submit a pull request if you want to contribute to this project or have any suggestions. 

Happy Monitoring! 👨‍💻🚀
