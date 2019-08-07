# Input data source

The following is a description of input data collected from public available sources to setup the virtual population 
model of Singapore.

## Death rates and life tables

These tables are used to calculate the probability of a person of a given age and gender of dying in a simulation year.

* **Description:** Complete Life Tables for Singapore Resident Population, 2016-2017.
* **File location:** `data/input_lifetable_sin_2003-2017.csv`
* **Source:** h<ttps://www.singstat.gov.sg/publications/population/complete-life-table>
* **Last accessed:** 27 March 2019

## Births and fertility rates

These tables are used to calculate the probability of a women with specific attributes to have a baby during the 
simulation year.

### Overall fertility rates per age group

* **Description:** Births And Fertility Rates.
* **File location:** ``data/input_birth_fertility_rates_sin_1961-2018.csv`
* **Source:** <https://www.tablebuilder.singstat.gov.sg/publicfacing/api/csv/title/13273.csv>
* **Last accessed:** 27 March 2019

### Children born per age group of married females

* **Description:** Citizen Ever-Married Females By Age Group And Number Of Children Born, Annual
* **File location:** `data/input_birth_number_by_age_1980-2018.csv`
* **Source:** <https://www.tablebuilder.singstat.gov.sg/publicfacing/api/csv/title/15697.csv>
* **Last accessed:** 27 March 2019

## Single parent births

* **Description:** Number of children born to women not married to father. 

* **File location:** none, raw info as below:


|  Description                                            | 2016 | 2017 |
| ------------------------------------------------------- |-----:| ----:|
| Single Parent Registration Births by citizen mothers    | 355  | 346  |
| Births by citizen mothers who were not married to father named in the child’s birth certificate at point of birth registration | 488  | 490  |
| Total                                                   | 843  | 836  |

* **Source:** <https://www.msf.gov.sg/media-room/Pages/Statistics-on-single-parent-registration-births-by-citizen-mothers.aspx>
* **Last accessed:** 27 March 2019

## Marriage rates

These tables are used to calculate the probability of a men and women with specific attributes to get married during a year.

* **Description:**  Marriage Rates, Annual
* **File location:** `data/input_marriage_rates_sin_1980-2017.csv`
* **Source:** <https://www.tablebuilder.singstat.gov.sg/publicfacing/api/csv/title/14168.csv>
* **Last accessed:** 27 March 2019

## Relationship status

These tables are used to initialise the population to mimic relationship status of the total population.
It is also used to refine marriage and birth statistics.

### Single population

* **Description:**  Proportion of Singles Among Citizen Population By Selected Age Group And Sex, Annual:
* **File location:** `data/input_proportion_singles_age_sin_1980-2018.csv`
* **Source:** <https://www.tablebuilder.singstat.gov.sg/publicfacing/api/csv/title/15694.csv>
* **Last accessed:** 27 March 2019

### Relationship status over 20 by sex and age group

* **Description:** Singapore Residents Aged 20 Years & Over By Sex, Age Group And Marital Status, Annual
* **File location:** `data/input_relationship_status_sin_1980-2018.csv`
* **Source:** <https://www.tablebuilder.singstat.gov.sg/publicfacing/api/csv/title/12084.csv>
* **Last accessed:** 27 March 2019
