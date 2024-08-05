docker image build -t img-resize-api ./img-resize-api --no-cache
docker run -p 5013:5000 img-resize-api