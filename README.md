# Geolocation
Verloop Assignment to create the GeoLocation API

## Starting the API
Using the following command 

```
uvicorn app.main:app
```
For development:
```
uvicorn app.main:app --reload
```

## Dependencies
Dependencies are managed by poetry.
Documentation is available [here](https://python-poetry.org/docs/)

After the installation, navigate inside the parent dir and run the following command
```
poetry install
```

### Docker Run
If you don't want to deal with the package dependencies, you can just run the docker
Steps:
1. Build the image
```
docker build -t <image_name> ./  
```
2. Once the image is built, you can run the container
```
docker run -d --name <container_name> -p 80:80 <image_name>
```

Note: 
1. All the project files are present (including the .env file)
Add the key `ACCESS_API_KEY` in .env to get the API up and running
2. You can use the Swagger UI to check the working API [here](http://127.0.0.1:8000/docs#)