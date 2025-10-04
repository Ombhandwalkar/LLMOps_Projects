# 🎌 AI-Powered Anime Recommender System

An end-to-end LLMOps project that combines Large Language Models, vector databases, and Kubernetes orchestration to deliver intelligent anime recommendations through an interactive web interface.

## 🎯 Project Overview

This project demonstrates a production-ready AI application that uses Groq LLM APIs and HuggingFace embeddings to provide personalized anime recommendations. The system leverages LangChain for LLM orchestration, ChromaDB for vector storage, and is deployed on Kubernetes with comprehensive monitoring via Grafana Cloud.

## ✨ Key Features

- **Intelligent Recommendations**: Natural language-based anime suggestions powered by Groq LLMs
- **Vector Search**: Efficient similarity search using ChromaDB and HuggingFace embeddings
- **Interactive UI**: User-friendly Streamlit interface for seamless interaction
- **Production Deployment**: Containerized application running on Kubernetes
- **Cloud Infrastructure**: Deployed on GCP VM with Minikube
- **Real-time Monitoring**: Comprehensive observability using Grafana Cloud
- **Custom Exception Handling**: Robust error management and logging

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **LLM & Embeddings** | Groq API, HuggingFace |
| **GenAI Framework** | LangChain |
| **Vector Database** | ChromaDB |
| **Frontend** | Streamlit |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (Minikube) |
| **Cloud Platform** | GCP VM |
| **Monitoring** | Grafana Cloud |
| **Version Control** | GitHub |
| **CLI Tools** | kubectl |


## 🎥 Demo Video

[![Demo Video](https://img.youtube.com/vi/SfqSzCTOybI/0.jpg)](https://youtu.be/SfqSzCTOybI)

## 🏗️ Architecture

```
┌─────────────────┐
│   User Input    │
│   (Streamlit)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   LangChain     │
│   Pipeline      │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐  ┌──────────┐
│ Groq   │  │ChromaDB  │
│  LLM   │  │Vector DB │
└────────┘  └──────────┘
         │
         ▼
┌─────────────────┐
│   Docker        │
│   Container     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Kubernetes     │
│  (Minikube)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Grafana Cloud  │
│   Monitoring    │
└─────────────────┘
```

## 📁 Project Structure

```
AI_Anime_Recommender/
├── src/
│   ├── config/
│   │   └── configuration.py
│   ├── data/
│   │   └── data_loader.py
│   ├── embeddings/
│   │   └── chroma_db.py
│   ├── prompts/
│   │   └── templates.py
│   ├── recommender/
│   │   └── engine.py
│   ├── utils/
│   │   ├── logger.py
│   │   └── exception.py
│   └── app.py
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── docker/
│   └── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Docker
- Kubernetes (Minikube for local development)
- kubectl CLI
- GCP account (for cloud deployment)
- Groq API key
- HuggingFace API token

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Ombhandwalkar/LLMOps_Projects.git
cd LLMOps_Projects/AI_Anime_Recommender_Grafana_Kubernetes__Langchain
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API keys**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_TOKEN=your_huggingface_token
```

### Local Development

**Run the Streamlit app locally**
```bash
streamlit run src/app.py
```

### Docker Deployment

1. **Build Docker image**
```bash
docker build -t anime-recommender:latest -f docker/Dockerfile .
```

2. **Run container**
```bash
docker run -p 8501:8501 anime-recommender:latest
```

### Kubernetes Deployment

1. **Start Minikube**
```bash
minikube start
```

2. **Apply Kubernetes configurations**
```bash
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

3. **Check deployment status**
```bash
kubectl get pods
kubectl get services
```

4. **Access the application**
```bash
minikube service anime-recommender-service
```

## 📊 Monitoring with Grafana Cloud

The project includes comprehensive monitoring setup for Kubernetes metrics:

1. **Cluster Health**: Node and pod status monitoring
2. **Resource Usage**: CPU, memory, and disk utilization
3. **Application Metrics**: Request rates, latencies, and errors
4. **Custom Dashboards**: Tailored views for LLM performance

### Setting up Grafana Cloud

1. Create a Grafana Cloud account
2. Install Grafana Agent on your Kubernetes cluster
3. Configure metrics collection from Minikube
4. Import pre-built Kubernetes dashboards
5. Set up alerts for critical metrics

## 🎓 What You'll Learn

This project covers essential LLMOps and DevOps concepts:

- ✅ Integrating LLM APIs (Groq) with GenAI frameworks (LangChain)
- ✅ Building semantic search with vector databases (ChromaDB)
- ✅ Creating production-ready prompt engineering pipelines
- ✅ Containerizing ML applications with Docker
- ✅ Orchestrating deployments with Kubernetes
- ✅ Implementing observability and monitoring
- ✅ Managing infrastructure on cloud platforms (GCP)
- ✅ CI/CD workflows for ML systems

## 🔮 Roadmap

- [ ] Implement GitHub Actions CI/CD pipeline
- [ ] Add RESTful API endpoints
- [ ] Enhance recommendation algorithms
- [ ] Add user authentication and personalization
- [ ] Create public demo deployment
- [ ] Add support for multiple languages
- [ ] Implement caching layer for faster responses
- [ ] Add A/B testing framework

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
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

- Groq for providing fast LLM inference
- HuggingFace for embedding models
- LangChain community for excellent documentation
- Grafana Labs for monitoring solutions
- The anime community for inspiration

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Grafana Cloud Documentation](https://grafana.com/docs/)

## 📬 Contact

For questions, feedback, or collaboration opportunities, feel free to reach out or open an issue in the repository.

---

⭐ If you find this project helpful, please consider giving it a star!

**Happy Coding! 🚀**
