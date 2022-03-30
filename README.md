<div id="top"></div>

[![commits](https://badgen.net/github/commits/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/main)](https://GitHub.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/graphs/commit-activity)
[![forks](https://badgen.net/github/forks/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile)](https://GitHub.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/network/members)
[![stars](https://badgen.net/github/stars/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile)](https://GitHub.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/stargazers)
[![issues](https://badgen.net/github/issues/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile)](https://GitHub.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/issues/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

<div align="center">
  <h1 align="center">Analyzing Rutgers Research Topics and Finding Potential Correlation Based on Google Scholar Profile</h1>
  <p align="center">
    <a href="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/CS439%20Project%20Final%20Report.pdf"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://GitHub.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile">View Demo</a>
    ·
    <a href="https://GitHub.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/issues">Report Bug</a>
    ·
    <a href="https://GitHub.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built with</a></li>
        <li><a href="#data-collection">Data Collection</a></li>
        <li><a href="#data-analysis">Data Analysis</a></li>
        <li><a href="#clustering-and-visualization">Clustering and Visualization</a></li>
        <li><a href="#classification-and-prediction">Classification and Prediction</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This is a course project of Rutgers CS439 Intro to Data Science. The project aims at solving two problems that undergraduate students might have when they want to start their research journey:
* Students may not know which research areas they could connect to produce new thought.
* Students may not know which researchers are in those research areas and could help them start their research journey.

The project provide a possible solution to these two problems based on data on Google Scholar by showing frequently related research areas at Rutgers and recommending specific researchers who are related to those research areas.

### Built with
* Language:
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

* Python Framework:
  ![scrapy version](https://img.shields.io/badge/scrapy-2.6-brightgreen)
* Python packages:
  ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
  ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
  ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  ![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
  ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
  ![matplotlib version](https://img.shields.io/badge/matplotlib-3.5.0-brightgreen)
  ![seaborn version](https://img.shields.io/badge/seaborn-0.11.2-brightgreen)
  ![mlxtend version](https://img.shields.io/badge/mlxtend-0.19.0-brightgreen)
  ![pymysql version](https://img.shields.io/badge/PyMySQL-1.0.2-brightgreen)

* JavaScript package: 
  ![D3.js version](https://img.shields.io/badge/D3.js-0.19.0-brightgreen)

* Database:
  ![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

### Data Collection
* Data source: Google Scholar
* Number of profiles extracted: 2908
* Number of interests extracted: 4597
* Data format:
  
  Logical Model

  <img width=500 height=350 alt="Data format" title="Data format" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Table%20Relation.png?raw=true">

* Statistics:
  * Top 30 interests
    
    <img width=600 height=600 alt="Top 30 Interests" title="Top 30 Interests" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Top%2030%20Interests%20Among%20Scholars.png?raw=true">
  * Distribution of number of interests each researcher has
    
    <img width=350 height=500 alt="Top 30 Interests" title="Top 30 Interests" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Distribution%20of%20Number%20of%20Interests%20Each%20Researcher%20Has.png?raw=true">

### Data Analysis

The above box plot shows that the mean interest number per scholar is 3.08 which means that one scholar may have multiple interests. Within this in mind, we can come up with that different authors may have the same interests and therefore, there might be some relations between each author bonded by their focused topics. In the same manner, we also may find out some relations between each interest because the more two interests displayed on a scholar profile, the higher possiblity of developing an interdisciplinary research they have. Based on these consideration, we can create a link between two scholars or two interests.

* Relations among scholars
  
  The following figure is a graph which shows the relations among Rutgers scholars.
  
  <img width=550 height=550 alt="Relation Graph" title="Relation Graph" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Relation%20Graph%20of%20Scholars.png?raw=true"/>

  The most crowded part on the bottom of the graph, it shows the scholars who are tightly connected by the topic Machine Learning.

* Relations among interests
  
  The following two graphs shows frequent interest pairs and interest triples generated by Apriori algorithm.

  <img width=450 height=450 alt="Frequent Interest Pairs" title="Frequent Interest Pairs" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Frequent%20Interest%20Pairs.png?raw=true"/>

  <img width=450 height=100 alt="Frequent Interest Triples" title="Frequent Interest Triples" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Frequent%20Interest%20Triples.png?raw=true"/>

### Clustering and Visualization

The above data analysis reveals that most interests in frequent interest pairs come from top 30 interests. Considering this, we can choose researchers whose interests contain one or more of these top 30 interests to classify them into several categories. To do this, we perform an unsupervised machine learning method to first seperate them into different clusters and then figure out the category based on the common interests of each researcher in each cluster.

* Data Preprocess: Use one hot encoding to convert each researcher to a row in a matrix.
  
  <img width=550 height=250 alt="One Hot Encoding Table" title="One Hot Encoding Table" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/One%20Hot%20Encoding%20Table.png?raw=true"/>

* Model Training: Apply Agglomerative Clustering in scikit-learn package to recursively merge pair of clusters of the input data based on linkage distance
  
* Dimension Reduction: Apply Principle Component Analysis (PCA) to reduce the dimensionality of the data and visualize the clusters in 3D and 2D.
  
  * Clusters in 3D
    
    <img width=400 height=250 alt="Clusters in 3D" title="Clusters in 3D" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Clusters%20in%203D%20Graph.png?raw=true"/>

  * Clusters in 2D
    
    <img width=400 height=250 alt="Clusters in 2D" title="Clusters in 2D" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Clusters%20in%202D%20Graph.png?raw=true"/>
* Consideration on underfit and overfit
  
  During the modelling process, we avoid the underfit and overfit by variously testing the hyperparameters and finally take 5 clusters as it best fit the training data.

  * Underfit cases

    <img width=400 height=250 alt="Underfit Example 1" title="Underfit Example 1" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Cluster%20Underfit%20Example%201.png?raw=true"/>

    <img width=400 height=250 alt="Underfit Example 2" title="Underfit Example 2" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Cluster%20Underfit%20Example%202.png?raw=true"/>
  
  * Overfit cases
  
    <img width=400 height=250 alt="Overfit Example 1" title="Overfit Example 1" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Cluster%20Overfit%20Example%201.png?raw=true"/>

    <img width=400 height=250 alt="Overfit Example 2" title="Overfit Example 2" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Cluster%20Overfit%20Example%202.png?raw=true"/>

* Use clustering model to add labels to original data
  
  <img width=600 height=200 alt="Overfit Example 2" title="Overfit Example 2" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Data%20with%20Classified%20Labels.png?raw=true"/>


### Classification and Prediction

With clustering, we are able to add labels on data. This allows us to perform a supervised machine learning to build a classifier model for prediction.

* Model training: 80% original data as training data and 20% original data as test data
* Model evaluation:
  
  <img width=500 height=200 alt="Overfit Example 2" title="Overfit Example 2" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Prediction%20Model%20Statistics.png?raw=true"/>

* Example:
  
  <img width=600 height=150 alt="Overfit Example 2" title="Overfit Example 2" src="https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile/blob/main/report/Prediction%20Example.png?raw=true"/>

## License

Distributed under the MIT License.

See `LICENSE` for more information.

## Contact

Feiyu Zheng - [feiyuzheng98@gmail.com](mailto:feiyuzheng98@gmail.com)

Junyan Dai - [jd1397@rutgers.edu](mailto:jd1397@rutgers.edu)

Project Link: [https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile](https://github.com/ChaserZ98/Analyzing-Rutgers-Research-Topics-and-Finding-Potential-Correlation-Based-on-Google-Scholar-Profile)

<p align="right">(<a href="#top">back to top</a>)</p>