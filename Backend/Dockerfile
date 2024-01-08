FROM python:3.11
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask","run","--host","0.0.0.0"]

# First build : docker build -t rest-api(any_name) .       (Dont forget the dot at the end)
# Then run : docker run -p 5000:5000 rest-api  (Earlier name that you gave)
# To auto run this container : docker run -dp 5000:5000 -w /app -v "$(pwd):/app" rest-api
