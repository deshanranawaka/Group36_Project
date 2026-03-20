# Cleaning and ingestion logic
import json

def extract_content(line):
    return json.loads(line).get("content", "")  # Parse JSON

def preprocess(input_rdd):
    return (input_rdd
        .map(lambda line: line.lower()) # lowercase
        .map(lambda line: line.split()) # tokenise on whitespace
        .map(lambda tokens: [t for t in tokens if t != ""]) # remove empty tokens
    )