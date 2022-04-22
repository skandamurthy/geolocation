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
poetry init
```

### Adding package
```
poetry add <package>
```
After adding the package, please do reload the app

Note: All the project files are present (including the .env file)
Add the key `ACCESS_API_KEY` in .env to get the API up and running