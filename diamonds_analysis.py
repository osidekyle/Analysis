import pandas as pd
import sklearn
from sklearn import svm,preprocessing

df=pd.read_csv("diamonds\diamonds.csv")


cut_class_dict={"Fair":1,"Good":2,"Very Good":3,"Premium":4,"Ideal": 5}
clarity_dict = {"I3": 1, "I2": 2, "I1": 3, "SI2": 4, "SI1": 5, "VS2": 6, "VS1": 7, "VVS2": 8, "VVS1": 9, "IF": 10, "FL":11}
color_dict = {"J": 1,"I": 2,"H": 3,"G": 4,"F": 5,"E": 6,"D": 7}


df['cut']=df['cut'].map(cut_class_dict)
df['clarity']=df['clarity'].map(clarity_dict)
df['color']=df['color'].map(color_dict)

df=sklearn.utils.shuffle(df)

X=df.drop("price",axis=1).values
X=preprocessing.scale(X)
y=df["price"].values


test_size = 200

X_train = X[:-test_size]
y_train = y[:-test_size]

X_test = X[-test_size:]
y_test = y[-test_size:]


clf=svm.SVR()
clf.fit(X_train,y_train)



for x,y in list(zip(X_test,y_test))[:10]:
   print("Estimate is:",clf.predict([x])[0],"Actual Value is:",y)