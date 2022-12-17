FROM python:3

# Create a new directory for the Python script
WORKDIR /app

RUN apt-get update && apt-get install -y wget
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x wait-for-it.sh
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app


# Run the Python script
CMD ["./wait-for-it.sh", "mariadb:3306", "--", "python", "bot.py"]
