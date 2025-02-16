DOCKER_COMPOSE = docker compose

COMPOSE_FILE = docker-compose.yml

DOCKER_COMPOSE_ENV_LOCAL = $(DOCKER_COMPOSE) -f $(COMPOSE_FILE)

lup: local-docker-up
down: local-docker-down
restart: down up
ps: local-docker-ps
logs: local-docker-logs


local-docker-up:
	$(DOCKER_COMPOSE_ENV_LOCAL) -f docker-compose.local.yml --env-file .env up --build --remove-orphans

local-docker-down:
	$(DOCKER_COMPOSE_ENV_LOCAL) down --remove-orphans

local-docker-ps:
	$(DOCKER_COMPOSE_ENV_LOCAL) ps --all

local-docker-logs:
	$(DOCKER_COMPOSE_ENV_LOCAL) logs

.PHONY: tests
