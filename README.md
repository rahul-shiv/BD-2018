# BD-2018
bd project

The objective of this project is to predict the outcome of an IPL match given the teams, the batting order, the bowling order, and which team goes first. We adopted two approaches to tackle this problem, both methods employing Pyspark and Spark Mllib. 
In the first method, we clustered the batsmen and bowlers separately and found the probability of the batsman scoring n (0,1,2,3,4,6) runs against the bowlers using these clusters. 
The next method involved building a decision tree and using its output to determine the output of the match.

#Clustering 

The Clustering notebook using Pyspark Mllib to cluster the batsmen and the bowlers into 5 clusters each.(5 is obtained by finding the elbow in the sum of square distances graph.) The batsmen and bowlers are clustered based on different attributes.
Average score, strike rate, balls faced, hundreds scored/innings, fifties scored/innings, fours rate, six rates, and vulnerability for batsmen, and bowler average, economy and bowler strike rate for bowler.


#clusters_read

The clusters_read notebook's primary purpose of this notebook is to replace the batsmen and bowlers with their cluster numbers, so that this can be looked up when runs are to be predicted. 


#final

The final notebook predicts matches by calculating the probability of n runs being scored or a wicket falling and refers to the clusters created in the previous notebook when there is not enough data.


#decision_tree

The decision_tree notebook specifies the labelled points for the decsion tree classifier. For batsman,  batsman,nonstrike,bowler,home,averagescore,sr,innings are used. For bowler,batsman,nonstrike,bowler,home,ave,sr,econ,innings are used to create labelled points. It also makes the Classifier Tree Model.


#decision_tree_final

The decision_tree_final notebook predicts match outcomes by simulating a match and using the decision tree classifer to predict runs and wickets.


#create_mappings
The create_mappings notebook makes mapping between the different formats of the names of players. (eg: Z Khan -> Zaheer Khan)




