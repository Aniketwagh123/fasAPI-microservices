# Employee Payroll App

## Description

The Employee Payroll App is a microservices-based application designed to manage employee payroll data. It leverages FastAPI for creating efficient and scalable APIs, RabbitMQ for message queuing, and MongoDB for data persistence. The architecture includes an API Gateway that routes requests to the appropriate microservices for employee and payroll management.

## Project Structure

- `api_gateway/` - Contains the API Gateway service that routes requests to the employee and payroll services.
- `employee_service/` - Microservice responsible for managing employee data.
- `payroll_service/` - Microservice responsible for managing payroll data.
- `docker-compose.yml` - Orchestrates the services including the API Gateway, employee service, payroll service, RabbitMQ, and MongoDB.
- `.env` - Contains environment variables for configuration.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/employee-payroll-app.git
   cd employee-payroll-app
   ```

2. **Build and start the services using Docker Compose:**

   ```bash
   docker-compose up --build
   ```

3. **Access the services:**

   - API Gateway: `http://localhost:8000`
   - Employee Service: `http://localhost:8001`
   - Payroll Service: `http://localhost:8002`
   - RabbitMQ Management: `http://localhost:15672` (default username: `guest`, password: `guest`)
   - MongoDB: `mongodb://localhost:27017`

## API Endpoints

### Employee Service

- **Create Employee**: `POST /employees`
- **Get Employee**: `GET /employees/{employee_id}`

### Payroll Service

- **Create Payroll**: `POST /payrolls`
- **Get Payroll**: `GET /payrolls/{payroll_id}`

## Testing

To run tests for the API Gateway, Employee Service, and Payroll Service:

```bash
# Run tests for API Gateway
docker-compose exec api_gateway pytest

# Run tests for Employee Service
docker-compose exec employee_service pytest

# Run tests for Payroll Service
docker-compose exec payroll_service pytest
```



## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [MongoDB](https://www.mongodb.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
