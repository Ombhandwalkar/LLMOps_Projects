# Flipkart Product Recommender System

**Flipkart Product Recommender System** — a demo/POC implementing a product recommender using **LangChain** with **RAG (Retrieval-Augmented Generation)**, embeddings stored in **AstraDB VectorStore**, deployed on **GCP (Minikube on VM)** and instrumented with **Prometheus** (metrics) and **Grafana** (visualization).

---


## 🎥 Demo Video

[![Demo Video](https://img.youtube.com/vi/cmVjsDW27lk/0.jpg)](https://youtu.be/cmVjsDW27lk)

---

## Project overview

This project demonstrates:

- Ingesting product data and building an embedding vector store using **LangChain** and **sentence-transformers**.
- Storing vectors in **AstraDB VectorStore**.
- Implementing a Flask app to expose a query/recommendation API using RAG.
- Containerizing the app and deploying to a Minikube cluster running on a GCP VM.
- Observability via **Prometheus** for metrics and **Grafana** for dashboards.

---

## Architecture

1. **Flask app** — REST endpoints for ingestion and recommendation. Uses LangChain embeddings + AstraDB VectorStore.  
2. **AstraDB VectorStore** — stores embeddings & metadata.  
3. **Kubernetes (Minikube)** — deployment + service for the Flask app.  
4. **Prometheus** — scrapes app metrics.  
5. **Grafana** — dashboards for visualization.  

---

