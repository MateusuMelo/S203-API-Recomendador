<br/>
<p align="center">
  <a href="https://github.com/MateusuMelo/S203-API-Recomendador">
    <img src="images/project-logo.png" alt="project-logo" width="512" height="512">
  </a>

  <p align="center">
    API Recomendador
    <br/>
    <br/>
    <a href="https://github.com/MateusuMelo/S203-API-Recomendador"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/MateusuMelo/S203-API-Recomendador">View Demo</a>
    .
    <a href="https://github.com/MateusuMelo/S203-API-Recomendador/issues">Report Bug</a>
    .
    <a href="https://github.com/MateusuMelo/S203-API-Recomendador/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/MateusuMelo/S203-API-Recomendador/total) ![Contributors](https://img.shields.io/github/contributors/MateusuMelo/S203-API-Recomendador?color=dark-green) ![Issues](https://img.shields.io/github/issues/MateusuMelo/S203-API-Recomendador) ![License](https://img.shields.io/github/license/MateusuMelo/S203-API-Recomendador) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

This project is being developed for a Database class. It utilizes Python and SQLite to create a simple recommendation system. The key features of the project include:
* User login functionality.
* Movie recommendations based on user preferences.
* Movie recommendations based on similarity with other movies.
* Rating system.

## Built With

* Python <img src="images/python-logo.png" alt="python-logo" width="35" height="35">
* SQLite <img src="images/sqlite-logo.png" alt="sqlite-logo" width="35" height="35">
* Flask <img src="images/flask-logo.png" alt="flask-logo" width="35" height="35">
* Visual Studio Code <img src="images/vscode-logo.png" alt="vscode-logo" width="35" height="35">

## Getting Started

After following all the [Installation](#installation) guide and running the flask server, a host will be show in the terminal. CTRL + Click this host link to go to your prefered browser, on just copy and paste. Now follow the [Usage](#usage) guide.

### Prerequisites

* Python
* Visual Studio Code

[Install last Python version](https://www.python.org/downloads/)

### Installation

1. Clone the repo

```sh
git clone https://github.com/MateusuMelo/S203-API-Recomendador.git
```

2. Install virtual environment

```sh
python -m venv .venv
```

3. Pip install the packages

```sh
pip install -r requirements.txt
```

4. Run while in virutal environment is activated

```sh
.venv/Scripts/activate
```
5. Run Flask server

```sh
cd server/
flask run
```

## Usage
*Main Page*
<img src="images/mainpage.png" alt="main-page">

# get_similar()
[API LINK](http://127.0.0.1:5000)
* To get similar movies 
http://127.0.0.1:5000/similar/<id_movie>.

* exemple : 
http://127.0.0.1:5000/similar/53
<img src="images/getsimilar.png" alt="getsimilar">

* results example:
```JSON
{
  "data": [
    {
      "index": 2,
      "movie_id": 20,
      "similarity_coefficient": 1
    },
    {
      "index": 31,
      "movie_id": 49,
      "similarity_coefficient": 1
    },
    {
      "index": 0,
      "movie_id": 18,
      "similarity_coefficient": 0.6666666667
    },
    {
      "index": 30,
      "movie_id": 48,
      "similarity_coefficient": 0.6666666667
    },
    {
      "index": 37,
      "movie_id": 55,
      "similarity_coefficient": 0.6666666667
    },
    {
      "index": 28,
      "movie_id": 46,
      "similarity_coefficient": 0.6666666667
    },
    {
      "index": 13,
      "movie_id": 31,
      "similarity_coefficient": 0.6666666667
    },
    {
      "index": 24,
      "movie_id": 42,
      "similarity_coefficient": 0.3333333333
    },
    {
      "index": 25,
      "movie_id": 43,
      "similarity_coefficient": 0.3333333333
    }
  ],
  "schema": {
    "fields": [
      {
        "name": "index",
        "type": "integer"
      },
      {
        "name": "movie_id",
        "type": "integer"
      },
      {
        "name": "similarity_coefficient",
        "type": "number"
      }
    ],
    "pandas_version": "1.4.0",
    "primaryKey": [
      "index"
    ]
  }
}
```

# recommend() 
[API LINK](http://127.0.0.1:5000)
* To get similar movies 
http://127.0.0.1:5000/recommend/<id_user>.

* exemple : 
http://127.0.0.1:5000/recommend/1
<img src="images/recommend.png" alt="recommend">

* results example:
```JSON
{
 {
  "data": [
    {
      "index": 5,
      "movie_id": 23,
      "similarity_coefficient": 0.6666666666
    },
    {
      "index": 12,
      "movie_id": 30,
      "similarity_coefficient": 0.5238095238
    },
    {
      "index": 3,
      "movie_id": 21,
      "similarity_coefficient": 0.5
    },
    {
      "index": 23,
      "movie_id": 41,
      "similarity_coefficient": 0.2777777778
    }
  ],
  "schema": {
    "fields": [
      {
        "name": "index",
        "type": "integer"
      },
      {
        "name": "movie_id",
        "type": "integer"
      },
      {
        "name": "similarity_coefficient",
        "type": "number"
      }
    ],
    "pandas_version": "1.4.0",
    "primaryKey": [
      "index"
    ]
  }
}
}
```


## Roadmap

See the [open issues](https://github.com/MateusuMelo/S203-API-Recomendador/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/MateusuMelo/S203-API-Recomendador/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/MateusuMelo/S203-API-Recomendador/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

_MIT_
MIT License

Copyright (c) 2024 Mateus Correa de Melo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors

* **Tales Machado** - *Soft Engineer Student* - [Tales Machado](https://github.com/RobinCharles984/)
* **Mateus Melo** - *Soft Engineer Student* - [Mateus Melo](https://github.com/MateusuMelo/)
* **Marcelo Alckmin** - *Soft Enginner Student* [Marcelo Alckmin](https://github.com/marceloalckmin)

## Acknowledgements

* [Tales Machado](https://github.com/RobinCharles984/)
* [Mateus Melo](https://github.com/MateusuMelo/)
* [Marcelo Alckmin](https://github.com/marceloalckmin)
* [Flask](https://flask.palletsprojects.com/en/3.0.x/)
* [ImgShields](https://shields.io/)
