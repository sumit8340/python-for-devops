# lists <------------
# lists is "mutable" means we can change when ever we want
# means we can add or remove from lists

#------------------------Difference-------------------------

# tuples <-----------
# tuples is "immutable" means we can't change them
# means we can't add or remove anything from tuple when it created

# --lists--

student_name = ["Monu", "Sonu", "Kushal", "Vikash"]
print(student_name)
#-------#
# lists use []

s3_buckets_lists = ["monu_demo_bucket", "moni_demo_bucket", "sonu_demo_bucket"] # Simple list
s3_buckets_lists.append("new_s3_bucket") # Add anything

#s3_buckets_lists.remove("new_s3_bucket") # Remove anything

print(s3_buckets_lists)
print(type(s3_buckets_lists))

#-------#
# tuple use ()

s3_buckets_lists = ("monu_demo_bucket", "moni_demo_bucket", "sonu_demo_bucket")
print(type(s3_buckets_lists))