<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the ArrangePy and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** prashantsengar, ArrangePy, prashanttgs, contact@prashants.in, ArrangePy, Organizes files in folders and helps you to clean your PC
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/prashantsengar/ArrangePy/">
    <img src="/img/logo.jpg" alt="Logo" width="250" height="110">
  </a>

  <h3 align="center">ArrangePy</h3>

  <p align="center">
    Organizes files in folders and helps you to clean your PC
    <br />
    <a href="https://github.com/prashantsengar/ArrangePy"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/prashantsengar/ArrangePy">View Demo</a>
    ·
    <a href="https://github.com/prashantsengar/ArrangePy/issues">Report Bug</a>
    ·
    <a href="https://github.com/prashantsengar/ArrangePy/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#community">Community</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
<!--    <li><a href="#acknowledgements">Acknowledgements</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## What it does

Organizes the files based on their extensions in folders. 

If you run the script in a directory containing hundreds of files of multiple filetypes, the script will arrange all of them in different directories based on the file type. For example, all PDFs are arranged in a directory for PDFs, all document based files (docx, doc, xlsx, pptx etc) are moved to the **docs** directory. 

All these files are moved to a directory named **ArrangedPy** in the directory on which the script was executed. So if you ran the script on your **Downloads** directory, a directory named *ArrangedPy* will be created in **Downloads**.

You can specify which files to move to which directory using the config.ini file. 

* Read about it on my [blog](https://prashants.in/blog/CleanPy-python-script-to-organize-your-files/)


## Features

Currently it has 2 modes

- Easy mode: Organzises files in the current directory
- Hard mode: Organizes files in the current directory and its subdirectories



### Built With

* [Python](https://python.org/)
* and some dedication by the [awesome contributors](https://github.com/prashantsengar/ArrangePy/graphs/contributors)


<!-- GETTING STARTED -->
## Getting Started

Follow the given steps to get started with ArrangePy

### Prerequisites

You should have Python installed on your system. You can move to Installation if you have it, otherwise continue with the next steps.

* Install [Python](https://python.org/) from python.org
* Make sure to add Python to PATH if you are on Windows
* To check that Python has been installed on your PC, open Command Prompt or Terminal and type in following command
    `python --version`

This should output `Python 3.x.x` where x.x is the version of your Python installation.
Note: If that does not work, try `python3 --version` or `py --version`

In the next part of the readme, `python` will be used, change it with the command that works for your PC


### Installation

#### Installation from PyPI

* Open command prompt/terminal and type the following command

  ```sh
  pip install arrangepy
  ```
  or
  ```sh
  pip3 install arrangepy
  ```
depending on the version.

It will install ArrangePy and the required packages.

* To confirm that ArrangePy has been installed successfully, type the following command in terminal

  ```sh
  arrange -h
  ```
It should show you a message on how to use it.


#### Installation from GitHub

* Clone the ArrangePy
  ```sh
  git clone https://github.com/prashantsengar/ArrangePy
  ```
* Change to the project directory
  ```sh
  cd ArrangePy
  ```
* Install requirements
  ```sh
  pip install -r requirements.txt
  ```
* Run ArrangePy
  ```sh
  python -m arrangepy
  ```

For the usage examples, replace `arrange` with `python -m arrangepy`



<!-- USAGE EXAMPLES -->
## Usage

```sh
usage: arrange [-h] [-w | -s | -b] [-nw] [directory]

positional arguments:
  directory          The directory to arrange, default is current working directory

optional arguments:
  -h, --help         show this help message and exit
  -w, --weak         Weak arrange
  -s, --strong       Strong arrange
  -b, --web          Run web GUI
  -nw, --no-warning  Don't show any warnings when running strong arrange
```

**Examples**

- `arrange` (Arranges current directory, asks for type of arrange [WEAK/STRONG] )
- `arrange -w` (Weak arranges current directory)
- `arrange -w PATH/TO/DIRECTORY` (Weak arranges given directory)
- `arrange -s -nw PATH/TO/DIRECTORY` (Strong arranges given directory without any warning)


### Running the Web GUI

- `arrange -b` # for the web interface


### Editing the CONFIG file

You can edit the config.ini file to change how the directories are created.
Say the initial configuration is this:

```
[ext]
PDF=['pdf'],
Images=['png','jpeg','jpg','gif', 'tiff', 'psd', 'ico'],
```

This will move all PDF files to a directory named *PDF* and all images of mentioned extensions to a directory named *Images*.


#### To add a new file type 
(say .eps) to the *Images* directory, add the new extension to the Images list. So it will change to:

```
[ext]
PDF=['pdf'],
Images=['png','jpeg','jpg','gif', 'tiff', 'psd', 'ico', 'eps'],
```

#### To add a new type of file (new directory)
Say you want to move all the video files along with PDFs and images. You can do that in this way:

```
[ext]
PDF=['pdf'],
Images=['png','jpeg','jpg','gif', 'tiff', 'psd', 'ico', 'eps'],
Videos=['mp4','mkv','avi','3gp'],
```

Now it will arrange all mp4, mkv, avi, 3gp files to the Videos directory.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/prashantsengar/ArrangePy/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


You can contribue to this project using multiple ways. **Here are a few things that you can work on**

- Improve this README to explain the idea better. GIFs can be added, for example.
- Adding extensions to the config.ini file will improve the experience for everyone. 
- Improve the code, add new features or fix [issues](https://github.com/prashantsengar/ArrangePy/issues/). 

Please read the [contribution guide](./CONTRIBUTING.md)


## Community 

Read the [contributing guide](./CONTRIBUTING.md)

Join the Telegram group for support and contributing. If you want to contribute, joining the group helps us all a lot because you can get instant feedback.

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1024px-Telegram_logo.svg.png" alt="mTracker Telegram Group" width="150" height="150">](https://t.me/joinchat/INDdLlDf-SFDPURESGgdrQ)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Prashant Sengar - [@prashanttgs](https://twitter.com/prashanttgs) - contact@prashants.in

Project Link: [https://github.com/prashantsengar/ArrangePy](https://github.com/prashantsengar/ArrangePy)



<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements

* []()
* []()
* []()
 -->




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/prashantsengar/ArrangePy.svg?style=for-the-badge
[contributors-url]: https://github.com/prashantsengar/ArrangePy/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/prashantsengar/ArrangePy.svg?style=for-the-badge
[forks-url]: https://github.com/prashantsengar/ArrangePy/network/members
[stars-shield]: https://img.shields.io/github/stars/prashantsengar/ArrangePy.svg?style=for-the-badge
[stars-url]: https://github.com/prashantsengar/ArrangePy/stargazers
[issues-shield]: https://img.shields.io/github/issues/prashantsengar/ArrangePy.svg?style=for-the-badge
[issues-url]: https://github.com/prashantsengar/ArrangePy/issues
[license-shield]: https://img.shields.io/github/license/prashantsengar/ArrangePy.svg?style=for-the-badge
[license-url]: https://github.com/prashantsengar/ArrangePy/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/prashant-sengar
