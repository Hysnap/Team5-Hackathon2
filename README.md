# Team 5 : Datga Analytics and AI BootCamp - Hactathon 2

A manager at the bank is disturbed with more and more customers leaving their credit card services. They would really appreciate if one could predict for them who is gonna get churned so they can proactively go to the customer to provide them better services and turn customers' decisions in the opposite direction

I got this dataset from a website with the URL as https://leaps.analyttica.com/home. I have been using this for a while to get datasets and accordingly work on them to produce fruitful results. The site explains how to solve a particular business problem.

Now, this dataset consists of 10,000 customers mentioning their age, salary, marital_status, credit card limit, credit card category, etc. There are nearly 18 features.

We have only 16.07% of customers who have churned. Thus, it's a bit difficult to train our model to predict churning customers.


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
    - Naives_Bayes_1 - Naives Bayes Attrition Flag Category - Historic Analysis - Ignore
    - Naives_Bayes_2 - Naives Bayes Attrition Flag Category - Historic Analysis - Ignore

## Business Requirements
* A manager at the bank is disturbed with more and more customers leaving their credit card services. They would really appreciate if one could predict for them who is gonna get churned so they can proactively go to the customer to provide them better services and turn customers' decisions in the opposite direction

* Now, this dataset consists of 10,000 customers mentioning their age, salary, marital_status, credit card limit, credit card category, etc. There are nearly 18 features.

* We have only 16.07% of customers who have churned. Thus, it's a bit difficult to train our model to predict churning customers.


## Hypothesis and how to validate?
* Women have a higher chance of leaving
* There are specific ages group more likely to leave
* We can forcast chance of leaving based on number of transactions
* Customers with unknown income are more likely to leave.

## Project Plan
* Ensure all team members are correctly set up to participate in the Project
* Undertake initial analysis to look at potential hypothesis to test.
* Agree Hypothesis to test and first steps.

## The rationale to map the business requirements to the Data Visualisations
* List your business requirements and a rationale to map them to the Data Visualisations

## Analysis techniques used
* List the data analysis methods used and explain limitations or alternative approaches.
* How did you structure the data analysis techniques. Justify your response.
* Did the data limit you, and did you use an alternative approach to meet these challenges?
* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

## Ethical considerations
* Were there any data privacy, bias or fairness issues with the data?
* How did you overcome any legal or societal issues?

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Unfixed Bugs
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Main Data Analysis Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The column details were taken from Kaggle along with the original Data.
- 
- 

## Acknowledgements (optional)
* Thank the people who provided support through this project.
