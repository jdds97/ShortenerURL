#!/bin/sh

set -e

# Build and start the services with docker-compose
docker_compose_up() {
    docker compose build --pull
    docker compose up --remove-orphans "$@"
}

# Run the backend container with arguments
run_backend() {
    if [ -t 1 ]; then
        INTERACTIVE="-it"
    else
        INTERACTIVE=""
    fi

    docker compose run --rm \
        --volume .:/app \
        --volume /app/.venv \
        $INTERACTIVE \
        backend "$@"
}

# Default action: build and start all services
if [ $# -eq 0 ]; then
    docker_compose_up
else
    # Handle different commands
    case "$1" in
        up)
            shift
            docker_compose_up "$@"
            ;;
        run)
            shift
            run_backend "$@"
            ;;
        *)
            echo "Unknown command: $1"
            echo "Usage: $0 [up|run] [arguments]"
            exit 1
            ;;
    esac
fi