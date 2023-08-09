# LOGGING_LEVEL = 'WARN'
# LOGGING_LEVEL = 'DEBUG'
LOGGING_LEVEL = "INFO"
LOG_STDOUT = True
# SQLALCHEMY Configuration
SQLALCHEMY_URL = "postgresql://postgres:postgres@postgres:5432/master"
SQLALCHEMY_ECHO = False
# REDIS Configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379
# Kafka Configuration
KAFKA_BROKER = "kafka:9092"
SCHEMA_REGISTRY_URL = "http://schema-registry:8081"
# Connector AVRO Schema Parameters
HARVESTER_OUTPUT_SCHEMA = "HarvesterOutputSchema"
HARVESTER_OUTPUT_TOPIC = "HarvesterOutput"
