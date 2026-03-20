#!/bin/bash

LOG="scaling_report.txt"
PY_DEPS="src/etl_job.py,src/config.py"
MASTER="spark://192.168.5.177:7077"

echo "REDDIT ANALYSIS BENCHMARK" > $LOG
echo "=========================" >> $LOG

run_spark() {
    local scenario=$1
    local total_cores=$2
    local exec_cores=$3
    local memory=$4

    echo "Testing $scenario..."
    echo "SCENARIO: $scenario" >> $LOG
    
    spark-submit \
        --master $MASTER \
        --py-files $PY_DEPS \
        --conf spark.dynamicAllocation.enabled=false \
        --conf spark.cores.max=$total_cores \
        --executor-cores $exec_cores \
        --executor-memory $memory \
        src/analysis_job.py >> $LOG 2>&1
}

# 1. Horizontal Scaling (1 vs 2 vs 3 Workers)
# Each worker has 2 cores.
run_spark "Horizontal - 1 Worker" 2 2 "1024m"
run_spark "Horizontal - 2 Workers" 4 2 "1024m"
run_spark "Horizontal - 3 Workers" 6 2 "1024m"

# 2. Vertical Compute Scaling (1 vs 2 Cores on 1 Worker)
run_spark "Vertical Compute - 1 Core" 1 1 "1024m"
run_spark "Vertical Compute - 2 Cores" 2 2 "1024m"

# 3. Vertical Memory Scaling (512m vs 1024m vs 2560m)
# Keeping compute constant at 3 workers (2 cores)
run_spark "Vertical Memory - 512m" 6 2 "512m"
run_spark "Vertical Memory - 1024m" 6 2 "1024m"
run_spark "Vertical Memory - 2560m" 6 2 "2560m"

echo "Done! Check $LOG for results."