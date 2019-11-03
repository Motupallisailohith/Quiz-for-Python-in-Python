# %%
import pickle

# %%
db = open('categories.pickle', 'rb')
test = pickle.load(db)
db.close()

# %%
test["names"].append("Mixed Type")
# %%
test

# %%
db_w = open("categories.pickle", 'wb')
pickle.dump(test, db_w)
db_w.close()

# %%
