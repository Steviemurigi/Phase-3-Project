# MovieShop Manager

## Description

**MovieShop Manager** is a command-line application designed to manage movie shops and their inventory of movies. Users can create, update, delete, and search for movie shops and movies based on various criteria such as genre and title.

## Features

**User-Friendly Command-Line Interface**: The MovieShop Manager offers an intuitive and easy-to-navigate command-line interface, allowing users to quickly access various functionalities without the need for complex commands. 

Such functionalities include:

- List all movie shops
- Find movie shops by name or ID
- Create, update, and delete movie shops
- List all movies in the database
- Find movies by title, genre, or ID
- Create, update, and delete movies
- View all movies available at a specific movie shop

## Project Structure

```
│
├── 📂 lib/                   
│   ├── 📂 models/
│   │   ├── 📄 __init__.py            
│   │   ├── 📄 movie.py
│   │   └── 📄 movieshop.py            
│   │   
│   ├── 📄 cli.py   
│   ├── 📄 helpers.py
│   └── 📄 seed.py
│   
├── LICENSE   
├── movies.db                 
├── Pipfile
├── Pipfile.lock
└── README.md                

```

## Getting started

Ensure you have the following installed:

- Python 3.8 or higher
- Pipenv 
- SQlite

## Installation and set up

Fork and clone this repository into your preferred terminal directory:

```bash

git clone git@github.com:Steviemurigi/Phase-3-Project.git

```

Navigate into the project directory.

```bash

cd Phase-3-Project

```

Run code . from the directory to open the project in your code editor.

Activate virtual environment

```bash

pipenv shell

```
## Usage

To view the movies database:

- Right click on movies.db from the editor explorer.
- Select open database
- This will enable one to explore the movies database from the SQlite explorer.

To run the CLI application from the terminal, run:

```bash

python lib/cli.py

```

This will open up the CLI application, where one can explore and perform various functions by following the CLI instructions.

## Technologies Used

- **Programming Language** : Python 3.x

- **SQLite** : For database management

- **Development Environment** : Any text editor e.g VS Code

## Contributing

Contributions are welcome to this project! If you'd like to help, please fork the repository and create a new branch for your feature or bug fix. Once you've made your changes, submit a pull request with a clear description of your contributions.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.



