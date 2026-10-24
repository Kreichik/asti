# Configuration

Executable components will receive documented environment settings and .env.example files as they are implemented. The current repository contains documentation tooling; its dependencies are in [tools/requirements.txt](../tools/requirements.txt).

Service credentials and model keys stay on the server, outside Git. Client responses and logs must not expose them. Examples use placeholders. Deployment configuration will cover the VPS environment, migrations, TLS and backup procedure.
