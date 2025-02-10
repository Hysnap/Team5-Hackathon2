# Team 5 : Data Analytics and AI BootCamp - Hactathon 2

A manager at the bank is disturbed with more and more customers leaving their credit card services. They would really appreciate if one could predict for them who is gonna get churned so they can proactively go to the customer to provide them better services and turn customers' decisions in the opposite direction

Now, this dataset consists of 10,000 customers mentioning their age, salary, marital_status, credit card limit, credit card category, etc. There are nearly 18 features.

We have only 16.07% of customers who have churned. 


# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* The data has been obtained from Kaggle at https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers/data.
* It contian 10000 rows and 23 Columns

* The Columns are defined by the source as follows
    - Client Num - Client number. Unique identifier for the customer holding the account
    - Attrition_Flag - Internal event (customer activity) variable - if the account is closed then 1 else 0
    - Customer_Age - Demographic variable - Customer's Age in Years
    - Gender - Demographic variable - M=Male, F=Female
    - Dependent_count - Demographic variable - Number of dependents
    - Education_Level - Demographic variable - Educational Qualification of the account holder (example: high school, college graduate, etc.)
    - Marital_Status - Demographic variable - Married, Single, Divorced, Unknown
    - Income_Category - Demographic variable - Annual Income Category of the account holder (< $40K, $40K - 60K, $60K - $80K, $80K-$120K, > $120K, Unknown)
    - Card_Category - Product Variable - Type of Card (Blue, Silver, Gold, Platinum)
    - Months_on_book - Period of relationship with bank
    - Total_Relationship_Count - Total no. of products held by the customer
    - Months_Inactive_12_mon - No. of months inactive in the last 12 months
    - Contacts_Count_12_mon - No. of Contacts in the last 12 months
    - Credit_Limit - Credit Limit on the Credit Card
    - Total_Revolving_Bal - Total Revolving Balance on the Credit Card - total amount paid out and in.
    - Avg_Open_To_Buy - Open to Buy Credit Line (Average of last 12 months) - Average available till limit hit.
    - Total_Amt_Chng_Q4_Q1 - Change in Transaction Amount (Q4 over Q1)
    - Total_Trans_Amt - Total Transaction Amount (Last 12 months)
    - Total_Trans_Ct - Total Transaction Count (Last 12 months)
    - Total_Ct_Chng_Q4_Q1 - Change in Transaction Count (Q4 over Q1)
    - Avg_Utilization_Ratio - Average Card Utilization Ratio
    - Naives_Bayes_1 - Naives Bayes Attrition Flag Category - Historic Analysis - Ignored
    - Naives_Bayes_2 - Naives Bayes Attrition Flag Category - Historic Analysis - Ignored

## Business Requirements
* A manager at the bank is disturbed with more and more customers leaving their credit card services. They would really appreciate if one could predict for them who is gonna get churned so they can proactively go to the customer to provide them better services and turn customers' decisions in the opposite direction

* Now, this dataset consists of 10,000 customers mentioning their age, salary, marital_status, credit card limit, credit card category, etc. There are nearly 18 features.

* We have only 16.07% of customers who have churned. Thus, it's a bit difficult to train our model to predict churning customers.


## Hypothesis and how to validate?
* Women have a higher chance of leaving
   * Compare the level of customer attrition for Women vs Men
   * Undertake T-test to confirm if any variance identified is statistically relevant
* There are specific ages group more likely to leave
   * Create Age Groups for analysis
   * Compare the level of customer attrition By age group
   * Undertake T-test to confirm if any variance identified is statistically relevant
* We can forcast chance of leaving based on number of transactions
   * Compare the level of customer attrition vs Total transactions Count
   * Compare the level of customer attrition vs Change in transaction count Q4 to Q1
   * Compare the level of customer attrition vs Average Utilization Ratio
   * Undertake T-test to confirm if any variance identified is statistically relevant
* Customers with unknown income are more likely to leave.
   * Compare the level of customer attrition by Income category
   * Undertake T-test to confirm if any variance identified is statistically relevant

## Project Plan
* Ensure all team members are correctly set up to participate in the Project
* Undertake initial analysis to look at potential hypothesis to test.
* Agree Hypothesis to test and first steps.
* Complete First ETL for core data
* Identify potential data to enhance analysis
* Undertake analysis to prove/disprove hypothesis
* Data Architects to undertake T-Tests on hypothesis and make results available to Data Analysts
* Compare Bank customer population vs American Census population to identify potentially missed opportunities.
* Produce commentary of hypothesis results and analysis

