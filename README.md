# AirBnB Clone Console Project

This project is the first step towards building a full-fledged AirBnB clone application. It implements a command-line interpreter (CLI) to manage core AirBnB objects.


### Project Overview

The project focuses on:

* **Object-Oriented Programming:** Building a `BaseModel` class with functionalities for object initialization, serialization (converting to JSON), and deserialization (reconstructing from JSON).

* **Data Management:** Creating specific classes for AirBnB entities like User, State, City, and Place, inheriting from `BaseModel`. Implementing a file-based storage engine using JSON files.

* **Testing:** Writing unit tests to ensure the correctness of each class and the storage engine.

* **User Interaction:** Designing a user-friendly CLI for object creation, retrieval, and updates.


### Getting Started

**Prerequisites:**

* Python 3 (tested with version 3.x)
* `json` library (`pip install json`)
* `unittest` library (for testing) (`pip install unittest`)
* `cmd` library (for CLI) (`pip install cmd`)
* `uuid` library (for objects id's) (`pip install uuid`)

**Project Structure:**

```
AirBnB_clone/
├── AUTHORS		# Project contributors
├── README.md		# This file
├── __init__.py		# Package initialization
├── console.py		# Main script for running the CLI
├── models		# Holds all class definitions for AirBnB entities
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py	# BaseModel class the parent class for all the AirBnB model classes
│   ├── city.py
│   ├── engine		# Storage Engine Directory
│   │   ├── __init__.py
│   │   └── file_storage.py	# Implements functions for storing and retrieving objects using JSON files
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── requirements.txt	# Required libraries for the project
└── tests		# Unit Tests for all components
    ├── test_amenity.py
    ├── test_basemodel.py
    ├── test_city.py
    ├── test_console.py
    ├── test_filestorage.py
    ├── test_place.py
    ├── test_review.py
    ├── test_state.py
    └── test_user.py

3 directories, 24 files
```

**Running the Project:**

1. Clone this repository.

2. Install required libraries:
```bash
$ pip install -r requirements.txt
```

3. Run the program:
```bash
$ python3 console.py
```
Another way:
```bash
$ ./console.py
```
in non-interactive mode:
```bash
$ echo "command" | ./console.py
```

4. Follow the on-screen instructions to interact with the CLI.

### Usage

The CLI provides functionalities for:

* `create`: Creates a new object (User, State, City, or Place) based on user input.
* `show`: Retrieves and displays information about an existing object by ID.
* `update`: Updates attributes of an existing object.
* `all`: Lists all objects of a specific type.
* `delete`: Deletes an existing object.

Type `help` or `?` for a list of available commands and their usage.

### Testing

Unit tests are included in the `tests` folder to verify the functionality of each class and the storage engine. You can run the tests using:

```
pytest
```

### Next Steps

This project provides the foundation for building a complete AirBnB clone application. The next steps could involve:

* Developing a web interface using HTML, CSS, and JavaScript.
* Implementing a database storage system for persistent data storage.
* Creating an API for data access from the web frontend.

By completing this initial project, you'll gain valuable experience in object-oriented programming, data management, and testing, crucial for building a web application like AirBnB.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Contributions

We welcome contributions to this project. Please submit pull requests with proper testing and documentation.

This README file provides a clear overview of the project, installation instructions, usage guide, and next steps. It also emphasizes testing and encourages contributions. Feel free to customize it further as your project evolves.

