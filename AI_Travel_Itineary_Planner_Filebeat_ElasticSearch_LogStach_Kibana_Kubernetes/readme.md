# AI Travel Itinerary Planner with ELK Stack on Kubernetes

A production-ready AI-powered travel itinerary planner that leverages Large Language Models (LLMs) to generate personalized travel plans, with comprehensive logging and monitoring using the ELK Stack (Elasticsearch, Logstash, Kibana) and Filebeat, deployed on Kubernetes.

## 🌟 Features

- **AI-Powered Itinerary Generation**: Utilizes LLMs to create personalized travel itineraries based on user preferences
- **Real-time Log Management**: Filebeat collects application logs and forwards them to the ELK stack
- **Centralized Logging**: Logstash processes and enriches log data for better insights
- **Data Storage & Search**: Elasticsearch stores and indexes logs for fast retrieval and analysis
- **Visual Analytics**: Kibana provides interactive dashboards for monitoring application performance and user behavior
- **Container Orchestration**: Kubernetes manages the deployment, scaling, and operations of all services
- **LLMOps Integration**: Monitoring and observability for LLM operations and performance

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Kubernetes Cluster                   │
│  ┌─────────────────────────────────────────────────┐   │
│  │  AI Travel Planner Application                   │   │
│  │  (FastAPI/Flask + LLM Integration)               │   │
│  └──────────────┬──────────────────────────────────┘   │
│                 │ Logs                                   │
│                 ▼                                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │            Filebeat (Log Shipper)                │   │
│  └──────────────┬──────────────────────────────────┘   │
│                 │                                        │
│                 ▼                                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │       Logstash (Log Processing)                  │   │
│  └──────────────┬──────────────────────────────────┘   │
│                 │                                        │
│                 ▼                                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │    Elasticsearch (Log Storage & Search)          │   │
│  └──────────────┬──────────────────────────────────┘   │
│                 │                                        │
│                 ▼                                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │      Kibana (Visualization & Dashboards)         │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## 📋 Prerequisites

- Kubernetes cluster (v1.20+)
- kubectl CLI tool
- Docker
- Helm (v3+)
- Python 3.8+
- LLM API access (OpenAI, Anthropic, or similar)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Ombhandwalkar/LLMOps_Projects.git
cd LLMOps_Projects/AI_Travel_Itineary_Planner_Filebeat_ElasticSearch_LogStach_Kibana_Kubernetes
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

Required environment variables:
```
LLM_API_KEY=your_llm_api_key
LLM_MODEL=gpt-4
ELASTICSEARCH_HOST=elasticsearch-service
ELASTICSEARCH_PORT=9200
LOGSTASH_HOST=logstash-service
LOGSTASH_PORT=5044
KIBANA_PORT=5601
```

### 3. Deploy to Kubernetes

#### Deploy Elasticsearch
```bash
kubectl apply -f kubernetes/elasticsearch-deployment.yaml
kubectl apply -f kubernetes/elasticsearch-service.yaml
```

#### Deploy Logstash
```bash
kubectl apply -f kubernetes/logstash-configmap.yaml
kubectl apply -f kubernetes/logstash-deployment.yaml
kubectl apply -f kubernetes/logstash-service.yaml
```

#### Deploy Kibana
```bash
kubectl apply -f kubernetes/kibana-deployment.yaml
kubectl apply -f kubernetes/kibana-service.yaml
```

#### Deploy Filebeat
```bash
kubectl apply -f kubernetes/filebeat-configmap.yaml
kubectl apply -f kubernetes/filebeat-daemonset.yaml
```

#### Deploy the AI Travel Planner Application
```bash
kubectl apply -f kubernetes/app-deployment.yaml
kubectl apply -f kubernetes/app-service.yaml
```

### 4. Verify Deployment

```bash
kubectl get pods -n default
kubectl get services -n default
```

### 5. Access the Services

