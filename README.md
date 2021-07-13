# SPY
## _Social media scanning python tool_

🕵️‍♂️ An OSINT tool to scan social media accounts by username across social networks

## Installation

clone or download the project

```sh
git clone https://github.com/cyb3r-g0d/SPY.git
```

## Usage

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-l            | --sitelist    | List of sites to scan (default=sites.txt)
-t            | --num-threads | Number of threads to use for subbrute bruteforce
-o            | --output      | Save the results to text file
-h            | --help        | Show the help message

### Examples

* To list all the basic options and switches use -h switch:

```python spy.py -h```

* To find a  of specific username:

``python spy.py alex``

* To find a  of specific from custom sitelist:

``python spy.py -l sitelixt.txt alex``


### List Of Sites (210 Sites In Total!)
View the list of sites [here](/res/site-names.txt)
