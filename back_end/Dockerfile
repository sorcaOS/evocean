# Python image to use.
FROM asia-east1-docker.pkg.dev/omelet-f0b89/github/evocean_django

# Set the working directory to /app
WORKDIR /app
RUN apt-get update

COPY . .
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip -q
RUN pip install -r requirements.txt -U -q
RUN pip install --upgrade requests certifi urllib3 -q

#set enviroment variables production = true
ENV IS_DOCKER=True
# Run app.py when the container launches
# RUN python manage.py collectstatic --noinput