- **AI Travel Planner**: `http://<node-ip>:<app-service-port>`
- **Kibana Dashboard**: `http://<node-ip>:5601`
- **Elasticsearch**: `http://<node-ip>:9200`

## 📊 Monitoring and Observability

### Kibana Dashboards

Access Kibana at `http://<kibana-service-url>:5601` to:

1. **View Application Logs**: Filter by service, severity, and timestamp
2. **Monitor LLM Performance**: Track response times, token usage, and error rates
3. **User Analytics**: Analyze travel preferences and popular destinations
4. **System Health**: Monitor Kubernetes pods, containers, and resource usage

### Key Metrics to Monitor

- LLM API response times
- Request/response token counts
- Error rates and types
- User query patterns
- System resource utilization
- Pod health and restarts

## 🔧 Configuration

### Filebeat Configuration

Located in `kubernetes/filebeat-configmap.yaml`:
- Collects logs from all pods with specific labels
- Forwards logs to Logstash for processing
- Supports JSON and plaintext log formats

### Logstash Configuration

Located in `kubernetes/logstash-configmap.yaml`:
- Parses and enriches log data
- Adds metadata (timestamps, log levels, service names)
- Filters and transforms data before indexing

### Elasticsearch Configuration

- Indexes: `travel-planner-logs-*`
- Retention policy: Configurable (default: 30 days)
- Shards and replicas: Configurable based on cluster size

## 🛠️ Development

### Local Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application locally
python app.py
```

### Running Tests

```bash
pytest tests/
```

### Building Docker Image

```bash
docker build -t ai-travel-planner:latest .
docker push your-registry/ai-travel-planner:latest
```

## 📚 API Documentation

### Generate Itinerary

**Endpoint**: `POST /api/v1/itinerary`

**Request Body**:
```json
{
  "destination": "Paris, France",
  "duration": "5 days",
  "budget": "moderate",
  "interests": ["museums", "food", "history"],
  "travel_dates": {
    "start": "2025-06-01",
    "end": "2025-06-05"
  }
}
```

**Response**:
```json
{
  "itinerary_id": "uuid",
  "destination": "Paris, France",
  "daily_plans": [...],
  "estimated_cost": {...},
  "recommendations": [...],
  "created_at": "timestamp"
}
```

## 🔐 Security Considerations

- API keys stored in Kubernetes secrets
- Network policies to restrict inter-pod communication
- TLS/SSL enabled for all external communications
- RBAC configured for Kubernetes access control
- Regular security updates and vulnerability scanning

## 📈 Scaling

### Horizontal Pod Autoscaling

```bash
kubectl autoscale deployment travel-planner --cpu-percent=70 --min=2 --max=10
```

### Elasticsearch Scaling

Increase the number of Elasticsearch nodes:
```bash
kubectl scale statefulset elasticsearch --replicas=3
```

## 🐛 Troubleshooting

### Common Issues

1. **Filebeat not collecting logs**
   - Check pod labels and Filebeat configuration
   - Verify log file paths are correct

2. **Logstash connection errors**
   - Ensure Logstash service is running
   - Check network policies and firewall rules

3. **Elasticsearch storage issues**
   - Monitor disk usage
   - Implement index lifecycle management (ILM)

4. **LLM API timeouts**
   - Check API rate limits
   - Implement retry logic with exponential backoff

### View Logs

```bash
# Application logs
kubectl logs -f deployment/travel-planner

# Filebeat logs
kubectl logs -f daemonset/filebeat

# Elasticsearch logs
kubectl logs -f statefulset/elasticsearch
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Om Bhandwalkar** - [GitHub](https://github.com/Ombhandwalkar)

## 🙏 Acknowledgments

- OpenAI/Anthropic for LLM APIs
- Elastic for the ELK Stack
- Kubernetes community
- All contributors and supporters

## 📞 Contact

For questions or support, please open an issue or contact [your-email@example.com]

---

**Note**: This is a learning project demonstrating LLMOps practices with production-grade logging and monitoring infrastructure.
