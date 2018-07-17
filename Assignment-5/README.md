## Using Data Lake Analytics to capture and analyze real time traffic data set and summarize findings

</br>

### Table Of Content




**[1. Tool Selection](https://github.com/amantewary/Classification-through-Spark-streaming-using-Twitter-data/tree/master/Assignment-5#1-tool-selection)**

**[2. Data Loading](https://github.com/amantewary/Classification-through-Spark-streaming-using-Twitter-data/tree/master/Assignment-5#2-data-loading)**

**[3. Data Cleaning](https://github.com/amantewary/Classification-through-Spark-streaming-using-Twitter-data/tree/master/Assignment-5#3-data-cleaning)**

**[4. Dashboard](https://github.com/amantewary/Classification-through-Spark-streaming-using-Twitter-data/tree/master/Assignment-5#4-dashboard)**

**[5. Output](https://github.com/amantewary/Classification-through-Spark-streaming-using-Twitter-data/tree/master/Assignment-5#5-output)**

**[6. Code Submission](https://github.com/amantewary/Classification-through-Spark-streaming-using-Twitter-data/tree/master/Assignment-5#6-code-submission)**

**[7. References](https://github.com/amantewary/Classification-through-Spark-streaming-using-Twitter-data/tree/master/Assignment-5#7-reference)**



</br>

### 1. Tool Selection

</br>

In this assignment we were required to analyze and visualize data provided by Toronto Transportation Services [1]. To complete the required task effectively, we used Microsoft Azure Data Lake Services & Microsoft Power BI which is a business analytics service. We choose Azure Data Lake for data analysis and transformation because it provides storage repository that can hold significantly large amount of raw data in its original format. Furthermore, it provides analytical services which can run  data transformation and processing programs in U-SQL [2] (and other analytical programming languages) over petabytes of data. It also allows to run parallel jobs with pay per job option. We chose Power BI for visualizing data because it provides interactive visualizations with self-service business intelligence capabilities. Power Bi supports Data Analysis Expression (DAX) which is a library of functions and operators that can be combined to build formulas [1]. We utilized DAX for data cleaning and data manipulation. Power BI also supports real-time filtering of data which we utilized to provide better insight on the given dataset.


</br>

### 2. Data Loading

</br>

**MICROSOFT AZURE DATA LAKE**

Step 1: In your data lake dashboard, Select Data Explorer.

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture.JPG?alt=media&token=1655061b-233a-43ff-8f26-d2b418614352)

</br>

Step 2: In “Data Explorer”, create two folders, “dalassign” and “outputs”. The “dalassign” folder will contain raw data and the “output” folder will contain the outputs of the analytical jobs.

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture1.JPG?alt=media&token=a8e5b3bd-eccc-4cb7-82ad-c73f05b6d25d)

</br>

Step 3: Inside “dalassign” folder, select “Upload” from toolbar and choose the file you want to upload from your system. We will use this data for our analysis.

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture2.JPG?alt=media&token=25c1044c-b031-40bc-bf00-c081b7c34aac)

</br>

### 3. Data Cleaning

We used Microsoft Visual Studio Code for our data cleaning task.

<ol>
    <li>In our raw data, one of the field was TCS #. We converted it from all uppercase to title-case as in U-SQL column names cannot be all uppercase. </li>
    <li>Most of the column names in our raw dataset had spaces between them. So we replaced spaces with underscore.</li>
    <li>In our raw dataset, two column names were starting with a number - “8 Peak Hr Vehicle Volume” & “8 Peak Hr Pedestrian Volume”. This is illegal syntax in C#. So we replaced numeric eight with word eight.</li>
</ol>

</br>

### 4. Dashboard

**[URL](https://app.powerbi.com/view?r=eyJrIjoiYTY0NWQwYjItYjU2MC00OGI1LTlhZDEtZDMxOWM3NzczZjc4IiwidCI6ImQ3OTA5NTVjLTc5MDMtNDc1NC04NDJiLTMyNTAzZDliNmVkYiIsImMiOjEwfQ%3D%3D)**


Dashboard:

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture3.JPG?alt=media&token=01214a9f-e96e-4922-b4cb-24e8663d6835)

</br>

Solution 1:

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture4.JPG?alt=media&token=d21bed72-438e-4603-9e29-7d9d6cd8fb28)

</br>

Solution 2:

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture5.JPG?alt=media&token=08f4b02f-6c00-4f18-a693-68288a39c134)

</br>

Solution 3:

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture6.JPG?alt=media&token=ecf103a7-689d-46dd-8778-d4c78e41140a)

</br>

Solution 4:

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture7.JPG?alt=media&token=3ad55aa5-b5ea-4bdf-a754-f47f08366102)