## The rationale to map the business requirements to the Data Visualisations
* List your business requirements and a rationale to map them to the Data Visualisations
* Women have a higher chance of leaving
    * Population split M/F attrited/Current showing comparative Percentages.
    * Analysis of other factors for the attrited women vs non attrited women/men so identify contributing elements.
* There are specific ages group more likely to leave
    * Comparison of attrition rates by Age Groups
    * Comparison of Attrition rate of age groups vs population average
* We can forcast chance of leaving based on number of transactions  
    * Comparison of attrition rates by Age Groups
    * Comparison of Attrition rate of age groups vs population average
* Customers with unknown income are more likely to leave.
    * Comparison of Attrition rate by Income category to confirm if Unknown is more or less at risk.

## Analysis techniques used
* List the data analysis methods used and explain limitations or alternative approaches.
    * Comparison of Attrition Rate aka Churn - defined as Attrited Customer as a Percentage of relevant population was undertaken against numerous potential impactful    measures.
    * This analysis was normalised by group in order to enable comparison for identification of relevance/impact.
* The core ETL was undertaken in Python and the encoding of text fields was prepared so that it would be available for use as part of the Data Analysis
    * Data Analysis was primarily undertaken in Tableau - initially each of the Data analysts undertook seperate investigations, but an attempt to merge this work proved futile and from that point on the work collaporatively on a single file.
    * Calculation of the T-test results for the hypothesis was undertaken with guidance from ChatGPt by the Data Architects in python to enable them to provide additional depth of understanding to the Data Analysts/
* The data was a single snapshot of customer state, several iterations of the data would of allowed for analysis of pre-emptive behaviour to better identify potential  
    churn risk factors and their relevance.
* During Ideation - ChatGPT was asked to identify potential relevant items for investigation and for guidance on types of visualisations that could be relevant.

## Ethical considerations
* The data was anonlymised so there was no private data issues.
* The fact that the data was around credit and debt and the customers aim was to increase loyalty raised potential issues around health/safe debt which were beyond the scope of this project.

## Dashboard Design
* Dashboard 1 - Churn Rate by Gender & Churn Rate by Age Group
* Dashboard 2 - Relationship between transactions and churn & Churn by Income Category

* Conclusion: Diffrence between genders not significant enough to confirm the hypothes that "Women have a higher chance of leaving than a men. "
Hyphotes that "There are specific ages group more likely to leave" was confirmed
Customers with lower transaction counts and amounts are more likely to churn, while higher transaction activity correlates with retention. Monitoring changes in transaction behavior over time can help predict and prevent customer attrition.
Hypothes that "Customers with unknown income are more likely to leave" was rejected.

## Unfixed Bugs
* By the end of the project one of the Team still did not have a working VSCode install and had contributed little to the project as they also struggled to commit data to GitHub.
* Time spent trying to support this team member meant that the team didnt achieve it max potential.

## Development Roadmap
* With 2 Data Analysts we looked to see if through using XML versions of the Tableau files we could enable parrallel development that would be combined later.  Alas due to the way that unique identifiers are allocated to data sets in Tableau this proved not possible.  Once this had been identified as not possible the data analysts worked in tandem on the same file using remote connects to discuss and support each other.
* Based on the project experience more knowledge is desirable around merge conflict resolution in GitHub, the benefit of Branching over Forking along with the associated issues.  Greater knowledge of interactivity in Tableau.

## Main Data Analysis Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits 

* LMS, Chatgpt and the team as a whole.

### Content 

- The column details were taken from Kaggle along with the original Data.

- Initial Ideation ChatGPT feedback is - "Initial Idiation ChatGPT Freedback.ipynb"

- The final ETL is - "ETL hackaton2 ETL new.py"
- The final core dataset is  - "BankChurners_Cleaned_Encoded.csv"
- The final dashboard is the "FInal Submission Documents\team5 assestment.twbx"

- A suplimentary data set of USA census population data that was prepared with the hope of inclusion in the final project but was not included is "adult_final.csv"
- A prototype of the charts potentially for inclusion based of the census data compared to the BankChurners data is include in "PowerBI_PopulationComparison.pbix" - this was not integrated into the final dashboard.

- The "Prep and Investigations" folder contains rough workings and future inclusion investigations undertaken by the team during the project.


