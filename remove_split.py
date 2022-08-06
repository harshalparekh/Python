def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     harsh is a good      "
n = remove_and_split(this, "harsh")
print(n)
# print(this)
# print(this.strip())
