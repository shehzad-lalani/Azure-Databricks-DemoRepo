# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World from SQL!"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC
# MAGIC text with **bold** and *italicized* in it
# MAGIC
# MAGIC Ordered List 
# MAGIC 1. One
# MAGIC 1. Two
# MAGIC 1. Three
# MAGIC
# MAGIC Unordered list:
# MAGIC * apple
# MAGIC * mango
# MAGIC * banana
# MAGIC | id | name | age |
# MAGIC |----|------|-----|
# MAGIC | 1  | shehz | 22 |
# MAGIC | 2  | qasim | 21 |
# MAGIC | 3  | Mansoor| 33|

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


