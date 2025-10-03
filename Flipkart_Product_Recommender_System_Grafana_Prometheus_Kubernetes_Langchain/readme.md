# Flipkart Product Recommender System

A production-ready LLM-powered product recommendation system built with LangChain, deployed on Kubernetes, and monitored using Prometheus and Grafana.

## 🎯 Overview

This project demonstrates a complete LLMOps pipeline for building an intelligent product recommendation system for Flipkart products. It leverages Large Language Models through LangChain to provide personalized product recommendations based on user queries and preferences.

## ✨ Features

- **LLM-Powered Recommendations**: Utilizes LangChain for intelligent product recommendations
- **Scalable Architecture**: Deployed on Kubernetes for horizontal scaling
- **Comprehensive Monitoring**: Real-time metrics collection with Prometheus
- **Visual Dashboards**: Custom Grafana dashboards for system observability
- **Production-Ready**: Complete MLOps/LLMOps pipeline with monitoring and alerting

## 🎥 Demo Video

[![Demo Video](https://img.youtube.com/vi/cmVjsDW27lk/0.jpg)](https://youtu.be/cmVjsDW27lk)


## 🏗️ Architecture

```
User Query → API Gateway → LangChain Service → LLM Model
                                ↓
                          Product Database
                                ↓
                          Recommendations
                                ↓
                    Prometheus (Metrics Collection)
                                ↓
                    Grafana (Visualization)
```

## 🛠️ Tech Stack

- **LLM Framework**: LangChain
- **Orchestration**: Kubernetes
- **Monitoring**: Prometheus
- **Visualization**: Grafana
- **Language**: Python
- **Container Runtime**: Docker

## 📋 Prerequisites

- Python 3.8+
- Docker
- Kubernetes cluster (minikube, kind, or cloud provider)
- kubectl CLI
- Helm (optional, for easier deployment)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ombhandwalkar/LLMOps_Projects.git
cd LLMOps_Projects/Flipkart_Product_Recommender_System_Grafana_Prometheus_Kubernetes_Langchain
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

Required environment variables:
```
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=your_database_url
PROMETHEUS_PORT=9090
GRAFANA_PORT=3000
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Build Docker Image

```bash
docker build -t flipkart-recommender:latest .
```

## 🎮 Usage

### Local Development

```bash
python app.py
```

### Kubernetes Deployment

#### Deploy Application

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

#### Deploy Prometheus

```bash
kubectl apply -f k8s/prometheus/
```

#### Deploy Grafana

```bash
kubectl apply -f k8s/grafana/
```

### Access Services

- **Application**: `http://localhost:8080`
- **Prometheus**: `http://localhost:9090`
- **Grafana**: `http://localhost:3000` (default credentials: admin/admin)

## 📊 Monitoring

### Prometheus Metrics

The application exposes the following metrics:

- `recommendation_requests_total`: Total number of recommendation requests
- `recommendation_latency_seconds`: Latency of recommendation generation
- `llm_tokens_used`: Number of tokens consumed by the LLM
- `recommendation_errors_total`: Total number of errors

### Grafana Dashboards

Import the provided dashboards from `grafana/dashboards/`:

1. **System Overview**: General system health and performance
2. **LLM Metrics**: Token usage, latency, and costs
3. **Application Metrics**: Request rates, error rates, and response times

## 🔧 Configuration

### LangChain Configuration

Configure your LangChain components in `config/langchain_config.yaml`:

```yaml
llm:
  model: gpt-3.5-turbo
  temperature: 0.7
  max_tokens: 500

embeddings:
  model: text-embedding-ada-002

vectorstore:
  type: faiss
  dimension: 1536
```

### Kubernetes Resources

Adjust resource limits in `k8s/deployment.yaml`:

```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

## 🧪 Testing

Run unit tests:

```bash
pytest tests/
```

Run integration tests:

```bash
pytest tests/integration/
```

## 📈 Scaling

### Horizontal Pod Autoscaling

```bash
kubectl apply -f k8s/hpa.yaml
```

This will automatically scale pods based on CPU utilization.

### Manual Scaling

```bash
kubectl scale deployment flipkart-recommender --replicas=5
```

## 🔍 Troubleshooting

### Check Pod Logs

```bash
kubectl logs -f deployment/flipkart-recommender
```

### Check Prometheus Targets

Navigate to Prometheus UI → Status → Targets

### Grafana Data Source Issues

Ensure Prometheus is correctly configured as a data source in Grafana:
- URL: `http://prometheus-service:9090`
- Access: Server (default)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Om Bhandwalkar**

- GitHub: [@Ombhandwalkar](https://github.com/Ombhandwalkar)
- Project Link: [LLMOps_Projects](https://github.com/Ombhandwalkar/LLMOps_Projects)

## 🙏 Acknowledgments

- LangChain for the LLM framework
- Prometheus and Grafana for monitoring solutions
- Kubernetes community for container orchestration
- OpenAI for LLM capabilities

## 📚 Documentation

For detailed documentation, please refer to:

- [LangChain Documentation](https://docs.langchain.com/)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

## 🗺️ Roadmap

- [ ] Add support for multiple LLM providers
- [ ] Implement A/B testing framework
- [ ] Add cost optimization features
- [ ] Implement caching layer
- [ ] Add support for batch processing
- [ ] Enhance security features
- [ ] Add API rate limiting

## 📞 Support

For support, email your-email@example.com or open an issue in the GitHub repository.

---

⭐ Star this repository if you find it helpful!
