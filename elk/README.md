# ELK Stack Setup

This project sets up an ELK (Elasticsearch, Logstash, Kibana) stack using Docker Compose for log management and analysis.

## Prerequisites

- Docker
- Docker Compose
- Python 3.x (for the Python applications)
- Required Python packages (install using `pip install -r requirements.txt`)

## Project Structure

```
elk/
├── docker-compose.yml      # Docker Compose configuration
├── logstash.conf          # Logstash pipeline configuration
├── main.py               # Main Python application
├── api.py                # API implementation
├── payment.py            # Payment processing module
├── log.py                # Logging configuration
├── elasticsearch/        # Elasticsearch configuration
├── logstash/            # Logstash configuration
└── kibana/              # Kibana configuration
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Vignesh-1101/docker-elk-python-
   cd elk
   ```

2. Start the ELK stack:
   ```bash
   docker-compose up -d
   ```

3. Verify the services are running:
   ```bash
   docker ps
   ```

## Service Ports

- Elasticsearch: http://localhost:9300
- Logstash: http://localhost:5050
- Kibana: http://localhost:5700

## Configuration

### Elasticsearch
- Version: 7.17.0
- Memory: 512MB allocated
- Security: Disabled (xpack.security.enabled=false)
- Data persistence: Using Docker volume `elasticsearch-data`

### Logstash
- Version: 7.17.0
- Pipeline configuration: `logstash.conf`
- Input: TCP on port 5050
- Output: Elasticsearch

### Kibana
- Version: 7.17.0
- Connected to Elasticsearch at http://elasticsearch:9200
- Security: Disabled

## Logstash Pipeline Configuration

The Logstash pipeline (`logstash.conf`) is configured to:
1. Accept TCP input on port 5050
2. Parse JSON input
3. Add timestamp and host information
4. Output to Elasticsearch

## Python Application Integration

The Python application (`main.py`) is configured to:
- Send logs to Logstash on port 5050
- Use structured logging format
- Include application-specific fields

## Usage

1. Start the ELK stack:
   ```bash
   docker-compose up -d
   ```

2. Run the Python application:
   ```bash
   python main.py
   ```

3. Access Kibana dashboard:
   - Open http://localhost:5700 in your browser
   - Create index pattern for your logs
   - Explore and visualize your data

## Troubleshooting

1. If services fail to start:
   ```bash
   docker-compose logs
   ```

2. Check service status:
   ```bash
   docker ps
   ```

3. Verify Elasticsearch is running:
   ```bash
   curl http://localhost:9300
   ```

## Maintenance

- To stop all services:
  ```bash
  docker-compose down
  ```

- To stop and remove volumes:
  ```bash
  docker-compose down -v
  ```

## Security Notes

- Security features are currently disabled for development purposes
- For production use, enable security features and configure proper authentication
- Consider using environment variables for sensitive configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 
