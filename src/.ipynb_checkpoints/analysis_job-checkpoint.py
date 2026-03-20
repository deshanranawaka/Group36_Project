# Main Spark/MapReduce logic
import time
from pyspark.sql import SparkSession
from config import *
from etl_job import preprocess, extract_content

# Minimalist Session: Only network requirements are kept
spark = SparkSession.builder \
    .appName("Group36-Reddit-Final-Project") \
    .config("spark.driver.host", DRIVER_HOST) \
    .config("spark.driver.bindAddress", BIND_ADDRESS) \
    .getOrCreate()

sc = spark.sparkContext

# Verification print for your logs
print(f"ACTUAL CORES GRANTED: {sc.getConf().get('spark.cores.max')}")

reddit_raw_rdd = sc.textFile(HDFS_PATH)

start_time = time.time()

content_rdd = reddit_raw_rdd.map(extract_content) 
preprocessed_rdd = preprocess(content_rdd)

word_counts = (preprocessed_rdd
    .flatMap(lambda tokens: tokens)
    .map(lambda word: ''.join(char for char in word if char.isalnum()))
    .filter(lambda word: word != "" and word not in NLTK_STOPWORDS)
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)

top_10 = word_counts.takeOrdered(10, key=lambda x: -x[1])
duration = time.time() - start_time

print("-" * 30)
print(f"Top 10 Reddit Words:")
for word, count in top_10:
    print(f"{word}: {count}")
print(f"\nTotal Runtime: {duration:.2f} seconds")
print("-" * 30)

spark.stop()