# 🤖 AI Travel Planner Chatbot on Kubernetes: Full-Stack Observability with the ELK Stack

This project showcases a production-grade deployment of an **AI-powered Travel Itinerary Planner Chatbot** on Kubernetes, with a dedicated, decoupled logging and monitoring pipeline using the **Elastic Stack (ELK)**.

---

## 💡 Project Thesis: Cloud-Native Observability

Our core achievement is demonstrating a **robust, scalable architecture** where the Chatbot's operational health, user interactions, and error logs are streamed in real-time into a dedicated observability stack. This ensures operational stability and rapid diagnostics in a distributed microservices environment.

---

## 🧩 System Components

| Component       | Role in the System                                                | Deployment Model         | Container Image                   |
|-----------------|-----------------------------------------------------------------|------------------------|----------------------------------|
| Travel Chatbot  | Core Service: Generates AI-driven travel plans.                 | Deployment             | Custom Python/Flask Image        |
| Elasticsearch   | Central Data Store: Scalable, high-speed indexing for all logs. | Deployment, Service    | `elasticsearch:7.17.0`           |
| Kibana          | Visualization Layer: Monitoring, dashboarding, error analysis. | Deployment, NodePort   | `kibana:7.17.0`                  |
| Logstash        | ETL Pipeline: Aggregation, enrichment, and transformation.     | Deployment, Service    | `logstash:7.17.0`                |
| Filebeat        | Log Shipper: Ensures every Chatbot instance's logs are captured.| DaemonSet             | `filebeat:7.17.0`                |

---

## 🏗️ Kubernetes Deployment Architecture

The entire pipeline is containerized and managed by Kubernetes, enforcing **resource limits**, **service discovery**, and **scalability**.
