# Languager

## First run
1) Install dependencies
2) Run migrations
3) `pre-commit install` 

## Run migrations
```
python manage.py makemigrations --settings=main.settings.localhost 
python manage.py migrate --settings=main.settings.localhost 
```

## Compile Tailwind CSS
```
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

# Project description
1) UI made by Flowbite 
