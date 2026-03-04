# Use a lightweight debian os as the base image
FROM debian:stable-slim

# Copy the compiled Go server into the container
COPY goserver /bin/goserver

# Run the server when the container starts
ENV PORT=8991
CMD ["/bin/goserver"]