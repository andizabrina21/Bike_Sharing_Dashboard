# Capital Bikeshare Analysis
Bike Sharing is a new generation of traditional bicycle rental systems, where the entire process—from membership registration and bike rental to bike return—is fully automated. Through this system, users can rent a bicycle from one station and return it to another using a smartphone app, GPS, and barcode scanning. Unlike other transportation services such as buses or subways, the duration of each trip as well as the departure and arrival locations are recorded in detail within the system. One of the well-known implementations of bike sharing is **Capital Bikeshare**, a public bicycle rental service operating in Washington, D.C. and the surrounding areas. The system provides a network of stations with thousands of bicycles that users can access for short-distance trips. Supported by technologies such as mobile applications and tracking systems, **Capital Bikeshare** is designed to provide convenience, flexibility, and support more sustainable urban mobility.

## Project Overview
This project analyzes data from the **Capital Bikeshare** app to evaluate service performance and identify bicycle usage patterns. Through this analysis, various insights are expected to be obtained regarding user behavior, rental trends, factors influencing the number of rentals, and information that can serve as a basis for decision-making to improve service quality and operational efficiency.

## Business Problem
As Capital Bikeshare's usage increases, the company needs to ensure bicycle availability, maintain fleet quality, and optimize operations across all stations. However, rental demand can fluctuate due to factors such as weather, season, day, and time. Without a clear understanding of these usage patterns, the company may face imbalanced bicycle distribution, reduced service quality, and operational inefficiencies. Therefore, data analysis is essential to understand usage patterns, identify the factors influencing demand, and generate insights that support decision-making and service improvement.

## Dataset Description
The dataset used in this project was obtained from Kaggle. It conatins two years of historical data (2011-2012) from the Capital Bikeshare system in Washington D.C., United States, which is publicly available at http://capitalbikeshare.com/system-data. The data was aggregated on an hourly and daily basis and enriched with corresponding weather and seasonal information. The weather data was obtained from http://www.freemeteo.com.

## Data Cleaning
Before the analysis was conducted, the data first undergoes a **data cleaning** process to ensure its quality and accuracy. This process includes checking the consistency between the **hour** and **day** datasets, handling *missing values*, identifying duplicate records, also validating and correcting the data as needed to prepare it for analysis.

## Dashboard
To view the data visualization results in the form of a dashboard, there are two ways as follows:
#### Access the online dashboard in Streamlit Cloud
[Click here to view the dashboard](https://bikesharingdashboard-kmrvb3enktryxype49mf6p.streamlit.app/).

#### Run Locally
1. Clone the repository
2. Install the required libraries
3. Run the dashboard, type the following in the terminal:
   "streamlit run bike_sharing_db.py"

### Dependencies
- Python 3.x
- streamlit
- pandas
- numpy
- matplotlib
- seaborn
- Babel

### Notes
- Make sure all CSV files are in the 'data/' folder.
- The Streamlit Cloud dashboard automatically redeploys if changes are made to GitHub.

## Dashboard Overview
![Dashboard](images/dashboard1.png)
### Key Performance Indicator
![KPI](images/dashboard2.png)
#### Key Insights & Business Recommendation
- A total of 3.29 million trips over two years demonstrates a high level of adoption and use of the service, making Capital Bikeshare a consistently used alternative form of urban transportation.
   - _Maintaining service quality through fleet maintenance, increasing bike availability, and expanding the station network in high-demand areas._
- Registered users (approximately 2.67 million) dominate usage compared to casual users (approximately 620 thousand), indicating that the business is primarily driven by loyal customers who use the service repeatedly rather than single-use users.
   -_ Increasing registered user retention through loyalty programs while encouraging casual users to become registered members through promotional campaigns and membership offers._
- Rental demand peaks at 5:00 PM, indicating that bicycles are widely used as a mode of transportation for commuting home from work.
   - _Optimize operations during peak hours by ensuring bicycle and docking space availability at high-demand stations and proactively redistributing bicycles before peak periods_

### User Trends Over Time
![UserTrend](images/dashboard3.png)
#### Key Insights & Business Recommendation
- The number of users increased significantly from approximately 1.24 million in 2011 to 2.05 million in 2012, indicating strong growth in service usage within one year.
   - _Supporting growth by expanding fleet capacity and station coverage in high-demand areas while improving service quality to sustain user growth._
- Usage exhibits a seasonal pattern, with peak rentals from June to September and declining at the beginning and end of the year. This indicates that demand is influenced by weather and seasonal conditions.
   - _Adjusting fleet allocation and maintenance schedules according to seasonal demand, and implement promotional campaigns during low-demand periods to maintain usage._
- The highest rental demand occurs on weekdays during commuting hours, particularly at 5:00 PM, indicating that Capital Bikeshare is widely used for commuting to and from work.
   - _Ensure bicycle and dock availability during peak hours through proactive fleet redistribution and prioritize operations at stations with high commuter demand._

### Environmental Impact
![Env](images/dashboard4.png)
#### Key Insights & Business Recommendation
- Bicycle rentals are highest during the fall season and under clear weather conditions, while demand declines sharply during heavy rain. This indicates that environmental conditions have a significant impact on bike-sharing demand.
   - _Adjust operations based on weather forecasts, such as optimizing bicycle distribution on clear days and implementing promotions or incentives during unfavorable weather to maintain usage levels._
- Weather has a greater influence than seasonality on rental demand. Although usage varies across seasons, the decline in demand caused by poor weather is considerably more significant.
   - _Utilize weather forecast data to support operational planning and marketing strategies rather than relying solely on seasonal patterns, enabling more effective fleet management and responsiveness to changes in demand._

### User Segmentation
![Segment](images/dahsboard5.png)
#### Key Insights & Business Recommendation
- Registered users dominate at 81.2% of total usage, while casual users represent only 18.8%, indicating that Capital Bikeshare is primarily used by regular users for their daily mobility needs.
   - _Maintain registered user loyalty through membership programs, rewards, and continuous service improvements, while encouraging casual users to become registered members through membership promotions._
- Registered and casual users exhibit different usage patterns. Registered users show clear demand peaks during weekday commuting hours (8:00 AM and 5:00–6:00 PM), whereas casual users are more active from midday to the afternoon, with relatively consistent usage, particularly on weekends.
   - _Optimizing bicycle availability during commuting hours in office areas for registered users, while increasing promotions and partnerships with tourist and recreational destinations on weekends to attract more casual users._

## Conclusion
Based on the analysis, Capital Bikeshare usage experienced significant growth from 2011 to 2012 and was primarily used for weekday commuting, especially during peak commuting hours toward the weekend. Furthermore, rental demand was higher under clear weather conditions, indicating that weather is a key factor influencing service demand. These findings suggest that Capital Bikeshare usage patterns are relatively consistent and predictable. Therefore, the company should optimize fleet distribution during peak hours, utilize weather forecasts into operational planning, and maintain the loyalty of registered users to improve service quality and support sustainable business growth.
