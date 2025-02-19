This Python script reads and analyzes country data from three different continents: Europe, Asia, and Africa. The data is stored in text files, and the script processes the information to provide insights such as the largest countries, the most populous countries, and countries with the highest population density. It also calculates median population densities and total sizes for each continent.
Files

The script reads data from the following files:

    forras_europa.txt: Contains data for European countries.

    forras_azsia.txt: Contains data for Asian countries.

    forras_afrika.txt: Contains data for African countries.

Each file is expected to have the following format:
Copy

Country Name;Capital;Size;Population;Population Density

Features

    Data Loading: The script reads country data from the specified text files and stores it in lists of dictionaries.

    Sorting and Filtering: The script sorts countries by size, population, and population density. It also filters countries based on population density thresholds.

    Statistical Analysis: The script calculates the median population density and total size for each continent.

    Output: The script prints the following information:

        The largest country in each continent by size.

        The most populous country in each continent.

        The country with the highest population density in each continent.

        The median population density for each continent.

        The total size of each continent.

        Countries with a population density greater than 150.

        Countries categorized by population density into small, medium, and large groups.

Usage

    Ensure that the input files (forras_europa.txt, forras_azsia.txt, forras_afrika.txt) are in the same directory as the script.

    Run the script using Python 3:
    bash
    Copy

    python script_name.py

    The script will output the analyzed data to the console.

Example Output
Copy

Legnagyobb országok:
 Európa: Russia,17098242
 Ázsia: China,9596961
 Afrika: Algeria,2381741

Legnépesebb országok:
 Európa: Germany,83783942
 Ázsia: China,1439323776
 Afrika: Nigeria,206139589

Legnagyobb népsűrűségű országok:
 Európa: Monaco,26337
 Ázsia: Singapore,8295
 Afrika: Mauritius,626

Népesség mediánok:
 Európa: 117.5
 Ázsia: 145.0
 Afrika: 45.0

Európa: 10180000
Ázsia: 44614500
Afrika: 30370000

Népesség mediánok:
 Európa: 10425212
 Ázsia: 33699999
 Afrika: 12399999

Countries with population density > 150:
 Monaco
 Singapore
 Mauritius
 ...

Dependencies

    Python 3.x

    statistics module (standard library)

Customization

You can modify the script to include additional analyses or adjust the sorting and filtering criteria by editing the relevant functions and loops.
License

This project is open-source and available under the MIT License.

Feel free to contribute or report issues if you find any!
New chat
