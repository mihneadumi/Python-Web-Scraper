# Python *Adaptive* Web Scraper
A python based web scraper whose main goal is to get all the products from a website, being able to sort or filter them quickly and make them easily exportable to excel or csv for better data manipulation or statistics (or just for fun)

## Currently Supported Websites
* [OLX](https://www.olx.ro/ "olx.ro")
* [Altex](https://altex.ro/ "altex.ro")
* [KSA Retail](https://ksaretail.ro/ "ksaretail.ro") - slow because of poor website design

## Used Technologies and principles
* [Requests](https://pypi.org/project/requests/) and [Selenium webdriver](https://pypi.org/project/selenium/) for getting the website's html
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for parsing the retrieved html
* [Pandas](https://pypi.org/project/pandas/) for quick data manipulation and export
* I've employed a simplified style [layered arhitecture design](https://www.baeldung.com/cs/layered-architecture) consisting of an UI layer and a Repository layer to reduce dependencies and also to keep my project fairly modular so that I can easily add/remove support for certain websites in the future

## Opening the app and Installation
* [Python 3.x](https://www.python.org/downloads/) is required to run the app.
* After opening the project in your preffered IDE (VSCode has some import problems that I'll talk about a little bit later you need to to the following pip installs in the terminal:
```bash
  pip install requests
```
```bash
  pip install selenium
```
```bash
  pip install pandas
```
```bash
  pip install bs4
```
* Run the 'main.py' file and paste the http link to the desired search query you want to scrape.
* For [**VSCode users**](https://i.ytimg.com/vi/Ux5cQbO_ybw/maxresdefault.jpg) only, if pylance is acting up, you need to go into IDE Settings (Ctrl+,) and search for "pylance path add' amd imder "Python › Analysis: Include" click on "Add Item" and enter the path of the folder in which the project is located (ex: "A:\Projects\Python-Web-Scraper"

## How to use
After you run the `main.py` file you will be greeted by a preview of the list of products and a simple 6 option menu, in which you can select the option by entering corresponding number:

![image](https://user-images.githubusercontent.com/50325644/222268085-04e2c9c8-5e33-45df-bc66-892f0be31de6.png)

Here you can sort/filter the products list before exporting it or directly export it. The exported excel/csv will be located in the project folder under the given name.
## Challenges faced
* I've encountered a wierd interaction with javascript in some websites such as [Altex](https://altex.ro/ "altex.ro"), where the javascript triggers 0.1 seconds after loading the page and then it loads all the products on the page thus making the initial html pull that [Requests](https://pypi.org/project/requests/) not work properly
* Also some websites *cough cough again* [Altex](https://altex.ro/ "altex.ro") came with some sort of poorly implemented bot protection which messed up the [Requests](https://pypi.org/project/requests/)'s way of pulling the html so I had to use [Selenium](https://pypi.org/project/selenium/) in order to trick the website into thinking a human is accesing it, and thus making the scraping a little bit slower since this method opens an Edge browser and then waits for the javascript to load the entire page with products.
