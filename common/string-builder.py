words = ["hello", "world", "!"]

# inefficient
result_inef = ""
for word in words:
    result_inef += word

# efficient
result_eff = "".join(words)

print("Inefficient: ", result_inef)
print("Efficient: ", result_eff)
