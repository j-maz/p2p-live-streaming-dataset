# p2p-live-streaming-dataset

The repository is for publishing the dataset of a hybrid p2p live streaming system, which generated this dataset containing logs of 7 sizeable live streaming channels in Europe and North Africa. We anonymized it and processed it, yielding p2p links with their observed throughput and delay. 

The primary dataset is composed of the following columns:
 
 ```
 #   Column           Non-Null Count  Dtype                 Description
---  ------           --------------  -----                 -----------
 0   pid1             11525 non-null  object                the receiver id
 1   pid2             11525 non-null  object                the sender id
 2   cnt              11525 non-null  int64                 the number of chunks exchanged during the session
 3   throughput_avg   11525 non-null  float64               the observed average throughput (KB/s)
 4   throughput_std   11525 non-null  float64               the std of the observed throughput (KB/s)
 5   total_bytes      11525 non-null  int64                 the total number of bytes exchanged
 6   total_timespent  11525 non-null  int64                 the total time elasped for exchanging all the bytes
 7   city1            11525 non-null  object                the city of the receiver
 8   city2            11525 non-null  object                the city of the sender
 9   fips_code1       11525 non-null  object                
 10  fips_code2       11525 non-null  object             
 11  continent_code1  11525 non-null  object             
 12  continent_code2  11525 non-null  object             
 13  isp1             11525 non-null  object                the isp name of the receiver
 14  isp2             11525 non-null  object                the isp name of the sender
 19  min_ts           11525 non-null  datetime64[ns, UTC]   the start of the session
 20  max_ts           11525 non-null  datetime64[ns, UTC]   the end of the session
 21  cnt_neighbour    11525 non-null  int64                 the count of neighbours for the receiver during the session
 ```
