# ShortenerURL
https://roadmap.sh/projects/url-shortening-service
URL shortening service built with Django and Django REST Framework. This project allows you to create short URLs and redirect to the original URLs, keeping a record of accesses.

## Features

- ✂️ Shortens long URLs to unique 6-character codes
- 📊 Tracks the number of accesses to each URL
- 🚀 REST API for URL management
- 🔄 Real-time development with hot-reload
- 🐳 Dockerized for easy deployment

## Prerequisites

- Docker and Docker Compose

## Installation and Execution

1. Clone the repository:
```bash
git clone https://github.com/jdds97/ShortenerURL.git
cd ShortenerURL
```

2. Start the services:
```bash
./start.sh
```

This will start:
- Django backend at `http://localhost:8000`
- PostgreSQL database

## Project Structure

```
ShortenerURL/
├── backend/           # Django application
│   ├── api/          # REST API
│   └── config/       # Project configuration
├── docker-compose.yml # Service configuration
└── start.sh          # Startup script
```

## Usage

### API Endpoints

- `POST /api/urls/`: Create a short URL
    ```json
    {
        "url": "https://www.example-long-url.com/very/long/path"
    }
    ```

- `GET /api/shorten/<shortCode>/`: Get information about a short URL

## Development

The project is configured with hot-reload, so changes to the code will be automatically reflected without needing to restart the services.

## License

[MIT](https://choosealicense.com/licenses/mit/)