</br>

Solution 5:

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment_5_Dw%2FCapture8.JPG?alt=media&token=3a61d406-957f-44fe-a79b-0e8068f08e48)

</br>

### 5. Output


**Query 1:**

    Values ranged from 1,081 (OLD FINCH AVE) to 29,797 (WILLIAM R ALLEN RD). The average volume of traffic decreased by 96% over the
    course of series, decreasing mainly in the final 133 streets. The largest single decline on a percentage basis occured in OLD FINCH
    AVE (-27%). However, the largest single decline on an absolute basis occured in STEELES AVE E (-4,343).

</br>

**Query 2:**

    The minimum value is 584,742 (KEELE ST) and the maximum is 1.4 Million (rounded), a difference of 783,067. The distribution is
    positively skewed as the average of 815,138 is much greater than the median of 804,398. The total volume of traffic is fairly 
    evenly distributed across all the streets.

</br>

**Query 3:**

    Average of total volume of traffic is 2.9 million in 14 years. The minimum value is 28,616 (2006) and the maximum is 10.6 million
    (2016). Total Volume of traffic fell 98% over the course of all the series but increased in the final year. The largest single
    decline on a percentage basis occured in 2007 (-87%). However, the largest single decline on an absolute basis occured in 2015 (-5.3
    million).

</br>

**Query 4:**

    The average of total volume of traffic is 5.8 million across all seven days. The distribution ranges from 27,268 (Sunday) to 10.1
    million (Wednesday), a difference of almost 10.1 million. Total volume of traffic is somewhat concentrated with four of the seven
    days (57%) representing 85% of the total.

</br>

**Query 5:**

    The busiest day of the week is Wednesday. For Wednesday, the distribution ranges from 4,301 (DWIGHT AVE) to 648746 (YOUNGE ST), 
    a difference of 644,445. The distribution is positively skewed as the average of 70,139 is much greater than the median 0f 27,504.
    Wednesday is somewhat concentrated with 46 of 144 streets (32%) representing 80% of the total. YOUNGE ST (648,756) is more than nine
    times bigger than the average across the 144 streets.

</br>



### 6. Code Submission

**[DASHBOARD URL: ](https://app.powerbi.com/view?r=eyJrIjoiYTY0NWQwYjItYjU2MC00OGI1LTlhZDEtZDMxOWM3NzczZjc4IiwidCI6ImQ3OTA5NTVjLTc5MDMtNDc1NC04NDJiLTMyNTAzZDliNmVkYiIsImMiOjEwfQ%3D%3D 
)**


### 7. Reference


    [1] City of Toronto, “Open Data Catalogue,” City of Toronto, 13-Jul-2018. [Online]. Available: https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#7c8e7c62-7630-8b0f-43ed-a2dfe24aadc9. [Accessed: 17-Jul-2018]

    [2] MikeRys, “U-SQL Language Reference,” About Processes and Threads (Windows). [Online]. Available: https://msdn.microsoft.com/en-us/azure/data-lake-analytics/u-sql/u-sql-language-reference. [Accessed: 17-Jul-2018]


