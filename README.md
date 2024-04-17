<br/>
<p align="center">
  <a href="https://github.com/MateusuMelo/S203-API-Recomendador">
    <img src="images/logo.png" alt="Logo" width="400" height="100">
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

![Screen Shot](images/screenshot.png)

The project is being created for Database class, using Python with a database, we choose SQLite. The project is just a simple recommender where:
* You can login into system
* Recommend movies
* Rate movies

## Built With

* Python
* SQLite
* Flask
* Visual Studio Code

## Getting Started

Use VSCode <img src="images/vscode.png" alt="vscodelogo" width="35" height="35"> with Python <img src="images/python.png" alt="vscodelogo" width="35" height="35">

### Prerequisites

* python

[Install last Python version](https://www.python.org/downloads/)

### Installation

1. Clone the repo

```sh
git clone [https://github.com/your_username_/Project-Name.git](https://github.com/MateusuMelo/S203-API-Recomendador.git)
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
python main.py
```
4. Run Flask server

```sh
cd server/
flask run
```

## Usage
# get_similar()
[API LINK](http://127.0.0.1:5000)
* To get similar movies 
http://127.0.0.1:5000/similar/<id_movie>.

* exemple : 
http://127.0.0.1:5000/similar/19

* results:
```JSON
{
 "movies_id_list": "[30,37,54,33,32,47,18,42,43,45,46,48,40,49,50,51,52,53,55,58,41,39,20,29,25,26,38,28,27,31,34,36,59]"
}
```

# recommend() 
[API LINK](http://127.0.0.1:5000)
* To get similar movies 
http://127.0.0.1:5000/recommend/<id_user>.

* exemple : 
http://127.0.0.1:5000/recommend/1

* results:
```JSON
{
 "movies_id_list": "[20,34,58,56,53,49,43,42,23,40,30,24,59,35,37,39,33,47,28,25]"
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

## Acknowledgements

* [Tales Machado](https://github.com/RobinCharles984/)
* [Mateus Melo](https://github.com/MateusuMelo/)
* [ImgShields](https://shields.io/)
