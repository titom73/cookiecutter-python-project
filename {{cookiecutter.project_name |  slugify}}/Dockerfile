ARG PYTHON_VER=3.9
ARG IMG_OPTION=alpine

### BUILDER

FROM python:${PYTHON_VER}-${IMG_OPTION} AS BUILDER

RUN pip install --upgrade pip

WORKDIR /local
COPY . /local

RUN python -m venv /opt/venv


ENV PATH="/opt/venv/bin:$PATH"

RUN apk add --no-cache build-base # Add build-base package
RUN pip --no-cache-dir install "."

# ----------------------------------- #

### BASE

FROM python:${PYTHON_VER}-${IMG_OPTION} AS BASE

# Add a system user
RUN adduser --system noroot

# Opencontainer labels
# Labels version and revision will be updating
# during the CI with accurate information
# To configure version and revision, you can use:
# docker build --label org.opencontainers.image.version=<your version> -t ...
# Doc: https://docs.docker.com/engine/reference/commandline/run/#label
LABEL   "org.opencontainers.image.title"="{{cookiecutter.project_name |  slugify}}" \
    "org.opencontainers.artifact.description"="{{cookiecutter.project_description}}." \
    "org.opencontainers.image.description"="{{cookiecutter.project_description}}." \
    "org.opencontainers.image.source"="https://{{cookiecutter.git_server}}/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name |  slugify}}" \
    "org.opencontainers.image.url"="https://{{cookiecutter.git_server}}/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name |  slugify}}" \
    "org.opencontainers.image.documentation"="https://{{cookiecutter.git_server}}/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name |  slugify}}" \
    "org.opencontainers.image.licenses"="{{cookiecutter.open_source_license}}" \
    "org.opencontainers.image.vendor"="{{cookiecutter.author}}" \
    "org.opencontainers.image.authors"="{{cookiecutter.author}}" \
    "org.opencontainers.image.base.name"="python" \
    "org.opencontainers.image.revision"="dev" \
    "org.opencontainers.image.version"="dev"

# Copy artifacts from builder
COPY --from=BUILDER /opt/venv /opt/venv

# Define PATH and default user
ENV PATH="/opt/venv/bin:$PATH"

USER noroot

ENTRYPOINT [ "ash" ]