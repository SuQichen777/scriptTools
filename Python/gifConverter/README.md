## Local GIF Converter
This is a simple Python script that converts a local GIF file to a series of PNG images. The script uses the `Pillow` library to handle the image conversion.

## Command Line NetEase Music Getter with MongoDB
This is a command line tool that allows you to get music album information from NetEase Music and store it in a MongoDB database. You should copy `.env.example` to `.env` and fill in your MongoDB connection string before running the script. You can run `python Python/netEaseGetter/app.py` to start the application and `ctrl + c` to stop it (it will run indefinitely). If you want to see a deployed and visualized version of this application, please check out [While-Listening-to-Albums](https://github.com/SuQichen777/While-Listening-to-Albums).

## Environment Dependencies
- Pillow 
` pip install Pillow`
- requests, beautifulsoup4, pymongo, dotenv
` pip install requests beautifulsoup4 pymongo dotenv`